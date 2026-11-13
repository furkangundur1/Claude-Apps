import bpy
sc = bpy.context.scene
print("SAHNE:", sc.name, "| nesneler:", [ (o.name,o.type) for o in sc.objects ])
k = bpy.data.objects.get("Cube")
print("KUP konum/donus/olcek:", tuple(k.location), tuple(k.rotation_euler), tuple(k.scale), "| donus modu:", k.rotation_mode)
m = k.data
print("MESH:", m.name, "kose:", len(m.vertices), "kenar:", len(m.edges), "yuz:", len(m.polygons))
print("ilk 3 kose:", [tuple(v.co) for v in m.vertices[:3]])
print("ilk yuz kose sirasi:", list(m.polygons[0].vertices))
print("Nesne<->veri ayri mi? nesne adi", k.name, "veri adi", m.name, "veri kullanan sayisi", m.users)
print("Malzeme:", [s.material.name if s.material else None for s in k.material_slots], "renk:", tuple(k.material_slots[0].material.diffuse_color))
print("Kamera:", tuple(sc.objects['Camera'].location), "lens", sc.objects['Camera'].data.lens)
print("Isik:", sc.objects['Light'].data.type, sc.objects['Light'].data.energy, "W")
print("Ust/alt iliskisi:", k.parent, [c.name for c in k.children])
print("Birim:", sc.unit_settings.system, sc.unit_settings.scale_length)
# Ekleme operatorleri (mesh menusu)
ops = sorted(n for n in dir(bpy.ops.mesh) if n.startswith("primitive_"))
print("EKLENEBILIR SEKILLER:", ops)
print("Ilk kez acilan klavye: G/R/S ->", [ (ki.type, ki.idname) for km in bpy.context.window_manager.keyconfigs.default.keymaps if km.name=="Object Mode" for ki in km.keymap_items if ki.type in ("G","R","S","X","A") and not ki.shift and not ki.ctrl and not ki.alt ])
# .blend dosya basligi
bpy.ops.wm.save_as_mainfile(filepath="/tmp/claude-0/-home-user-rea/0065b623-2e46-57a5-8679-3fdb16682e8f/scratchpad/blender/ornek.blend")
