# Effect Types and Triggers Specifics



## EffectTriggerType

The game's stock options - may be incompatible with certain target types and/or be bugged.

- Passive
- OnActivation
- OnHit
- OnDamaged
- OnWeaponFire
- OnUnitActivationBegin
- OnUnitActivationEnd
- OnUnitActivationBeginOrEnd
- TurnUpdate
- Preview

`OnHit` functions when a weapon hits the target. However, if a status effect with trigger `OnHit` is part of an ability with `"ActivationTime" : "Passive"`, the game seems to consider the host unit to be the target.

## EffectTargetType

The game's stock options - may be incompatible with certain trigger types and/or be bugged.

- NotSet
- Creator
- SingleTarget
- LanceMatesWithinRange
- AlliesWithinRange
- EnemiesWithinRange
- AllLanceMates
- AllAllies
- AllEnemies

`AllLanceMates` and possibly all options besides `Creator` and `SingleTarget` may be incompatible with `OnDamaged` trigger.

`AllLanceMates` is apparently only works with `DamageReductionMultiplierAll`. If used with a specific `DamageReductionMultiplier___` type, status effect will silently fail. Use `Creator` instead.

---

Return to [Status Effects Info](../Docs-Detailed/Status-effects-info.md)