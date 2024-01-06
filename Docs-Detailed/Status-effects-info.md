# Status Effects Info

AI Generated notes to help explain the **many** elements that make up a Status Effect in BattleTech. This aims to explain what a named option in the status effect does, to help you make the right choices. You are encouraged to use `CRTL+F` to find what you're specifically looking for.

If you spot any egregious errors, please correct them.

**NOTE:** This data is only guaranteed valid for creating status effects compatible with Vanilla BattleTech. Any mod/mod pack that significantly alters game functionality through patching may **not** be compatible with the following explanations.

## StatisticEffect.OnEffectPhaseBegin

```
public override void OnEffectPhaseBegin()
		{
			base.OnEffectPhaseBegin();
			if (this.effectData.targetingData.effectTriggerType == EffectTriggerType.OnDamaged)
			{
				return;
			}
			if (this.effectData.statisticData.appliesEachTick && !this.effectData.durationData.ticksOnActivations)
			{
				int num = this.statCollection.ModifyStatistic(this.id, this.stackItemUID, this.effectData.statisticData.statName, this.effectData.statisticData.operation, this.modVariant, -1, true);
				this.historyEventUIDs.Add(num);
			}
		}
```
This C# Unity code is a method named `OnEffectPhaseBegin` that is overriding a method from its base class. Here's what it does in plain English:

1. It first calls the `OnEffectPhaseBegin` method of its base class. This is done using `base.OnEffectPhaseBegin()`. This means it will execute whatever functionality is defined in the parent class's `OnEffectPhaseBegin` method.

2. It then checks if the `effectTriggerType` of the `targetingData` of `effectData` is equal to `OnDamaged`. If it is, the method returns immediately and no further code is executed. This means that this method does nothing when the effect is triggered by damage.

3. If the `effectTriggerType` is not `OnDamaged`, it checks if `appliesEachTick` of `statisticData` of `effectData` is true and `ticksOnActivations` of `durationData` of `effectData` is false. If both conditions are met, it proceeds to the next step. This means that the following code only runs if the effect applies each tick and does not tick on activations.

4. It calls the `ModifyStatistic` method on `statCollection` with several parameters, including `id`, `stackItemUID`, `statName`, `operation`, `modVariant`, `-1`, and `true`. The result of this method call (which is an integer) is stored in the variable `num`. This means it modifies a statistic in the `statCollection` and stores the result.

5. It adds `num` to `historyEventUIDs`. This means it keeps track of the result of the statistic modification.

So, in summary, this method modifies a statistic and tracks the result if certain conditions about the effect and its duration are met, and the effect is not triggered by damage. Otherwise, it does nothing. Please note that the exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet.

## StatisticEffect.OnEffectTakeDamage

```
public override void OnEffectTakeDamage(AbstractActor attacker, AbstractActor target)
		{
			base.OnEffectTakeDamage(attacker, target);
			if (this.effectData.targetingData.effectTriggerType == EffectTriggerType.OnDamaged && (this.effectData.targetingData.triggerLimit <= 0 || base.triggerCount < this.effectData.targetingData.triggerLimit) && this.SpecialRulesMet(attacker, target))
			{
				int num = base.triggerCount + 1;
				base.triggerCount = num;
				this.eTimer.IncrementActivations(this.effectData.targetingData.extendDurationOnTrigger);
				StatCollection statCollectionContaining = attacker.GetStatCollectionContaining(this.effectData.statisticData.statName);
				if (statCollectionContaining != null)
				{
					int num2 = statCollectionContaining.ModifyStatistic(this.id, this.stackItemUID, this.effectData.statisticData.statName, this.effectData.statisticData.operation, this.modVariant, -1, true);
					this.historyEventUIDs.Add(num2);
				}
			}
		}
```

This C# Unity code is a method named `OnEffectTakeDamage` that is overriding a method from its base class. Here's what it does in plain English:

1. It first calls the `OnEffectTakeDamage` method of its base class. This is done using `base.OnEffectTakeDamage(attacker, target)`. This means it will execute whatever functionality is defined in the parent class's `OnEffectTakeDamage` method.

2. It then checks if several conditions are met:
   - The `effectTriggerType` of the `targetingData` of `effectData` is equal to `OnDamaged`.
   - The `triggerLimit` of the `targetingData` of `effectData` is less than or equal to 0, or the `triggerCount` of the base class is less than the `triggerLimit` of the `targetingData` of `effectData`.
   - The `SpecialRulesMet(attacker, target)` method returns true.
   
   If all these conditions are met, it proceeds to the next step. Otherwise, it does nothing.

3. It increments the `triggerCount` of the base class by 1.

4. It calls the `IncrementActivations` method on `eTimer` with the `extendDurationOnTrigger` of the `targetingData` of `effectData` as the parameter. This means it increments the activations of the effect timer, possibly extending its duration.

5. It calls the `GetStatCollectionContaining` method on `attacker` with the `statName` of the `statisticData` of `effectData` as the parameter, and stores the result in `statCollectionContaining`.

6. If `statCollectionContaining` is not null, it calls the `ModifyStatistic` method on `statCollectionContaining` with several parameters, including `id`, `stackItemUID`, `statName`, `operation`, `modVariant`, `-1`, and `true`. The result of this method call (which is an integer) is stored in `num2`. It then adds `num2` to `historyEventUIDs`. This means it modifies a statistic in the stat collection of the attacker and keeps track of the result if the stat collection contains the statistic.

So, in summary, this method modifies a statistic and tracks the result if certain conditions about the effect, its trigger, and special rules are met when the effect takes damage. Otherwise, it does nothing. Please note that the exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet.

## StatisticEffect.SpecialRulesMet

```
private bool SpecialRulesMet(AbstractActor attacker, AbstractActor target)
		{
			AbilityDef.SpecialRules specialRules = this.effectData.targetingData.specialRules;
			return specialRules != AbilityDef.SpecialRules.HalfArmorOrLess || target.CurrentArmor <= target.StartingArmor * 0.5f;
		}
```

This C# Unity code is a method named `SpecialRulesMet` that takes two parameters: `attacker` and `target`, both of type `AbstractActor`. Here's what it does in plain English:

1. It first retrieves the `specialRules` from the `targetingData` of `effectData`. This `specialRules` is of type `AbilityDef.SpecialRules`, which is likely an enumeration representing different special rules that can be applied.

2. It then checks if `specialRules` is not equal to `AbilityDef.SpecialRules.HalfArmorOrLess` or if the `CurrentArmor` of the `target` is less than or equal to half of the `target`'s `StartingArmor`.

3. It returns the result of this check. This means that the method returns `true` if the special rule is not `HalfArmorOrLess` or if the target's current armor is half or less than its starting armor. Otherwise, it returns `false`.

So, in summary, this method checks if certain special rules are met based on the attacker and target. The exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet. Please note that the names `AbilityDef`, `SpecialRules`, `HalfArmorOrLess`, `AbstractActor`, `CurrentArmor`, and `StartingArmor` are likely specific to your project or the libraries you're using, and their exact meanings may vary.

## StatisticEffect.OnEffectActivationEnd

```
public override void OnEffectActivationEnd()
		{
			base.OnEffectActivationEnd();
			if (this.effectData.targetingData.effectTriggerType == EffectTriggerType.OnDamaged)
			{
				return;
			}
			if (this.effectData.statisticData.appliesEachTick && this.effectData.durationData.ticksOnActivations)
			{
				int num = this.statCollection.ModifyStatistic(this.id, this.stackItemUID, this.effectData.statisticData.statName, this.effectData.statisticData.operation, this.modVariant, -1, true);
				this.historyEventUIDs.Add(num);
			}
		}
```

This C# Unity code is a method named `OnEffectActivationEnd` that is overriding a method from its base class. Here's what it does in plain English:

1. It first calls the `OnEffectActivationEnd` method of its base class. This is done using `base.OnEffectActivationEnd()`. This means it will execute whatever functionality is defined in the parent class's `OnEffectActivationEnd` method.

2. It then checks if the `effectTriggerType` of the `targetingData` of `effectData` is equal to `OnDamaged`. If it is, the method returns immediately and no further code is executed. This means that this method does nothing when the effect is triggered by damage.

3. If the `effectTriggerType` is not `OnDamaged`, it checks if `appliesEachTick` of `statisticData` of `effectData` is true and `ticksOnActivations` of `durationData` of `effectData` is true. If both conditions are met, it proceeds to the next step. This means that the following code only runs if the effect applies each tick and ticks on activations.

4. It calls the `ModifyStatistic` method on `statCollection` with several parameters, including `id`, `stackItemUID`, `statName`, `operation`, `modVariant`, `-1`, and `true`. The result of this method call (which is an integer) is stored in the variable `num`. This means it modifies a statistic in the `statCollection` and stores the result.

5. It adds `num` to `historyEventUIDs`. This means it keeps track of the result of the statistic modification.

So, in summary, this method modifies a statistic and tracks the result if certain conditions about the effect and its duration are met, and the effect is not triggered by damage. Otherwise, it does nothing. Please note that the exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet.

## StatisticEffect.OnEffectEnd

```
public override void OnEffectEnd(bool expired, bool skipLogging = false)
		{
			if (this.effectData.targetingData.effectTriggerType != EffectTriggerType.OnDamaged && (!expired || !this.effectData.statisticData.effectsPersistAfterDestruction))
			{
				if (this.statCollection == null)
				{
					Debug.LogError("Stat collection doesn't exists. " + this.Target.Description.Id + " | " + this.ModVariant.statName);
					base.OnEffectEnd(expired, skipLogging);
					return;
				}
				Statistic statistic = this.statCollection.GetStatistic(this.effectData.statisticData.statName);
				for (int i = this.historyEventUIDs.Count - 1; i >= 0; i--)
				{
					int num = this.historyEventUIDs[i];
					this.statCollection.RemoveHistoryEvent(statistic, num, skipLogging);
				}
			}
			base.OnEffectEnd(expired, skipLogging);
		}
```

This C# Unity code is a method named `OnEffectEnd` that is overriding a method from its base class. Here's what it does in plain English:

1. It first checks if the `effectTriggerType` of the `targetingData` of `effectData` is not equal to `OnDamaged` and if the effect has not expired or if the `effectsPersistAfterDestruction` of the `statisticData` of `effectData` is false. If these conditions are met, it proceeds to the next step. Otherwise, it calls the `OnEffectEnd` method of its base class with `expired` and `skipLogging` as parameters and ends the current method.

2. It then checks if `statCollection` is null. If it is, it logs an error message using `Debug.LogError`, calls the `OnEffectEnd` method of its base class with `expired` and `skipLogging` as parameters, and ends the current method. This means that it does nothing if the stat collection doesn't exist, except for logging an error and calling the base method.

3. If `statCollection` is not null, it retrieves a statistic from `statCollection` using the `statName` of the `statisticData` of `effectData` and stores it in `statistic`.

4. It then iterates over `historyEventUIDs` in reverse order. For each item in `historyEventUIDs`, it calls the `RemoveHistoryEvent` method on `statCollection` with `statistic`, the current item, and `skipLogging` as parameters. This means it removes history events from the stat collection.

5. Finally, it calls the `OnEffectEnd` method of its base class with `expired` and `skipLogging` as parameters. This means it will execute whatever functionality is defined in the parent class's `OnEffectEnd` method.

So, in summary, this method removes history events from a stat collection if certain conditions about the effect and its expiration are met, and the effect is not triggered by damage. Otherwise, it does nothing except for calling the base method. Please note that the exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet.

## StatisticEffect.CheckEffectTarget

```
public override bool CheckEffectTarget(object target)
		{
			AbstractActor abstractActor = target as AbstractActor;
			return this.Target == abstractActor;
		}
```
This C# Unity code is a method named `CheckEffectTarget` that is overriding a method from its base class. Here's what it does in plain English:

1. It first tries to cast the `target` parameter to `AbstractActor` type and assigns the result to `abstractActor`. The `as` keyword in C# is used for safe type casting. If `target` is not an `AbstractActor`, `abstractActor` will be `null`.

2. It then checks if `this.Target` is equal to `abstractActor` and returns the result of this comparison. `this.Target` refers to the `Target` property of the current instance of the class.

So, in summary, this method checks if the provided target is the same as the `Target` property of the current instance and returns `true` if they are the same, and `false` otherwise. Please note that the exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet.

## StatisticEffect.GetProperStatCollectionOnLoad

```
private void GetProperStatCollectionOnLoad()
		{
			StatisticEffectData.TargetCollection targetCollection = this.effectData.statisticData.targetCollection;
			if (targetCollection == StatisticEffectData.TargetCollection.NotSet)
			{
				this.statCollection = this.Target.StatCollection;
				return;
			}
			if (targetCollection == StatisticEffectData.TargetCollection.Pilot)
			{
				if (this.Target.GetPilot() != null)
				{
					this.statCollection = this.Target.GetPilot().StatCollection;
					return;
				}
				Debug.LogError(string.Format("Failed to find Pilot for StatCollection Target: {0}", this.Target.UnitName));
				return;
			}
			else
			{
				if (string.IsNullOrEmpty(this.StatCollectionOwnerGUID))
				{
					Debug.LogError(string.Format("StatCollectionOwnerGUID is not set for Effect {0} on Hydrate", this.effectData.Description.Name));
					return;
				}
				foreach (MechComponent mechComponent in this.Target.allComponents)
				{
					if (mechComponent.StatCollection.GUID == this.StatCollectionOwnerGUID)
					{
						this.statCollection = mechComponent.StatCollection;
						return;
					}
				}
				Mech mech = this.Target as Mech;
				if (mech != null)
				{
					if (mech.MeleeWeapon.StatCollection.GUID == this.StatCollectionOwnerGUID)
					{
						this.statCollection = mech.MeleeWeapon.StatCollection;
						return;
					}
					if (mech.DFAWeapon.StatCollection.GUID == this.StatCollectionOwnerGUID)
					{
						this.statCollection = mech.DFAWeapon.StatCollection;
						return;
					}
				}
				Debug.LogError(string.Format("Failed to find StatCollection for {0} with target {1}", this.effectData.Description.Name, this.Target.Description.Name));
				return;
			}
		}
```

This C# Unity code is a method named `GetProperStatCollectionOnLoad`. Here's what it does in plain English:

1. It first retrieves the `targetCollection` from the `statisticData` of `effectData`.

2. It then checks if `targetCollection` is equal to `NotSet` from `StatisticEffectData.TargetCollection`. If it is, it sets `this.statCollection` to `this.Target.StatCollection` and ends the method. This means that if no specific target collection is set, it uses the stat collection of the target.

3. If `targetCollection` is not `NotSet`, it checks if it is equal to `Pilot` from `StatisticEffectData.TargetCollection`. If it is and the target has a pilot (checked by `this.Target.GetPilot() != null`), it sets `this.statCollection` to the stat collection of the pilot and ends the method. If the target does not have a pilot, it logs an error message and ends the method.

4. If `targetCollection` is neither `NotSet` nor `Pilot`, it checks if `this.StatCollectionOwnerGUID` is null or empty. If it is, it logs an error message and ends the method.

5. If `this.StatCollectionOwnerGUID` is not null or empty, it iterates over all components of the target. For each component, if the GUID of the component's stat collection is equal to `this.StatCollectionOwnerGUID`, it sets `this.statCollection` to the component's stat collection and ends the method.

6. If no component's stat collection has the matching GUID, it tries to cast the target to `Mech` type. If the target is a `Mech` and either the melee weapon's stat collection or the DFA weapon's stat collection has the matching GUID, it sets `this.statCollection` to the corresponding weapon's stat collection and ends the method.

7. If no matching stat collection is found, it logs an error message.

So, in summary, this method sets `this.statCollection` to the appropriate stat collection based on the `targetCollection` and the `StatCollectionOwnerGUID`. If no appropriate stat collection is found, it logs an error message. Please note that the exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet.

## EffectData.Load

```
public void Load(SerializationStream stream)
		{
			this.effectType = (EffectType)Enum.Parse(typeof(EffectType), stream.GetString());
			this.durationData = new EffectDurationData();
			this.durationData.Load(stream);
			this.targetingData = default(EffectTargetingData);
			this.targetingData.Load(stream);
			this.Description = new BaseDescriptionDef();
			this.Description.Load(stream);
			switch (this.effectType)
			{
			case EffectType.StatisticEffect:
				this.statisticData = new StatisticEffectData();
				this.statisticData.Load(stream);
				break;
			case EffectType.TagEffect:
				this.tagData = new TagEffectData();
				this.tagData.Load(stream);
				break;
			case EffectType.ActorBurningEffect:
				this.actorBurningData = new ActorBurningEffectData();
				this.actorBurningData.Load(stream);
				break;
			case EffectType.VFXEffect:
				this.vfxData = new VFXEffectData();
				this.vfxData.Load(stream);
				break;
			case EffectType.InstantModEffect:
				this.instantModData = new InstantModEffectData();
				this.instantModData.Load(stream);
				break;
			case EffectType.PoorlyMaintainedEffect:
				this.poorlyMaintainedEffectData = new PoorlyMaintainedEffectData();
				this.poorlyMaintainedEffectData.Load(stream);
				break;
			case EffectType.FloatieEffect:
				this.floatieData = new FloatieEffectData();
				this.floatieData.Load(stream);
				break;
			case EffectType.ActiveAbility:
				this.activeAbilityEffectData = new ActiveAbilityEffectData();
				this.activeAbilityEffectData.Load(stream);
				break;
			}
			this.nature = (EffectNature)Enum.Parse(typeof(EffectNature), stream.GetString());
		}
```

This code defines a method named `Load` that takes a `SerializationStream` object as an argument. The purpose of this method is to load data from the stream into the properties of the current object.

Here's a breakdown of what happens inside the method:

1. The `effectType` property is set by parsing a string from the stream into an `EffectType` enumeration value.
2. A new `EffectDurationData` object is created and its `Load` method is called with the stream as an argument, loading data into the `durationData` property.
3. The `targetingData` property is set to its default value, and then its `Load` method is called with the stream as an argument.
4. A new `BaseDescriptionDef` object is created and its `Load` method is called with the stream as an argument, loading data into the `Description` property.
5. Depending on the value of the `effectType` property, a different type of effect data object is created and its `Load` method is called with the stream as an argument. This could be a `StatisticEffectData`, `TagEffectData`, `ActorBurningEffectData`, `VFXEffectData`, `InstantModEffectData`, `PoorlyMaintainedEffectData`, `FloatieEffectData`, or `ActiveAbilityEffectData` object.
6. Finally, the `nature` property is set by parsing a string from the stream into an `EffectNature` enumeration value.

This method is typically used to load serialized data into an object, allowing the state of the object to be restored from a previously saved state. The `Load` method of each property is responsible for reading the correct amount of data from the stream. This is known as deserialization. It's the opposite of serialization, which is the process of converting an object's state to a byte stream for storage or transmission.

## EffectManager.CreateEffect

```
public List<Effect> CreateEffect(EffectData effectData, string effectID, int stackItemUID, Team creator, ICombatant target, WeaponHitInfo hitInfo, int attackIndex, bool skipLogging = false)
		{
			List<Effect> allEffectsTargetingWithBaseID = this.GetAllEffectsTargetingWithBaseID(target, effectData.Description.Id);
			List<Effect> allEffectsTargetingWithUniqueID = this.GetAllEffectsTargetingWithUniqueID(target, effectID);
			List<Effect> list = new List<Effect>();
			switch (effectData.effectType)
			{
			case EffectType.StatisticEffect:
			{
				List<StatCollection> targetStatCollections = this.GetTargetStatCollections(effectData, target);
				for (int i = 0; i < targetStatCollections.Count; i++)
				{
					if (targetStatCollections[i].ContainsStatistic(effectData.statisticData.statName))
					{
						list.Add(new StatisticEffect(base.Combat, effectID, stackItemUID, creator, target, targetStatCollections[i], effectData, hitInfo, attackIndex));
					}
				}
				break;
			}
			case EffectType.TagEffect:
				list.Add(new TagEffect(base.Combat, effectID, stackItemUID, creator, target, effectData, hitInfo, attackIndex));
				break;
			case EffectType.ActorBurningEffect:
				list.Add(new ActorBurningEffect(base.Combat, effectID, stackItemUID, creator, target, effectData, hitInfo, attackIndex));
				break;
			case EffectType.VFXEffect:
				list.Add(new VFXEffect(base.Combat, effectID, stackItemUID, creator, target, effectData, hitInfo, attackIndex));
				break;
			case EffectType.InstantModEffect:
				list.Add(new InstantModEffect(base.Combat, effectID, stackItemUID, creator, target, effectData, hitInfo, attackIndex));
				break;
			case EffectType.PoorlyMaintainedEffect:
				list.Add(new PoorlyMaintainedEffect(base.Combat, effectID, stackItemUID, creator, target, effectData, hitInfo, attackIndex));
				break;
			case EffectType.FloatieEffect:
			{
				List<object> targetObjects = this.GetTargetObjects(effectData, target);
				for (int j = 0; j < targetObjects.Count; j++)
				{
					list.Add(new FloatieEffect(base.Combat, effectID, stackItemUID, creator, target, targetObjects[j], effectData, hitInfo, attackIndex));
				}
				break;
			}
			}
			for (int k = 0; k < list.Count; k++)
			{
				Effect effect = list[k];
				if (effect != null)
				{
					if (allEffectsTargetingWithUniqueID.Count > 0 && effect.EffectData.durationData.uniqueEffectIdStackLimit > 0 && allEffectsTargetingWithUniqueID.Count >= effect.EffectData.durationData.uniqueEffectIdStackLimit)
					{
						Effect oldestEffect = this.GetOldestEffect(allEffectsTargetingWithUniqueID);
						this.RefreshEffect(oldestEffect, effect);
					}
					else if (allEffectsTargetingWithBaseID.Count > 0 && effect.EffectData.durationData.stackLimit > 0 && allEffectsTargetingWithBaseID.Count >= effect.EffectData.durationData.stackLimit)
					{
						Effect oldestEffect2 = this.GetOldestEffect(allEffectsTargetingWithBaseID);
						this.RefreshEffect(oldestEffect2, effect);
					}
					else
					{
						this.AddEffect(effect, skipLogging);
					}
					if (EffectManager.AbilityLogger.IsLogEnabled)
					{
						LogLevel logLevel = (skipLogging ? LogLevel.Debug : LogLevel.Log);
						EffectManager.AbilityLogger.LogAtLevel(logLevel, string.Format("{0} gains effect {1} from team {2}", target.DisplayName, effect.EffectData.Description.Name, creator.DisplayName));
					}
				}
			}
			return list;
		}
```

This code defines a method named `CreateEffect` that takes several parameters and returns a list of `Effect` objects. 

Here's a breakdown of what happens inside the method:

1. It retrieves all effects targeting the same target with the same base ID and unique ID.
2. It creates an empty list of `Effect` objects.
3. Depending on the `effectType` of the `effectData` parameter, it creates a new effect of the corresponding type and adds it to the list. For example, if `effectType` is `StatisticEffect`, it gets all the target's stat collections that contain the statistic specified in `effectData.statisticData.statName` and creates a new `StatisticEffect` for each of them.
4. After all effects have been created, it iterates over the list of effects. For each effect:
   - If there are already effects targeting the same target with the same unique ID and the stack limit for unique effect IDs has been reached, it refreshes the oldest effect with the new effect.
   - If there are already effects targeting the same target with the same base ID and the stack limit for base IDs has been reached, it refreshes the oldest effect with the new effect.
   - Otherwise, it adds the new effect.
   - If logging is enabled, it logs a message indicating that the target has gained the effect from the creator team.
5. Finally, it returns the list of effects.

This method is typically used to create and apply effects to targets in a combat scenario. The effects could be anything from statistic modifications to visual effects, depending on the `EffectType`.

The `skipLogging` parameter allows you to control whether the creation and application of effects should be logged. This can be useful for debugging or tracking game events.

The `stackItemUID` and `attackIndex` parameters seem to be identifiers used for tracking or referencing the effects. The `hitInfo` parameter likely contains information about the attack that caused the effects.

The `creator` parameter is the team that created the effects, and the `target` parameter is the combatant that the effects are applied to. The `effectData` parameter contains the data needed to create the effects, and the `effectID` parameter is a unique identifier for the effects. The method ensures that the number of effects targeting the same target with the same base ID or unique ID does not exceed the respective stack limits specified in the `effectData`.

If the stack limit is reached, the oldest effect is refreshed with the new effect. Otherwise, the new effect is added. This ensures that the most recent effects are always applied and that the number of effects does not exceed the stack limits.

The method also logs a message whenever an effect is added or an old effect is refreshed, if logging is enabled. This can be useful for tracking game events or debugging. Finally, the method returns the list of effects that were created. This list can then be used elsewhere in the code, for example to apply the effects to the target or to display them in the game's user interface.

## EffectManager.GetTargetCombatantForEffect

```
public List<ICombatant> GetTargetCombatantForEffect(EffectData effect, ICombatant creator, ICombatant initialTarget)
		{
			List<ICombatant> list = new List<ICombatant>();
			new List<AbstractActor>();
			List<AbstractActor> list2 = new List<AbstractActor>();
			switch (effect.targetingData.effectTargetType)
			{
			case EffectTargetType.Creator:
				list.Add(creator);
				return list;
			case EffectTargetType.SingleTarget:
				list.Add(initialTarget);
				return list;
			case EffectTargetType.LanceMatesWithinRange:
			{
				list2 = base.Combat.AllActors.FindAll((AbstractActor x) => x.team == creator.team);
				for (int i = 0; i < list2.Count; i++)
				{
					if (Vector3.Distance(creator.CurrentPosition, list2[i].CurrentPosition) <= effect.targetingData.range)
					{
						list.Add(list2[i]);
					}
				}
				return list;
			}
			case EffectTargetType.AlliesWithinRange:
			{
				list2 = base.Combat.AllActors.FindAll((AbstractActor x) => x.team.IsFriendly(creator.team));
				for (int j = 0; j < list2.Count; j++)
				{
					if (Vector3.Distance(creator.CurrentPosition, list2[j].CurrentPosition) <= effect.targetingData.range)
					{
						list.Add(list2[j]);
					}
				}
				return list;
			}
			case EffectTargetType.EnemiesWithinRange:
			{
				list2 = base.Combat.AllActors.FindAll((AbstractActor x) => x.team.IsEnemy(creator.team));
				for (int k = 0; k < list2.Count; k++)
				{
					if (Vector3.Distance(creator.CurrentPosition, list2[k].CurrentPosition) <= effect.targetingData.range)
					{
						list.Add(list2[k]);
					}
				}
				return list;
			}
			case EffectTargetType.AllLanceMates:
				list2 = base.Combat.AllActors.FindAll((AbstractActor x) => x.team == creator.team);
				list.AddRange(list2);
				return list;
			case EffectTargetType.AllAllies:
				list2 = base.Combat.AllActors.FindAll((AbstractActor x) => x.team.IsFriendly(creator.team));
				list.AddRange(list2);
				return list;
			case EffectTargetType.AllEnemies:
				list2 = base.Combat.AllActors.FindAll((AbstractActor x) => x.team.IsEnemy(creator.team));
				list.AddRange(list2);
				return list;
			}
			EffectTriggerType effectTriggerType = effect.targetingData.effectTriggerType;
			if (effectTriggerType == EffectTriggerType.OnHit || effectTriggerType == EffectTriggerType.OnWeaponFire)
			{
				list.Add(initialTarget);
			}
			else
			{
				list.Add(creator);
			}
			return list;
		}
```

This code defines a method named `GetTargetCombatantForEffect` that takes three parameters: an `EffectData` object named `effect`, an `ICombatant` object named `creator`, and another `ICombatant` object named `initialTarget`. The method returns a list of `ICombatant` objects.

Here's a breakdown of what happens inside the method:

1. A new list of `ICombatant` objects is created, named `list`.
2. A new list of `AbstractActor` objects is created, named `list2`.
3. The method then checks the `effectTargetType` property of the `targetingData` property of the `effect` object.
4. Depending on the value of `effectTargetType`, the method does different things:
   - If `effectTargetType` is `Creator`, the `creator` is added to `list`.
   - If `effectTargetType` is `SingleTarget`, the `initialTarget` is added to `list`.
   - If `effectTargetType` is `LanceMatesWithinRange`, `AlliesWithinRange`, or `EnemiesWithinRange`, the method finds all actors in `base.Combat.AllActors` that meet certain team conditions, adds them to `list2`, and then checks each actor in `list2`. If the distance between the `creator` and the actor is less than or equal to `effect.targetingData.range`, the actor is added to `list`.
   - If `effectTargetType` is `AllLanceMates`, `AllAllies`, or `AllEnemies`, the method finds all actors in `base.Combat.AllActors` that meet certain team conditions and adds them to `list`.
5. After the switch statement, the method checks the `effectTriggerType` property of the `targetingData` property of the `effect` object. If `effectTriggerType` is `OnHit` or `OnWeaponFire`, the `initialTarget` is added to `list`. Otherwise, the `creator` is added to `list`.
6. Finally, the method returns `list`.

This method is used to get a list of combatants that are the targets for a certain effect. The targets are determined based on the `effectTargetType` and `effectTriggerType` properties of the `effect` object, and can include the `creator`, the `initialTarget`, or other actors within a certain range. The method returns a list of these targets. The returned list can then be used elsewhere in the program to apply the effect to these targets.

## EffectManager.GetTargetComponents

```
private List<MechComponent> GetTargetComponents(ICombatant target, StatisticEffectData.TargetCollection targetCollection, WeaponSubType weaponSubType, WeaponType weaponType, WeaponCategoryValue weaponCategoryValue, AmmoCategoryValue ammoCategoryValue)
		{
			List<MechComponent> list = new List<MechComponent>();
			if (targetCollection == StatisticEffectData.TargetCollection.SingleRandomWeapon)
			{
				AbstractActor abstractActor = target as AbstractActor;
				if (abstractActor != null)
				{
					List<Weapon> list2 = abstractActor.Weapons.FindAll((Weapon x) => !x.IsDisabled);
					if (list2.Count > 0)
					{
						int num = base.Combat.TurnDirector.CurrentPhase * 113 + base.Combat.TurnDirector.CurrentRound * 779 + base.Combat.TurnDirector.ActiveTurnActor.GetNumUnusedUnitsForCurrentPhase() * 397 + base.Combat.TurnDirector.TotalElapsedPhases * 237;
						num %= list2.Count;
						list.Add(list2[num]);
					}
				}
			}
			else if (targetCollection == StatisticEffectData.TargetCollection.StrongestWeapon)
			{
				AbstractActor abstractActor2 = target as AbstractActor;
				if (abstractActor2 != null)
				{
					List<Weapon> list3 = abstractActor2.Weapons.FindAll((Weapon x) => !x.IsDisabled);
					if (list3.Count > 0)
					{
						list3.Sort((Weapon a, Weapon b) => b.DamagePerShot.CompareTo(a.DamagePerShot * (float)a.ShotsWhenFired));
						list.Add(list3[0]);
					}
				}
			}
			else if (targetCollection == StatisticEffectData.TargetCollection.Weapon)
			{
				AbstractActor abstractActor3 = target as AbstractActor;
				if (abstractActor3 != null)
				{
					List<Weapon> list4 = new List<Weapon>();
					if (weaponSubType != WeaponSubType.NotSet)
					{
						if (weaponSubType == WeaponSubType.Melee)
						{
							Mech mech = abstractActor3 as Mech;
							if (mech != null)
							{
								list4.Add(mech.MeleeWeapon);
							}
						}
						else if (weaponSubType == WeaponSubType.DFA)
						{
							Mech mech2 = abstractActor3 as Mech;
							if (mech2 != null)
							{
								list4.Add(mech2.DFAWeapon);
							}
						}
						else
						{
							list4 = abstractActor3.Weapons.FindAll((Weapon x) => x.WeaponSubType == weaponSubType);
						}
					}
					else if (weaponType != WeaponType.NotSet)
					{
						list4 = abstractActor3.Weapons.FindAll((Weapon x) => x.Type == weaponType);
					}
					else if (!weaponCategoryValue.Is_NotSet)
					{
						list4 = abstractActor3.Weapons.FindAll((Weapon x) => x.WeaponCategoryValue.ID == weaponCategoryValue.ID);
					}
					else
					{
						list4 = new List<Weapon>(abstractActor3.Weapons);
					}
					for (int i = 0; i < list4.Count; i++)
					{
						list.Add(list4[i]);
					}
				}
			}
			else if (targetCollection == StatisticEffectData.TargetCollection.AmmoBox)
			{
				AbstractActor abstractActor4 = target as AbstractActor;
				if (abstractActor4 != null)
				{
					List<AmmunitionBox> list5 = new List<AmmunitionBox>();
					if (!ammoCategoryValue.Is_NotSet)
					{
						list5 = abstractActor4.ammoBoxes.FindAll((AmmunitionBox x) => x.ammoCategoryValue.Equals(ammoCategoryValue));
					}
					else
					{
						list5 = new List<AmmunitionBox>(abstractActor4.ammoBoxes);
					}
					for (int j = 0; j < list5.Count; j++)
					{
						list.Add(list5[j]);
					}
				}
			}
			return list;
		}
```

This code defines a method named `GetTargetComponents` that takes six parameters: an `ICombatant` object named `target`, a `StatisticEffectData.TargetCollection` enumeration named `targetCollection`, a `WeaponSubType` enumeration named `weaponSubType`, a `WeaponType` enumeration named `weaponType`, a `WeaponCategoryValue` object named `weaponCategoryValue`, and an `AmmoCategoryValue` object named `ammoCategoryValue`. The method returns a list of `MechComponent` objects.

Here's a breakdown of what happens inside the method:

1. A new list of `MechComponent` objects is created, named `list`.
2. The method then checks the value of `targetCollection`.
3. Depending on the value of `targetCollection`, the method does different things:
   - If `targetCollection` is `SingleRandomWeapon`, the method finds all non-disabled weapons of the `target` (if it's an `AbstractActor`), calculates a random index based on the current phase, round, number of unused units, and total elapsed phases, and adds the weapon at that index to `list`.
   - If `targetCollection` is `StrongestWeapon`, the method finds all non-disabled weapons of the `target` (if it's an `AbstractActor`), sorts them in descending order of damage per shot, and adds the strongest weapon to `list`.
   - If `targetCollection` is `Weapon`, the method finds all weapons of the `target` (if it's an `AbstractActor`) that meet certain conditions based on `weaponSubType`, `weaponType`, and `weaponCategoryValue`, and adds them to `list`.
   - If `targetCollection` is `AmmoBox`, the method finds all ammunition boxes of the `target` (if it's an `AbstractActor`) that meet certain conditions based on `ammoCategoryValue`, and adds them to `list`.
4. Finally, the method returns `list`.

This method is used to get a list of components (weapons or ammunition boxes) of a target combatant that meet certain conditions. The conditions are determined based on the `targetCollection`, `weaponSubType`, `weaponType`, `weaponCategoryValue`, and `ammoCategoryValue` parameters. The method returns a list of these components. The returned list can then be used elsewhere in the program to apply effects to these components. For example, an effect might damage a random weapon, the strongest weapon, all weapons of a certain type, or all ammunition boxes of a certain category. This method provides a way to get the target components for such effects.

## EffectManager.GetTargetObjects

```
private List<object> GetTargetObjects(EffectData effectData, ICombatant target)
		{
			List<object> list = new List<object>();
			StatisticEffectData.TargetCollection targetCollection = effectData.floatieData.targetCollection;
			WeaponSubType targetWeaponSubType = effectData.floatieData.targetWeaponSubType;
			WeaponType targetWeaponType = effectData.floatieData.targetWeaponType;
			WeaponCategoryValue targetWeaponCategoryValue = effectData.floatieData.TargetWeaponCategoryValue;
			AmmoCategoryValue targetAmmoCategoryValue = effectData.floatieData.TargetAmmoCategoryValue;
			if (targetCollection == StatisticEffectData.TargetCollection.NotSet)
			{
				list.Add(target);
			}
			else if (targetCollection == StatisticEffectData.TargetCollection.Pilot)
			{
				if (target.IsPilotable && target.GetPilot() != null)
				{
					list.Add(target.GetPilot());
				}
			}
			else
			{
				list.AddRange(this.GetTargetComponents(target, targetCollection, targetWeaponSubType, targetWeaponType, targetWeaponCategoryValue, targetAmmoCategoryValue).ConvertAll<object>((MechComponent x) => x));
			}
			return list;
		}
```

This code defines a method named `GetTargetObjects` that takes two parameters: an `EffectData` object named `effectData`, and an `ICombatant` object named `target`. The method returns a list of objects.

Here's a breakdown of what happens inside the method:

1. A new list of objects is created, named `list`.
2. Several properties of the `floatieData` property of the `effectData` object are retrieved and stored in local variables.
3. The method then checks the value of `targetCollection`.
4. Depending on the value of `targetCollection`, the method does different things:
   - If `targetCollection` is `NotSet`, the `target` is added to `list`.
   - If `targetCollection` is `Pilot`, and if the `target` is pilotable and has a pilot, the pilot of the `target` is added to `list`.
   - Otherwise, the method calls the `GetTargetComponents` method with the `target` and the local variables as arguments, converts the returned list of `MechComponent` objects to a list of objects, and adds the converted list to `list`.
5. Finally, the method returns `list`.

This method is used to get a list of target objects for a certain effect. The targets are determined based on the `targetCollection` property of the `effectData` object, and can include the `target` itself, its pilot, or its components. The method returns a list of these targets. The returned list can then be used elsewhere in the program to apply the effect to these targets. For example, an effect might apply to the target combatant, its pilot, or its weapons or ammunition boxes. This method provides a way to get the target objects for such effects.

## EffectManager.GetTargetStatCollection

```
private List<StatCollection> GetTargetStatCollections(EffectData effectData, ICombatant target)
		{
			List<StatCollection> list = new List<StatCollection>();
			StatisticEffectData.TargetCollection targetCollection = effectData.statisticData.targetCollection;
			WeaponSubType targetWeaponSubType = effectData.statisticData.targetWeaponSubType;
			WeaponType targetWeaponType = effectData.statisticData.targetWeaponType;
			WeaponCategoryValue targetWeaponCategoryValue = effectData.statisticData.TargetWeaponCategoryValue;
			AmmoCategoryValue targetAmmoCategoryValue = effectData.statisticData.TargetAmmoCategoryValue;
			if (targetCollection == StatisticEffectData.TargetCollection.NotSet)
			{
				list.Add(target.StatCollection);
			}
			else if (targetCollection == StatisticEffectData.TargetCollection.Pilot)
			{
				if (target.IsPilotable && target.GetPilot() != null)
				{
					list.Add(target.GetPilot().StatCollection);
				}
			}
			else
			{
				List<MechComponent> targetComponents = this.GetTargetComponents(target, targetCollection, targetWeaponSubType, targetWeaponType, targetWeaponCategoryValue, targetAmmoCategoryValue);
				for (int i = 0; i < targetComponents.Count; i++)
				{
					list.Add(targetComponents[i].StatCollection);
				}
			}
			return list;
		}
```

This code is a method named `GetTargetStatCollections` that takes two parameters: `effectData` of type `EffectData` and `target` of type `ICombatant`. The purpose of this method is to gather a list of `StatCollection` objects based on the `effectData` and `target` provided.

Here's a step-by-step explanation:

1. It initializes an empty list of `StatCollection` objects.
2. It retrieves various properties from the `effectData` object, such as `targetCollection`, `targetWeaponSubType`, `targetWeaponType`, `TargetWeaponCategoryValue`, and `TargetAmmoCategoryValue`.
3. It checks the value of `targetCollection`. If it's `NotSet`, it adds the `StatCollection` of the `target` to the list.
4. If `targetCollection` is `Pilot`, it checks if the `target` is pilotable and has a pilot. If so, it adds the `StatCollection` of the pilot to the list.
5. If `targetCollection` is neither `NotSet` nor `Pilot`, it retrieves a list of `MechComponent` objects by calling the `GetTargetComponents` method with the `target` and the properties retrieved from `effectData`. It then adds the `StatCollection` of each `MechComponent` to the list.
6. Finally, it returns the list of `StatCollection` objects.

This method seems to be part of a larger system, possibly a game or simulation, where different combatants have different stats that can be affected by various effects. The `StatCollection` objects represent these stats. The method is used to determine which stats should be affected by a given effect. The specifics would depend on the definitions of `EffectData`, `ICombatant`, `StatCollection`, `StatisticEffectData.TargetCollection`, `WeaponSubType`, `WeaponType`, `WeaponCategoryValue`, `AmmoCategoryValue`, and `MechComponent`.

## FactorUtil.DoesActorHaveECM

```
public static bool DoesActorHaveECM(AbstractActor actor)
		{
			if (actor == null || actor.IsDead)
			{
				return false;
			}
			if (actor.AuraComponents == null || actor.AuraComponents.Count <= 0)
			{
				return false;
			}
			for (int i = 0; i < actor.AuraComponents.Count; i++)
			{
				MechComponent mechComponent = actor.AuraComponents[i];
				for (int j = 0; j < mechComponent.componentDef.statusEffects.Length; j++)
				{
					EffectData effectData = mechComponent.componentDef.statusEffects[j];
					if (effectData.targetingData.auraEffectType == AuraEffectType.ECM_GENERAL || effectData.targetingData.auraEffectType == AuraEffectType.ECM_GHOST)
					{
						return true;
					}
				}
			}
			return false;
		}
```

This C# Unity code is a method named `DoesActorHaveECM` that checks if a given actor has an ECM (Electronic Countermeasure) effect. Here's what it does in plain English:

1. It first checks if the `actor` parameter is `null` or if the actor is dead. If either of these conditions is true, it immediately returns `false`. This means that it considers actors that are `null` or dead to not have an ECM effect.

2. It then checks if the `AuraComponents` of the actor is `null` or if it has no elements. If either of these conditions is true, it immediately returns `false`. This means that it considers actors with no aura components to not have an ECM effect.

3. If the actor is not `null` or dead and has aura components, it iterates over each `MechComponent` in the actor's `AuraComponents`.

4. For each `MechComponent`, it iterates over each `EffectData` in the component's `statusEffects`.

5. It checks if the `auraEffectType` of the `EffectData`'s `targetingData` is either `ECM_GENERAL` or `ECM_GHOST`. If it is, it immediately returns `true`. This means that it considers actors with at least one aura component that has a status effect of type `ECM_GENERAL` or `ECM_GHOST` to have an ECM effect.

6. If it iterates over all aura components and status effects and doesn't find an `ECM_GENERAL` or `ECM_GHOST` effect, it returns `false`.

So, in summary, this method checks if a given actor has an ECM effect and returns `true` if it does, and `false` otherwise. Please note that the exact behavior might vary depending on the implementation of the methods and properties being used. This is a high-level explanation based on the provided code snippet.

## SpecialRule Data

Go to [the SpecialRule breakdown](./Status-Effect-Parts/Special-rules.md) for more information on the SpecialRule options.

## ActiveAbilityEffectData

```
[SerializableContract("ActiveAbilityEffectData")]
	public class ActiveAbilityEffectData : ISaveable
	{
		public ActiveAbilityEffectData()
		{
		}

		public ActiveAbilityEffectData(string abilityName)
		{
			this.abilityName = abilityName;
		}

		public int Size()
		{
			return 0 + Serialization.StorageSpaceString(this.abilityName);
		}

		public bool ShouldSave()
		{
			return true;
		}

		public void Save(SerializationStream stream)
		{
			stream.PutString(this.abilityName);
		}

		public void Load(SerializationStream stream)
		{
			this.abilityName = stream.GetString();
		}

		public void LoadComplete()
		{
		}

		[SerializableMember(SerializationTarget.SaveGame)]
		public string abilityName;
	}
```

This Unity C# code defines a class `ActiveAbilityEffectData` within the `BattleTech` namespace. Here's what it does in plain English:

- The class `ActiveAbilityEffectData` implements the `ISaveable` interface, which means it has methods related to saving and loading data.
- It has a public string field `abilityName` that is marked with the `SerializableMember` attribute, indicating that it should be saved when the game is saved.
- It has two constructors:
  - The default constructor `ActiveAbilityEffectData()` which initializes a new instance of the class.
  - The parameterized constructor `ActiveAbilityEffectData(string abilityName)` which initializes a new instance of the class and sets the `abilityName` field.
- The `Size()` method returns the storage space required for the `abilityName` string.
- The `ShouldSave()` method always returns `true`, indicating that an instance of this class should be saved.
- The `Save(SerializationStream stream)` method saves the `abilityName` to the provided `stream`.
- The `Load(SerializationStream stream)` method loads the `abilityName` from the provided `stream`.
- The `LoadComplete()` method is an empty method, possibly intended to be overridden in derived classes or to be filled in with additional logic later.

## ActiveAbilityOrderInfo

```
public ActiveAbilityOrderInfo(AbstractActor movingUnit, ICombatant targetUnit)
		: base(OrderType.ActiveAbility)
	{
		this.movingUnit = movingUnit;
		this.targetUnit = targetUnit;
	}

	public abstract ActiveAbilityID GetActiveAbilityID();

	public AbstractActor movingUnit;

	public ICombatant targetUnit;
```

This Unity C# code defines an abstract class `ActiveAbilityOrderInfo` that inherits from the `OrderInfo` class. Here's what it does in plain English:

- The class `ActiveAbilityOrderInfo` is an abstract class, which means it cannot be instantiated directly and is intended to be subclassed.
- It has two public fields: `movingUnit` of type `AbstractActor` and `targetUnit` of type `ICombatant`. These fields represent the unit that is moving and the unit that is being targeted, respectively.
- It has a constructor `ActiveAbilityOrderInfo(AbstractActor movingUnit, ICombatant targetUnit)` that takes two parameters: a moving unit and a target unit. This constructor initializes a new instance of the class and sets the `movingUnit` and `targetUnit` fields. It also calls the base class constructor with `OrderType.ActiveAbility`.
- It has an abstract method `GetActiveAbilityID()` that returns an `ActiveAbilityID`. This method must be implemented in any non-abstract class that inherits from `ActiveAbilityOrderInfo`. This method is intended to get the ID of the active ability associated with the order.

## Pilot.SortAbilityIntoLists

```
private void SortAbilityIntoLists(Ability ability)
		{
			AbilityDef def = ability.Def;
			if (def.ActivationTime != AbilityDef.ActivationTiming.Passive && def.ActivationTime != AbilityDef.ActivationTiming.NotSet)
			{
				this.ActiveAbilities.Add(ability);
			}
			if (def.specialRules == AbilityDef.SpecialRules.Aura)
			{
				this.AuraAbilities.Add(ability);
			}
			if (def.ActivationTime == AbilityDef.ActivationTiming.Passive && def.specialRules == AbilityDef.SpecialRules.NotSet)
			{
				this.PassiveAbilities.Add(ability);
			}
			if (def.ActivationTime == AbilityDef.ActivationTiming.Passive && def.specialRules == AbilityDef.SpecialRules.OnInjured)
			{
				this.OnInjuredAbilities.Add(ability);
			}
			if (def.ActivationTime == AbilityDef.ActivationTiming.Passive && def.specialRules == AbilityDef.SpecialRules.OnReserve)
			{
				this.OnReserveAbilities.Add(ability);
			}
		}
```

Sure, here's what the Unity C# code does in plain English:

- The function `SortAbilityIntoLists` takes an `Ability` object as an argument.
- It retrieves the `AbilityDef` object from the `Ability` object and assigns it to the variable `def`.
- The function then checks the `ActivationTime` and `specialRules` properties of the `def` object and sorts the `Ability` object into different lists based on these properties.

Here are the conditions and the corresponding actions in bullet points:

- If the `ActivationTime` of the `Ability` is neither `Passive` nor `NotSet`, the `Ability` is added to the `ActiveAbilities` list.
- If the `specialRules` of the `Ability` is set to `Aura`, the `Ability` is added to the `AuraAbilities` list.
- If the `ActivationTime` of the `Ability` is `Passive` and `specialRules` is `NotSet`, the `Ability` is added to the `PassiveAbilities` list.
- If the `ActivationTime` of the `Ability` is `Passive` and `specialRules` is `OnInjured`, the `Ability` is added to the `OnInjuredAbilities` list.
- If the `ActivationTime` of the `Ability` is `Passive` and `specialRules` is `OnReserve`, the `Ability` is added to the `OnReserveAbilities` list.

This function essentially categorizes abilities based on their activation time and special rules, and adds them to the appropriate lists for further use in the program.

## Pilot.GetActiveAbility

```
public Ability GetActiveAbility(ActiveAbilityID abilityID)
		{
			if (abilityID == ActiveAbilityID.SensorLock)
			{
				return this.Abilities.Find((Ability x) => x.Def.Targeting == AbilityDef.TargetingType.SensorLock);
			}
			return null;
		}
```

Sure, here's what the Unity C# code does in plain English:

- The function `GetActiveAbility` takes an `ActiveAbilityID` object as an argument, which is named `abilityID`.
- It checks if the `abilityID` is equal to `ActiveAbilityID.SensorLock`.
- If the `abilityID` is `SensorLock`, it searches the `Abilities` list for an `Ability` object where the `Targeting` property of the `Ability`'s `Def` object is `SensorLock`.
- If it finds such an `Ability` object, it returns that object.
- If the `abilityID` is not `SensorLock`, or if no matching `Ability` object is found, it returns `null`.

Here are the actions in bullet points:

- The function `GetActiveAbility` is declared, which takes an `ActiveAbilityID` named `abilityID` as an argument.
- An `if` statement checks if `abilityID` equals `ActiveAbilityID.SensorLock`.
- If the `if` condition is true, the function returns an `Ability` from the `Abilities` list where the `Targeting` property of the `Ability`'s `Def` object equals `AbilityDef.TargetingType.SensorLock`.
- If the `if` condition is false, the function returns `null`.

This function essentially retrieves a specific `Ability` object from the `Abilities` list based on the `abilityID` provided.

## effectType Data

Go to [the effectType breakdown](./Status-Effect-Parts/Effect-type.md) for more information on the SpecialRule options.