import json

def prompt_with_default(prompt, default):
    response = input(prompt)
    return response if response else default

try:
    id = prompt_with_default("Enter id (automatically appended with castDef_): ", "")
    id = "castDef_" + id
    firstName = prompt_with_default("Enter firstName: ", None)
    lastName = prompt_with_default("Enter lastName: ", None)
    callsign = prompt_with_default("Enter callsign: ", None)
    rank = prompt_with_default("Enter rank/position: ", None)
    gender = prompt_with_default("Enter gender: ", "UNSET")
    factionID = prompt_with_default("Enter factionID: ", "UNSET")
    sgCharType = prompt_with_default("Enter sgCharType: ", "UNSET")
    showRank = bool(prompt_with_default("Enter showRank (True/False): ", False))
    showFirstName = bool(prompt_with_default("Enter showFirstName (True/False, default false): ", False))
    showCallsign = bool(prompt_with_default("Enter showCallsign (True/False, default false): ", False))
    showLastName = bool(prompt_with_default("Enter showLastName (True/False, default false): ", False))
    localizeName = bool(prompt_with_default("Enter localizeName (True/False, default false): ", False))
    portraitAssetPath = "../../Mods/[ModName]/[Sprite Folder]/guiTxrPort_" + id + ".png"

    data = {
        "id": id,
        "internalName": id.replace("castDef_", ""),
        "firstName": firstName,
        "lastName": lastName,
        "callsign": callsign,
        "rank": rank,
        "gender": gender,
        "factionID": factionID,
        "sgCharType": sgCharType,
        "showRank": showRank,
        "showFirstName": showFirstName,
        "showCallsign": showCallsign,
        "showLastName": showLastName,
        "localizeName": localizeName,
        "defaultEmotePortrait": {
            "emote": "Default",
            "portraitAssetPath": portraitAssetPath
        },
        "emotePotraitList": []
    }

    with open(id + '.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(f"JSON saved to {id}.json")

except Exception as e:
    print(f"An error occurred: {e}")