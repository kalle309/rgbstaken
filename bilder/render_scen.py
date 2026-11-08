"""Fotorealistisk rendering av RGB-staken i ett svenskt fönster en decemberkväll (Blender 4.2, Cycles).

Kör:  blender -b -P bilder/render_scen.py -- <projektmapp> <utfil.png> [samples]
Staken byggs av de riktiga STL-filerna i stl/ (mm), allt annat är enkel scenografi.
"""
import bpy, math, random, sys, os
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ROOT = args[0] if len(args) > 0 else os.getcwd()
OUT = args[1] if len(args) > 1 else os.path.join(ROOT, "bilder", "fonster_december.png")
SAMPLES = int(args[2]) if len(args) > 2 else 384
random.seed(12)

# ---------------- mått från bas.sc (mm) ----------------
SP, ST, H0, SD, L_VIS, TAPP = 50, 40, 180, 16, 61, 6 * 39 / 44
XS = [0, 50, -50, 100, -100, 150, -150]
HS = [H0, H0 - ST, H0 - ST, H0 - 2 * ST, H0 - 2 * ST, H0 - 3 * ST, H0 - 3 * ST]
MM = 0.001

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene

# ---------------- material ----------------
def mat(name, base=(0.8, 0.8, 0.8), rough=0.5, **kw):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*base, 1)
    b.inputs["Roughness"].default_value = rough
    for k, v in kw.items():
        b.inputs[k].default_value = v
    return m

paint = mat("Vitmålad stake", (0.80, 0.77, 0.71), 0.55)
tube = mat("Ljusrör", (0.86, 0.84, 0.79), 0.45,
           **{"Subsurface Weight": 0.25, "Subsurface Radius": (2.0, 1.5, 1.0), "Subsurface Scale": 0.002})
wood = mat("Fönsterbåge", (0.80, 0.78, 0.74), 0.4)
sill_m = mat("Fönsterbräda", (0.82, 0.80, 0.76), 0.3, **{"Coat Weight": 0.3})
wall_m = mat("Vägg", (0.62, 0.55, 0.47), 0.85)
snow_m = mat("Snö", (0.85, 0.88, 0.95), 0.6, **{"Subsurface Weight": 0.2, "Subsurface Scale": 0.05})
red_m = mat("Falurött", (0.32, 0.05, 0.03), 0.8)
dark_m = mat("Mörk", (0.02, 0.025, 0.03), 0.8)
pine_m = mat("Gran", (0.01, 0.03, 0.015), 0.9)

glass = bpy.data.materials.new("Glas"); glass.use_nodes = True
gb = glass.node_tree.nodes["Principled BSDF"]
gb.inputs["Base Color"].default_value = (1, 1, 1, 1)
gb.inputs["Transmission Weight"].default_value = 1.0
gb.inputs["Roughness"].default_value = 0.0
gb.inputs["IOR"].default_value = 1.5

def emissive(name, color, strength):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    e = nt.nodes.new("ShaderNodeEmission"); e.inputs[0].default_value = (*color, 1); e.inputs[1].default_value = strength
    o = nt.nodes.new("ShaderNodeOutputMaterial"); nt.links.new(e.outputs[0], o.inputs[0])
    return m

# lågan: frostad, genomskinlig PETG som lyser inifrån
flame_m = bpy.data.materials.new("Låga"); flame_m.use_nodes = True
nt = flame_m.node_tree; nt.nodes.clear()
pb = nt.nodes.new("ShaderNodeBsdfPrincipled")
pb.inputs["Base Color"].default_value = (1.0, 0.93, 0.80, 1)
pb.inputs["Roughness"].default_value = 0.35
pb.inputs["Transmission Weight"].default_value = 0.9
pb.inputs["Emission Color"].default_value = (1.0, 0.72, 0.38, 1)
pb.inputs["Emission Strength"].default_value = 9.0
out = nt.nodes.new("ShaderNodeOutputMaterial"); nt.links.new(pb.outputs[0], out.inputs[0])

window_light = emissive("Grannfönster", (1.0, 0.62, 0.28), 3.5)
lamp_light = emissive("Gatlykta", (1.0, 0.75, 0.45), 40.0)

# ---------------- staken ----------------
def import_stl(path, name, m, loc=(0, 0, 0)):
    bpy.ops.wm.stl_import(filepath=path, global_scale=MM)
    o = bpy.context.selected_objects[0]; o.name = name
    o.location = loc
    o.data.materials.clear(); o.data.materials.append(m)
    bpy.ops.object.shade_auto_smooth(angle=math.radians(35))
    return o

stl = lambda n: os.path.join(ROOT, "stl", n)
import_stl(stl("base_left.stl"), "Bas vänster", paint)
import_stl(stl("base_right.stl"), "Bas höger", paint)
pillar0 = import_stl(stl("pillar.stl"), "Pelare", tube)
flame0 = import_stl(stl("flame.stl"), "Låga", flame_m)
for i, (x, h) in enumerate(zip(XS, HS)):
    p = pillar0 if i == 0 else pillar0.copy()
    f = flame0 if i == 0 else flame0.copy()
    if i:
        sc.collection.objects.link(p); sc.collection.objects.link(f)
    p.location = (x * MM, 0, (h - SD) * MM)
    f.location = (x * MM, 0, (h + L_VIS - TAPP) * MM)
    # ljuskälla inuti varje låga (LED:en), varmvit
    bpy.ops.object.light_add(type="POINT", location=(x * MM, 0, (h + L_VIS + 12) * MM))
    l = bpy.context.object; l.data.energy = 1.3; l.data.shadow_soft_size = 0.004
    l.data.color = (1.0, 0.68, 0.36)

# ---------------- rummet: fönsternisch, bräda, vägg ----------------
def box(name, x0, x1, y0, y1, z0, z1, m, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(location=((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2))
    o = bpy.context.object; o.name = name
    o.scale = ((x1 - x0) / 2, (y1 - y0) / 2, (z1 - z0) / 2)
    bpy.ops.object.transform_apply(scale=True)
    if bevel:
        b = o.modifiers.new("Fas", "BEVEL"); b.width = bevel; b.segments = 3
    o.data.materials.append(m)
    return o

OW, OB, OT = 0.56, 0.0, 1.30          # öppningens halvbredd, nederkant (=brädans ovansida), överkant
GY = 0.12                              # glasets läge (y)
# vägg med nisch
box("Vägg vänster", -2.5, -OW - 0.06, -0.06, 0.30, -1.2, 2.6, wall_m)
box("Vägg höger", OW + 0.06, 2.5, -0.06, 0.30, -1.2, 2.6, wall_m)
box("Vägg över", -OW - 0.06, OW + 0.06, -0.06, 0.30, OT + 0.06, 2.6, wall_m)
box("Vägg under", -OW - 0.06, OW + 0.06, -0.06, 0.30, -1.2, -0.03, wall_m)
# fönsterbräda (sticker ut i rummet)
box("Fönsterbräda", -OW - 0.10, OW + 0.10, -0.17, GY, -0.03, 0.0, sill_m, bevel=0.006)
# karm
box("Karm vänster", -OW - 0.06, -OW, 0.08, 0.16, OB, OT + 0.06, wood, 0.003)
box("Karm höger", OW, OW + 0.06, 0.08, 0.16, OB, OT + 0.06, wood, 0.003)
box("Karm topp", -OW, OW, 0.08, 0.16, OT, OT + 0.06, wood, 0.003)
box("Karm botten", -OW, OW, 0.08, 0.16, OB, OB + 0.035, wood, 0.003)
# två bågar med mittpost och spröjs
FW = 0.045
for side in (-1, 1):
    x0, x1 = (-OW, -0.012) if side < 0 else (0.012, OW)
    box("Båge", x0, x0 + FW, 0.095, 0.135, OB + 0.035, OT, wood, 0.003)
    box("Båge", x1 - FW, x1, 0.095, 0.135, OB + 0.035, OT, wood, 0.003)
    box("Båge", x0, x1, 0.095, 0.135, OT - FW, OT, wood, 0.003)
    box("Båge", x0, x1, 0.095, 0.135, OB + 0.035, OB + 0.035 + 0.06, wood, 0.003)
    zs = OB + 0.035 + 0.06 + (OT - FW - OB - 0.095) * 0.62
    box("Spröjs", x0, x1, 0.105, 0.125, zs, zs + 0.022, wood, 0.002)
    xm = (x0 + x1) / 2
    box("Spröjs", xm - 0.011, xm + 0.011, 0.105, 0.125, OB + 0.095, OT - FW, wood, 0.002)
    g = box("Glas", x0 + FW - 0.005, x1 - FW + 0.005, GY - 0.002, GY + 0.002, OB + 0.09, OT - FW + 0.005, glass)
box("Mittpost", -0.012, 0.012, 0.09, 0.15, OB, OT, wood, 0.002)

# ---------------- ute: snö, hus, granar, lykta, snöflingor ----------------
GROUND = -1.1
bpy.ops.mesh.primitive_plane_add(size=200, location=(0, 60, GROUND))
bpy.context.object.data.materials.append(snow_m)

def roof(cx, cy, w, d, zt, pitch=0.42):
    o = 0.35
    x0, x1, y0, y1, zr = cx - w / 2 - o, cx + w / 2 + o, cy - d / 2 - o, cy + d / 2 + o, zt + w * pitch
    v = [(x0, y0, zt), (x1, y0, zt), (cx, y0, zr), (x0, y1, zt), (x1, y1, zt), (cx, y1, zr)]
    f = [(0, 1, 2), (3, 5, 4), (0, 2, 5, 3), (1, 4, 5, 2), (0, 3, 4, 1)]
    me = bpy.data.meshes.new("Tak"); me.from_pydata(v, [], f); me.update()
    ob = bpy.data.objects.new("Tak", me); sc.collection.objects.link(ob)
    me.materials.append(snow_m)
    return ob

def house(cx, cy, w, d, h, wall, lit=(1, 1, 1, 0)):
    box("Hus", cx - w / 2, cx + w / 2, cy - d / 2, cy + d / 2, GROUND, GROUND + h, wall)
    roof(cx, cy, w, d, GROUND + h)
    n = 0
    for k in range(2):
        for j in range(2):
            wx = cx - w / 2 + w * (0.25 + 0.5 * k)
            wz = GROUND + h * (0.22 + 0.42 * j)
            m = window_light if lit[n] else dark_m
            n += 1
            box("Fönster", wx - 0.5, wx + 0.5, cy - d / 2 - 0.05, cy - d / 2 - 0.01, wz, wz + 1.15, m)
            box("Spröjs ute", wx - 0.04, wx + 0.04, cy - d / 2 - 0.08, cy - d / 2 - 0.04, wz, wz + 1.15, wood)
            box("Spröjs ute", wx - 0.5, wx + 0.5, cy - d / 2 - 0.08, cy - d / 2 - 0.04, wz + 0.68, wz + 0.74, wood)

yellow_m = mat("Gul panel", (0.55, 0.42, 0.18), 0.8)
house(-14.0, 46, 8.0, 8, 5.2, red_m, (1, 1, 0, 1))
house(-2.0, 58, 9.0, 9, 6.0, red_m, (1, 0, 1, 1))
house(11.0, 48, 7.5, 7, 5.0, yellow_m, (0, 1, 1, 1))
house(24.0, 62, 8.0, 8, 5.5, red_m, (1, 1, 1, 0))
for i in range(40):  # granskog bakom husen
    x = random.uniform(-45, 45); y = random.uniform(70, 95); hgt = random.uniform(8, 16)
    bpy.ops.mesh.primitive_cone_add(vertices=10, radius1=hgt * 0.27, depth=hgt, location=(x, y, GROUND + hgt / 2))
    bpy.context.object.data.materials.append(pine_m)
# gatlyktor längs gatan
for lx, ly in ((5.5, 20.0), (-9.0, 30.0), (16.0, 34.0)):
    box("Lyktstolpe", lx - 0.04, lx + 0.04, ly - 0.04, ly + 0.04, GROUND, GROUND + 4.0, dark_m)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.18, location=(lx, ly, GROUND + 4.1))
    bpy.context.object.data.materials.append(lamp_light)
    bpy.ops.object.light_add(type="POINT", location=(lx, ly, GROUND + 3.85))
    bpy.context.object.data.energy = 1000; bpy.context.object.data.color = (1.0, 0.72, 0.42)
    bpy.context.object.data.shadow_soft_size = 0.2
# fallande snö (blir mjuka, oskarpa prickar)
flake = mat("Snöflinga", (1, 1, 1), 0.5, **{"Emission Color": (0.75, 0.82, 1.0, 1), "Emission Strength": 0.2})
for i in range(700):
    y = random.uniform(0.4, 14.0)
    spread = 0.6 + y * 0.5
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=random.uniform(0.004, 0.014),
                                          location=(random.uniform(-spread, spread), y,
                                                    random.uniform(GROUND + 0.2, 0.9 + y * 0.6)))
    bpy.context.object.data.materials.append(flake)

# måne/himmel: mörkblått kvällsljus
world = bpy.data.worlds.new("Decemberkväll"); sc.world = world; world.use_nodes = True
wn = world.node_tree.nodes; wl = world.node_tree.links; wn.clear()
tc = wn.new("ShaderNodeTexCoord"); sep = wn.new("ShaderNodeSeparateXYZ")
ramp = wn.new("ShaderNodeValToRGB")
ramp.color_ramp.elements[0].position = 0.0; ramp.color_ramp.elements[0].color = (0.16, 0.22, 0.42, 1)   # horisont
ramp.color_ramp.elements[1].position = 0.45; ramp.color_ramp.elements[1].color = (0.012, 0.025, 0.08, 1)  # zenit
e = ramp.color_ramp.elements.new(0.06); e.color = (0.09, 0.14, 0.32, 1)
bg = wn.new("ShaderNodeBackground"); bg.inputs[1].default_value = 0.45
wl.new(tc.outputs["Generated"], sep.inputs[0]); wl.new(sep.outputs["Z"], ramp.inputs[0])
wl.new(ramp.outputs[0], bg.inputs[0])
o = wn.new("ShaderNodeOutputWorld"); wl.new(bg.outputs[0], o.inputs[0])
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(62), 0, math.radians(200)))
s = bpy.context.object.data; s.energy = 0.02; s.color = (0.55, 0.65, 1.0); s.angle = math.radians(1)

# svag varm rumsbelysning bakom kameran (en lampa längre in i rummet)
bpy.ops.object.light_add(type="AREA", location=(-1.2, -2.6, 1.2))
a = bpy.context.object; a.data.energy = 6; a.data.size = 1.0; a.data.color = (1.0, 0.7, 0.45)
a.rotation_euler = (math.radians(70), 0, math.radians(-25))
a.visible_glossy = False; a.visible_transmission = False; a.visible_camera = False

# ---------------- kamera ----------------
bpy.ops.object.camera_add(location=(0.17, -0.95, 0.24))
cam = bpy.context.object; sc.camera = cam
target = Vector((0.0, 0.03, 0.18))
cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()
cam.data.lens = 40
cam.data.dof.use_dof = True
cam.data.dof.focus_distance = (target - cam.location).length
cam.data.dof.aperture_fstop = 2.2
cam.data.dof.aperture_blades = 7

# ---------------- rendering ----------------
sc.render.engine = "CYCLES"
cy = sc.cycles
prefs = bpy.context.preferences.addons["cycles"].preferences
for dev_type in ("OPTIX", "CUDA", "HIP", "ONEAPI"):
    try:
        prefs.compute_device_type = dev_type; prefs.get_devices()
        if any(d.type == dev_type for d in prefs.devices):
            for d in prefs.devices:
                d.use = d.type in (dev_type, "CPU")
            cy.device = "GPU"; print("Renderar på", dev_type); break
    except Exception:
        pass
cy.samples = SAMPLES
cy.use_denoising = True
cy.max_bounces = 10; cy.transmission_bounces = 10; cy.caustics_reflective = False; cy.caustics_refractive = False
cy.light_tree = True
sc.render.resolution_x, sc.render.resolution_y = 1600, 1067
sc.view_settings.view_transform = "AgX"
sc.view_settings.look = "AgX - Medium High Contrast"
sc.view_settings.exposure = 0.6
sc.render.film_transparent = False

# glöd runt lågorna (bloom) och lite filmkorn i kompositören
sc.use_nodes = True
ct = sc.node_tree; ct.nodes.clear()
rl = ct.nodes.new("CompositorNodeRLayers")
glare = ct.nodes.new("CompositorNodeGlare"); glare.glare_type = "FOG_GLOW"; glare.quality = "HIGH"
glare.threshold = 1.5; glare.size = 8; glare.mix = -0.7
lens = ct.nodes.new("CompositorNodeLensdist"); lens.inputs["Dispersion"].default_value = 0.012
lens.inputs["Distortion"].default_value = -0.008
comp = ct.nodes.new("CompositorNodeComposite")
ct.links.new(rl.outputs["Image"], glare.inputs[0])
ct.links.new(glare.outputs[0], lens.inputs[0])
ct.links.new(lens.outputs[0], comp.inputs[0])

sc.render.filepath = OUT
sc.render.image_settings.file_format = "PNG"
bpy.ops.render.render(write_still=True)
print("Klar:", OUT)
