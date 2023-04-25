import yaml
import copy

with open("rally-k8s/v2/pod_load/template.yaml", "r") as r:
    template = yaml.safe_load(r)

ITER_MAX = 10000
i = 20

print(template)

while i <= 2000:
    current = copy.deepcopy(template["subtasks"][0])
    current["runner"]["rps"]["rps"] = i
    current["runner"]["rps"]["times"] = min(i * 100, ITER_MAX)
    template["subtasks"].append(current)

    if i >= 20 and i < 100:
        i += 10
    elif i >= 100 and i < 200:
        i += 20
    elif i >= 200 and i < 300:
        i += 25
    elif i >= 300 and i < 1000:
        i += 50
    elif i>= 1000 and i < 2000:
        i += 100
    elif i >= 2000:
        break

template["subtasks"].pop(0)
with open("rally-k8s/v2/pod_load/load.yaml", "w") as w:
    yaml.safe_dump(template, w)