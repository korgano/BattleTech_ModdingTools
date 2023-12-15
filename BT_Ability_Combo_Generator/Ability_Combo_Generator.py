import json
import itertools
from collections import defaultdict

# Load JSON data
with open('Skill_List.json') as f:
    data = json.load(f)

# Convert data into a dictionary
skills_dict = defaultdict(lambda: defaultdict(list))
for category, levels in data['Progression'].items():
    for level, traits in levels.items():
        for trait in traits:
            if 'TraitDef' in trait:
                skills_dict[category][int(level.split()[-1])].append(('Trait', trait))
            elif 'AbilityDef' in trait:
                skills_dict[category][int(level.split()[-1])].append(('Ability', trait))

# Get user input and validate
user_levels = {}
for category in skills_dict.keys():
    while True:
        level = input(f"Enter desired level for {category}: ")
        if level.isdigit():
            user_levels[category] = int(level)
            break
        else:
            print("Invalid input. Please enter an integer.")

# Generate list of valid Traits
valid_traits = []
for category, user_level in user_levels.items():
    for level in range(1, user_level + 1):
        valid_traits.extend([trait for trait_type, trait in skills_dict[category][level] if trait_type == 'Trait'])

# Generate list of all possible combinations of abilities
valid_abilities = []
category_level_abilities = {}
combinations = []

if all(level >= 2 for level in user_levels.values()):
    combinations.append(('AbilityDefT5A', 'AbilityDef_MultiTarget'))

for category, level in user_levels.items():
    if level > 3:
        abilities = [ability for ability_type, ability in skills_dict[category][level] if ability_type == 'Ability']
        # Remove 'AbilityDefT5A' and 'AbilityDef_MultiTarget' if they are already in the list
        abilities = [ability for ability in abilities if ability not in ['AbilityDefT5A', 'AbilityDef_MultiTarget']]
        category_level_abilities[(category, level)] = abilities

for (category1, level1), abilities1 in category_level_abilities.items():
    for ability1 in abilities1:
        for (category2, level2), abilities2 in category_level_abilities.items():
            if (category1, level1) != (category2, level2):  # Ensure abilities are from different categories and levels
                for ability2 in abilities2:
                    combinations.append((ability1, ability2))

# Filter combinations to ensure ('AbilityDefT5A', 'AbilityDef_MultiTarget') is the only combination of those two abilities
combinations = [combo for combo in combinations if set(combo) != set(['AbilityDefT5A', 'AbilityDef_MultiTarget']) or combo == ('AbilityDefT5A', 'AbilityDef_MultiTarget')]

# Your code for writing the output to a .TXT file goes here
    #Generate filename
filename = f"Ability_Combo_Gun{user_levels['GunnerySkills']}_P{user_levels['PilotingSkills']}_Guts{user_levels['GutsSkills']}_T{user_levels['TacticsSkills']}.txt"

# Output both lists to a .TXT output file
with open(filename, 'w') as f:
    f.write("Valid Traits:\n")
    for trait in valid_traits:
        f.write(f"{trait}\n")
    f.write("\nPossible Combinations of Abilities:\n")
    for combo in combinations:
        f.write(f"{combo}\n")
