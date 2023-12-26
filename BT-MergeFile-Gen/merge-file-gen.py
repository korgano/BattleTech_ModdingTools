import json
import os

# Define the dictionary
tag_dict = {
    'vehicledef': 'VehicleTags',
    'mechdef': 'MechTags',
    'Weapon': 'ComponentTags', #Weapon = key, WeaponDef = overall type
    'pilot': 'PilotTags',
    'lancedef': 'LanceTags',
    'Gear': 'ComponentTags'
}

# Ask for the filename
filename = input("Enter the filename: ")

# Check if the file exists before opening it
if not os.path.isfile(filename):
    print(f"The file {filename} does not exist.")
else:
    try:
        # Open the file
        with open(filename, 'r') as file:
            # Read the lines from the file
            lines = file.readlines()

            # Determine the dictionary association to use
            #association = tag_dict.get(lines[0].strip())
            # Determine the dictionary association to use
            key = lines[0].strip().split('_')[0]
            association = tag_dict.get(key)

            # Generate JSONs for each line in the file
            for line in lines:
                line = line.strip()
                # Create the JSON object
                json_obj = {
                    "TargetID": line,
                    "Instructions": [
                        {
                            "JSONPath": f"{association}.items",
                            "Action": "ArrayAdd",
                            "Value": []
                        }
                    ]
                }

                # Save the JSON object to a file
                with open(f"{line}.json", 'w') as json_file:
                    json.dump(json_obj, json_file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")
