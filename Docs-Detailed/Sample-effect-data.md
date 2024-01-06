# How to Use the Status Effect Generator

Here's a sample of code generated with the Status Effect generator, with a brief summary of the options.

## Complete Status Effect

```
{
    "durationData": {
        "duration": 1,
        "ticksOnActivations": false,
        "useActivationsOfTarget": false,
        "ticksOnEndOfRound": false,
        "ticksOnMovements": false,
        "stackLimit": 1,
        "clearedWhenAttacked": false
    },
    "targetingData": {
        "effectTriggerType": "Passive",
        "triggerLimit": 1,
        "extendDurationOnTrigger": 0,
        "specialRules": "NotSet",
        "effectTargetType": "NotSet",
        "range": 0,
        "forcePathRebuild": false,
        "forceVisRebuild": false,
        "showInTargetPreview": false,
        "showInStatusPanel": false
    },
    "effectType": "StatisticEffect",
    "Description": {
        "Id": "StatusEffect-Sample-Effect",
        "Name": "SAMPLE EFFECT",
        "Details": "Demo code of a status effect.",
        "Icon": "uixSvgIcon_DemoIcon"
    },
    "nature": "Buff",
    "statisticData": {
        "appliesEachTick": false,
        "statName": "Name a stat.",
        "modType": "System.Single",
        "operation": "Set",
        "modValue": "0",
        "additionalRules": "NotSet",
        "targetCollection": "NotSet",
        "targetWeaponCategory": "NotSet",
        "targetWeaponType": "NotSet",
        "targetAmmoCategory": "NotSet",
        "targetWeaponSubType": "NotSet"
    },
    "tagData": "null",
    "floatieData": "null",
    "actorBurningData": "null",
    "vfxData": "null",
    "instantModData": "null",
    "poorlyMaintainedEffectData": "null"
}
```

## DurationData

```
"durationData": {
        "duration": 1,
        "ticksOnActivations": false,
        "useActivationsOfTarget": false,
        "ticksOnEndOfRound": false,
        "ticksOnMovements": false,
        "stackLimit": 1,
        "clearedWhenAttacked": false
    },
```

- `Duration`: -1 = infinite duration, 0 = no duration, anything greater than 1 is the exact amount of turns the StatusEffect will last.
- `ticksOnActivations`: `true` or `false`, start duration turn count at unit activation?
- `useActivationsOfTarget`: `true` or `false`, start duration count at activation of target?
- `ticksOnEndOfRound`: `true` or `false`, start duration count at end of turn?
- `ticksOnMovements`: `true` or `false`, start duration count when unit moves?
- `stackLimit`: -1 = infinite stacking, 0 = no stacking, 1 or greater is the amount of times the same effect can be applied to one unit
- `clearedWhenAttacked`: `true` or `false`, removes effect when unit possessing it is attacked

## TargetingData

```
"targetingData": {
        "effectTriggerType": "Passive",
        "triggerLimit": 1,
        "extendDurationOnTrigger": 0,
        "specialRules": "NotSet",
        "effectTargetType": "NotSet",
        "range": 0,
        "forcePathRebuild": false,
        "forceVisRebuild": false,
        "showInTargetPreview": false,
        "showInStatusPanel": false
    },
```

- `effectTriggerType`: `Passive|OnActivation|OnHit|OnDamaged|OnWeaponFire|OnUnitActivationBegin|OnUnitActivationBeginOrEnd|OnUnitActivationEnd|TurnUpdate|Preview` - OnHit = hitting enemy unit, OnDamaged = source getting damaged
- `triggerLimit`: -1 = infinite trigger amounts, 0 = no trigger, 1 or greater is the amount of times the same effect can be activated
- `extendDurationOnTrigger"`: How many extra turns to add once effect is triggered
- `specialRules`: `NotSet|LoneWolf|LanceMate|Rally|Retreat|Strafe|Artillery|SpawnTurret|Aura|OnInjured|OnReserve|OnDoneWithMech|HalfArmorOrLess` - `Rally|Retreat|Strafe|Artillery|SpawnTurret` may not be functional
- `effectTargetType`: `NotSet|Creator|SingleTarget|LanceMatesWithinRange|AlliesWithinRange|EnemiesWithinRange|AllLanceMates|AllAllies|AllEnemies` - SingleTarget is Sensor Lock targeting method
- `range`: Numerical value in meters?
- `forcePathRebuild`: Rebuild movement pathing?
- `forceVisRebuild`: Rebuild visualization
- `showInTargetPreview`: Show under target information panel
- `showInStatusPanel`: Show in right side panel below evasion

## effectType

Options: 

- `NotSet`: Non-functional?
- `StatisticEffect`: Main effect type, handles changes to stats
- `TagEffect`: Non-functional?
- `ActorBurningEffect`: Add burning effect to target, non-functional?
- `VFXEffect`: Add specific visual effect to target, used for TAG and NARC
- `InstantModEffect`: Non-functional?
- `PoorlyMaintainedEffect`: Applies debuffs to simulate old gear, non-functional/handled by unit tags?
- `FloatieEffect`: Adds pop-up text label for effect
- `ActiveAbility`: Sensor Lock only?

## Description

```
"Description": {
        "Id": "StatusEffect-Sample-Effect",
        "Name": "SAMPLE EFFECT",
        "Details": "Demo code of a status effect.",
        "Icon": "uixSvgIcon_DemoIcon"
    },
```

- `Id`: Used to track duration/stacking/targeting of `StatusEffect`, shows up in certain logs 
- `Name`: Shows up in `CombatLog.AbilitiesAndEffects` log entries
- `Details`: String of text that shows up in Status Panel and Target Preview
- `Icon`: Optional, SVG image that shows up in Status Panel and Target Preview

## Nature

Options:
- Buff: Improves unit stats
- Debuff: Degrades unit stats

## statisticData

```
"statisticData": {
        "appliesEachTick": false,
        "statName": "Name a stat.",
        "modType": "System.Single",
        "operation": "Set",
        "modValue": 0,
        "additionalRules": "NotSet",
        "targetCollection": "NotSet",
        "targetWeaponCategory": "NotSet",
        "targetWeaponType": "NotSet",
        "targetAmmoCategory": "NotSet",
        "targetWeaponSubType": "NotSet"
    },
```

- `appliesEachTick`: `true` or `false`, presumably non-functional without Duration tick options
- `statName`: The name of the stat you want to modify. [Non-comprehensive list at BattleTech Paradox forums.](https://forum.paradoxplaza.com/forum/threads/study-on-statuseffects-statisticdata.1110871/)
- `modType`: `System.Boolean|System.Int32|System.Single|System.Double|System.String` - whichever option you pick determines the options you have for the `operation` field
- `operation`: For All: `Set`; For Boolean: `Bool_Equals, Bool_NotEquals`; For Int32: `Int_Add, Int_Subtract, Int_Multiply, Int_Divide`; For Single and Double: `Float_Add, Float_Subtract, Float_Multiply, Float_Divide`; For String: `String_Append`
- `additionalRules`: Non-functional, use NotSet
- `targetCollection`: `NotSet|Pilot|Weapon|AmmoBox|SingleRandomWeapon|StrongestWeapon` - Optional, use to apply effect to MechWarrior/Pilot or specific Mech component
- `targetWeaponCategory`: `NotSet|Ballistic|Energy|Missile|AntiPersonnel (Support)|AMS|Melee` - Optional - use only with `AmmoBox` or Weapon `TargetCollections`, AMS is non-functional, leave out ` (Support)`
- `targetWeaponType`: `NotSet|Autocannon|Gauss|Laser|LRM|SRM|Flame|MachineGun|Melee|AMS|COIL` - Optional, use only with Weapon `TargetCollections`
- `targetAmmoCategory`: `NotSet|AC2|AC5|AC10|AC20|LRM|SRM|MG|AMS|GAUSS|Flamer` - only necessary for ammo using weapons, use NotSet for energy weapons
- `targetWeaponSubType`: `NotSet|AC2|AC5|AC10|AC20|Gauss|SmallLaser|MediumLaser|LargeLaser|PPC|LRM5|LRM10|LRM15|LRM20|SRM2|SRM4|SRM6|Flamer|MachineGun|Melee|AMS|DFA|AIImaginary|SmallLaserPulse|MediumLaserPulse|LargeLaserPulse|SmallLaserER|MediumLaserER|LargeLaserER|PPCER|UAC2|UAC5|UAC10|UAC20|LB2X|LB5X|LB10X|LB20X|SRMInferno|SRMInferno|Narc|PPCSnub|TAG|COILS|COILM|COILM` - Optional, use only with Weapon `TargetCollections`

## Optional Elements

```
    "tagData": "null",
    "floatieData": "null",
    "actorBurningData": "null",
    "vfxData": "null",
    "instantModData": "null",
    "poorlyMaintainedEffectData": "null"
```

Can be omitted from most StatusEffects. [Samples of vfxData and floatieData available on the full effectType breakdown page.](./Status-Effect-Parts/Effect-type.md)

## How to Approach Making a Status Effect

Making a status effect for your mod is not a difficult process with the Python script, but does require some foresight going in. Make sure you know the following things going in:

- Will the effect tick on Activation (of the target), end of round, or movement?
- What effectTriggerType will you use?
- Will you use SpecialRules? If so, which one?
- What effectTargetType will you use?
- What ID will you use for your status effect?
- If you have multiple similar effects on a component/in an ability, are the names distinct?
- Will you use an icon for the effect?
- What stat will you change?
- What modType is that stat, and how will you change it?
- Do you need to use the TargetCollections, or can you skip them? 

In terms of tweaking values, 

---

Return to [Repo Landing Page](/README.md)