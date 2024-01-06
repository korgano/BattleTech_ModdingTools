# BattleTech_ModdingTools
Python scripts and other tools for HBS BattleTech modding. Run in PyCharm or other IDE configured to run Python 3+.

## Pilot Generator

Python script to create bare minimum PilotDef files. Intended for generating NPC pilots.

## BT Ability List Generator

Python script to come up with lists of traits and combinations of skills for Abilifier/[Skill Tree Rebuild](https://github.com/korgano/SkillTreeRebuild). [Requires `Skill_List.json` file that contains SimGameConstant data a specific format](Docs-Detailed/Ability-list-gen.md).

Currently contains certain hard coded elements specific to Skill Tree Rebuild in results generation process.

## Faction Generator

Python script for generating `Faction.json` entries and a list of generated faction names. **DOES NOT** generate `faction_NAME.json` files.

Creates an appendable list that contains all factions/faction names generated. For best results, [read the Faction Generation Information documentation](Docs-Detailed/Faction-gen-info.md).

## VehicleDef Generator

Python script for generating `VehicleDef` JSON files. Auto-populates numerical fields with `00` and prompts user for specific vehicle data, as well as number and type of inventory slots (weapons or other items).

## CastDef Generator

Python script for creating basic `CastDef` JSON file for use in Flashpoints and other narrative content that require specific characters. Prompts users for most fields, set certain ones to `true` or `false` to affect how the name is displayed in-game.

## Merge File Generator

Python script for generating files to add data to existing JSONs through ModTek Advanced JSON Merging. Currently configured to add tags to specific `Def` files.

## StatusEffect Generator

Python Script for generating `StatusEffect` JSON data for AbilityDef, TraitDef, ComponentDef, and WeaponDef files. Shows user all possible options for specific configuration of specific fields. Mainly intended for use with `StatisticEffect` type `StatusEffects`, due to general rarity of other effect types.

For detailed information on how the `StatusEffect` data is organized, read [likwueron's analysis](https://forum.paradoxplaza.com/forum/threads/study-on-statuseffects-statisticdata.1110871/) and [check out the detailed breakdown of the game code](Docs-Detailed/Status-effects-info).

## Log Cleaner Script

PowerShell script for pulling specific log strings from the ModTek `battletech-log.txt file`. Replace sections in [] brackets with desired file paths or text strings you want to match.

## Credits and Attributions

Scripts/tools by korgano
* Pilot Generator
* BT Ability List Generator
* Faction Generator
* VehicleDef Generator
* CastDef Generator
* Merge File Generator
* StatusEffect Generator
* Log Cleaner Script

Scripts/tools by lanleonheart 
* 

All code provided free of charge for the mod community. Contributions of new code/tools are encouraged!
