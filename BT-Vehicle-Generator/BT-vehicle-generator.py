import json

# Prompt the user for input
Id = input("Enter Id (automatically adds vehicledef_): ")
Name = input("Enter Name: ")
Details = input("Enter Details: ")
ChassisID = input("Enter ChassisID (automatically add vehiclechassisdef_): ")

# Automatically append prefixes to Id and ChassisID
Id = "vehicledef_" + Id
ChassisID = "vehiclechassisdef_" + ChassisID

# Only populate VehicleTags with "unit_vehicle"
VehicleTags = {
    "items": ["unit_vehicle"],
    "tagSetSourceFile": ""
}

# Use 00 for cost
cost = 00

# Use 00 to populate all armor values
armor_value = 00
Locations = [
    {"Location": loc, "CurrentArmor": armor_value, "CurrentInternalStructure": 00, "AssignedArmor": armor_value, "DamageLevel": "Functional"}
    for loc in ["Front", "Left", "Right", "Rear", "Turret"]
]

# Prompt user for number of Inventory items
num_weapons = int(input("Enter number of Inventory items that are weapons: "))
num_ammo_gear = int(input("Enter number of Inventory items that are Ammunition or Gear: "))

# Generate all Inventory items with blank ComponentDefID
Inventory = []
for i in range(num_weapons):
    Inventory.append({"ComponentDefID": "", "ComponentDefType": "Weapon", "MountedLocation": "Turret|Front", "HardpointSlot": i, "DamageLevel": "Functional"})

for i in range(num_ammo_gear):
    Inventory.append({"ComponentDefID": "", "ComponentDefType": "AmmunitionBox|HeatSink|Upgrade", "MountedLocation": "Front|Rear", "HardpointSlot": -1, "DamageLevel": "Functional"})

# Create the JSON data
data = {
    "Version": 1,
    "Description": {
        "Id": Id,
        "Name": Name,
        "Details": Details,
        "Icon": "",
        "Cost": cost,
        "Rarity": 0,
        "Purchasable": False
    },
    "ChassisID": ChassisID,
    "VehicleTags": VehicleTags,
    "Locations": Locations,
    "Inventory": Inventory
}

# Convert the data to a JSON string
json_data = json.dumps(data, indent=3)

# Write the data to a JSON file
with open(f"{Id}.json", "w") as file:
    file.write(json_data)

print(f"Data successfully written to {Id}.json")
