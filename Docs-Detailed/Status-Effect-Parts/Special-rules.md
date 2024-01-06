# SpecialRule

AI Generated notes to help explain the **many** elements that make up a Status Effect in BattleTech. This aims to explain what a named option in the status effect does, to help you make the right choices. You are encouraged to use `CRTL+F` to find what you're specifically looking for.

If you spot any egregious errors, please correct them.

**NOTES:** 

- This data is only guaranteed valid for creating status effects compatible with Vanilla BattleTech. Any mod/mod pack that significantly alters game functionality through patching may **not** be compatible with the following explanations.
- SpecialRules `Rally|Retreat|Strafe|Artillery|SpawnTurret` may not be functional without additional programming.

Return to [Status Effects Info](../Docs-Detailed/Status-effects-info)

## Ability.ActivateSpecialAbility

There are multiple variants of this function, each associated with a different triggers.

```
private void ActivateSpecialAbility(AbstractActor creator, ICombatant target)
{
	AbilityDef.SpecialRules specialRules = this.Def.specialRules;
	if (specialRules == AbilityDef.SpecialRules.LoneWolf)
	{
this.activateLoneWolf(creator);
return;
	}
	if (specialRules != AbilityDef.SpecialRules.LanceMate)
	{
return;
	}
	this.activateLanceMate(creator);
}

```

`ActivateSpecialAbility(AbstractActor creator, ICombatant target)`: This function activates a special ability for an actor (creator) against a target. The special ability is determined by the `specialRules` field of the `AbilityDef` object. If the rule is `LoneWolf`, it activates the Lone Wolf ability. If the rule is `LanceMate`, it activates the Lance Mate ability.

```
private void ActivateSpecialAbility(Team team, ICombatant target)
{
	AbilityDef.SpecialRules specialRules = this.Def.specialRules;
	if (specialRules == AbilityDef.SpecialRules.Rally)
	{
this.activateRally(team);
return;
	}
	if (specialRules != AbilityDef.SpecialRules.Retreat)
	{
return;
	}
	this.activateRetreat(team);
}
```

`ActivateSpecialAbility(Team team, ICombatant target)`: This function activates a special ability for a team against a target. If the rule is `Rally`, it activates the Rally ability. If the rule is `Retreat`, it activates the Retreat ability.

```
private void ActivateSpecialAbility(Team team, Vector3 positionA, Vector3 positionB)
{
	AbilityDef.SpecialRules specialRules = this.Def.specialRules;
	if (specialRules == AbilityDef.SpecialRules.Strafe)
	{
this.ActivateStrafe(team, positionA, positionB, this.Def.FloatParam1);
return;
	}
	if (specialRules != AbilityDef.SpecialRules.SpawnTurret)
	{
return;
	}
	this.ActivateSpawnTurret(team, positionA, positionB);
}
```

`ActivateSpecialAbility(Team team, Vector3 positionA, Vector3 positionB)`: This function activates a special ability for a team between two positions (positionA and positionB). If the rule is `Strafe`, it activates the Strafe ability. If the rule is `SpawnTurret,` it activates the Spawn Turret ability.

```
private void ActivateSpecialAbility(Team team, Vector3 targetPos)
{
	AbilityDef.SpecialRules specialRules = this.Def.specialRules;
	if (specialRules == AbilityDef.SpecialRules.Artillery)
	{
this.ActivateArtilleryStrike(team, targetPos, this.Def.FloatParam1);
	}
}
```

`ActivateSpecialAbility(Team team, Vector3 targetPos)`: This function activates a special ability for a team at a target position. If the rule is `Artillery`, it activates the Artillery Strike ability.

```
private void ActivateSpecialAbility(AbstractActor creator, Vector3 positionA, Vector3 positionB)
{
}
```

`ActivateSpecialAbility(AbstractActor creator, Vector3 positionA, Vector3 positionB)`: This function seems to be a placeholder for activating a special ability for an actor between two positions. However, it currently does nothing.

```
private void ActivateSpecialAbility(AbstractActor creator, Vector3 targetPos)
{
	AbilityDef.SpecialRules specialRules = this.Def.specialRules;
	if (specialRules == AbilityDef.SpecialRules.Artillery)
	{
this.ActivateArtilleryStrike(creator, targetPos, this.Def.FloatParam1);
	}
}
```

`ActivateSpecialAbility(AbstractActor creator, Vector3 targetPos)`: This function activates a special ability for an actor at a target position. If the rule is `Artillery`, it activates the Artillery Strike ability.

## Ability.ActivateStrafe

```
private void ActivateStrafe(Team team, Vector3 positionA, Vector3 positionB, float radius)
		{
			AbstractActor abstractActor = team.FindSupportActor(this.Def.ActorResource);
			if (abstractActor == null)
			{
				Ability.abilityLogger.LogError(string.Format("Couldn't find actor {0} for ability {1} - aborting", this.Def.ActorResource, this.Def.Description.Name));
				return;
			}
			StrafeSequence strafeSequence = new StrafeSequence(abstractActor, positionA, positionB, radius);
			TurnEvent turnEvent = new TurnEvent(GUIDFactory.GetGUID(), this.Combat, this.Def.ActivationETA, null, strafeSequence, this.Def, true);
			this.Combat.TurnDirector.AddTurnEvent(turnEvent);
			if (this.Def.IntParam1 > 0)
			{
				this.SpawnFlares(positionA, positionB, this.Def.StringParam1, this.Def.IntParam1, this.Def.ActivationETA);
			}
		}
```

This Unity C# function, `ActivateStrafe(Team team, Vector3 positionA, Vector3 positionB, float radius)`, is used to activate a "strafe" ability in a game. Here's what it does in plain English:

1. It tries to find a support actor for the team using the `ActorResource` defined in the ability definition (`this.Def`). The support actor is likely a character or entity in the game that can provide support abilities.

2. If it can't find the support actor, it logs an error message and aborts the function.

3. If the support actor is found, it creates a `StrafeSequence` with the support actor, two positions (`positionA` and `positionB`), and a radius. This `StrafeSequence` likely represents the action of the support actor performing a strafing run between the two positions with a certain effect radius.

4. It then creates a `TurnEvent` with a unique ID, the combat context, the activation time of the ability, the `StrafeSequence`, the ability definition, and a flag indicating that the event is real (not simulated or predicted). This `TurnEvent` likely represents an event in the game's turn-based system, such as an actor taking an action.

5. The `TurnEvent` is added to the game's `TurnDirector`, which likely manages the sequence of events in each turn of the game.

6. If the `IntParam1` field of the ability definition is greater than 0, it spawns flares between the two positions. The parameters for spawning the flares are taken from the ability definition.

So, in summary, this function activates a strafing ability for a support actor in a team, creates an event for this action in the game's turn system, and optionally spawns flares.

## Ability.ActivateSpawnTurret

```
private void ActivateSpawnTurret(Team team, Vector3 positionA, Vector3 positionB)
		{
			Quaternion quaternion = Quaternion.LookRotation(positionB - positionA);
			AbstractActor abstractActor = this.SpawnTurret(team, this.Def.ActorResource, positionA, quaternion);
			team.SupportTeam.AddUnit(abstractActor);
			abstractActor.OnPlayerVisibilityChanged(VisibilityLevel.LOSFull);
			abstractActor.OnPositionUpdate(positionA, quaternion, -1, true, null, false);
			abstractActor.BehaviorTree = BehaviorTreeFactory.MakeBehaviorTree(this.Combat.BattleTechGame, abstractActor, BehaviorTreeIDEnum.CoreAITree);
			UnitSpawnedMessage unitSpawnedMessage = new UnitSpawnedMessage("FROM_ABILITY", abstractActor.GUID);
			this.Combat.MessageCenter.PublishMessage(unitSpawnedMessage);
		}
```

This Unity C# function, `ActivateSpawnTurret(Team team, Vector3 positionA, Vector3 positionB)`, is used to activate a "spawn turret" ability in a game. Here's what it does in plain English:

1. It calculates the rotation (`quaternion`) needed for something (presumably a turret) to face from `positionA` towards `positionB`.

2. It calls the `SpawnTurret` method to create a turret at `positionA` with the calculated rotation. The type of turret to spawn is determined by `this.Def.ActorResource`. The spawned turret is represented as an `AbstractActor`.

3. It adds the spawned turret to the team's support units.

4. It updates the visibility status of the spawned turret to `VisibilityLevel.LOSFull`, which likely means that the turret is fully visible to the player.

5. It updates the position and rotation of the spawned turret. The `-1` likely represents an invalid or unspecified value for a parameter that is not used in this case.

6. It assigns a behavior tree to the spawned turret, which likely determines how the turret will behave or react in the game. The behavior tree is created using a factory method and is based on the `CoreAITree` type.

7. It creates a `UnitSpawnedMessage` with a specified message and the unique ID of the spawned turret. This message likely serves to notify other parts of the game that a unit has been spawned.

8. It publishes the `UnitSpawnedMessage` to the game's `MessageCenter`, which likely handles and distributes these messages to the appropriate parts of the game.

So, in summary, this function spawns a turret at a specific location, adds it to a team, updates its visibility and position, assigns it a behavior, and sends a message to the game to indicate that a unit has been spawned.

## Ability.SpawnTurret

```
private AbstractActor SpawnTurret(Team team, string unitID, Vector3 position, Quaternion rotation)
		{
			PilotDef orCreate = this.Combat.DataManager.PilotDefs.GetOrCreate(UnitSpawnPointGameLogic.PilotDef_Default);
			TurretDef orCreate2 = this.Combat.DataManager.TurretDefs.GetOrCreate(unitID);
			orCreate2.Refresh();
			Turret turret = ActorFactory.CreateTurret(orCreate2, orCreate, team.EncounterTags, this.Combat, team.GetNextSupportUnitGuid(), "", null);
			turret.Init(position, rotation.eulerAngles.y, true);
			turret.InitGameRep(null);
			return turret;
		}
```

This Unity C# function, `SpawnTurret(Team team, string unitID, Vector3 position, Quaternion rotation)`, is used to spawn a turret in a game. Here's what it does in plain English:

1. It retrieves or creates a default `PilotDef` object. This object likely represents the definition of a pilot, which could include attributes like skills, abilities, etc.

2. It retrieves or creates a `TurretDef` object using the provided `unitID`. This object likely represents the definition of a turret, which could include attributes like health, damage, range, etc.

3. It refreshes the `TurretDef` object, which might update its state or data.

4. It creates a `Turret` object using the `TurretDef` and `PilotDef` objects, the team's encounter tags, the combat context, a unique ID generated by the team, and some other parameters. This `Turret` object represents an actual turret in the game.

5. It initializes the `Turret` object with the provided position, the Y angle of the provided rotation, and a flag set to `true`. This might set the turret's initial position and orientation in the game world.

6. It calls `InitGameRep(null)` on the `Turret` object. This method likely initializes the game representation of the turret, which could include setting up its visual model, animations, etc.

7. Finally, it returns the `Turret` object.

So, in summary, this function spawns a turret at a specific location with a specific orientation, and returns the spawned turret. 

## Ability.ActivateArtilleryStrike

```
private void ActivateArtilleryStrike(Team team, Vector3 targetPos, float radius)
		{
			Weapon weapon = team.FindSupportWeapon(this.Def.WeaponResource);
			if (weapon == null)
			{
				Ability.abilityLogger.LogError(string.Format("Couldn't find weapon {0} for ability {1} - aborting", this.Def.WeaponResource, this.Def.Description.Name));
				return;
			}
			ArtillerySequence artillerySequence = new ArtillerySequence(this.Combat, team.GUID, weapon, this.Def.StringParam2, targetPos, radius);
			TurnEvent turnEvent = new TurnEvent(GUIDFactory.GetGUID(), this.Combat, this.Def.ActivationETA, null, artillerySequence, this.Def, true);
			this.Combat.TurnDirector.AddTurnEvent(turnEvent);
			if (this.Def.IntParam1 > 0)
			{
				this.SpawnFlares(targetPos, targetPos, this.Def.StringParam1, this.Def.IntParam1, this.Def.ActivationETA);
			}
		}
```

This Unity C# function, `ActivateArtilleryStrike(Team team, Vector3 targetPos, float radius)`, is used to activate an "artillery strike" ability in a game. Here's what it does in plain English:

1. It tries to find a support weapon for the team using the `WeaponResource` defined in the ability definition (`this.Def`). The support weapon is likely a weapon that can be used by the team to provide support in combat.

2. If it can't find the support weapon, it logs an error message and aborts the function.

3. If the support weapon is found, it creates an `ArtillerySequence` with the combat context, the team's unique ID, the weapon, a string parameter from the ability definition, the target position, and the radius. This `ArtillerySequence` likely represents the action of the support weapon performing an artillery strike at the target position with a certain effect radius.

4. It then creates a `TurnEvent` with a unique ID, the combat context, the activation time of the ability, the `ArtillerySequence`, the ability definition, and a flag indicating that the event is real (not simulated or predicted). This `TurnEvent` likely represents an event in the game's turn-based system, such as a weapon taking an action.

5. The `TurnEvent` is added to the game's `TurnDirector`, which likely manages the sequence of events in each turn of the game.

6. If the `IntParam1` field of the ability definition is greater than 0, it spawns flares at the target position. The parameters for spawning the flares are taken from the ability definition.

So, in summary, this function activates an artillery strike ability for a support weapon in a team, creates an event for this action in the game's turn system, and optionally spawns flares.

## Ability.ActivateArtilleryStrike

```
private void ActivateArtilleryStrike(AbstractActor creator, Vector3 targetPos, float radius)
		{
			Weapon weapon = null;
			foreach (MechComponent mechComponent in creator.supportComponents)
			{
				if (mechComponent.componentDef == null)
				{
					mechComponent.baseComponentRef.RefreshComponentDef();
				}
				if (mechComponent.componentDef.Description.Id == this.Def.WeaponResource)
				{
					weapon = mechComponent as Weapon;
					break;
				}
			}
			if (weapon == null)
			{
				Ability.abilityLogger.LogError(string.Format("Couldn't find weapon {0} for ability {1} - aborting", this.Def.WeaponResource, this.Def.Description.Name));
				return;
			}
			List<Vector3> list = new List<Vector3> { targetPos };
			List<ICombatant> list2 = new List<ICombatant>();
			List<Collider> list3 = new List<Collider>(Physics.OverlapSphere(targetPos, radius));
			foreach (ICombatant combatant in this.Combat.GetAllCombatants())
			{
				if (!combatant.IsDead && !combatant.IsFlaggedForDeath)
				{
					if (combatant.UnitType == UnitType.Building)
					{
						if (Vector3.Distance(targetPos, combatant.CurrentPosition) <= 2f * radius)
						{
							for (int i = 0; i < combatant.GameRep.AllRaycastColliders.Length; i++)
							{
								Collider collider = combatant.GameRep.AllRaycastColliders[i];
								if (list3.Contains(collider))
								{
									list2.Add(combatant);
									break;
								}
							}
						}
					}
					else if (Vector3.Distance(targetPos, combatant.CurrentPosition) <= radius)
					{
						list2.Add(combatant);
					}
				}
			}
			MessageCenterMessage messageCenterMessage = new MechMortarInvocation(creator, list, list2, weapon, this);
			this.Combat.MessageCenter.PublishMessage(messageCenterMessage);
		}
```

This Unity C# function, `ActivateArtilleryStrike(AbstractActor creator, Vector3 targetPos, float radius)`, is used to activate an "artillery strike" ability in a game. Here's what it does in plain English:

1. It starts by setting a `Weapon` variable to `null`. It then loops through the `supportComponents` of the `creator` (which is an `AbstractActor`, likely representing a character or entity in the game).

2. If a `MechComponent` (a component of a mech, which is a type of actor in the game) doesn't have a `componentDef` (which likely defines the properties of the component), it refreshes the `componentDef`.

3. If the ID of the `componentDef` matches the `WeaponResource` of the ability definition (`this.Def`), it sets the `Weapon` variable to the `MechComponent` (cast as a `Weapon`), and breaks the loop.

4. If no matching weapon is found (the `Weapon` variable is still `null`), it logs an error message and aborts the function.

5. It creates a list of `Vector3` positions with `targetPos` as the only element, and an empty list of `ICombatant` (which likely represents a combatant in the game).

6. It creates a list of `Collider` objects that overlap a sphere centered at `targetPos` with a radius of `radius`. This could be used to detect which objects in the game world are within the area of effect of the artillery strike.

7. It then loops through all combatants in the game. If a combatant is not dead or flagged for death, it checks the distance between the combatant's position and `targetPos`.

8. If the combatant is a building and its distance to `targetPos` is less than or equal to `2f * radius`, it loops through the combatant's `AllRaycastColliders`. If any of these colliders are in the list of overlapping colliders, it adds the combatant to the list of `ICombatant`.

9. If the combatant is not a building and its distance to `targetPos` is less than or equal to `radius`, it adds the combatant to the list of `ICombatant`.

10. It creates a `MechMortarInvocation` message with the `creator`, the list of positions, the list of `ICombatant`, the `Weapon`, and the ability itself. This message likely represents the action of the `creator` using the `Weapon` to perform an artillery strike.

11. It publishes the `MechMortarInvocation` message to the game's `MessageCenter`, which likely handles and distributes these messages to the appropriate parts of the game.

So, in summary, this function activates an artillery strike ability for a weapon of a creator, determines the affected combatants, and sends a message to the game to indicate that an artillery strike has been performed.

## Ability.SpawnFlares

```
private void SpawnFlares(Vector3 positionA, Vector3 positionB, string prefabName, int numFlares, int numPhases)
		{
			Vector3 vector = (positionB - positionA) / (float)numFlares;
			Vector3 vector2 = positionA;
			vector2.y = this.Combat.MapMetaData.GetLerpedHeightAt(vector2, false);
			List<ObjectSpawnData> list = new List<ObjectSpawnData>();
			for (int i = 0; i < this.Def.IntParam1; i++)
			{
				ObjectSpawnData objectSpawnData = new ObjectSpawnData(prefabName, vector2, Quaternion.identity, true, false);
				list.Add(objectSpawnData);
				vector2 += vector;
				vector2.y = this.Combat.MapMetaData.GetLerpedHeightAt(vector2, false);
			}
			SpawnObjectSequence spawnObjectSequence = new SpawnObjectSequence(this.Combat, list);
			this.Combat.MessageCenter.PublishMessage(new AddSequenceToStackMessage(spawnObjectSequence));
			List<ObjectSpawnData> spawnedObjects = spawnObjectSequence.spawnedObjects;
			CleanupObjectSequence cleanupObjectSequence = new CleanupObjectSequence(this.Combat, spawnedObjects);
			TurnEvent turnEvent = new TurnEvent(GUIDFactory.GetGUID(), this.Combat, numPhases, null, cleanupObjectSequence, this.Def, false);
			this.Combat.TurnDirector.AddTurnEvent(turnEvent);
		}
```

This Unity C# code defines a method named `SpawnFlares` that is used to spawn a number of flares in a game. Here's a step-by-step explanation of what the code does:

1. The method takes five parameters: two `Vector3` positions (`positionA` and `positionB`), a string for the prefab name (`prefabName`), and two integers for the number of flares (`numFlares`) and the number of phases (`numPhases`).

2. It calculates a vector (`vector`) that represents the direction and distance between each flare.

3. It initializes a new vector (`vector2`) at `positionA` and adjusts its y-coordinate to match the height of the terrain at that point.

4. It creates an empty list of `ObjectSpawnData` objects. This list will hold the data for each flare that will be spawned.

5. It then enters a loop that runs for the number of times specified by `this.Def.IntParam1`. In each iteration of the loop:
    - It creates a new `ObjectSpawnData` object with the given prefab name, the current position (`vector2`), and some other parameters.
    - It adds this `ObjectSpawnData` object to the list.
    - It moves `vector2` along the direction of `vector` and adjusts its y-coordinate to match the height of the terrain at the new point.

6. After all the `ObjectSpawnData` objects have been created, it creates a new `SpawnObjectSequence` object with the list of `ObjectSpawnData` objects and adds this sequence to the game's message center.

7. It then creates a `CleanupObjectSequence` object that will be responsible for cleaning up the spawned objects after they are no longer needed.

8. Finally, it creates a `TurnEvent` object with the `CleanupObjectSequence` and adds this event to the game's turn director. This event will be executed after a certain number of phases, as specified by `numPhases`.

In summary, this method spawns a series of flares along a line between two points in the game world, and sets up events to clean up these flares after a certain number of phases. The flares are spawned at the height of the terrain at their respective positions. The prefab for the flares is specified by `prefabName`. The number of flares and the number of phases are specified by `numFlares` and `numPhases`, respectively. The actual number of flares spawned is determined by `this.Def.IntParam1`.

## Ability.activateRally

```
private void activateRally(Team team)
		{
			for (int i = 0; i < team.unitCount; i++)
			{
				AbstractActor abstractActor = team.units[i];
				if (abstractActor.IsProne)
				{
					abstractActor.StandFromProne();
				}
				this.Combat.MessageCenter.PublishMessage(new FloatieMessage(abstractActor.GUID, abstractActor.GUID, new Text(this.Def.Description.Name, Array.Empty<object>()), FloatieMessage.MessageNature.Buff));
			}
		}
```

This Unity C# code defines a method named `activateRally` that is used to activate a rally for a team in a game. Here's a step-by-step explanation of what the code does:

1. The method takes one parameter, `team`, which represents a team in the game.

2. It then enters a loop that runs for the number of units in the team (`team.unitCount`). In each iteration of the loop:
    - It gets the unit at the current index (`i`) and assigns it to `abstractActor`.
    - If `abstractActor` is prone (i.e., lying down), it calls the `StandFromProne` method on `abstractActor` to make it stand up.
    - It then publishes a `FloatieMessage` to the game's message center. This message is associated with `abstractActor` (as indicated by `abstractActor.GUID`), contains some text (the name of the definition of the current object, as indicated by `this.Def.Description.Name`), and is of the nature `Buff`.

In summary, this method goes through each unit in a team, makes any prone units stand up, and publishes a buff message for each unit. The buff message is likely used to display some kind of visual effect or notification in the game to indicate that the unit has been buffed (i.e., had its abilities enhanced in some way). The exact nature of the buff is not specified in this method and would be determined elsewhere in the game's code. The `activateRally` method could be used, for example, to simulate a rally cry that boosts the morale of a team and makes them stand ready for battle.

## Ability.activateRetreat

```
private void activateRetreat(Team team)
		{
			AudioEventManager.PlayComputerVO(ComputerVOEvents.Retreat_Confirmed, null, null);
			AudioEventManager.PlayRandomPilotVO(VOEvents.Commander_Retreat, team, team.units);
			EncounterLayerData encounterLayerData = Object.FindObjectOfType<EncounterLayerData>();
			this.Combat.MessageCenter.PublishMessage(new MissionFailedMessage(null, encounterLayerData.IsGoodFaithEffort));
		}
```

This Unity C# code defines a method named `activateRetreat` that is used to activate a retreat for a team in a game. Here's a step-by-step explanation of what the code does:

1. The method takes one parameter, `team`, which represents a team in the game.

2. It then plays a computer voice-over (VO) event named `Retreat_Confirmed` using the `PlayComputerVO` method of the `AudioEventManager`. This could be used to play a sound or voice-over that confirms the retreat order.

3. It also plays a random pilot VO event named `Commander_Retreat` for the team using the `PlayRandomPilotVO` method of the `AudioEventManager`. This could be used to play a sound or voice-over from a random pilot in the team that acknowledges the retreat order.

4. It finds an object of type `EncounterLayerData` in the game. This object could contain data about the current encounter or battle in the game.

5. Finally, it publishes a `MissionFailedMessage` to the game's message center. This message could be used to indicate that the mission has failed and the team needs to retreat. The `IsGoodFaithEffort` property of the `encounterLayerData` is passed to the message, which could be used to determine whether the team made a good faith effort in the mission.

In summary, this method plays some audio events to indicate a retreat order, and sends a message to indicate that the mission has failed and the team needs to retreat. The `activateRetreat` method could be used, for example, to simulate a retreat order in a battle scenario in the game. The exact effects of the retreat order would be determined elsewhere in the game's code. The `team` parameter specifies the team that needs to retreat. The `IsGoodFaithEffort` property could be used to determine whether the team made a good faith effort in the mission, which could affect the consequences of the retreat.

## Ability.activateLoneWolf

```
private void activateLoneWolf(AbstractActor creator)
		{
			AbstractActor abstractActor = null;
			List<AbstractActor> allAlliesOf = this.Combat.GetAllAlliesOf(creator);
			float num = float.MaxValue;
			for (int i = 0; i < allAlliesOf.Count; i++)
			{
				float num2 = Vector3.Distance(creator.CurrentPosition, allAlliesOf[i].CurrentPosition);
				if (num2 < num)
				{
					num = num2;
					abstractActor = allAlliesOf[i];
				}
			}
			if (abstractActor != null)
			{
				int num3 = (int)(num / this.Def.FloatParam1);
				if (num3 > 0)
				{
					for (int j = 0; j < this.Def.EffectData.Count; j++)
					{
						if (this.Def.EffectData[j].effectType == EffectType.StatisticEffect)
						{
							EffectData effectData = EffectData.CreateCopy(this.Def.EffectData[j]);
							effectData.statisticData.modValue = (float.Parse(effectData.statisticData.modValue, NumberFormatInfo.InvariantInfo) * (float)num3).ToString();
							effectData.Description = new BaseDescriptionDef(effectData.Description.Id, effectData.Description.Name, effectData.Description.Details.Replace("x", effectData.statisticData.modValue), effectData.Description.Icon);
							this.ActivateEffect(effectData, creator, creator);
						}
					}
				}
			}
		}
```

This Unity C# code defines a method named `activateLoneWolf` that is used to activate a "Lone Wolf" effect for a game character (an `AbstractActor` named `creator`). Here's a step-by-step explanation of what the code does:

1. The method takes one parameter, `creator`, which represents the game character that is activating the "Lone Wolf" effect.

2. It then gets a list of all allies of `creator` in the game.

3. It initializes a variable `num` to `float.MaxValue`, and a variable `abstractActor` to `null`. These variables will be used to find the ally that is closest to `creator`.

4. It then enters a loop that runs for each ally in the list. In each iteration of the loop:
    - It calculates the distance between `creator` and the current ally.
    - If this distance is less than `num`, it updates `num` to this distance and `abstractActor` to the current ally.

5. After the loop, if `abstractActor` is not `null` (i.e., if there is at least one ally), it calculates `num3` as the integer part of the division of `num` by `this.Def.FloatParam1`.

6. If `num3` is greater than 0, it enters another loop that runs for each effect in `this.Def.EffectData`. In each iteration of the loop:
    - If the effect type is `StatisticEffect`, it creates a copy of the effect data and modifies its `modValue` by multiplying it with `num3`.
    - It also replaces the "x" in the effect description details with the new `modValue`.
    - Finally, it activates the effect for `creator`.

In summary, this method activates a "Lone Wolf" effect for a game character. The effect is stronger the farther the character is from its closest ally. The exact nature of the "Lone Wolf" effect is not specified in this method and would be determined by the `StatisticEffect` and its `modValue`. The `activateLoneWolf` method could be used, for example, to simulate a game mechanic where a character gets stronger when they are isolated from their allies. The `creator` parameter specifies the character that is activating the "Lone Wolf" effect. The `this.Def.FloatParam1` property could be used to adjust the strength of the effect based on the distance to the closest ally.

## Ability.activateLanceMate

```
private void activateLanceMate(AbstractActor creator)
		{
			int num = 0;
			List<AbstractActor> allAlliesOf = this.Combat.GetAllAlliesOf(creator);
			for (int i = 0; i < allAlliesOf.Count; i++)
			{
				if (Vector3.Distance(creator.CurrentPosition, allAlliesOf[i].CurrentPosition) < this.Def.FloatParam2)
				{
					num++;
				}
			}
			if (num > 0)
			{
				float num2 = 1f - (float)num * this.Def.FloatParam1;
				if (num2 < 0f)
				{
					num2 = 0f;
				}
				for (int j = 0; j < this.Def.EffectData.Count; j++)
				{
					if (this.Def.EffectData[j].effectType == EffectType.StatisticEffect)
					{
						EffectData effectData = EffectData.CreateCopy(this.Def.EffectData[j]);
						effectData.statisticData.modValue = num2.ToString();
						effectData.Description = new BaseDescriptionDef(effectData.Description.Id, effectData.Description.Name, effectData.Description.Details.Replace("x", ((float)num * this.Def.FloatParam1).ToString()), effectData.Description.Icon);
						this.ActivateEffect(effectData, creator, creator);
					}
				}
			}
		}
```

This Unity C# code defines a method named `activateLanceMate` that is used to activate a "Lance Mate" effect for a game character (an `AbstractActor` named `creator`). Here's a step-by-step explanation of what the code does:

1. The method takes one parameter, `creator`, which represents the game character that is activating the "Lance Mate" effect.

2. It then gets a list of all allies of `creator` in the game.

3. It initializes a variable `num` to 0. This variable will be used to count the number of allies that are within a certain distance from `creator`.

4. It then enters a loop that runs for each ally in the list. In each iteration of the loop:
    - It calculates the distance between `creator` and the current ally.
    - If this distance is less than `this.Def.FloatParam2`, it increments `num` by 1.

5. After the loop, if `num` is greater than 0 (i.e., if there is at least one ally within the specified distance), it calculates `num2` as `1f` minus `num` times `this.Def.FloatParam1`. If `num2` is less than `0f`, it sets `num2` to `0f`.

6. It then enters another loop that runs for each effect in `this.Def.EffectData`. In each iteration of the loop:
    - If the effect type is `StatisticEffect`, it creates a copy of the effect data and sets its `modValue` to `num2`.
    - It also replaces the "x" in the effect description details with the product of `num` and `this.Def.FloatParam1`.
    - Finally, it activates the effect for `creator`.

In summary, this method activates a "Lance Mate" effect for a game character. The effect is weaker the more allies the character has within a certain distance. The exact nature of the "Lance Mate" effect is not specified in this method and would be determined by the `StatisticEffect` and its `modValue`. The `activateLanceMate` method could be used, for example, to simulate a game mechanic where a character gets weaker when they are close to their allies. The `creator` parameter specifies the character that is activating the "Lance Mate" effect. The `this.Def.FloatParam1` and `this.Def.FloatParam2` properties could be used to adjust the strength of the effect based on the number of nearby allies and the distance to them, respectively.

---

Return to [Status Effects Info](../Docs-Detailed/Status-effects-info.md)