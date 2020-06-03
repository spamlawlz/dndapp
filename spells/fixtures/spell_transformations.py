# import json, os
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# myfile = os.path.join(THIS_FOLDER, 'spells.json')

# with open(myfile, 'r') as f:
#     spells = json.load(f)

# new_list = []
# i = 1
# for spell in spells:
#     new_list.append({'model': 'spells.Spell', 'pk': i, 'fields': spell})
#     i += 1

# with open(myfile, 'w') as f:
#     json.dump(new_list, f, indent=2)