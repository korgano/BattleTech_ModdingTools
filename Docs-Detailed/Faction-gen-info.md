# Faction Generation Information

## BattleTech Dev Info

Presumably added by Chris Eck, but there is no actual attribution for the information in the original `DataDrivenEnumNotes.txt` file. The file is distributed with the game to all customers, and is being reposted here to provide reference for modders.

The Faction Generator script's inputs were designed based on the information in this file. Understanding FactionValue fields is **very important** for generating your factions.

I take **NO** credit for the information marked (BT Dev).

### Data Driven Enums (BT Dev)

The purpose of data driven enums is to replace the hard-coded C# enums.

Instead of code that is tied directly to hard-coded values, I drive logic by the fields I created for individual rows. For example: In the Faction enums, there is now a bit named DoesGainReputation. In the original system, this logic was driven by hardcoding specific enum values in the code. Now, each FactionValue knows this information about itself

```
    // Old Code
	if (DoesFactionGainReputation(employer))
		; // Do something

	public static bool DoesFactionGainReputation(Faction faction)
	{
		if (faction == Faction.INVALID_UNSET)
			return false;
		if (faction >= Faction.Player1sMercUnit)
			return false;
		if (faction == Faction.MercenaryReviewBoard ||
			faction == Faction.NoFaction ||
			faction == Faction.ComStar ||
			faction == Faction.AuriganMercenaries ||
			faction == Faction.Locals)
			return false;
		return true;
	}

	// New Code
	if(employerValue.DoesGainReputation)
		; // Do Something
```

The main benefits of driving this logic through data is that it allows us and modders the ability to create new enum values without having to update all the code in dozens of files in order to support this new value. 

### General (BT Dev)

One problem to solve was to make sure all existing data and save games could easily upgrade to the new system, without invalidating the existing content and save games. Let's work through the example so you can see what gets changed.

```
	// Old Code
	public Faction Faction;
	
	// New Code
	// We hide the field from external users so they're forced to use the new item.
	[fastJSON.JsonSerialized]
	[Obsolete("Use FactionValue instead")]
	protected Faction Faction;

	// The new field is backed by a string. This will be the original text value of the enum.
	[fastJSON.JsonSerialized]
	protected string factionID = FactionEnumeration.INVALID_DEFAULT_ID;

	// External users are forced to use the FactionValue property.
	private FactionValue factionValue = null;
	public FactionValue FactionValue
	{
		get
		{
			// If this new item hasn't been initialized yet, we need to upgrade from the original value.
			if (string.IsNullOrEmpty(factionID))
			{
				UpgradeToDataDrivenEnums(); // factionID = Faction.ToString()
			}

			// If the cached row is null or out of date, pull the correct one from the FactionEnumeration.
			if (factionValue == null || factionValue.Name != factionID)
			{
				factionValue = FactionEnumeration.GetFactionByName(factionID); // FactionEnumeration pulls the values from the database once then keeps a cached dictionary
			}

			return factionValue;
		}

		private set
		{
			factionValue = value;
			factionID = factionValue.Name;
		}
	}
```

Now any external users are forced to access the data through this public property. It checks to see if we need to upgrade from the original value. Then it pulls the new row from the database and caches it in the FactionEnumeration so future requests will be faster. Then it returns the requested value.

### Factions (BT Dev)

To add a new faction, you need to create a new entry in the Faction.json.

It will be easiest to do this by copying an existing row that matches the type of faction you want to create. For internal designers, this is likely to be those one-off factions that just exist for a Flashpoint or custom mission. 

```
{
			"ID" : 67,  
			"Name" : "DuchyOfAndurien", // Computer friendly - suggested no spaces, capel camel case.
			"FriendlyName" : "Duchy Of Andurien", // User friendly 
			"Description" : "",
			"FactionDefID" : "faction_DuchyOfAndurien",
			"IsRealFaction" : true,
			"IsGreatHouse" : false,
			"IsClan" : false,
			"IsMercenary" : false,
			"IsPirate" : false,
			"DoesGainReputation" : false,
			"CanAlly" : false,
			"IsProceduralContractFaction" : false,
			"IsCareerScoringFaction" : false,
			"IsCareerIgnoredContractTarget" : false,
			"IsCareerStartingDisplayFaction" : false,
			"IsStoryStartingDisplayFaction" : false,
			"HasAIBehaviorVariableScope" : false
},
```

### FactionValue Fields (BT Dev)

ID: A unique number that identifies the faction. - This will map to old Enum int values where they already exist.
		**NOTE** - If you specify an ID <=0 (or leave it unset) - then the ID will be an autoincreminting integer and 
		will get generated automatically without you having to worry about it. If you specify an ID > 0 then it will
		use that ID.

	Name: Computer friendly name of the enum. - This will map to the old Enum text values where they already exist.

	FriendlyName: User friendly name of the faction. Should be able to show in UI. Human Readable

	Description: Not used for factions. Feel free to use as a designer comment - localization might pick it up though.

	FactionDefID: The name of the file that holds the FactionDef for this faction.

	IsRealFaction: Should be true for real factions/factions that have a FactionDefID. False for code-only factions like "Owner" or "Employer"

	IsGreatHouse, IsClan, IsMercenary, IsPirate: Not really used by HBS, but it could be useful to modders who need to select a random Merc unit.

	DoesGainReputation: When true, the game will keep up with Company reputation stats for this faction.

	CanAlly: Is it possible to ever ally with this faction?

	IsProceduralContractFaction: Should this faction be choosable by procedural factions. (You'll still have to adjust individual planets for faction influence)

	IsCareerScoringFaction: Does this faction earn points during end of faction scoring?

	IsCareerIgnoredContractTarget: This one was weird. Currently only the AuriganDirectorate is added to this list. It pulls this entry from being a procedural contract participant and prevents it showing up in Allied/Enemy faction lists. 

	Is(Story/Career)StartingDisplayFaction: When true, adds it to the display list for that game mode. It's supposed to also show up in the reputation screen, but that list is currently hard-coded to the factions for the few that show up for HBS. I believe modders already have this problem solved so I may not make that screen fully dynamic.

	HasAIBehaviorVariableScope: When true, an entry is created in the list of AIBehaviorVariableScopes. Currently those entries are just empty scopes that don't do anything.

Once you have created your new entry (make sure it has a unique ID!), you'll also need to create an associated FactionDef. The file name should match the FactionDefID field case exactly. I'd copy the same factionDef that corresponds to the original FactionValue row that you copied and adjust it accordingly.

### New FactionDef Fields (BT Dev)

FactionDefs already held lots of data about factions. And still more data was scattered around in different files (like SimGameContants). I kept most of the logic variables in FactionValue, but other data I decided to place in FactionDef.

icon: name of the image file (match spelling and case) This used to be auto generated by faction name, now two factions can point to the same icon.

factionTagOverride: This value was just the original Faction text (like Liao or Kurita), but there was some code that manually adjusted two factions. Locals and AuriganPirates. I recommend not using this field.

factionStorePlanetTag: This was hardcoded in a function and is the tag used to identify faction shops

factionStoreColor/factionMapColor: These colors were defined in hard-coded UI prefabs, so I pulled these out into fields. 

### Icon (BT Dev)

I recommend copying an existing icon for your faction and renaming it. After you wire it up, designers should log a new task so artists can create the new icon (if necessary).

### Heraldry Def (BT Dev)

If your faction requires a new Heraldry def, create a new one. Or you can point to an existing one.

### Put it in the Game (BT Dev)

Add an entry into the manifest for the created items (FactionDef file, image file, Heraldry file). For designers, you can just rebuild the manifest from unity:
	`HBS->Data->Manifest->Rebuild`

Once that is complete, you'll need entries in the MDDB. For designers, you can do this in Unity. 
	`HBS->MDD->Types->Rebuild Factions (or Rebuild Enums for all enums)

For modders, I added this ability in the EventEditor. 
	`Utility->MDDB Operations->Enums->Rebuild Factions`
	
Now your faction should be ready to use.

Designers note:

If you "Rebuild Transactions" after this point, you'll lose your new MDD entry. A better name for this would be "Reset MDD to Git's Version". Once you push your changes, the transactions.sql needs to be rebuilt. You can ping Jesse to teach you how to run that job for your branch.

