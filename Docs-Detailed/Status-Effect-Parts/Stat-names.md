# Stat Names

Here's a list of statistic names that can be changed using StatisticEffects, broken down into categories. Each one will have their appropriate statistic type (Float/Int/bool), name, and default value displayed. If necessary, clarifying notes will follow the default value.

For ease of use and legibility, individual items have been grouped together based on what type of statistic they modify.

**Note:** Several statistics share the same name across categories, and may interact with different unit types differently.

## AbstractActor (Combatants)

- Type: float | Name: "ToHitIndirectModifier", Default Value: 0f
- Type: float | Name: "AccuracyModifier", Default Value: 0f

- Type: bool | Name: "CriticalHitImmunity", Default Value: false
- Type: float | Name: "CriticalHitChanceReceivedMultiplier", Default Value: 1f

- Type: bool | Name: "EvasiveSafeFromSensorLock", Default Value: false - Sensor Lock/Active Probe cannot strip evasion from this unit.
- Type: bool | Name: "IsIndirectImmune", Default Value: false - LRMs cannot hit this unit.
- Type: bool | Name: "KnockdownImmunity", Default Value: false

- Type: float | Name: "CalledShotBonusMultiplier", Default Value: 1f
- Type: float | Name: "WeaponHeatMultiplier", Default Value: 1f
- Type: float | Name: "JumpDistanceMultiplier", Default Value: 1f

- Type: bool | Name: "CanShootAfterSprinting", Default Value: false
- Type: bool | Name: "CanMoveAfterShooting", Default Value: false

- Type: float | Name: "DamageReductionMultiplierAll", Default Value: 1f
- Type: float | Name: "DamageReductionMultiplierMelee", Default Value: 1f
- Type: float | Name: "DamageReductionMultiplierEnergy", Default Value: 1f
- Type: float | Name: "DamageReductionMultiplierBallistic", Default Value: 1f
- Type: float | Name: "DamageReductionMultiplierMissile", Default Value: 1f
- Type: float | Name: "DamageReductionMultiplierAntipersonnel", Default Value: 1f

- Type: bool | Name: "IgnorePilotInjuries", Default Value: false

- Type: float | Name: "ToHitThisActor", Default Value: 0f
- Type: float | Name: "ToHitThisActorBallistic", Default Value: 0f
- Type: float | Name: "ToHitThisActorEnergy", Default Value: 0f
- Type: float | Name: "ToHitThisActorMissile", Default Value: 0f
- Type: float | Name: "ToHitThisActorSmall", Default Value: 0f
- Type: float | Name: "ToHitThisActorMelee", Default Value: 0f
- Type: float | Name: "ToHitThisActorDirectFire", Default Value: 0f

- Type: bool | Name: "IsTargetingDummy", Default Value: false
- Type: bool | Name: "IsCoolantVenting", Default Value: false

- Type: bool | Name: "GuaranteeNextBackHit", Default Value: false - guarantees the next hit to rear of unit with this stat will hit.
- Type: bool | Name: "GuaranteeUnhittable", Default Value: false

- Type: bool | Name: "HasActiveProbe", Default Value: false

- Type: int | Name: "GhostEffectStacks", Default Value: 0
- Type: bool | Name: "HasGhostSpotter", Default Value: false

- Type: int | Name: "MoraleBonusGain", Default Value: 0

- Type: bool | Name: "PrecisionStrike", Default Value: false - provides Breaching Shot, **not** Precision Shot/Called Shot (OffensivePush).

- Type: int | Name: "MaxEvasivePips", Default Value: 6

- Type: bool | Name: "DeferResetsInstability", Default Value: false - Reserving clears stability damage.
- Type: bool | Name: "GuardedIsUpgraded", Default Value: false - Entrenched.
- Type: bool | Name: "GainEntrenchedOnNormalMove", Default Value: false

- Type: int | Name: "PhaseModifier", Default Value: 0
- Type: int | Name: "PhaseModifierSelf", Default Value: 0

## Ammo Box

- Type: int | Name: "CurrentAmmo", Default Value: this.ammunitionBoxDef.Capacity
- Type: int | Name: "AmmoCapacity", Default Value: this.ammunitionBoxDef.Capacity

## Mech

- Type: int | Name: "BaseInitiative", Default Value: base.Initiative
- Type: int | Name: "TurnRadius", Default Value: this.MechDef.Chassis.TurnRadius
- Type: int | Name: "MaxJumpjets", Default Value: this.MechDef.Chassis.MaxJumpjets

- Type: float | Name: "SpotterDistanceMultiplier", Default Value: this.MechDef.Chassis.SpotterDistanceMultiplier
- Type: float | Name: "SpotterDistanceAbsolute", Default Value: 0f
- Type: float | Name: "SpottingVisibilityMultiplier", Default Value: this.MechDef.Chassis.VisibilityMultiplier
- Type: float | Name: "SpottingVisibilityAbsolute", Default Value: 0f

- Type: float | Name: "SensorDistanceMultiplier", Default Value: this.MechDef.Chassis.SensorRangeMultiplier
- Type: float | Name: "SensorDistanceAbsolute", Default Value: 0f
- Type: float | Name: "SensorSignatureModifier", Default Value: this.MechDef.Chassis.Signature

- Type: float | Name: "EngageRangeModifier", Default Value: this.MechDef.Chassis.EngageRangeModifier

- Type: float | Name: "MinStability", Default Value: 0f
- Type: float | Name: "MaxStability", Default Value: this.MechDef.Chassis.Stability
- Type: float | Name: "UnsteadyThreshold", Default Value: base.Combat.Constants.ResolutionConstants.DefaultUnsteadyThreshold
- Type: float | Name: "Stability", Default Value: 0f
- Type: bool | Name: "IsProne", Default Value: false

- Type: int | Name: "MaxHeat", Default Value: base.Combat.Constants.Heat.MaxHeat
- Type: int | Name: "OverheatLevel", Default Value: (int)((float)base.Combat.Constants.Heat.MaxHeat * base.Combat.Constants.Heat.OverheatLevel)
- Type: int | Name: "MinHeatNextActivation", Default Value: -1
- Type: int | Name: "HeatSinkCapacity", Default Value: 0
- Type: bool | Name: "IgnoreHeatToHitPenalties", Default Value: false
- Type: bool | Name: "IgnoreHeatMovementPenalties", Default Value: false
- Type: int | Name: "EndMoveHeat", Default Value: 0
- Type: int | Name: "CurrentHeat", Default Value: 0

- Type: float | Name: "WalkSpeed", Default Value: this.MovementCaps.MaxWalkDistance
- Type: float | Name: "RunSpeed", Default Value: this.MovementCaps.MaxSprintDistance

- Type: float | Name: "DFASelfDamage", Default Value: this.MechDef.Chassis.DFASelfDamage
- Type: bool | Name: "DFACausesSelfUnsteady", Default Value: true
- Type: int | Name: "EvasivePipsGainedAdditional", Default Value: 0
- Type: int | Name: "MeleeHitPushBackPhases", Default Value: 0

- Type: bool | Name: "HeadShotImmunity", Default Value: false

- Type: float | Name: "Head.Armor", Default Value: this.MechDef.Head.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "Head.Structure", Default Value: this.MechDef.Head.CurrentInternalStructure * this.StructureMultiplier

- Type: float | Name: "CenterTorso.Armor", Default Value: this.MechDef.CenterTorso.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "CenterTorso.RearArmor", Default Value: this.MechDef.CenterTorso.AssignedRearArmor * this.ArmorMultiplier
- Type: float | Name: "CenterTorso.Structure", Default Value: this.MechDef.CenterTorso.CurrentInternalStructure * this.StructureMultiplier

- Type: float | Name: "LeftTorso.Armor", Default Value: this.MechDef.LeftTorso.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "LeftTorso.RearArmor", Default Value: this.MechDef.LeftTorso.AssignedRearArmor * this.ArmorMultiplier
- Type: float | Name: "LeftTorso.Structure", Default Value: this.MechDef.LeftTorso.CurrentInternalStructure * this.StructureMultiplier

- Type: float | Name: "RightTorso.Armor", Default Value: this.MechDef.RightTorso.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "RightTorso.RearArmor", Default Value: this.MechDef.RightTorso.AssignedRearArmor * this.ArmorMultiplier
- Type: float | Name: "RightTorso.Structure", Default Value: this.MechDef.RightTorso.CurrentInternalStructure * this.StructureMultiplier

- Type: float | Name: "LeftArm.Armor", Default Value: this.MechDef.LeftArm.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "LeftArm.Structure", Default Value: this.MechDef.LeftArm.CurrentInternalStructure * this.StructureMultiplier

- Type: float | Name: "RightArm.Armor", Default Value: this.MechDef.RightArm.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "RightArm.Structure", Default Value: this.MechDef.RightArm.CurrentInternalStructure * this.StructureMultiplier

- Type: float | Name: "LeftLeg.Armor", Default Value: this.MechDef.LeftLeg.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "LeftLeg.Structure", Default Value: this.MechDef.LeftLeg.CurrentInternalStructure * this.StructureMultiplier

- Type: float | Name: "RightLeg.Armor", Default Value: this.MechDef.RightLeg.AssignedArmor * this.ArmorMultiplier
- Type: float | Name: "RightLeg.Structure", Default Value: this.MechDef.RightLeg.CurrentInternalStructure * this.StructureMultiplier

## Turret

- Type: int | Name: "BaseInitiative", Default Value: base.Initiative

- Type: float | Name: "SpotterDistanceMultiplier", Default Value: this.TurretDef.Chassis.SpotterDistanceMultiplier
- Type: float | Name: "SpotterDistanceAbsolute", Default Value: 0f
- Type: float | Name: "SpottingVisibilityMultiplier", Default Value: this.TurretDef.Chassis.VisibilityMultiplier
- Type: float | Name: "SpottingVisibilityAbsolute", Default Value: 0f

- Type: float | Name: "SensorDistanceMultiplier", Default Value: this.TurretDef.Chassis.SensorRangeMultiplier
- Type: float | Name: "SensorDistanceAbsolute", Default Value: 0f
- Type: float | Name: "SensorSignatureModifier", Default Value: this.TurretDef.Chassis.Signature

## Vehicle

- Type: int | Name: "BaseInitiative", Default Value: base.Initiative
- Type: int | Name: "TurnRadius", Default Value: this.VehicleDef.Chassis.TurnRadius

- Type: float | Name: "SpotterDistanceMultiplier", Default Value: this.VehicleDef.Chassis.SpotterDistanceMultiplier
- Type: float | Name: "SpotterDistanceAbsolute", Default Value: 0f
- Type: float | Name: "SpottingVisibilityMultiplier", Default Value: this.VehicleDef.Chassis.VisibilityMultiplier
- Type: float | Name: "SpottingVisibilityAbsolute", Default Value: 0f

- Type: float | Name: "SensorDistanceMultiplier", Default Value: this.VehicleDef.Chassis.SensorRangeMultiplier
- Type: float | Name: "SensorDistanceAbsolute", Default Value: 0f
- Type: float | Name: "SensorSignatureModifier", Default Value: this.VehicleDef.Chassis.Signature

- Type: float | Name: "CruiseSpeed", Default Value: this.MovementCaps.MaxWalkDistance
- Type: float | Name: "FlankSpeed", Default Value: this.MovementCaps.MaxSprintDistance

## Weapon

- Type: float | Name: "MinRange", Default Value: this.weaponDef.MinRange
- Type: float | Name: "MinRangeMultiplier", Default Value: 1f
- Type: float | Name: "LongRangeModifier", Default Value: 0f
- Type: float | Name: "MaxRange", Default Value: this.weaponDef.MaxRange
- Type: float | Name: "MaxRangeModifier", Default Value: 0f

- Type: float | Name: "ShortRange", Default Value: this.weaponDef.ShortRange
- Type: float | Name: "MediumRange", Default Value: this.weaponDef.MediumRange
- Type: float | Name: "LongRange", Default Value: this.weaponDef.LongRange

- Type: float | Name: "HeatGenerated", Default Value: (float)this.weaponDef.HeatGenerated
- Type: float | Name: "HeatDamageModifier", Default Value: this.weaponDef.HeatDamage

- Type: float | Name: "StructureDamage", Default Value: this.weaponDef.StructureDamage
- Type: float | Name: "CriticalChanceMultiplier", Default Value: this.weaponDef.CriticalChanceMultiplier

- Type: int | Name: "AttackRecoil", Default Value: this.weaponDef.AttackRecoil
- Type: int | Name: "RefireModifier", Default Value: this.weaponDef.RefireModifier

- Type: int | Name: "ShotsWhenFired", Default Value: this.weaponDef.ShotsWhenFired
- Type: int | Name: "ProjectilesPerShot", Default Value: this.weaponDef.ProjectilesPerShot
- Type: int | Name: "VolleyDivisor", Default Value: this.weaponDef.VolleyDivisor

- Type: int | Name: "InternalAmmo", Default Value: this.weaponDef.StartingAmmoCapacity
- Type: float | Name: "EvasivePipsIgnored", Default Value: this.weaponDef.EvasivePipsIgnored
- Type: bool | Name: "TemporarilyDisabled", Default Value: false

- Type: float | Name: "ClusteringModifier", Default Value: this.weaponDef.ClusteringModifier
- Type: float | Name: "JumpingWeaponDamageModifier", Default Value: 1f
- Type: float | Name: "OverheatedDamageMultiplier", Default Value: this.weaponDef.OverheatedDamageMultiplier
- Type: float | Name: "StructureDamagePerShot", Default Value: this.weaponDef.StructureDamage
- Type: float | Name: "HeatDamagePerShot", Default Value: this.weaponDef.HeatDamage

Weapon damage is calculated through a series of checks, based on whether the weapon is for DFA (Death From Above), standard melee, or a ranged attack:

```
if WeaponType.Melee:
if (this.WeaponSubType == WeaponSubType.DFA)
{
	- Type: float | Name: "DamagePerShot", Default Value: chassis.DFADamage
	- Type: float | Name: "Instability", Default Value: chassis.DFAInstability
	- Type: float | Name: "AccuracyModifier", Default Value: chassis.DFAToHitModifier
}
else
{
	- Type: float | Name: "DamagePerShot", Default Value: chassis.MeleeDamage
	- Type: float | Name: "Instability", Default Value: chassis.MeleeInstability
	- Type: float | Name: "AccuracyModifier", Default Value: chassis.MeleeToHitModifier
}
- Type: int | Name: "DamageVariance", Default Value: 0
else
{
- Type: float | Name: "DamagePerShot", Default Value: this.weaponDef.Damage
- Type: float | Name: "Instability", Default Value: this.weaponDef.Instability
- Type: float | Name: "AccuracyModifier", Default Value: this.weaponDef.AccuracyModifier
- Type: int | Name: "DamageVariance", Default Value: this.weaponDef.DamageVariance
}
```

## Component

- Type: ComponentDamageLevel | Name: "DamageLevel", Default Value: this.baseComponentRef.DamageLevel

## Pilot

- Type: int | Name: "Piloting", Default Value: this.pilotDef.SkillPiloting
- Type: int | Name: "Gunnery", Default Value: this.pilotDef.SkillGunnery
- Type: int | Name: "Guts", Default Value: this.pilotDef.SkillGuts
- Type: int | Name: "Tactics", Default Value: this.pilotDef.SkillTactics

- Type: int | Name: "Injuries", Default Value: this.pilotDef.Injuries
- Type: int | Name: "Health", Default Value: this.pilotDef.Health
- Type: int | Name: "BonusHealth", Default Value: 0
- Type: bool | Name: "LethalInjury", Default Value: this.pilotDef.LethalInjury

- Type: bool | Name: "HasEjected", Default Value: false
- Type: int | Name: "MaxTargets", Default Value: 1

- Type: bool | Name: "CanUseCoolantVent", Default Value: false
- Type: bool | Name: "CanEject", Default Value: true

- Type: float | Name: "ArmorDamageInflicted", Default Value: 0f
- Type: float | Name: "StructureDamageInflicted", Default Value: 0f

- Type: int | Name: "UnitsKilled", Default Value: 0
- Type: int | Name: "MechsKilled", Default Value: 0
- Type: int | Name: "OthersKilled", Default Value: 0

- Type: int | Name: "ExperienceUnspent", Default Value: this.pilotDef.ExperienceUnspent
- Type: int | Name: "ExperienceSpent", Default Value: this.pilotDef.ExperienceSpent

## Building

- Type: float | Name: "Structure", Default Value: (float)this.BuildingDef.StructurePoints
- Type: LocationDamageLevel | Name: "DamageLevel", Default Value: LocationDamageLevel.Functional

## Team
- Type: int | Name: "Morale", Default Value: moraleInitialDefault
- Type: bool | Name: "MoraleSuppression", Default Value: false