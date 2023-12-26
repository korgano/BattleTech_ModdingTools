import json

def get_bool(prompt):
    while True:
        try:
            return {"true": True, "false": False}[input(prompt).lower()]
        except KeyError:
            print("Invalid input! Please enter True or False.")

def get_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(template.format(" or ".join(map(str, range_))))
        else:
            return ui

data = {
    "durationData": {
        "duration": get_input("Enter duration (# of turns, -1 = infinite): ", int, 0),
        "ticksOnActivations": get_bool("Enter ticks on activations (True/False): "),
        "useActivationsOfTarget": get_bool("Enter use activations of target (True/False): "),
        "ticksOnEndOfRound": get_bool("Enter ticks on end of round (True/False): "),
        "ticksOnMovements": get_bool("Enter ticks on movements (True/False): "),
        "stackLimit": get_input("Enter stack limit (# of applications per enemy, -1 = infinite): ", int, -1),
        "clearedWhenAttacked": get_bool("Enter cleared when attacked (True/False): ")
    },
    "targetingData": {
        "effectTriggerType": get_input("Enter effect trigger type (Passive|OnActivation|OnHit|OnDamaged|OnWeaponFire|OnUnitActivationBegin|OnUnitActivationBegin|OnUnitActivationEnd|TurnUpdate|Preview): "),
        "triggerLimit": get_input("Enter trigger limit (# of activations per enemy): ", int, 0),
        "extendDurationOnTrigger": get_input("Enter extend duration on trigger (# of turns): ", int, 0),
        "specialRules": get_input("Enter special rules (NotSet|LoneWolf|LanceMate|Rally|Retreat|Strafe|Artillery|SpawnTurret|Aura|OnInjured|OnReserve|OnDoneWithMech|HalfArmorOrLess): "),
        "effectTargetType": get_input("Enter effect target type (NotSet|Creator|SingleTarget|LanceMatesWithinRange|AlliesWithinRange|EnemiesWithinRange|AllLanceMates|AllAllies|AllEnemies): "),
        "range": get_input("Enter range: ", int, 0),
        "forcePathRebuild": get_bool("Enter force path rebuild (True/False): "),
        "forceVisRebuild": get_bool("Enter force vis rebuild (True/False): "),
        "showInTargetPreview": get_bool("Enter show in target preview (True/False): "),
        "showInStatusPanel": get_bool("Enter show in status panel (True/False): ")
    },
    "effectType": get_input("Enter effect type (NotSet|StatisticEffect|TagEffect|ActorBurningEffect|VFXEffect|InstantModEffect|PoorlyMaintainedEffect|FloatieEffect|ActiveAbility): "),
    "Description": {
        "Id": "StatusEffect-" + get_input("Enter Id (automatically prefixed with StatusEffect-): "),
        "Name": get_input("Enter name: "),
        "Details": get_input("Enter details: "),
        "Icon": "uixSvgIcon_" + get_input("Enter icon: ")
    },
    "nature": get_input("Enter nature (Buff|Debuff): "),
    "statisticData": {
        "appliesEachTick": get_bool("Enter applies each tick (True/False): "),
        "statName": get_input("Enter stat name: "),
        "modType": get_input("Enter mod type (System.Boolean|System.Int32|System.Single|System.Double|System.String): "),
        "operation": get_input("Enter operation (For Boolean: Bool_Equals, Bool_NotEquals, Bool_Set; For Int32: Int_Add, Int_Subtract, Int_Multiply, Int_Divide, Int_Set; For Single and Double: Float_Add, Float_Subtract, Float_Multiply, Float_Divide, Float_Set; For String: String_Set, String_Append): "),
        "modValue": get_input("Enter mod value (bool (true or false)|int (whole #)|float & double (decimal #)|string (text)): "),
        "additionalRules": get_input("Enter Additional Rules (default = NotSet, no known function): "),
        "targetCollection": get_input("Enter item collection (NotSet|Pilot|Weapon|AmmoBox|SingleRandomWeapon|StrongestWeapon): "),
        "targetWeaponCategory": get_input("Enter Weapon Category (NotSet|Ballistic|Energy|Missile|AntiPersonnel (Support)|AMS|Melee): "),
        "targetWeaponType": get_input("Enter Weapon Type (NotSet|Autocannon|Gauss|Laser|LRM|SRM|Flame|MachineGun|Melee|AMS|COIL): "),
        "targetAmmoCategory": get_input("Enter AmmoCategory name (NotSet|AC2|AC5|AC10|AC20|LRM|SRM|MG|AMS|GAUSS|Flamer): "),
        "targetWeaponSubType": get_input("Enter SubType name (NotSet|AC2|AC5|AC10|AC20|Gauss|SmallLaser|MediumLaser|LargeLaser|PPC|LRM5|LRM10|LRM15|LRM20|SRM2|SRM4|SRM6|Flamer|MachineGun|Melee|AMS|DFA|AIImaginary|SmallLaserPulse|MediumLaserPulse|LargeLaserPulse|SmallLaserER|MediumLaserER|LargeLaserER|PPCER|UAC2|UAC5|UAC10|UAC20|LB2X|LB5X|LB10X|LB20X|SRMInferno|SRMInferno|Narc|PPCSnub|TAG|COILS|COILM|COILM): ")
    },
    "tagData": get_input("Enter tag data: "),
    "floatieData": get_input("Enter floatie data: "),
    "actorBurningData": get_input("Enter actor burning data: "),
    "vfxData": get_input("Enter vfx data: "),
    "instantModData": get_input("Enter instant mod data: "),
    "poorlyMaintainedEffectData": get_input("Enter poorly maintained effect data: ")
}

filename = data["Description"]["Id"] + ".json"
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Data saved to {filename}")
