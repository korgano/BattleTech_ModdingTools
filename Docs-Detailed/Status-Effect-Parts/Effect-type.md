# effectType Data

AI Generated notes to help explain the **many** elements that make up a Status Effect in BattleTech. This aims to explain what a named option in the status effect does, to help you make the right choices. You are encouraged to use `CRTL+F` to find what you're specifically looking for.

If you spot any egregious errors, please correct them.

**NOTES:** 
- This data is only guaranteed valid for creating status effects compatible with Vanilla BattleTech. Any mod/mod pack that significantly alters game functionality through patching may **not** be compatible with the following explanations.
- Only `FloatieEffect` and `VFXEffect` have known code implementations via the Heavy Metal DLC.

Return to [Status Effects Info](../Docs-Detailed/Status-effects-info)


## FloatieEffect

```
	[SerializableContract("FloatieEffect")]
	public class FloatieEffect : Effect
	{
		// (get) Token: 0x06007335 RID: 29493 RVA: 0x001E1A16 File Offset: 0x001DFC16
		public new AbstractActor Target
		{
			get
			{
				return this.target as AbstractActor;
			}
		}

		public FloatieEffect(CombatGameState combat, string effectID, int stackItemUID, ICombatant creator, ICombatant target, object targetObject, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, targetObject, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		public FloatieEffect(CombatGameState combat, string effectID, int stackItemUID, Team creator, ICombatant target, object targetObject, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, targetObject, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		public FloatieEffect()
		{
		}

		public override void OnEffectBegin(bool skipLogging = false)
		{
			base.OnEffectBegin(skipLogging);
			this.Trigger();
		}

		public override void OnEffectTakeDamage(AbstractActor attacker, AbstractActor target)
		{
			base.OnEffectTakeDamage(attacker, target);
			if (this.effectData.targetingData.effectTriggerType == EffectTriggerType.OnDamaged && this.SpecialRulesMet(attacker, target))
			{
				this.Trigger();
			}
		}

		public override void Trigger()
		{
			base.Trigger();
			if (this.effectData.targetingData.triggerLimit <= 0 || base.triggerCount < this.effectData.targetingData.triggerLimit)
			{
				int num = base.triggerCount + 1;
				base.triggerCount = num;
				this.eTimer.IncrementActivations(this.effectData.targetingData.extendDurationOnTrigger);
				this.combat.MessageCenter.PublishMessage(new FloatieMessage(this.Target.GUID, this.Target.GUID, this.effectData.Description.Details, (this.effectData.nature == EffectNature.Buff) ? FloatieMessage.MessageNature.Buff : FloatieMessage.MessageNature.Debuff));
			}
		}

		private bool SpecialRulesMet(AbstractActor attacker, AbstractActor target)
		{
			AbilityDef.SpecialRules specialRules = this.effectData.targetingData.specialRules;
			return specialRules != AbilityDef.SpecialRules.HalfArmorOrLess || target.CurrentArmor <= target.StartingArmor * 0.5f;
		}

		// Token: 0x0600733D RID: 29501 RVA: 0x001E1BB2 File Offset: 0x001DFDB2
		public override string ToString()
		{
			if (!string.IsNullOrEmpty(this.effectData.Description.Details))
			{
				return string.Format(this.effectData.Description.Details, Array.Empty<object>());
			}
			return "";
		}
	}
```

Sure, here's what the Unity C# code does in plain English:

- The `FloatieEffect` class is a subclass of the `Effect` class and is marked as serializable with the contract name "FloatieEffect".
- It has a property `Target` that gets the `target` field cast as an `AbstractActor`.
- It has three constructors:
    - The first constructor takes several parameters including `CombatGameState`, `effectID`, `stackItemUID`, `creator`, `target`, `targetObject`, `effectData`, `hitInfo`, and `attackIndex`. It calls the base class constructor with these parameters.
    - The second constructor is similar to the first but takes a `Team` object as the `creator` instead of an `ICombatant`.
    - The third constructor is a parameterless constructor.
- It overrides the `OnEffectBegin` method from the base class to call the base method and then trigger the effect.
- It overrides the `OnEffectTakeDamage` method to call the base method and then, if certain conditions are met, trigger the effect.
- It overrides the `Trigger` method to call the base method and then, if certain conditions are met, increment the trigger count, extend the duration of the effect, and publish a `FloatieMessage`.
- It has a private method `SpecialRulesMet` that checks if certain special rules are met based on the `attacker` and `target`.
- It overrides the `ToString` method to return a formatted string based on the `effectData.Description.Details` if it's not null or empty, otherwise it returns an empty string.

Here are the actions in bullet points:

- The `FloatieEffect` class is declared, which extends the `Effect` class.
- The `Target` property is declared, which gets the `target` field cast as an `AbstractActor`.
- Three constructors are declared for the `FloatieEffect` class.
- The `OnEffectBegin` method is overridden to trigger the effect when the effect begins.
- The `OnEffectTakeDamage` method is overridden to trigger the effect when the effect takes damage, if certain conditions are met.
- The `Trigger` method is overridden to increment the trigger count, extend the duration of the effect, and publish a `FloatieMessage`, if certain conditions are met.
- The `SpecialRulesMet` method is declared to check if certain special rules are met.
- The `ToString` method is overridden to return a formatted string based on the `effectData.Description.Details`.

This class essentially represents a special type of effect in a combat game that can be triggered under certain conditions and can send messages when triggered.

## InstantModEffect

```
	[SerializableContract("InstantModEffect")]
	public class InstantModEffect : Effect
	{

		public new AbstractActor Target
		{
			get
			{
				return this.target as AbstractActor;
			}
		}

		public InstantModEffect(CombatGameState combat, string effectID, int stackItemUID, ICombatant creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		public InstantModEffect(CombatGameState combat, string effectID, int stackItemUID, Team creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		// Token: 0x06007341 RID: 29505 RVA: 0x001DE68A File Offset: 0x001DC88A
		public InstantModEffect()
		{
		}

		public override void OnEffectBegin(bool skipLogging = false)
		{
			base.OnEffectBegin(skipLogging);
			InstantModEffectData.StatToMod targetStat = this.effectData.instantModData.targetStat;
			if (targetStat != InstantModEffectData.StatToMod.Stability)
			{
				if (targetStat == InstantModEffectData.StatToMod.Heat)
				{
					Mech mech = this.Target as Mech;
					if (mech != null)
					{
						mech.AdjustHeatDirectly(base.EffectData.instantModData.floatMod, this.stackItemUID, mech.GUID);
						return;
					}
				}
			}
			else
			{
				Mech mech2 = this.Target as Mech;
				if (mech2 != null)
				{
					mech2.AddRelativeInstability(base.EffectData.instantModData.floatMod, StabilityChangeSource.Effect, this.creatorID);
				}
			}
		}

		public override void OnEffectEnd(bool expired, bool skipLogging = false)
		{
			base.OnEffectEnd(expired, skipLogging);
			if (this.effectData.targetingData.effectTriggerType == EffectTriggerType.OnDamaged)
			{
				return;
			}
			if (!expired)
			{
				InstantModEffectData.StatToMod targetStat = this.effectData.instantModData.targetStat;
				if (targetStat != InstantModEffectData.StatToMod.Stability)
				{
					if (targetStat == InstantModEffectData.StatToMod.Heat && !Mathf.Approximately(base.EffectData.instantModData.floatMod, 0f))
					{
						Mech mech = this.Target as Mech;
						if (mech != null)
						{
							mech.AdjustHeatDirectly(1f / base.EffectData.instantModData.floatMod, 0, mech.GUID);
							return;
						}
					}
				}
				else
				{
					Mech mech2 = this.Target as Mech;
					if (mech2 != null)
					{
						mech2.AddRelativeInstability(-1f * base.EffectData.instantModData.floatMod, StabilityChangeSource.Effect, this.creatorID);
					}
				}
			}
		}

		public override bool CheckEffectTarget(object target)
		{
			AbstractActor abstractActor = target as AbstractActor;
			return this.Target == abstractActor;
		}

		public override string ToString()
		{
			return this.effectData.Description.Details;
		}
	}
```

Sure, here's what the Unity C# code does in plain English:

- The `InstantModEffect` class is a subclass of the `Effect` class and is marked as serializable with the contract name "InstantModEffect".
- It has a property `Target` that gets the `target` field cast as an `AbstractActor`.
- It has three constructors:
    - The first constructor takes several parameters including `CombatGameState`, `effectID`, `stackItemUID`, `creator`, `target`, `effectData`, `hitInfo`, and `attackIndex`. It calls the base class constructor with these parameters.
    - The second constructor is similar to the first but takes a `Team` object as the `creator` instead of an `ICombatant`.
    - The third constructor is a parameterless constructor.
- It overrides the `OnEffectBegin` method from the base class to apply the effect immediately when it begins based on the `targetStat` of the `effectData`.
- It overrides the `OnEffectEnd` method to reverse the effect when it ends, if it has not expired and certain conditions are met.
- It overrides the `CheckEffectTarget` method to check if the target of the effect is the same as the provided target.
- It overrides the `ToString` method to return the `Details` of the `Description` of the `effectData`.

Here are the conditions and the corresponding actions in bullet points:

- The `InstantModEffect` class is declared, which extends the `Effect` class.
- The `Target` property is declared, which gets the `target` field cast as an `AbstractActor`.
- Three constructors are declared for the `InstantModEffect` class.
- The `OnEffectBegin` method is overridden to apply the effect immediately when it begins.
- The `OnEffectEnd` method is overridden to reverse the effect when it ends, if it has not expired and certain conditions are met.
- The `CheckEffectTarget` method is overridden to check if the target of the effect is the same as the provided target.
- The `ToString` method is overridden to return the `Details` of the `Description` of the `effectData`.

This class essentially represents a special type of effect in a combat game that is applied immediately when it begins and can be reversed when it ends.

## VFXEffect

```
public int hitLocation
		{
			get
			{
				if (this.vfxData.attachToImpactPoint)
				{
					int firstHitLocationForTarget = this.hitInfo.GetFirstHitLocationForTarget(this.Target.GUID);
					if (firstHitLocationForTarget >= 0)
					{
						return this.hitInfo.hitLocations[firstHitLocationForTarget];
					}
				}
				return this.vfxData.location;
			}
		}

		public VFXEffect(CombatGameState combat, string effectID, int stackItemUID, ICombatant creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		public VFXEffect(CombatGameState combat, string effectID, int stackItemUID, Team creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		private VFXEffect()
		{
		}

		public override void OnEffectBegin(bool skipLogging = false)
		{
			base.OnEffectBegin(skipLogging);
			if (!this.vfxData.isOneShot)
			{
				this.CreateVFX();
			}
		}

		public override void OnEffectPhaseBegin()
		{
			base.OnEffectPhaseBegin();
			if (!this.effectData.durationData.ticksOnActivations && this.vfxData.isOneShot)
			{
				this.CreateVFX();
			}
		}

		public override void OnEffectActivationEnd()
		{
			base.OnEffectActivationEnd();
			if (this.effectData.durationData.ticksOnActivations && this.vfxData.isOneShot)
			{
				this.CreateVFX();
			}
		}

		public override void OnEffectMovementEnd()
		{
			base.OnEffectMovementEnd();
			if (this.effectData.durationData.ticksOnMovements && this.vfxData.isOneShot)
			{
				this.CreateVFX();
			}
		}

		public override void OnEffectEnd(bool expired, bool skipLogging = false)
		{
			base.OnEffectEnd(expired, skipLogging);
			this.StopVFX();
		}

		public override void OnEffectRemoval(bool skipLogging = false)
		{
			base.OnEffectRemoval(skipLogging);
		}

		public override void OnEffectExpiration()
		{
			base.OnEffectExpiration();
		}

		public override bool CheckEffectTarget(object target)
		{
			return this.target == target;
		}

		private void CreateVFX()
		{
			Vector3 vector = Vector3.zero;
			if (this.vfxData.facesAttacker)
			{
				ICombatant combatant = this.combat.FindCombatantByGUID(this.creatorID, false);
				if (combatant != null && combatant != this.Target)
				{
					vector = combatant.CurrentPosition;
				}
			}
			int firstHitLocationForTarget = this.hitInfo.GetFirstHitLocationForTarget(this.Target.GUID);
			if (firstHitLocationForTarget < 0 || firstHitLocationForTarget >= this.hitInfo.hitPositions.Length)
			{
				Debug.LogError("hit failed for target " + this.Target.DisplayName);
				return;
			}
			Transform vfxtransform = this.gameRep.GetVFXTransform(this.hitLocation);
			Vector3 vector2 = this.hitInfo.hitPositions[firstHitLocationForTarget];
			vector2 = vfxtransform.InverseTransformPoint(vector2);
			this.gameRep.PlayVFXAt(vfxtransform, vector2, this.vfxData.vfxName, this.vfxData.isAttached, vector, this.vfxData.isOneShot, this.vfxData.duration);
			this.storedHitLoc = this.hitLocation;
			this.storedHitPos = vector2;
			this.storedLookatPos = vector;
		}

		private void CreateVFXFromSave()
		{
			if (this.Target == null)
			{
				Debug.LogError("Target is unavailable for VFXEffect on Loading From Save");
				return;
			}
			VFXEffect.StoredVFXEffectData storedVFXEffectData = new VFXEffect.StoredVFXEffectData
			{
				hitLocation = this.storedHitLoc,
				hitPos = this.storedHitPos,
				vfxName = this.vfxData.vfxName,
				isAttached = this.vfxData.isAttached,
				lookatPos = this.storedLookatPos,
				isOneShot = this.vfxData.isOneShot,
				duration = this.vfxData.duration
			};
			this.Target.VFXDataFromLoad.Add(storedVFXEffectData);
			Debug.LogError("VFXData Applied to Target");
		}
```

Sure, here's what the Unity C# code does in plain English:

- The `VFXEffect` class is a subclass of the `Effect` class.
- It has a property `hitLocation` that gets the hit location based on the `vfxData` and `hitInfo`.
- It has three constructors:
    - The first constructor takes several parameters including `CombatGameState`, `effectID`, `stackItemUID`, `creator`, `target`, `effectData`, `hitInfo`, and `attackIndex`. It calls the base class constructor with these parameters.
    - The second constructor is similar to the first but takes a `Team` object as the `creator` instead of an `ICombatant`.
    - The third constructor is a parameterless constructor.
- It overrides several methods from the base class to handle different stages of the effect, such as when it begins, when a phase begins, when activation ends, when movement ends, when it ends, when it's removed, and when it expires.
- It has a method `CheckEffectTarget` that checks if the target of the effect is the same as the provided target.
- It has a method `CreateVFX` that creates a visual effect at the hit location.
- It has a method `CreateVFXFromSave` that creates a visual effect from saved data.

Here are the actions in bullet points:

- The `VFXEffect` class is declared, which extends the `Effect` class.
- The `hitLocation` property is declared, which gets the hit location based on the `vfxData` and `hitInfo`.
- Three constructors are declared for the `VFXEffect` class.
- Several methods are overridden to handle different stages of the effect.
- The `CheckEffectTarget` method is declared to check if the target of the effect is the same as the provided target.
- The `CreateVFX` method is declared to create a visual effect at the hit location.
- The `CreateVFXFromSave` method is declared to create a visual effect from saved data.

This class essentially represents a visual effect in a combat game that can be created at a specific location and at different stages of the effect.

## ActorBurningEffect

```
	[SerializableContract("ActorBurningEffect")]
	public class ActorBurningEffect : Effect
	{
		public ActorBurningEffect(CombatGameState combat, string effectID, int stackItemUID, ICombatant creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
			if (base.EffectData.targetingData.effectTargetsCreator)
			{
				this.InitBurningEffect(creator);
				return;
			}
			this.InitBurningEffect(target);
		}

		public ActorBurningEffect(CombatGameState combat, string effectID, int stackItemUID, Team creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
			this.InitBurningEffect(target);
		}

		public ActorBurningEffect()
		{
		}

		private void InitBurningEffect(ICombatant target)
		{
			this.targetActor = target as AbstractActor;
			if (this.targetActor == null)
			{
				throw new Exception("Something other than an actor is on fire! We need to handle this!");
			}
			this.targetMech = target as Mech;
			this.targetVehicle = target as Vehicle;
			this.targetTurret = target as Turret;
			this.targetBuilding = target as Building;
			if (this.targetMech != null)
			{
				this.hitLocation = 8;
			}
			if (this.targetVehicle != null)
			{
				this.hitLocation = 2;
			}
			if (this.targetTurret != null)
			{
				this.hitLocation = 2;
			}
			if (this.targetBuilding != null)
			{
				this.hitLocation = 2;
			}
			this.hasGameRep = target.GameRep != null;
			this.initialTickDone = false;
		}

		public override void OnEffectBegin(bool skipLogging = false)
		{
			base.OnEffectBegin(skipLogging);
			this.PerformTick();
			this.initialTickDone = true;
			if (this.hasGameRep)
			{
				this.targetActor.GameRep.PlayVFX(this.hitLocation, this.targetActor.Combat.Constants.VFXNames.flamer_persistent, true, Vector3.zero, false, -1f);
			}
		}

		public override void OnEffectPhaseBegin()
		{
			base.OnEffectPhaseBegin();
			if (!this.effectData.durationData.ticksOnActivations)
			{
				this.PerformTick();
			}
		}

		public override void OnEffectActivationEnd()
		{
			base.OnEffectActivationEnd();
			if (this.effectData.durationData.ticksOnActivations)
			{
				this.PerformTick();
			}
		}

		public override void PerformTick()
		{
			if (!this.initialTickDone)
			{
				return;
			}
			base.PerformTick();
			if (this.targetMech != null)
			{
				this.targetMech.AddExternalHeat("BURNING", this.effectData.actorBurningData.heatPerTick);
				this.targetMech.GenerateAndPublishHeatSequence(-1, false, false, "ActorBurningEffect");
			}
			this.targetActor.TakeWeaponDamage(this.hitInfo, this.hitLocation, this.targetActor.Weapons[0], (float)this.effectData.actorBurningData.damagePerTick, 0f, 0, DamageType.Unknown);
			this.targetActor.ResolveWeaponDamage(this.hitInfo, this.targetActor.Weapons[0], MeleeAttackType.NotSet);
			this.targetActor.HandleDeath(this.hitInfo.attackerId);
			if (this.hasGameRep)
			{
				this.targetActor.GameRep.PlayVFX(this.hitLocation, this.targetActor.Combat.Constants.VFXNames.flamer_impact, true, Vector3.zero, true, 1f);
			}
		}

		public override void OnEffectEnd(bool expired, bool skipLogging = false)
		{
			base.OnEffectEnd(expired, skipLogging);
			if (this.hasGameRep)
			{
				this.targetActor.GameRep.StopManualPersistentVFX(this.targetActor.Combat.Constants.VFXNames.flamer_persistent);
			}
		}

		public override void OnEffectRemoval(bool skipLogging = false)
		{
			base.OnEffectRemoval(skipLogging);
		}

		public override void OnEffectExpiration()
		{
			base.OnEffectExpiration();
		}

		public override bool CheckEffectTarget(object target)
		{
			return this.target == target;
		}

		public override void Hydrate(CombatGameState combat, SerializableReferenceContainer references)
		{
			base.Hydrate(combat, references);
			ICombatant item = references.GetItem<ICombatant>(this, "targetActor");
			this.targetActor = item as AbstractActor;
			if (item != null)
			{
				this.targetMech = item as Mech;
				this.targetVehicle = item as Vehicle;
				this.targetTurret = item as Turret;
				this.targetBuilding = item as Building;
			}
			ActorBurningEffect.logger.LogError("Hydrating an ActorBurningEffect, this may not function as intended due to missing WeaponHitInfo");
		}
	}
```

Sure, here's what the Unity C# code does in plain English:

- The `ActorBurningEffect` class is a subclass of the `Effect` class and is marked as serializable with the contract name "ActorBurningEffect".
- It has three constructors:
    - The first constructor takes several parameters including `CombatGameState`, `effectID`, `stackItemUID`, `creator`, `target`, `effectData`, `hitInfo`, and `attackIndex`. It calls the base class constructor with these parameters. If the effect targets the creator, it initializes the burning effect with the creator as the target, otherwise it initializes the burning effect with the target.
    - The second constructor is similar to the first but takes a `Team` object as the `creator` instead of an `ICombatant`. It initializes the burning effect with the target.
    - The third constructor is a parameterless constructor.
- It has a method `InitBurningEffect` that initializes the burning effect by setting the target actor, target mech, target vehicle, target turret, target building, hit location, has game rep, and initial tick done based on the target.
- It overrides several methods from the base class to handle different stages of the effect, such as when it begins, when a phase begins, when activation ends, when it ends, when it's removed, and when it expires. In these methods, it performs a tick, plays a visual effect, stops a visual effect, and checks if the target of the effect is the same as the provided target.
- It has a method `PerformTick` that performs a tick by adding external heat to the target mech, generating and publishing a heat sequence, taking weapon damage, resolving weapon damage, handling death, and playing a visual effect if the initial tick has been done.

Here are the actions in bullet points:

- The `ActorBurningEffect` class is declared, which extends the `Effect` class.
- Three constructors are declared for the `ActorBurningEffect` class.
- The `InitBurningEffect` method is declared to initialize the burning effect.
- Several methods are overridden to handle different stages of the effect.
- The `PerformTick` method is declared to perform a tick.

This class essentially represents a burning effect in a combat game that can be applied to an actor and has different behaviors at different stages of the effect.

## TagEffect

```
	[SerializableContract("TagEffect")]
	public class TagEffect : Effect
	{
		public TagEffect(CombatGameState combat, string effectID, int stackItemUID, ICombatant creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		public TagEffect(CombatGameState combat, string effectID, int stackItemUID, Team creator, ICombatant target, EffectData effectData, WeaponHitInfo hitInfo, int attackIndex)
			: base(combat, effectID, stackItemUID, creator, target, creator.GUID, target.GUID, effectData, hitInfo, attackIndex)
		{
		}

		private TagEffect()
		{
		}

		public override void OnEffectBegin(bool skipLogging = false)
		{
			base.OnEffectBegin(skipLogging);
		}

		public override void OnEffectPhaseBegin()
		{
			base.OnEffectPhaseBegin();
		}

		public override void OnEffectActivationEnd()
		{
			base.OnEffectActivationEnd();
		}

		public override void OnEffectEnd(bool expired, bool skipLogging = false)
		{
			base.OnEffectEnd(expired, skipLogging);
		}

		public override void OnEffectRemoval(bool skipLogging = false)
		{
			base.OnEffectRemoval(skipLogging);
		}

		public override void OnEffectExpiration()
		{
			base.OnEffectExpiration();
		}

		public override bool CheckEffectTarget(object target)
		{
			return this.target == target;
		}
	}

```

Sure, here's what the Unity C# code does in plain English:

- The `TagEffect` class is a subclass of the `Effect` class and is marked as serializable with the contract name "TagEffect".
- It has three constructors:
    - The first constructor takes several parameters including `CombatGameState`, `effectID`, `stackItemUID`, `creator`, `target`, `effectData`, `hitInfo`, and `attackIndex`. It calls the base class constructor with these parameters.
    - The second constructor is similar to the first but takes a `Team` object as the `creator` instead of an `ICombatant`. It calls the base class constructor with these parameters.
    - The third constructor is a parameterless constructor.
- It overrides several methods from the base class to handle different stages of the effect, such as when it begins, when a phase begins, when activation ends, when it ends, when it's removed, and when it expires. In these methods, it calls the corresponding method from the base class.
- It has a method `CheckEffectTarget` that checks if the target of the effect is the same as the provided target.

Here are the actions in bullet points:

- The `TagEffect` class is declared, which extends the `Effect` class.
- Three constructors are declared for the `TagEffect` class.
- Several methods are overridden to handle different stages of the effect.
- The `CheckEffectTarget` method is declared to check if the target of the effect is the same as the provided target.

This class essentially represents a tag effect in a combat game that can be applied to a target and has different behaviors at different stages of the effect.

## VFXEffect Sample Code

```
{
			"durationData" : {
                "duration" : 2,
                "ticksOnActivations" : true,
                "useActivationsOfTarget" : false,
                "ticksOnEndOfRound" : false,
                "ticksOnMovements" : false,
                "stackLimit" : 1,
                "clearedWhenAttacked" : false,
				"activeTrackedEffect" : true
            },
			"targetingData" : {
                "effectTriggerType" : "OnHit",
                "triggerLimit" : 0,
                "extendDurationOnTrigger" : 0,
                "specialRules" : "NotSet",
                "effectTargetType" : "NotSet",
                "range" : 0,
                "forcePathRebuild" : false,
                "forceVisRebuild" : false,
                "showInTargetPreview" : false,
                "showInStatusPanel" : false,
                "hideApplicationFloatie" : true
            },
			"effectType" : "VFXEffect",
            "Description" : {
                "Id" : "StatusEffect-NARC-IndicatorVFX",
                "Name" : "NARC ATTACHED",
                "Details" : "Visual indicator of the NARC effect",
                "Icon" : "uixSvgIcon_statusMarked"
            },
            "nature" : "Debuff",
			"vfxData" : {
				"vfxName" : "vfxPrfPrtl_narcMarker_loop",
				"attachToImpactPoint" : true,
				"location" : -1,
				"isAttached" : true,
				"facesAttacker" : false,
				"isOneShot" : false,
				"duration" : -1.0		
			}
}
```

## FloatieEffect Sample Code

```
{
            "Description" : {
                "Id" : "StatusEffect-BWCL-WidowsKissFloatie",
                "Name" : "WIDOW'S KISS",
                "Details" : "WIDOW'S KISS",
                "Icon" : "UixSvgIcon_specialAbility_BWCL"
            },
            "effectType" : "FloatieEffect",
            "nature" : "Buff",
            "durationData" : {
                "duration" : 1,
                "stackLimit" : 0,
                "triggerLimit" : 1
            },
            "targetingData" : {
                "effectTriggerType" : "OnWeaponFire",
                "effectTargetType" : "Creator",
                "showInTargetPreview" : false,
                "showInStatusPanel" : false,
                "hideApplicationFloatie" : true
            },
            "floatieData" : {
                "targetCollection" : "NotSet"
            }
}
```

---

Return to [Status Effects Info](../Docs-Detailed/Status-effects-info.md)