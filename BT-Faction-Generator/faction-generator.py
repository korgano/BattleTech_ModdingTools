import json

# Define the keys for boolean fields
boolean_keys = ["IsRealFaction", "IsGreatHouse", "IsClan", "IsMercenary", "IsPirate", "DoesGainReputation", "CanAlly", "IsProceduralContractFaction", "IsCareerScoringFaction", "IsCareerIgnoredContractTarget", "IsCareerStartingDisplayFaction", "IsStoryStartingDisplayFaction", "HasAIBehaviorVariableScope"]

# Initialize an empty dictionary to hold the data
data = {}

# Prompt for ID
data["ID"] = int(input("Enter ID (Leave at 0 for game auto-numbering, or assign value greater than 0): "))

# Prompt for Name
data["Name"] = input("Enter Name (Computer Friendly Name - No spaces, capitalize first letter of each word): ")

# Generate FactionDefID based on Name
data["FactionDefID"] = "faction_" + data["Name"]

# Prompt for FriendlyName
data["FriendlyName"] = input("Enter FriendlyName (In-Game text name): ")

# Prompt for Description
data["Description"] = input("Enter Description: ")

# Prompt for boolean fields
for key in boolean_keys:
    while True:
        value = input(f"Enter {key} (True or False): ")
        if value.lower() not in ["true", "false"]:
            print("Invalid input. Please enter True or False.")
        else:
            data[key] = value.lower() == "true"
            break

# Convert the data to JSON
json_data = json.dumps(data, indent=4)

# Write the data to a file
with open("Factions-Generator.txt", "a") as file:
    file.write(json_data + ",\n")

# Write the FactionDefID to another file
with open("FactionNames.txt", "a") as file:
    file.write(data["Name"] + "\n")

print("Data successfully written to Factions-Generator.txt and FactionIDs.txt")
