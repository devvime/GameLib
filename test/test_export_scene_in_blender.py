import bpy
import json
import os

# Pasta base do projeto (mesma do .blend)
BASE_PATH = bpy.path.abspath("//")
MODELS_DIR = os.path.join(BASE_PATH, "models")

os.makedirs(MODELS_DIR, exist_ok=True)

objects_data = []

# Salva seleção atual
original_selection = bpy.context.selected_objects
original_active = bpy.context.view_layer.objects.active

for obj in bpy.context.scene.objects:

    if obj.type not in {"MESH", "EMPTY"}:
        continue

    model_path = None

    # EXPORTA GLB APENAS SE FOR MESH
    if obj.type == "MESH":
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        model_filename = f"{obj.name}.glb"
        model_path = os.path.join("models", model_filename)

        bpy.ops.export_scene.gltf(
            filepath=os.path.join(MODELS_DIR, model_filename),
            export_format='GLB',
            use_selection=True,
            export_apply=True
        )

    objects_data.append({
        "name": obj.name,
        "type": obj.get("type", "static"),
        "model": model_path,  # null para EMPTY
        "position": {
            "x": obj.location.x,
            "y": obj.location.z,   # Z → Y (raylib)
            "z": obj.location.y
        },
        "rotation": {
            "x": obj.rotation_euler.x,
            "y": obj.rotation_euler.z,
            "z": obj.rotation_euler.y
        },
        "scale": {
            "x": obj.scale.x,
            "y": obj.scale.z,
            "z": obj.scale.y
        }
    })

# Restaura seleção
bpy.ops.object.select_all(action='DESELECT')
for obj in original_selection:
    obj.select_set(True)
bpy.context.view_layer.objects.active = original_active

# Exporta JSON
json_path = os.path.join(BASE_PATH, "level.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(objects_data, f, indent=4)

print("✔ Level.json e modelos .glb exportados com sucesso!")