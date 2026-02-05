from pyray import *
import json

with open("level.json") as f:
    level = json.load(f)

models_cache = {}

for obj in level:
    if obj["model"]:
        if obj["model"] not in models_cache:
            models_cache[obj["model"]] = load_model(obj["model"])

        model = models_cache[obj["model"]]

        pos = obj["position"]
        draw_model(
            model,
            Vector3(pos["x"], pos["y"], pos["z"]),
            1.0,
            WHITE
        )
