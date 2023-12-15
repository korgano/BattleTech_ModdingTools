import json

# Prompt the user for input
Id = "pilot_" + input("Enter Id (automatically prefixed with 'pilot_'): ")
Name = input("Enter Name: ")
FirstName = input("Enter FirstName: ")
LastName = input("Enter LastName: ")
Callsign = input("Enter Callsign: ")
Gender = input("Enter Gender: ")
Age = int(input("Enter Age: "))  # Convert the input to an integer

# Validate the Age input
while True:
    try:
        Age = int(input("Enter Age: "))  # Convert the input to an integer
        if Age < 0:
            print("Age must be a positive integer. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer for Age.")

# Create a dictionary with the specified format
data = {
    "Description": {
        "Id": Id,
        "Name": Name,
        "FirstName": FirstName,
        "LastName": LastName,
        "Callsign": Callsign,
        "Gender": Gender,
        "factionID": "INVALID_UNSET",
        "Age": Age,
        "Details": "A generic pilot with average skills",
        "Icon": ""
    },
    "BaseGunnery": 0,
    "BonusGunnery": 0,
    "BasePiloting": 0,
    "BonusPiloting": 0,
    "BaseGuts": 0,
    "BonusGuts": 0,
    "BaseTactics": 0,
    "BonusTactics": 0,
    "ExperienceUnspent": 0,
    "ExperienceSpent": 0,
    "Injuries": 0,
    "Health": 3,
    "LethalInjury": False,
    "Incapacitated": False,
    "Morale": 0,
    "Voice": "",
    "abilityDefNames": [],
    "AIPersonality": "Undefined",
    "PilotTags": {
        "items": [],
        "tagSetSourceFile": ""
    },
    "PilotCost": 0
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data, indent=4)

# Assuming Id is defined and contains the desired filename
filename = f'{Id}.json'

# Write the JSON string to a file
with open(filename, 'w') as f:
    f.write(json_data)
