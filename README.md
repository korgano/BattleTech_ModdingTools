# BattleTech_ModdingTools
Python scripts and other tools for HBS BattleTech modding. Run in PyCharm or other IDE configured to run Python 3+.

## Pilot Generator

Python script to create bare minimum PilotDef files. Intended for generating NPC pilots.

## BT Ability List Generator

Python script to come up with lists of traits and combinations of skills for Abilifier/[Skill Tree Rebuild](https://github.com/korgano/SkillTreeRebuild). Requires `Skill_List.json` file that contains SimGameConstant data in the following format:

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

Currently contains certain hard coded elements specific to Skill Tree Rebuild in results generation process.

## Faction Generator

Python script for generating `Faction.json` entries and a list of generated faction names. **DOES NOT** generate `faction_NAME.json` files.

Creates an appendable list that contains all factions/faction names generated.

## Credits and Attributions

Scripts/tools by korgano
* Pilot Generator
* BT Ability List Generator
* Faction Generator

Scripts/tools by lanleonheart 
* 

All code provided free of charge for the mod community. Contributions of new code/tools are encouraged!
