#!/usr/bin/env python3

import json
import os

dependencies = {}

for root, dirs, files in os.walk("/usr/local/mecca_head/mecca/"):
    for file in files:
        if file == "depends.opt":
            with open(os.path.join(root, file), 'r') as f:
                project = os.path.basename(root)
                dependencies[project] = f.read().splitlines()

# Print the dependencies
for project, deps in dependencies.items():
    print(f"{project} depends on: {', '.join(deps)}")

# Write the dependencies to a JSON file
with open('dependencies.json', 'w') as fp:
    json.dump(dependencies, fp, indent=4)

