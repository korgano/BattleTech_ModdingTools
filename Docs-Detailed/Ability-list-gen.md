# BT Ability List Generator Details

## Functional Requirements

The Ability List Generator requires a `Skill_List.json` file that contains SimGameConstant data in the following format:

```
{
"Progression" : {
    "GunnerySkills" :{
        "Level 1": [
            "TraitDefWeaponHit1"
        ],
        "Level 2": [
            "AbilityDef_MultiTarget",
            "TraitDefWeaponHit2"
        ],
        "Level 3": [
            "TraitDefWeaponHit3"
        ],
        "Level 4": [
            "AbilityDef_CIFS",
            "AbilityDef_Missileer",
            "AbilityDef_Suppression",
            "TraitDefWeaponHit4"
        ],
        "Level 5": [
            "TraitDefWeaponHit5",
            "TraitDefWeaponHit5b"				
        ],
        "Level 6": [
            "AbilityDef_ClosePersonal",
            "AbilityDef_JackAll",
            "AbilityDef_Longshot",
            "TraitDefWeaponHit6"
        ],
        "Level 7": [
            "TraitDefWeaponHit7"
        ],
        "Level 8": [
            "TraitDefWeaponHit8",
            "AbilityDef_Overclock",
            "AbilityDef_TargetFiring"		
        ],
        "Level 9": [
            "TraitDefWeaponHit9"
        ],
        "Level 10": [
            "TraitDefWeaponHit10",
            "TraitDefWeaponHit10b"            
        ]
    },
...
}
}
```

All `____Skills` entries **MUST** be within `{}` for the JSON parser to process the data without an error. Using the game standard format below **WILL** cause an error:

```
"Progression" : {
    "GunnerySkills" :[
        [
            "TraitDefWeaponHit1"
        ],
        [
            "AbilityDef_MultiTarget",
            "TraitDefWeaponHit2"
        ],
        [
            "TraitDefWeaponHit3"
        ],
        [
            "AbilityDef_CIFS",
            "AbilityDef_Missileer",
            "AbilityDef_Suppression",
            "TraitDefWeaponHit4"
        ],
        [
            "TraitDefWeaponHit5",
            "TraitDefWeaponHit5b"				
        ],
        [
            "AbilityDef_ClosePersonal",
            "AbilityDef_JackAll",
            "AbilityDef_Longshot",
            "TraitDefWeaponHit6"
        ],
        [
            "TraitDefWeaponHit7"
        ],
        [
            "TraitDefWeaponHit8",
            "AbilityDef_Overclock",
            "AbilityDef_TargetFiring"		
        ],
        [
            "TraitDefWeaponHit9"
        ],
        [
            "TraitDefWeaponHit10",
            "TraitDefWeaponHit10b"            
        ]
    ],
```

## Output Formating

Generated output is as follows:

```
Valid Traits:
TraitDefWeaponHit1
TraitDefWeaponHit2
TraitDefWeaponHit3
TraitDefWeaponHit4
TraitDefWeaponHit5
TraitDefWeaponHit5b
TraitDefWeaponHit6
TraitDefMeleeHit1
TraitDefMeleeHit2
TraitDefUnsteadySet60
TraitDefMeleeHit3
TraitDefMeleeHit4
TraitDefMeleeHit5
TraitDefEvasionBoost
TraitDefEvasiveChargeAddOne
TraitDefMeleeHit6
TraitDefHealthAddOne
TraitDefRefireReduceOne
TraitDefBerserkHitDefense
TraitDefIndirectReduceOne
TraitDefMinRangeReduce45
TraitDefSpotterProficiency
TraitDefCalledShotImprove

Possible Combinations of Abilities:
('AbilityDefT5A', 'AbilityDef_MultiTarget')
('AbilityDef_ClosePersonal', 'AbilityDef_DodgeMaster')
('AbilityDef_ClosePersonal', 'AbilityDef_JumpMaven')
('AbilityDef_JackAll', 'AbilityDef_DodgeMaster')
('AbilityDef_JackAll', 'AbilityDef_JumpMaven')
('AbilityDef_Longshot', 'AbilityDef_DodgeMaster')
('AbilityDef_Longshot', 'AbilityDef_JumpMaven')
('AbilityDef_DodgeMaster', 'AbilityDef_ClosePersonal')
('AbilityDef_DodgeMaster', 'AbilityDef_JackAll')
('AbilityDef_DodgeMaster', 'AbilityDef_Longshot')
('AbilityDef_JumpMaven', 'AbilityDef_ClosePersonal')
('AbilityDef_JumpMaven', 'AbilityDef_JackAll')
('AbilityDef_JumpMaven', 'AbilityDef_Longshot')
```

All traits up to the specified levels will be added to the file. `('AbilityDefT5A', 'AbilityDef_MultiTarget')` are hardcoded to appear at the top of the list at Level 2+ and are specific to Skill Tree Rebuild's skill tree.

**NOTE:** For NPC pilots, only include the `TraitDefWeaponHit`/`TraitDefMeleeHit` entries that are absolutely necessary. These are typically the highest numerical value ones, but any `TraitDef` file that contains a `StatusEffect` should be included in the `PilotDef` ability list. **ESPECIALLY** if the pilot is being created for Skirmish mode.

(Abilifier/Skill Tree Rebuild automatically appends traits to campaign/career mode NPC pilots based on their levels and the skill list.)