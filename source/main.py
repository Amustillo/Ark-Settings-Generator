#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import ttk, messagebox
import configparser

class ArkSettingsGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ark Survival Ascended Settings Generator")
        self.root.geometry("1400x1000")  # Larger window for better visibility
        self.root.minsize(1200, 900)  # Minimum window size
        self.root.configure(bg='#2b2b2b')  # Modern dark background

        # Modern color palette
        self.colors = {
            'bg_dark': '#2b2b2b',
            'bg_medium': '#3a3a3a',
            'bg_light': '#4a4a4a',
            'accent': '#00bfa5',  # Modern teal accent
            'accent_hover': '#00e5cc',
            'text_primary': '#ffffff',
            'text_secondary': '#b0b0b0',
            'border': '#555555'
        }

        # Set modern style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Button styles
        style.configure('TButton', 
                       font=('Segoe UI', 11, 'bold'), 
                       padding=10, 
                       background=self.colors['accent'], 
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none')
        style.map('TButton',
                 background=[('active', self.colors['accent_hover'])],
                 foreground=[('active', 'white')])
        
        # Label styles
        style.configure('TLabel', 
                       font=('Segoe UI', 10), 
                       background=self.colors['bg_dark'], 
                       foreground=self.colors['text_primary'])
        style.configure('Title.TLabel', 
                       font=('Segoe UI', 18, 'bold'), 
                       background=self.colors['bg_dark'], 
                       foreground=self.colors['text_primary'])
        style.configure('Subtitle.TLabel', 
                       font=('Segoe UI', 11, 'bold'), 
                       background=self.colors['bg_dark'], 
                       foreground=self.colors['accent'])
        style.configure('Description.TLabel', 
                       font=('Segoe UI', 9), 
                       background=self.colors['bg_dark'], 
                       foreground=self.colors['text_secondary'])
        
        # Checkbutton style
        style.configure('TCheckbutton', 
                       font=('Segoe UI', 10), 
                       background=self.colors['bg_dark'], 
                       foreground=self.colors['text_primary'])
        
        # Combobox style with better contrast
        style.configure('TCombobox', 
                       font=('Segoe UI', 10), 
                       fieldbackground=self.colors['bg_dark'],  # Darker background for better contrast
                       foreground=self.colors['text_primary'],
                       background=self.colors['bg_dark'],
                       arrowcolor=self.colors['accent'],
                       bordercolor=self.colors['border'],
                       lightcolor=self.colors['bg_medium'],
                       darkcolor=self.colors['bg_medium'],
                       selectbackground=self.colors['accent'],
                       selectforeground='white')
        style.map('TCombobox',
                 fieldbackground=[('readonly', self.colors['bg_dark'])],
                 selectbackground=[('readonly', self.colors['accent'])],
                 foreground=[('readonly', self.colors['text_primary'])],
                 arrowcolor=[('readonly', self.colors['accent'])])
        
        # Spinbox style
        style.configure('TSpinbox', 
                       font=('Segoe UI', 10), 
                       fieldbackground=self.colors['bg_light'], 
                       foreground=self.colors['text_primary'])
        
        # Scale style
        style.configure('TScale', 
                       background=self.colors['bg_dark'],
                       troughcolor=self.colors['bg_light'],
                       borderwidth=0)
        
        # Entry style
        style.configure('TEntry', 
                       font=('Segoe UI', 10), 
                       fieldbackground=self.colors['bg_light'], 
                       foreground=self.colors['text_primary'],
                       borderwidth=1,
                       relief='flat')
        
        # Notebook/Tab styles
        style.configure('TNotebook', 
                       background=self.colors['bg_dark'],
                       borderwidth=0)
        style.configure('TNotebook.Tab', 
                       font=('Segoe UI', 11, 'bold'), 
                       padding=[15, 8], 
                       background=self.colors['bg_medium'], 
                       foreground=self.colors['text_secondary'])
        style.map('TNotebook.Tab',
                 background=[('selected', self.colors['accent'])],
                 foreground=[('selected', 'white')])
        
        # Frame styles
        style.configure('TFrame', background=self.colors['bg_dark'])
        style.configure('Card.TFrame', 
                       background=self.colors['bg_medium'], 
                       relief='flat',
                       borderwidth=1)

        # Default settings
        self.settings = {
            'ServerSettings': {
                'DifficultyOffset': 0.2,
                'MaxPlayers': 70,
                'ServerPassword': '',
                'ServerAdminPassword': '',
                'ServerName': '',
                'ServerHardcore': False,
                'DisablePvEGamma': False,
                'EnablePvPGamma': False,
                'AdminLogging': True,
                'RCONEnabled': True,
                'RCONPort': 32330,
                'RCONServerGameLogBuffer': 600,
                'DinoDamageMultiplier': 1.0,
                'PlayerDamageMultiplier': 1.0,
                'StructureDamageMultiplier': 1.0,
                'PlayerResistanceMultiplier': 1.0,
                'DinoResistanceMultiplier': 1.0,
                'StructureResistanceMultiplier': 1.0,
                'XPMultiplier': 1.0,
                'TamingSpeedMultiplier': 1.0,
                'HarvestAmountMultiplier': 1.0,
                'HarvestHealthMultiplier': 1.0,
                'DinoCountMultiplier': 1.0,
                'ResourcesRespawnPeriodMultiplier': 1.0,
                'PlayerCharacterWaterDrainMultiplier': 1.0,
                'PlayerCharacterFoodDrainMultiplier': 1.0,
                'PlayerCharacterStaminaDrainMultiplier': 1.0,
                'PlayerCharacterHealthRecoveryMultiplier': 1.0,
                'DinoCharacterFoodDrainMultiplier': 1.0,
                'DinoCharacterStaminaDrainMultiplier': 1.0,
                'DinoCharacterHealthRecoveryMultiplier': 1.0,
                'DayCycleSpeedScale': 1.0,
                'NightTimeSpeedScale': 1.0,
                'DayTimeSpeedScale': 1.0,
                'DisableWeatherFog': False,
                'serverPVE': False,
                'TheMaxStructuresInRange': 10500,
                'bAllowPlatformSaddleMultiFloors': False,
                'AllowCaveBuildingPvE': False,
                'AllowCaveBuildingPvP': False,
                'PvEDinoDecayPeriodMultiplier': 1.0,
                'DisableDinoDecayPvE': False,
                'DisableStructureDecayPvE': False,
                'MaxTributeDinos': 20,
                'MaxTributeItems': 50,
                'TributeItemExpirationSeconds': 86400,
                'TributeDinoExpirationSeconds': 86400,
                'noTributeDownloads': False,
                'alwaysNotifyPlayerJoined': False,
                'alwaysNotifyPlayerLeft': False,
                'allowThirdPersonPlayer': False,
                'globalVoiceChat': False,
                'proximityChat': False,
                'ShowMapPlayerLocation': False,
                'serverForceNoHud': False,
                'AllowFlyerCarryPvE': False,
                'RandomSupplyCratePoints': False,
                'SupplyCrateLootQualityMultiplier': 1.0,
                'FishingLootQualityMultiplier': 1.0,
                'ItemStackSizeMultiplier': 1.0,
                'ActiveEvent': 'None',
                # Add more advanced settings here
                'ActiveMods': '',
                'AllowAnyoneBabyImprintCuddle': True,
                'AlwaysAllowStructurePickup': False,
                'AlwaysNotifyPlayerLeft': False,
                'ArmadoggoDeathCooldown': 3600,
                'AutoDestroyDecayedDinos': False,
                'AutoDestroyOldStructuresMultiplier': 0.0,
                'AutoSavePeriodMinutes': 15.0,
                'BanListURL': 'https://cdn2.arkdedicated.com/asa/BanList.txt',
                'bForceCanRideFliers': False,
                'ClampItemSpoilingTimes': False,
                'ClampItemStats': False,
                'ClampResourceHarvestDamage': False,
                'CosmeticWhitelistOverride': '',
                'CosmoWeaponAmmoReloadAmount': 1,
                'CustomDynamicConfigUrl': '',
                'CustomLiveTuningUrl': 'https://cdn2.arkdedicated.com/asa/livetuningoverloads.json',
                'DayCycleSpeedScale': 1.0,
                'DayTimeSpeedScale': 1.0,
                'DestroyTamesOverTheSoftTameLimit': False,
                'DisableCryopodEnemyCheck': False,
                'DisableCryopodFridgeRequirement': False,
                'DisableDinoDecayPvE': False,
                'DisableImprintDinoBuff': False,
                'DisablePvEGamma': False,
                'DisableStructureDecayPvE': False,
                'DisableWeatherFog': False,
                'DontAlwaysNotifyPlayerJoined': False,
                'EnableExtraStructurePreventionVolumes': False,
                'EnablePvPGamma': False,
                'ExtinctionEventTimeInterval': 0,
                'FastDecayUnsnappedCoreStructures': False,
                'ForceAllStructureLocking': False,
                'ForceGachaUnhappyInCaves': True,
                'globalVoiceChat': False,
                'IgnoreLimitMaxStructuresInRangeTypeFlag': False,
                'ImplantSuicideCD': 28800,
                'KickIdlePlayersPeriod': 3600.0,
                'MaxCosmoWeaponAmmo': -1,
                'MaxPersonalTamedDinos': 0,
                'MaxPlatformSaddleStructureLimit': 75,
                'MaxTamedDinos': 5000.0,
                'MaxTamedDinos_SoftTameLimit': 5000,
                'MaxTamedDinos_SoftTameLimit_CountdownForDeletionDuration': 604800,
                'MaxTrainCars': 8,
                'MaxTributeCharacters': 10,
                'MaxTributeDinos': 20,
                'MaxTributeItems': 50,
                'NightTimeSpeedScale': 1.0,
                'NonPermanentDiseases': False,
                'NPCNetworkStasisRangeScalePlayerCountStart': 0,
                'NPCNetworkStasisRangeScalePlayerCountEnd': 0,
                'NPCNetworkStasisRangeScalePercentEnd': 0.55,
                'OnlyAutoDestroyCoreStructures': False,
                'OnlyDecayUnsnappedCoreStructures': False,
                'OverrideOfficialDifficulty': 0.0,
                'PerPlatformMaxStructuresMultiplier': 1.0,
                'PersonalTamedDinosSaddleStructureCost': 0,
                'PlatformSaddleBuildAreaBoundsMultiplier': 1.0,
                'PlayerCharacterFoodDrainMultiplier': 1.0,
                'PlayerCharacterHealthRecoveryMultiplier': 1.0,
                'PlayerCharacterStaminaDrainMultiplier': 1.0,
                'PlayerResistanceMultiplier': 1.0,
                'PreventDiseases': False,
                'PreventMateBoost': False,
                'PreventOfflinePvP': False,
                'PreventOfflinePvPInterval': 0.0,
                'PreventSpawnAnimations': False,
                'PreventTribeAlliances': False,
                'PvEStructureDecayPeriodMultiplier': 1.0,
                'PvPDinoDecay': False,
                'PvPStructureDecay': False,
                'RaidDinoCharacterFoodDrainMultiplier': 1.0,
                'RandomSupplyCratePoints': False,
                'RCONEnabled': True,
                'RCONPort': 27020,
                'RCONServerGameLogBuffer': 600.0,
                'ResourcesRespawnPeriodMultiplier': 1.0,
                'ServerAdminPassword': '',
                'ServerAutoForceRespawnWildDinosInterval': 0.0,
                'ServerCrosshair': True,
                'ServerForceNoHUD': False,
                'ServerHardcore': False,
                'ServerPassword': '',
                'serverPVE': False,
                'ShowFloatingDamageText': False,
                'ShowMapPlayerLocation': True,
                'SpectatorPassword': '',
                'StructureDamageMultiplier': 1.0,
                'StructurePickupHoldDuration': 0.5,
                'StructurePickupTimeAfterPlacement': 30.0,
                'StructurePreventResourceRadiusMultiplier': 1.0,
                'TheMaxStructuresInRange': 10500,
                'TribeLogDestroyedEnemyStructures': False,
                'TribeNameChangeCooldown': 15.0,
                'UseFjordurTraversalBuff': False,
                'UseOptimizedHarvestingHealth': False,
                'XPMultiplier': 1.0,
                'YoungIceFoxDeathCooldown': 3600,
            },
            '/script/shootergame.shootergamemode': {
                'MatingIntervalMultiplier': 1.0,
                'EggHatchSpeedMultiplier': 1.0,
                'BabyMatureSpeedMultiplier': 1.0,
                'BabyFoodConsumptionSpeedMultiplier': 1.0,
                'BabyImprintingStatScaleMultiplier': 1.0,
                'BabyCuddleIntervalMultiplier': 1.0,
                'BabyCuddleGracePeriodMultiplier': 1.0,
                'BabyCuddleLoseImprintQualitySpeedMultiplier': 1.0,
                'MaxTamedDinos': 4000,
                'MaxNumberOfPlayersInTribe': 0,
                'MaxAlliancesPerTribe': 0,
                'MaxTribesPerAlliance': 0,
                'bOnlyAllowSpecifiedEngrams': False,
                'CustomRecipeEffectivenessMultiplier': 1.0,
                'CustomRecipeSkillMultiplier': 1.0,
                'bDisableLootCrates': False,
                'bAppendItemSets': False,
                'GlobalSpoilingTimeMultiplier': 1.0,
                'GlobalItemDecompositionTimeMultiplier': 1.0,
                'GlobalCorpseDecompositionTimeMultiplier': 1.0,
                'PvEStructureDecayPeriodMultiplier': 1.0,
                'PvEDinoDecayPeriodMultiplier': 1.0,
                'bAutoPvETimer': False,
                'bPvEDisableFriendlyFire': False,
                'bDisableFriendlyFire': False,
                'bAllowCustomRecipes': True,
                'bAutoUnlockAllEngrams': False,
                # Add more Game.ini settings
                'AutoPvEStartTimeSeconds': 0.0,
                'bAllowFlyerSpeedLeveling': False,
                'bAllowPlatformSaddleMultiFloors': False,
                'bAllowSpeedLeveling': False,
                'bAutoPvEUseSystemTime': False,
                'bDisableDinoBreeding': False,
                'bDisableDinoRiding': False,
                'bDisableDinoTaming': False,
                'bIncreasePvPRespawnInterval': True,
                'bPassiveDefensesDamageRiderlessDinos': False,
                'bUseCorpseLocator': True,
                'bUseDinoLevelUpAnimations': True,
                'bUseSingleplayerSettings': False,
                'bUseTameLimitForStructuresOnly': False,
                'CheatTeleportLocations': '',
                'ConfigAddNPCSpawnEntriesContainer': '',
                'ConfigOverrideItemCraftingCosts': '',
                'ConfigOverrideItemMaxQuantity': '',
                'ConfigOverrideNPCSpawnEntriesContainer': '',
                'ConfigOverrideSupplyCrateItems': '',
                'ConfigSubtractNPCSpawnEntriesContainer': '',
                'CraftingSkillBonusMultiplier': 1.0,
                'CraftXPMultiplier': 1.0,
                'CropGrowthSpeedMultiplier': 1.0,
                'ExcludeItemIndices': '',
                'FastDecayInterval': 43200,
                'FishingLootQualityMultiplier': 1.0,
                'FuelConsumptionIntervalMultiplier': 1.0,
                'GenericXPMultiplier': 1.0,
                'HairGrowthSpeedMultiplier': 1.0,
                'HarvestResourceItemAmountClassMultipliers': '',
                'HarvestXPMultiplier': 1.0,
                'IncreasePvPRespawnIntervalBaseAmount': 60.0,
                'IncreasePvPRespawnIntervalCheckPeriod': 300.0,
                'LayEggIntervalMultiplier': 1.0,
                'LevelExperienceRampOverrides': '',
                'LimitNonPlayerDroppedItemsCount': 0,
                'LimitNonPlayerDroppedItemsRange': 0,
                'MatingIntervalMultiplier': 1.0,
                'MaxFallSpeedMultiplier': 1.0,
                'MaxNumberOfPlayersInTribe': 0,
                'MaxStructuresInSmallRadius': 0,
                'MaxStructuresToProcess': 0,
                'NPCReplacements': '',
                'OverrideMaxExperiencePointsDino': 0,
                'OverrideMaxExperiencePointsPlayer': 0,
                'OverridePlayerLevelEngramPoints': '',
                'PassiveTameIntervalMultiplier': 1.0,
                'PerLevelStatsMultiplier_Player': '',
                'PerLevelStatsMultiplier_DinoTamed': '',
                'PerLevelStatsMultiplier_DinoWild': '',
                'PhotoModeRangeLimit': 3000,
                'PlayerBaseStatMultipliers': '',
                'PlayerHarvestingDamageMultiplier': 1.0,
                'PoopIntervalMultiplier': 1.0,
                'PreventBreedingForClassNames': '',
                'PreventDinoTameClassNames': '',
                'PreventOfflinePvPConnectionInvincibleInterval': 5.0,
                'ResourceNoReplenishRadiusPlayers': 1.0,
                'ResourceNoReplenishRadiusStructures': 1.0,
                'SpecialXPMultiplier': 1.0,
                'TribeSlotReuseCooldown': 0.0,
                'UseCorpseLifeSpanMultiplier': 1.0,
                'WildDinoCharacterFoodDrainMultiplier': 1.0,
                'LimitTurretsRange': 10000.0,
                'ValgueroMemorialEntries': '',
                'AdjustableMutagenSpawnDelayMultiplier': 1.0,
                'BaseHexagonRewardMultiplier': 1.0,
                'bDisableHexagonStore': False,
                'bDisableDefaultMapItemSets': False,
                'bDisableGenesisMissions': False,
                'bDisableWorldBuffs': False,
                'bEnableWorldBuffScaling': False,
                'bGenesisUseStructuresPreventionVolumes': False,
                'bHexStoreAllowOnlyEngramTradeOption': False,
                'HexagonCostMultiplier': 1.0,
            }
        }

        # Descriptions for settings
        self.descriptions = {
            'DifficultyOffset': 'Base difficulty level (0.0-1.0+); higher increases dino levels and aggression.',
            'MaxPlayers': 'Maximum concurrent players.',
            'ServerPassword': 'Password to join (leave empty for open server).',
            'ServerAdminPassword': 'Password for admin commands.',
            'ServerName': 'Name displayed in server browser.',
            'ServerHardcore': 'Enables hardcore mode; players reset to level 1 on death.',
            'DisablePvEGamma': 'Prevents gamma/console commands in PvE.',
            'EnablePvPGamma': 'Allows gamma/console commands in PvP.',
            'AdminLogging': 'Logs admin commands to chat.',
            'RCONEnabled': 'Enables RCON for remote admin.',
            'RCONPort': 'Port for RCON connections.',
            'RCONServerGameLogBuffer': 'Lines of gamelogs sent over RCON.',
            'DinoDamageMultiplier': 'Dino attack damage (>1.0 increases).',
            'PlayerDamageMultiplier': 'Player attack damage (>1.0 increases).',
            'StructureDamageMultiplier': 'Structure attack damage (>1.0 increases).',
            'PlayerResistanceMultiplier': 'Player damage resistance (>1.0 increases taken damage).',
            'DinoResistanceMultiplier': 'Dino damage resistance (>1.0 increases taken damage).',
            'StructureResistanceMultiplier': 'Structure damage resistance (>1.0 increases taken damage).',
            'XPMultiplier': 'Experience points earned (>1.0 increases XP).',
            'TamingSpeedMultiplier': 'Dino taming speed (>1.0 speeds up taming).',
            'HarvestAmountMultiplier': 'Harvest yield (>1.0 increases resources).',
            'HarvestHealthMultiplier': 'Harvestable object durability (>1.0 makes harder to destroy).',
            'DinoCountMultiplier': 'Dino spawn count (>1.0 increases spawns).',
            'ResourcesRespawnPeriodMultiplier': 'Resource respawn time (>1.0 slows respawns).',
            'PlayerCharacterWaterDrainMultiplier': 'Player water consumption (>1.0 increases thirst).',
            'PlayerCharacterFoodDrainMultiplier': 'Player food consumption (>1.0 increases hunger).',
            'PlayerCharacterStaminaDrainMultiplier': 'Player stamina consumption (>1.0 increases fatigue).',
            'PlayerCharacterHealthRecoveryMultiplier': 'Player health regen (>1.0 speeds up healing).',
            'DinoCharacterFoodDrainMultiplier': 'Dino food consumption (>1.0 increases hunger).',
            'DinoCharacterStaminaDrainMultiplier': 'Dino stamina consumption (>1.0 increases fatigue).',
            'DinoCharacterHealthRecoveryMultiplier': 'Dino health regen (>1.0 speeds up healing).',
            'DayCycleSpeedScale': 'Day/night cycle speed (>1.0 accelerates).',
            'NightTimeSpeedScale': 'Night duration relative to day (>1.0 lengthens nights).',
            'DayTimeSpeedScale': 'Day duration relative to night (>1.0 lengthens days).',
            'DisableWeatherFog': 'Disables fog effects.',
            'serverPVE': 'Enables PvE mode; disables PvP.',
            'TheMaxStructuresInRange': 'Max structures per player/tribe in an area.',
            'bAllowPlatformSaddleMultiFloors': 'Allows multiple floors on platform saddles.',
            'AllowCaveBuildingPvE': 'Allows building in caves in PvE.',
            'AllowCaveBuildingPvP': 'Allows building in caves in PvP.',
            'PvEDinoDecayPeriodMultiplier': 'Dino ownership decay time in PvE (>1.0 slows decay).',
            'DisableDinoDecayPvE': 'Disables dino ownership decay in PvE.',
            'DisableStructureDecayPvE': 'Disables structure decay in PvE.',
            'MaxTributeDinos': 'Max dinos transferable via tributes.',
            'MaxTributeItems': 'Max items transferable via tributes.',
            'TributeItemExpirationSeconds': 'Tribute expiration time in seconds.',
            'TributeDinoExpirationSeconds': 'Dino tribute expiration time in seconds.',
            'noTributeDownloads': 'Disables downloading tributes.',
            'alwaysNotifyPlayerJoined': 'Notifies all players of joins.',
            'alwaysNotifyPlayerLeft': 'Notifies all players of leaves.',
            'allowThirdPersonPlayer': 'Enables third-person view.',
            'globalVoiceChat': 'Makes voice chat global.',
            'proximityChat': 'Limits chat to nearby players.',
            'ShowMapPlayerLocation': 'Shows player locations on map.',
            'serverForceNoHud': 'Forces HUD off.',
            'AllowFlyerCarryPvE': 'Allows flyers to carry dinos/players in PvE.',
            'RandomSupplyCratePoints': 'Randomizes supply crate locations.',
            'SupplyCrateLootQualityMultiplier': 'Loot quality in crates (>1.0 improves).',
            'FishingLootQualityMultiplier': 'Fishing loot quality (>1.0 improves).',
            'ItemStackSizeMultiplier': 'Global item stack sizes (>1.0 increases stacks).',
            'ActiveEvent': 'Enables a specified event (e.g., WinterWonderland for colors).',
            'ActiveMods': 'Comma-separated list of mod IDs to load.',
            'AllowAnyoneBabyImprintCuddle': 'Allows anyone to cuddle imprinted babies.',
            'AllowCrateSpawnsOnTopOfStructures': 'Allows supply crates on structures.',
            'AllowCryoFridgeOnSaddle': 'Allows cryofridges on platform saddles.',
            'AllowFlyingStaminaRecovery': 'Allows stamina recovery while flying.',
            'AllowHideDamageSourceFromLogs': 'Hides damage sources in tribe logs.',
            'AllowHitMarkers': 'Enables hit markers for ranged attacks.',
            'AllowIntegratedSPlusStructures': 'Enables S+ structures.',
            'AllowMultipleAttachedC4': 'Allows multiple C4 per dino.',
            'AllowRaidDinoFeeding': 'Allows feeding Titanosaurs.',
            'AllowSharedConnections': 'Allows family sharing connections.',
            'AllowTekSuitPowersInGenesis': 'Enables Tek suit powers in Genesis.',
            'AllowThirdPersonPlayer': 'Enables third-person view.',
            'AlwaysAllowStructurePickup': 'Disables pickup timer.',
            'AlwaysNotifyPlayerLeft': 'Always notifies of player leaves.',
            'ArmadoggoDeathCooldown': 'Cooldown for Armadoggo respawn.',
            'AutoDestroyDecayedDinos': 'Auto-destroys decayed dinos.',
            'AutoDestroyOldStructuresMultiplier': 'Multiplier for auto-destroying old structures.',
            'AutoSavePeriodMinutes': 'Auto-save interval in minutes.',
            'BanListURL': 'URL for global ban list.',
            'bForceCanRideFliers': 'Forces flyer riding on maps where disabled.',
            'ClampItemSpoilingTimes': 'Clamps spoiling times to max.',
            'ClampItemStats': 'Enables stat clamping for items.',
            'ClampResourceHarvestDamage': 'Limits harvest damage to resources.',
            'CosmeticWhitelistOverride': 'URL for whitelisted cosmetics.',
            'CosmoWeaponAmmoReloadAmount': 'Ammo reload amount for Cosmo weapon.',
            'CustomDynamicConfigUrl': 'URL for dynamic config.',
            'CustomLiveTuningUrl': 'URL for live tuning.',
            'DestroyTamesOverTheSoftTameLimit': 'Destroys dinos over soft tame limit.',
            'DisableCryopodEnemyCheck': 'Allows cryopods near enemies.',
            'DisableCryopodFridgeRequirement': 'Allows cryopods without fridge.',
            'DisableImprintDinoBuff': 'Disables imprint stat bonuses.',
            'DontAlwaysNotifyPlayerJoined': 'Disables global join notifications.',
            'EnableExtraStructurePreventionVolumes': 'Prevents building in resource areas.',
            'ExtinctionEventTimeInterval': 'Time interval for extinction event.',
            'FastDecayUnsnappedCoreStructures': 'Fast decay for unsnapped structures.',
            'ForceAllStructureLocking': 'Forces all structures to lock.',
            'ForceGachaUnhappyInCaves': 'Makes Gachas unhappy in caves.',
            'IgnoreLimitMaxStructuresInRangeTypeFlag': 'Ignores decorative structure limits.',
            'ImplantSuicideCD': 'Cooldown for implant respawn.',
            'KickIdlePlayersPeriod': 'Idle kick time in seconds.',
            'MaxCosmoWeaponAmmo': 'Max ammo for Cosmo weapon.',
            'MaxPersonalTamedDinos': 'Per-tribe dino limit.',
            'MaxPlatformSaddleStructureLimit': 'Max structures on platform saddles.',
            'MaxTamedDinos': 'Global tamed dino cap.',
            'MaxTamedDinos_SoftTameLimit': 'Soft tame limit.',
            'MaxTamedDinos_SoftTameLimit_CountdownForDeletionDuration': 'Deletion countdown for over-limit dinos.',
            'MaxTrainCars': 'Max cars per train.',
            'MaxTributeCharacters': 'Max characters transferable.',
            'NightTimeSpeedScale': 'Night duration relative to day.',
            'NonPermanentDiseases': 'Makes diseases non-permanent.',
            'NPCNetworkStasisRangeScalePlayerCountStart': 'Min players for stasis scaling.',
            'NPCNetworkStasisRangeScalePlayerCountEnd': 'Max players for stasis scaling.',
            'NPCNetworkStasisRangeScalePercentEnd': 'Max scale percentage.',
            'OnlyAutoDestroyCoreStructures': 'Only auto-destroys core structures.',
            'OnlyDecayUnsnappedCoreStructures': 'Only decays unsnapped core structures.',
            'OverrideOfficialDifficulty': 'Overrides official difficulty.',
            'PerPlatformMaxStructuresMultiplier': 'Multiplier for max structures on saddles.',
            'PersonalTamedDinosSaddleStructureCost': 'Tame slots used by platform saddles.',
            'PlatformSaddleBuildAreaBoundsMultiplier': 'Build area multiplier for saddles.',
            'PlayerResistanceMultiplier': 'Player damage resistance.',
            'PreventDiseases': 'Disables diseases.',
            'PreventMateBoost': 'Disables mate boosting.',
            'PreventOfflinePvP': 'Enables offline raid prevention.',
            'PreventOfflinePvPInterval': 'Time before ORP activates.',
            'PreventSpawnAnimations': 'Disables spawn animations.',
            'PreventTribeAlliances': 'Disables tribe alliances.',
            'PvEStructureDecayPeriodMultiplier': 'Structure decay in PvE.',
            'PvPDinoDecay': 'Enables dino decay in PvP during ORP.',
            'PvPStructureDecay': 'Enables structure decay in PvP during ORP.',
            'RaidDinoCharacterFoodDrainMultiplier': 'Food drain for raid dinos.',
            'RCONServerGameLogBuffer': 'RCON game log buffer.',
            'ResourcesRespawnPeriodMultiplier': 'Resource respawn time.',
            'ServerAutoForceRespawnWildDinosInterval': 'Force respawn interval for wild dinos.',
            'ServerCrosshair': 'Enables crosshair.',
            'ServerForceNoHUD': 'Forces no HUD.',
            'ServerHardcore': 'Hardcore mode.',
            'ServerPassword': 'Server password.',
            'ShowFloatingDamageText': 'Enables floating damage text.',
            'SpectatorPassword': 'Password for spectator mode.',
            'StructurePickupHoldDuration': 'Pickup hold duration.',
            'StructurePickupTimeAfterPlacement': 'Pickup time after placement.',
            'StructurePreventResourceRadiusMultiplier': 'Resource radius multiplier.',
            'TribeLogDestroyedEnemyStructures': 'Logs enemy structure destruction.',
            'TribeNameChangeCooldown': 'Cooldown for tribe name changes.',
            'UseFjordurTraversalBuff': 'Enables traversal buff in Fjordur.',
            'UseOptimizedHarvestingHealth': 'Optimizes harvesting health.',
            'XPMultiplier': 'XP multiplier.',
            'YoungIceFoxDeathCooldown': 'Cooldown for Veilwyn respawn.',
            'MatingIntervalMultiplier': 'Time between mating attempts (>1.0 increases interval).',
            'EggHatchSpeedMultiplier': 'Egg hatching speed (>1.0 speeds up).',
            'BabyMatureSpeedMultiplier': 'Baby growth speed (>1.0 speeds up maturation).',
            'BabyFoodConsumptionSpeedMultiplier': 'Baby food consumption (>1.0 increases hunger).',
            'BabyImprintingStatScaleMultiplier': 'Imprinting stat bonus (>1.0 increases bonuses).',
            'BabyCuddleIntervalMultiplier': 'Cuddle frequency (>1.0 increases intervals).',
            'BabyCuddleGracePeriodMultiplier': 'Grace period before imprint loss (>1.0 extends).',
            'BabyCuddleLoseImprintQualitySpeedMultiplier': 'Imprint loss speed (>1.0 speeds up loss).',
            'MaxTamedDinos': 'Global tamed dino cap.',
            'MaxNumberOfPlayersInTribe': 'Tribe size limit (0 = unlimited).',
            'MaxAlliancesPerTribe': 'Alliance limit per tribe (0 = unlimited).',
            'MaxTribesPerAlliance': 'Tribes per alliance (0 = unlimited).',
            'bOnlyAllowSpecifiedEngrams': 'Hides unspecified engrams.',
            'CustomRecipeEffectivenessMultiplier': 'Custom recipe efficiency (>1.0 improves output).',
            'CustomRecipeSkillMultiplier': 'Crafting skill impact on recipes (>1.0 increases impact).',
            'bDisableLootCrates': 'Disables loot crates.',
            'bAppendItemSets': 'Appends to crate items instead of overriding.',
            'GlobalSpoilingTimeMultiplier': 'Item spoilage time (>1.0 prolongs).',
            'GlobalItemDecompositionTimeMultiplier': 'Dropped item decay (>1.0 slows).',
            'GlobalCorpseDecompositionTimeMultiplier': 'Corpse decay (>1.0 slows).',
            'PvEStructureDecayPeriodMultiplier': 'Structure decay in PvE (>1.0 slows).',
            'PvEDinoDecayPeriodMultiplier': 'Dino decay in PvE (>1.0 slows).',
            'bAutoPvETimer': 'Enables timed PvE/PvP switches.',
            'bPvEDisableFriendlyFire': 'Disables friendly fire in PvE.',
            'bDisableFriendlyFire': 'Disables friendly fire in PvP.',
            'bAllowCustomRecipes': 'Enables custom recipes.',
            'bAutoUnlockAllEngrams': 'Unlocks all engrams.',
            'AutoPvEStartTimeSeconds': 'PvE start time in seconds.',
            'bAllowFlyerSpeedLeveling': 'Enables flyer speed leveling.',
            'bAllowPlatformSaddleMultiFloors': 'Allows multiple floors on saddles.',
            'bAllowSpeedLeveling': 'Enables speed leveling.',
            'bAutoPvEUseSystemTime': 'Uses system time for PvE timer.',
            'bDisableDinoBreeding': 'Disables dino breeding.',
            'bDisableDinoRiding': 'Disables dino riding.',
            'bDisableDinoTaming': 'Disables dino taming.',
            'bIncreasePvPRespawnInterval': 'Increases PvP respawn interval.',
            'bPassiveDefensesDamageRiderlessDinos': 'Allows defenses to damage riderless dinos.',
            'bUseCorpseLocator': 'Enables corpse locator.',
            'bUseDinoLevelUpAnimations': 'Enables level up animations.',
            'bUseSingleplayerSettings': 'Uses singleplayer settings.',
            'bUseTameLimitForStructuresOnly': 'Applies tame limit only to structures.',
            'CheatTeleportLocations': 'Teleport locations for cheat commands.',
            'ConfigAddNPCSpawnEntriesContainer': 'Adds NPC spawn entries.',
            'ConfigOverrideItemCraftingCosts': 'Overrides crafting costs.',
            'ConfigOverrideItemMaxQuantity': 'Overrides item max quantities.',
            'ConfigOverrideNPCSpawnEntriesContainer': 'Overrides NPC spawns.',
            'ConfigOverrideSupplyCrateItems': 'Overrides supply crate items.',
            'ConfigSubtractNPCSpawnEntriesContainer': 'Subtracts NPC spawn entries.',
            'CraftingSkillBonusMultiplier': 'Crafting skill bonus.',
            'CraftXPMultiplier': 'XP from crafting.',
            'CropGrowthSpeedMultiplier': 'Crop growth speed.',
            'ExcludeItemIndices': 'Excludes items from crates.',
            'FastDecayInterval': 'Fast decay interval.',
            'FuelConsumptionIntervalMultiplier': 'Fuel consumption interval.',
            'GenericXPMultiplier': 'Generic XP multiplier.',
            'HairGrowthSpeedMultiplier': 'Hair growth speed.',
            'HarvestResourceItemAmountClassMultipliers': 'Harvest multipliers by class.',
            'HarvestXPMultiplier': 'XP from harvesting.',
            'IncreasePvPRespawnIntervalBaseAmount': 'Base PvP respawn increase.',
            'IncreasePvPRespawnIntervalCheckPeriod': 'Check period for respawn increase.',
            'LayEggIntervalMultiplier': 'Egg laying interval.',
            'LevelExperienceRampOverrides': 'Custom XP ramps.',
            'LimitNonPlayerDroppedItemsCount': 'Limit for dropped items.',
            'LimitNonPlayerDroppedItemsRange': 'Range for dropped items limit.',
            'MaxFallSpeedMultiplier': 'Fall speed multiplier.',
            'MaxStructuresInSmallRadius': 'Max structures in small radius.',
            'MaxStructuresToProcess': 'Max structures to process per tick.',
            'NPCReplacements': 'Replaces NPCs.',
            'OverrideMaxExperiencePointsDino': 'Max XP for dinos.',
            'OverrideMaxExperiencePointsPlayer': 'Max XP for players.',
            'OverridePlayerLevelEngramPoints': 'Engram points per level.',
            'PassiveTameIntervalMultiplier': 'Passive tame interval.',
            'PerLevelStatsMultiplier_Player': 'Player stat multipliers per level.',
            'PerLevelStatsMultiplier_DinoTamed': 'Tamed dino stat multipliers.',
            'PerLevelStatsMultiplier_DinoWild': 'Wild dino stat multipliers.',
            'PhotoModeRangeLimit': 'Photo mode range limit.',
            'PlayerBaseStatMultipliers': 'Base stat multipliers for players.',
            'PlayerHarvestingDamageMultiplier': 'Player harvesting damage.',
            'PoopIntervalMultiplier': 'Poop interval.',
            'PreventBreedingForClassNames': 'Prevents breeding for classes.',
            'PreventDinoTameClassNames': 'Prevents taming for classes.',
            'PreventOfflinePvPConnectionInvincibleInterval': 'Invincible interval after login.',
            'ResourceNoReplenishRadiusPlayers': 'Resource radius around players.',
            'ResourceNoReplenishRadiusStructures': 'Resource radius around structures.',
            'SpecialXPMultiplier': 'Special XP multiplier.',
            'TribeSlotReuseCooldown': 'Tribe slot reuse cooldown.',
            'UseCorpseLifeSpanMultiplier': 'Corpse lifespan multiplier.',
            'WildDinoCharacterFoodDrainMultiplier': 'Wild dino food drain.',
            'LimitTurretsRange': 'Turret range limit.',
            'ValgueroMemorialEntries': 'Memorial entries for Valguero.',
            'AdjustableMutagenSpawnDelayMultiplier': 'Mutagen spawn delay.',
            'BaseHexagonRewardMultiplier': 'Hexagon reward multiplier.',
            'bDisableHexagonStore': 'Disables hexagon store.',
            'bDisableDefaultMapItemSets': 'Disables default map item sets.',
            'bDisableGenesisMissions': 'Disables Genesis missions.',
            'bDisableWorldBuffs': 'Disables world buffs.',
            'bEnableWorldBuffScaling': 'Enables world buff scaling.',
            'bGenesisUseStructuresPreventionVolumes': 'Uses prevention volumes in Genesis.',
            'bHexStoreAllowOnlyEngramTradeOption': 'Allows only engram trades in store.',
            'HexagonCostMultiplier': 'Hexagon cost multiplier.',
        }

        # Dino data for calculations
        self.dino_data = {
            'Argentavis': {
                'taming_time': 180,  # minutes
                'maturation_time': 48,  # hours
                'imprint_interval': 8,  # hours between imprints
                'max_imprint': 100,  # max imprint %
                'incubation_time': 120,  # minutes
                'mating_cooldown': 18,  # hours
                'status': 'working'
            },
            'Rex': {
                'taming_time': 240,
                'maturation_time': 72,
                'imprint_interval': 8,
                'max_imprint': 100,
                'incubation_time': 180,
                'mating_cooldown': 18,
                'status': 'working'
            },
            'Spino': {
                'taming_time': 300,
                'maturation_time': 96,
                'imprint_interval': 8,
                'max_imprint': 100,
                'incubation_time': 240,
                'mating_cooldown': 18,
                'status': 'working'
            },
            'Giga': {
                'taming_time': 360,
                'maturation_time': 120,
                'imprint_interval': 8,
                'max_imprint': 100,
                'incubation_time': 300,
                'mating_cooldown': 18,
                'status': 'working'
            },
            'Titanosaur': {
                'taming_time': 480,
                'maturation_time': 168,
                'imprint_interval': 12,
                'max_imprint': 100,
                'incubation_time': 480,
                'mating_cooldown': 24,
                'status': 'working'
            },
            'Megalodon': {
                'taming_time': 120,
                'maturation_time': 36,
                'imprint_interval': 6,
                'max_imprint': 100,
                'incubation_time': 90,
                'mating_cooldown': 12,
                'status': 'working'
            },
            'Mosasaurus': {
                'taming_time': 180,
                'maturation_time': 60,
                'imprint_interval': 8,
                'max_imprint': 100,
                'incubation_time': 150,
                'mating_cooldown': 18,
                'status': 'working'
            },
            'Plesiosaur': {
                'taming_time': 150,
                'maturation_time': 48,
                'imprint_interval': 6,
                'max_imprint': 100,
                'incubation_time': 120,
                'mating_cooldown': 15,
                'status': 'working'
            },
            'Therizino': {
                'taming_time': 210,
                'maturation_time': 84,
                'imprint_interval': 8,
                'max_imprint': 100,
                'incubation_time': 180,
                'mating_cooldown': 18,
                'status': 'working'
            },
            'Thylacoleo': {
                'taming_time': 90,
                'maturation_time': 30,
                'imprint_interval': 6,
                'max_imprint': 100,
                'incubation_time': 75,
                'mating_cooldown': 12,
                'status': 'working'
            }
        }

        # Events data with status indicators
        self.events_data = {
            'None': {'status': 'working', 'description': 'No active event'},
            'WinterWonderland': {'status': 'working', 'description': 'Winter holiday event - cosmetics and bonuses'},
            'WinterWonderland2': {'status': 'working', 'description': 'Winter 2nd year event'},
            'WinterWonderland3': {'status': 'working', 'description': 'Winter 3rd year event'},
            'WinterWonderland4': {'status': 'working', 'description': 'Winter 4th year event'},
            'WinterWonderland5': {'status': 'working', 'description': 'Winter 5th year event'},
            'WinterWonderland6': {'status': 'working', 'description': 'Winter 6th year event'},
            'WinterWonderland7': {'status': 'working', 'description': 'Winter 7th year event'},
            'Easter': {'status': 'working', 'description': 'Eggcellent Adventure - Easter egg hunt themes'},
            'SummerBash': {'status': 'working', 'description': 'Summer vacation event - beach themes'},
            'FearEvolved': {'status': 'working', 'description': 'Fear Evolved/Fear Ascended - Halloween spooky creatures'},
            'TurkeyTrial': {'status': 'working', 'description': 'Turkey Trial - Thanksgiving event with challenges'},
            'LoveEvolved': {'status': 'working', 'description': 'Love Evolved - Valentine breeding event bonuses'},
            'Birthday': {'status': 'working', 'description': 'Birthday/Anniversary event - celebration bonuses'},
            'EvolutionEvent': {'status': 'working', 'description': 'Evolution Event - creature variant spawns'},
            'ExtraLife': {'status': 'working', 'description': 'Extra Life event - charity event bonuses'},
            'ARKaeology': {'status': 'working', 'description': 'ARKaeology - artifact discovery event'},
            'ARKdependenceDay': {'status': 'working', 'description': 'ARKdependence Day - July 4th themed event'},
        }

        # Selected dino variable
        self.selected_dino = tk.StringVar(value='Argentavis')

        # Mode: 'basic' or 'advanced'
        self.mode = tk.StringVar(value='basic')

        # Basic settings subsets
        self.basic_server = [
            'DifficultyOffset', 'MaxPlayers', 'ServerPassword', 'ServerAdminPassword', 'ServerName', 'ServerHardcore',
            'DinoDamageMultiplier', 'PlayerDamageMultiplier', 'XPMultiplier', 'TamingSpeedMultiplier', 'HarvestAmountMultiplier',
            'DayCycleSpeedScale', 'serverPVE', 'ShowMapPlayerLocation', 'TheMaxStructuresInRange', 'ActiveEvent'
        ]
        self.basic_game = [
            'MatingIntervalMultiplier', 'EggHatchSpeedMultiplier', 'BabyMatureSpeedMultiplier', 'BabyImprintingStatScaleMultiplier',
            'MaxTamedDinos', 'GlobalSpoilingTimeMultiplier', 'PvEStructureDecayPeriodMultiplier'
        ]

        self.create_widgets()

    def create_widgets(self):
        # Header frame with title
        header_frame = ttk.Frame(self.root, style='TFrame')
        header_frame.pack(fill='x', pady=(0, 15))
        
        title_label = ttk.Label(header_frame, 
                               text="⚙️ Ark Survival Ascended Settings Generator", 
                               style='Title.TLabel')
        title_label.pack(pady=15)
        
        subtitle_label = ttk.Label(header_frame,
                                   text="Configure your server settings with real-time calculations",
                                   style='Description.TLabel')
        subtitle_label.pack(pady=(0, 10))

        # Mode selection with modern styling
        mode_frame = ttk.Frame(self.root, style='Card.TFrame')
        mode_frame.pack(pady=(0, 15), padx=20, fill='x')
        
        mode_inner = ttk.Frame(mode_frame, style='Card.TFrame')
        mode_inner.pack(pady=12, padx=15)
        
        ttk.Label(mode_inner, text="🎮 Configuration Mode:", style='Subtitle.TLabel').pack(side=tk.LEFT, padx=(0, 20))
        ttk.Radiobutton(mode_inner, text="Basic", variable=self.mode, value='basic', command=self.switch_mode).pack(side=tk.LEFT, padx=15)
        ttk.Radiobutton(mode_inner, text="Advanced", variable=self.mode, value='advanced', command=self.switch_mode).pack(side=tk.LEFT, padx=15)

        # Button frame at top (pack before main_frame so it's visible)
        button_frame = ttk.Frame(self.root, style='TFrame')
        button_frame.pack(pady=(10, 15))
        
        self.generate_btn = ttk.Button(button_frame, 
                                       text="💾 Generate INI Files", 
                                       command=self.generate_files,
                                       width=25)
        self.generate_btn.pack(side=tk.LEFT, padx=10)
        
        self.reset_btn = ttk.Button(button_frame, 
                                    text="🔄 Reset to Defaults", 
                                    command=self.reset_to_defaults,
                                    width=25)
        self.reset_btn.pack(side=tk.LEFT, padx=10)

        # Main content area with notebook and calculations
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))

        # Left side - Settings tabs (larger for better visibility)
        self.notebook = ttk.Notebook(main_frame, width=750)
        self.notebook.pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 15))

        # Right panel for calculations with card styling
        self.calc_frame = ttk.Frame(main_frame, width=380, style='Card.TFrame')
        self.calc_frame.pack(side=tk.RIGHT, fill='y')
        self.calc_frame.pack_propagate(False)

        calc_title = ttk.Label(self.calc_frame, 
                              text="📊 Real-Time Calculations", 
                              style='Subtitle.TLabel')
        calc_title.pack(pady=15, padx=15)

        # Dino selection dropdown with better styling
        dino_frame = ttk.Frame(self.calc_frame, style='Card.TFrame')
        dino_frame.pack(pady=(0, 15), padx=15, fill='x')
        
        ttk.Label(dino_frame, text="🦖 Select Dino:", style='TLabel').pack(anchor='w', pady=(5, 8))
        
        # Format dino options with status indicators
        dino_display_names = []
        for dino_name in self.dino_data.keys():
            status = self.dino_data[dino_name].get('status', 'unknown')
            if status == 'working':
                display_name = f"✅ {dino_name}"
            else:
                display_name = f"⏰ {dino_name} (Coming Soon)"
            dino_display_names.append(display_name)
        
        dino_combo = ttk.Combobox(dino_frame, 
                                 values=dino_display_names, 
                                 state='readonly', 
                                 width=20,
                                 font=('Segoe UI', 10))
        dino_combo.set("✅ Argentavis")  # Set default with status indicator
        dino_combo.pack(fill='x', pady=(0, 5))
        
        # Handle combobox selection - extract actual dino name and update
        def on_dino_select(event):
            selected_text = dino_combo.get()
            # Extract dino name from the display format
            dino_name = selected_text.replace("✅ ", "").replace("⏰ ", "").replace(" (Coming Soon)", "")
            self.selected_dino.set(dino_name)
            self.update_calculations()
        
        dino_combo.bind('<<ComboboxSelected>>', on_dino_select)

        # Scrollable calculations frame
        calc_scrollable = ttk.Frame(self.calc_frame, style='Card.TFrame')
        calc_scrollable.pack(fill='both', expand=True, padx=15, pady=(0, 15))

        # Calculation labels with modern styling
        self.taming_label = ttk.Label(calc_scrollable, text="⏱️ Taming Time:", style='TLabel')
        self.taming_label.pack(anchor='w', pady=(10, 5), padx=10)
        self.taming_values = ttk.Label(calc_scrollable, text="", style='Description.TLabel')
        self.taming_values.pack(anchor='w', padx=20, pady=(0, 10))

        self.maturation_label = ttk.Label(calc_scrollable, text="🐣 Maturation Time:", style='TLabel')
        self.maturation_label.pack(anchor='w', pady=(5, 5), padx=10)
        self.maturation_values = ttk.Label(calc_scrollable, text="", style='Description.TLabel')
        self.maturation_values.pack(anchor='w', padx=20, pady=(0, 10))

        self.imprint_label = ttk.Label(calc_scrollable, text="💝 Imprinting:", style='TLabel')
        self.imprint_label.pack(anchor='w', pady=(5, 5), padx=10)
        self.imprint_values = ttk.Label(calc_scrollable, text="", style='Description.TLabel')
        self.imprint_values.pack(anchor='w', padx=20, pady=(0, 10))

        self.incubation_label = ttk.Label(calc_scrollable, text="🥚 Incubation Time:", style='TLabel')
        self.incubation_label.pack(anchor='w', pady=(5, 5), padx=10)
        self.incubation_values = ttk.Label(calc_scrollable, text="", style='Description.TLabel')
        self.incubation_values.pack(anchor='w', padx=20, pady=(0, 10))

        self.mating_label = ttk.Label(calc_scrollable, text="❤️ Mating Cooldown:", style='TLabel')
        self.mating_label.pack(anchor='w', pady=(5, 5), padx=10)
        self.mating_values = ttk.Label(calc_scrollable, text="", style='Description.TLabel')
        self.mating_values.pack(anchor='w', padx=20, pady=(0, 10))

        self.level_label = ttk.Label(calc_scrollable, text="📈 Max Wild Dino Level:", style='TLabel')
        self.level_label.pack(anchor='w', pady=(5, 5), padx=10)
        self.level_values = ttk.Label(calc_scrollable, text="", style='Description.TLabel')
        self.level_values.pack(anchor='w', padx=20, pady=(0, 10))

        # Tab for ServerSettings
        self.server_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.server_tab, text='Server Settings')

        # Tab for Game.ini
        self.game_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.game_tab, text='Game Settings')

        # Tab for Mods (always visible in both basic and advanced)
        self.mods_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.mods_tab, text='🎮 Mods')

        # Populate tabs
        self.populate_tabs()
        self.create_mods_tab()

        # Initial calculation (after variables are created)
        self.update_calculations()
        
        # Optimize window movement performance
        self._configure_timer = None
        self._canvases = []  # Track canvases for optimization
        
        def throttle_window_updates(event):
            # Cancel pending timer if exists
            if self._configure_timer:
                self.root.after_cancel(self._configure_timer)
            
            # Disable canvas updates during window movement
            for canvas in self._canvases:
                if canvas.winfo_exists():
                    canvas.configure(scrollregion=canvas.bbox("all"))
            
            # Re-enable after movement stops (100ms delay)
            self._configure_timer = self.root.after(100, lambda: None)
        
        self.root.bind('<Configure>', throttle_window_updates)

    def update_calculations(self):
        # Get current values (use default if variable doesn't exist yet)
        taming_mult = getattr(self, 'server_TamingSpeedMultiplier', None)
        if taming_mult is None:
            taming_mult = 1.0
        else:
            taming_mult = taming_mult.get()

        maturation_mult = getattr(self, 'game_BabyMatureSpeedMultiplier', None)
        if maturation_mult is None:
            maturation_mult = 1.0
        else:
            maturation_mult = maturation_mult.get()

        imprint_mult = getattr(self, 'game_BabyImprintingStatScaleMultiplier', None)
        if imprint_mult is None:
            imprint_mult = 1.0
        else:
            imprint_mult = imprint_mult.get()

        hatch_mult = getattr(self, 'game_EggHatchSpeedMultiplier', None)
        if hatch_mult is None:
            hatch_mult = 1.0
        else:
            hatch_mult = hatch_mult.get()

        mating_mult = getattr(self, 'game_MatingIntervalMultiplier', None)
        if mating_mult is None:
            mating_mult = 1.0
        else:
            mating_mult = mating_mult.get()

        # Get selected dino data
        dino_name = self.selected_dino.get()
        dino_stats = self.dino_data.get(dino_name, self.dino_data['Argentavis'])

        # Calculate adjusted times
        taming_time = dino_stats['taming_time'] / taming_mult
        maturation_time = dino_stats['maturation_time'] / maturation_mult
        imprint_interval = dino_stats['imprint_interval'] / imprint_mult
        max_imprint = dino_stats['max_imprint'] * imprint_mult
        incubation_time = dino_stats['incubation_time'] / hatch_mult
        mating_cooldown = dino_stats['mating_cooldown'] / mating_mult

        # Update labels
        self.taming_values.config(text=f"{taming_time:.1f} minutes")
        self.maturation_values.config(text=f"{maturation_time:.1f} hours")

        imprint_text = f"Interval: {imprint_interval:.1f} hrs\nMax Imprint: {max_imprint:.1f}%"
        self.imprint_values.config(text=imprint_text)

        self.incubation_values.config(text=f"{incubation_time:.1f} minutes")
        self.mating_values.config(text=f"{mating_cooldown:.1f} hours")

        # Calculate max wild dino level based on difficulty
        difficulty_offset = getattr(self, 'server_DifficultyOffset', None)
        if difficulty_offset is None:
            difficulty_offset = 0.2
        else:
            difficulty_offset = difficulty_offset.get()

        override_difficulty = getattr(self, 'server_OverrideOfficialDifficulty', None)
        if override_difficulty is not None:
            override_difficulty = override_difficulty.get()
            if override_difficulty > 0:
                difficulty_offset = override_difficulty

        # Ark dino level formula: base level + (difficulty * multiplier)
        # Base max level is typically 150, difficulty multiplier is usually 30
        max_dino_level = 150 + (difficulty_offset * 30)
        
        level_text = f"Level: {max_dino_level:.0f}\nDifficulty: {difficulty_offset:.2f}"
        self.level_values.config(text=level_text)

    def switch_mode(self):
        # Clear canvas tracking list
        if hasattr(self, '_canvases'):
            self._canvases.clear()
        
        # Destroy existing content and repopulate
        for widget in self.server_tab.winfo_children():
            widget.destroy()
        for widget in self.game_tab.winfo_children():
            widget.destroy()
        self.populate_tabs()

    def populate_tabs(self):
        self.create_server_settings()
        self.create_game_settings()
        # Mods tab is created separately and persists across mode switches

    def create_mods_tab(self):
        # Clear existing widgets if any
        for widget in self.mods_tab.winfo_children():
            widget.destroy()
        
        # Main container with padding
        main_container = ttk.Frame(self.mods_tab, style='TFrame')
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title and instructions
        title = ttk.Label(main_container, text="🎮 Mod Management", style='Title.TLabel')
        title.pack(pady=(0, 15))
        
        # Instructions card
        instructions_frame = ttk.Frame(main_container, style='Card.TFrame')
        instructions_frame.pack(fill='x', pady=(0, 20))
        
        inst_inner = ttk.Frame(instructions_frame, style='Card.TFrame')
        inst_inner.pack(padx=15, pady=15, fill='x')
        
        ttk.Label(inst_inner, text="📖 How to Add Mods:", style='Subtitle.TLabel').pack(anchor='w', pady=(0, 10))
        
        instructions = [
            "1. Visit CurseForge Ark: Survival Ascended Mods page",
            "2. Find the mod you want and click on it",
            "3. The Mod ID is in the URL (e.g., curseforge.com/.../mods/12345)",
            "4. Enter the Mod ID below and click 'Add Mod'",
            "5. Mods will be loaded in the order shown in the list"
        ]
        
        for instruction in instructions:
            inst_label = tk.Label(inst_inner, text=instruction, 
                                 font=('Segoe UI', 9),
                                 fg=self.colors['text_secondary'],
                                 bg=self.colors['bg_medium'],
                                 anchor='w')
            inst_label.pack(anchor='w', pady=2, padx=10)
        
        # Mod management frame
        management_frame = ttk.Frame(main_container, style='Card.TFrame')
        management_frame.pack(fill='both', expand=True)
        
        mgmt_inner = ttk.Frame(management_frame, style='Card.TFrame')
        mgmt_inner.pack(padx=15, pady=15, fill='both', expand=True)
        
        # Add mod section
        add_frame = ttk.Frame(mgmt_inner, style='Card.TFrame')
        add_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Label(add_frame, text="Add Mod:", style='TLabel').pack(side=tk.LEFT, padx=(0, 10))
        
        self.mod_id_entry = ttk.Entry(add_frame, width=30)
        self.mod_id_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.mod_id_entry.bind('<Return>', lambda e: self.add_mod())
        
        add_btn = ttk.Button(add_frame, text="➕ Add Mod", command=self.add_mod, width=15)
        add_btn.pack(side=tk.LEFT)
        
        # Current mods list
        list_label = ttk.Label(mgmt_inner, text="Current Mods:", style='Subtitle.TLabel')
        list_label.pack(anchor='w', pady=(15, 10))
        
        # Container for listbox and buttons (side by side)
        list_container = ttk.Frame(mgmt_inner, style='Card.TFrame')
        list_container.pack(fill='both', expand=True)
        
        # Left side - Listbox with scrollbar
        list_frame = ttk.Frame(list_container, style='Card.TFrame')
        list_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 15))
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        
        self.mods_listbox = tk.Listbox(list_frame, 
                                       font=('Segoe UI', 10),
                                       bg=self.colors['bg_dark'],
                                       fg=self.colors['text_primary'],
                                       selectbackground=self.colors['accent'],
                                       selectforeground='white',
                                       height=12,
                                       width=50,
                                       yscrollcommand=scrollbar.set)
        self.mods_listbox.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=self.mods_listbox.yview)
        
        # Right side - Buttons for list management (vertical layout)
        btn_frame = ttk.Frame(list_container, style='Card.TFrame')
        btn_frame.pack(side=tk.RIGHT, fill='y')
        
        remove_btn = ttk.Button(btn_frame, text="🗑️ Remove", command=self.remove_mod, width=18)
        remove_btn.pack(pady=(0, 10))
        
        move_up_btn = ttk.Button(btn_frame, text="⬆️ Move Up", command=self.move_mod_up, width=18)
        move_up_btn.pack(pady=(0, 10))
        
        move_down_btn = ttk.Button(btn_frame, text="⬇️ Move Down", command=self.move_mod_down, width=18)
        move_down_btn.pack(pady=(0, 10))
        
        clear_btn = ttk.Button(btn_frame, text="🧹 Clear All", command=self.clear_mods, width=18)
        clear_btn.pack(pady=(0, 0))
        
        # Load existing mods
        self.load_mods_to_listbox()
    
    def load_mods_to_listbox(self):
        """Load mods from ActiveMods setting to listbox"""
        self.mods_listbox.delete(0, tk.END)
        active_mods = self.settings['ServerSettings'].get('ActiveMods', '')
        if active_mods:
            mod_list = [mod.strip() for mod in active_mods.split(',') if mod.strip()]
            for mod in mod_list:
                self.mods_listbox.insert(tk.END, mod)
    
    def add_mod(self):
        """Add a mod ID to the list"""
        mod_id = self.mod_id_entry.get().strip()
        if mod_id:
            # Validate it's a number
            if not mod_id.isdigit():
                messagebox.showwarning("Invalid Mod ID", "Mod ID must be a number")
                return
            
            # Check if already exists
            existing_mods = self.mods_listbox.get(0, tk.END)
            if mod_id in existing_mods:
                messagebox.showinfo("Duplicate", "This mod is already in the list")
                return
            
            self.mods_listbox.insert(tk.END, mod_id)
            self.mod_id_entry.delete(0, tk.END)
            self.update_active_mods()
    
    def remove_mod(self):
        """Remove selected mod from list"""
        selection = self.mods_listbox.curselection()
        if selection:
            self.mods_listbox.delete(selection[0])
            self.update_active_mods()
    
    def clear_mods(self):
        """Clear all mods from list"""
        if messagebox.askyesno("Clear All Mods", "Are you sure you want to remove all mods?"):
            self.mods_listbox.delete(0, tk.END)
            self.update_active_mods()
    
    def move_mod_up(self):
        """Move selected mod up in the list"""
        selection = self.mods_listbox.curselection()
        if selection and selection[0] > 0:
            idx = selection[0]
            mod = self.mods_listbox.get(idx)
            self.mods_listbox.delete(idx)
            self.mods_listbox.insert(idx - 1, mod)
            self.mods_listbox.selection_set(idx - 1)
            self.update_active_mods()
    
    def move_mod_down(self):
        """Move selected mod down in the list"""
        selection = self.mods_listbox.curselection()
        if selection and selection[0] < self.mods_listbox.size() - 1:
            idx = selection[0]
            mod = self.mods_listbox.get(idx)
            self.mods_listbox.delete(idx)
            self.mods_listbox.insert(idx + 1, mod)
            self.mods_listbox.selection_set(idx + 1)
            self.update_active_mods()
    
    def update_active_mods(self):
        """Update ActiveMods setting from listbox"""
        mods = self.mods_listbox.get(0, tk.END)
        self.settings['ServerSettings']['ActiveMods'] = ','.join(mods)

    def create_server_settings(self):
        canvas = tk.Canvas(self.server_tab, bg=self.colors['bg_dark'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.server_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')

        # Register canvas for performance optimization
        if hasattr(self, '_canvases'):
            self._canvases.append(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Removed scrollbar bindings to prevent lag during window moves
        # Canvas handles scrolling automatically

        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y", pady=10)

        # Update scroll region when content changes
        def update_scroll_region():
            canvas.configure(scrollregion=canvas.bbox("all"))
        scrollable_frame.bind('<Configure>', lambda e: canvas.after_idle(update_scroll_region))

        # Enable mouse wheel scrolling
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)
        # Unbind when leaving the canvas to avoid conflicts
        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        settings_to_show = self.basic_server if self.mode.get() == 'basic' else list(self.settings['ServerSettings'].keys())

        row = 0
        for key in settings_to_show:
            if key in self.descriptions:
                # Setting name with modern styling
                label = tk.Label(scrollable_frame, 
                                text=key, 
                                font=('Segoe UI', 10, 'bold'),
                                fg=self.colors['text_primary'],
                                bg=self.colors['bg_dark'])
                label.grid(row=row, column=0, sticky='w', padx=10, pady=(15, 5))
                
                # Description with better visibility
                desc = self.descriptions.get(key, '')
                desc_label = tk.Label(scrollable_frame, 
                                     text=desc, 
                                     font=('Segoe UI', 9),
                                     fg=self.colors['text_secondary'],
                                     bg=self.colors['bg_dark'],
                                     wraplength=500,
                                     justify='left')
                desc_label.grid(row=row+1, column=0, columnspan=4, sticky='w', padx=10, pady=(0, 5))
                value = self.settings['ServerSettings'].get(key, 0)
                if isinstance(value, bool):
                    var = tk.BooleanVar(value=value)
                    chk = ttk.Checkbutton(scrollable_frame, variable=var)
                    chk.grid(row=row, column=1, padx=5, pady=2)
                    setattr(self, f'server_{key}', var)
                elif isinstance(value, int):
                    var = tk.IntVar(value=value)
                    spin = ttk.Spinbox(scrollable_frame, from_=0, to=100000, textvariable=var, width=10)
                    spin.grid(row=row, column=1, padx=5, pady=2)
                    setattr(self, f'server_{key}', var)
                elif isinstance(value, float):
                    var = tk.DoubleVar(value=value)
                    # Determine if this key needs calculation updates
                    needs_calc_update = key in ['DifficultyOffset', 'TamingSpeedMultiplier', 'OverrideOfficialDifficulty']
                    
                    if needs_calc_update:
                        scale_cmd = lambda val: self.update_calculations()
                    else:
                        scale_cmd = None
                    
                    scale = ttk.Scale(scrollable_frame, from_=0.0, to=10.0, variable=var, orient='horizontal',
                                     command=scale_cmd)
                    scale.grid(row=row, column=1, padx=5, pady=2)
                    label = ttk.Label(scrollable_frame, textvariable=var, width=5)
                    label.grid(row=row, column=2, padx=5, pady=2)
                    entry = ttk.Entry(scrollable_frame, textvariable=var, width=10)
                    entry.grid(row=row, column=3, padx=5, pady=2)
                    # Bind entry changes for real-time updates
                    if needs_calc_update:
                        entry.bind('<KeyRelease>', lambda e: self.update_calculations())
                    setattr(self, f'server_{key}', var)
                else:  # string
                    var = tk.StringVar(value=value)
                    if key == 'ActiveEvent':
                        # Format event options with status indicators
                        event_display_names = []
                        for event_name in sorted(self.events_data.keys()):
                            status = self.events_data[event_name].get('status', 'unknown')
                            if status == 'working':
                                display_name = f"✅ {event_name}"
                            else:
                                display_name = f"⏰ {event_name} (Coming Soon)"
                            event_display_names.append(display_name)
                        
                        combo = ttk.Combobox(scrollable_frame, values=event_display_names, state='readonly', width=35)
                        combo.grid(row=row, column=1, columnspan=2, padx=5, pady=2, sticky='w')
                        
                        # Create a closure to capture combo properly
                        def make_event_handler(c, v):
                            def on_event_select(event_obj):
                                selected_text = c.get()
                                # Remove indicators to get actual event name
                                event_name = selected_text.replace("✅ ", "").replace("⏰ ", "").replace(" (Coming Soon)", "")
                                v.set(event_name)
                            return on_event_select
                        
                        # Set default value based on current value
                        default_value = "✅ None" if value == 'None' else f"✅ {value}"
                        if default_value in event_display_names:
                            combo.set(default_value)
                        else:
                            combo.set(event_display_names[0] if event_display_names else "✅ None")
                        
                        combo.bind('<<ComboboxSelected>>', make_event_handler(combo, var))
                        setattr(self, f'server_{key}_combo', combo)
                    else:
                        entry = ttk.Entry(scrollable_frame, textvariable=var, width=15)
                        entry.grid(row=row, column=1, padx=5, pady=2)
                    setattr(self, f'server_{key}', var)
                row += 2

        # Add footer with tips
        row += 1
        ttk.Separator(scrollable_frame, orient='horizontal').grid(row=row, column=0, columnspan=4, sticky='ew', pady=20, padx=10)
        row += 1
        ttk.Label(scrollable_frame, 
                 text="💡 Server Settings Tips:", 
                 font=('Segoe UI', 11, 'bold'),
                 foreground=self.colors['accent'],
                 background=self.colors['bg_dark']).grid(row=row, column=0, sticky='w', padx=10, pady=(10, 8))
        row += 1
        tips = [
            "• DifficultyOffset 1.0 = 150 max level. Each 0.033 adds ~1 level (5.0 = 300)",
            "• XP multiplier affects both players and dinos - higher = faster leveling",
            "• HarvestAmountMultiplier 3.0+ can cause mesh issues with resource nodes",
            "• TamingSpeed 10.0+ allows instant tames but may skip feeding animations",
            "• Set MaxTributeDinos=0 to disable cross-server dino transfers"
        ]
        for tip in tips:
            ttk.Label(scrollable_frame, 
                     text=tip, 
                     font=('Segoe UI', 9),
                     foreground=self.colors['text_secondary'],
                     background=self.colors['bg_dark']).grid(row=row, column=0, columnspan=4, sticky='w', padx=10, pady=3)
            row += 1

        # Removed scroll region update entirely to prevent any canvas performance issues
        # Canvas should handle scrolling automatically without explicit scrollregion

    def create_game_settings(self):
        canvas = tk.Canvas(self.game_tab, bg=self.colors['bg_dark'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.game_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')

        # Register canvas for performance optimization
        if hasattr(self, '_canvases'):
            self._canvases.append(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Removed scrollbar bindings to prevent lag during window moves
        # Canvas handles scrolling automatically

        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y", pady=10)

        # Update scroll region when content changes
        def update_scroll_region():
            canvas.configure(scrollregion=canvas.bbox("all"))
        scrollable_frame.bind('<Configure>', lambda e: canvas.after_idle(update_scroll_region))

        # Enable mouse wheel scrolling
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)
        # Unbind when leaving the canvas to avoid conflicts
        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        settings_to_show = self.basic_game if self.mode.get() == 'basic' else list(self.settings['/script/shootergame.shootergamemode'].keys())

        row = 0
        for key in settings_to_show:
            if key in self.descriptions:
                ttk.Label(scrollable_frame, text=key, font=('Arial', 9, 'bold')).grid(row=row, column=0, sticky='w', padx=5, pady=2)
                desc = self.descriptions.get(key, '')
                ttk.Label(scrollable_frame, text=desc, font=('Arial', 8), foreground='gray').grid(row=row+1, column=0, columnspan=4, sticky='w', padx=5, pady=1)
                value = self.settings['/script/shootergame.shootergamemode'].get(key, 0)
                if isinstance(value, bool):
                    var = tk.BooleanVar(value=value)
                    chk = ttk.Checkbutton(scrollable_frame, variable=var)
                    chk.grid(row=row, column=1, padx=5, pady=2)
                    setattr(self, f'game_{key}', var)
                elif isinstance(value, int):
                    var = tk.IntVar(value=value)
                    spin = ttk.Spinbox(scrollable_frame, from_=0, to=100000, textvariable=var, width=10)
                    spin.grid(row=row, column=1, padx=5, pady=2)
                    setattr(self, f'game_{key}', var)
                elif isinstance(value, float):
                    var = tk.DoubleVar(value=value)
                    # Determine if this key needs calculation updates
                    needs_calc_update = key in ['BabyMatureSpeedMultiplier', 'BabyImprintingStatScaleMultiplier', 
                                               'EggHatchSpeedMultiplier', 'MatingIntervalMultiplier']
                    
                    if needs_calc_update:
                        scale_cmd = lambda val: self.update_calculations()
                    else:
                        scale_cmd = None
                    
                    scale = ttk.Scale(scrollable_frame, from_=0.0, to=10.0, variable=var, orient='horizontal',
                                     command=scale_cmd)
                    scale.grid(row=row, column=1, padx=5, pady=2)
                    label = ttk.Label(scrollable_frame, textvariable=var, width=5)
                    label.grid(row=row, column=2, padx=5, pady=2)
                    entry = ttk.Entry(scrollable_frame, textvariable=var, width=10)
                    entry.grid(row=row, column=3, padx=5, pady=2)
                    # Bind entry changes for real-time updates
                    if needs_calc_update:
                        entry.bind('<KeyRelease>', lambda e: self.update_calculations())
                    setattr(self, f'game_{key}', var)
                else:  # string
                    var = tk.StringVar(value=value)
                    entry = ttk.Entry(scrollable_frame, textvariable=var, width=15)
                    entry.grid(row=row, column=1, padx=5, pady=2)
                    setattr(self, f'game_{key}', var)
                row += 2

        # Add footer with tips
        row += 1
        ttk.Separator(scrollable_frame, orient='horizontal').grid(row=row, column=0, columnspan=4, sticky='ew', pady=20, padx=10)
        row += 1
        ttk.Label(scrollable_frame, 
                 text="💡 Game Settings Tips:", 
                 font=('Segoe UI', 11, 'bold'),
                 foreground=self.colors['accent'],
                 background=self.colors['bg_dark']).grid(row=row, column=0, sticky='w', padx=10, pady=(10, 8))
        row += 1
        tips = [
            "• BabyMatureSpeed 36.0 + EggHatch 36.0 = ~10min raise (official: ~6hrs)",
            "• MatingInterval 0.01 = ~18sec cooldown (official: 18-48hrs per species)",
            "• ImprintStatScale >1.0 gives bonus stats but can exceed 100% imprint",
            "• CuddleInterval multiplier doesn't exist - use MatureSpeed to adjust",
            "• MaxTamedDinos affects server performance - 5000+ causes lag spikes"
        ]
        for tip in tips:
            ttk.Label(scrollable_frame, 
                     text=tip, 
                     font=('Segoe UI', 9),
                     foreground=self.colors['text_secondary'],
                     background=self.colors['bg_dark']).grid(row=row, column=0, columnspan=4, sticky='w', padx=10, pady=3)
            row += 1

        # Removed scroll region update entirely to prevent any canvas performance issues
        # Canvas should handle scrolling automatically without explicit scrollregion

    def generate_files(self):
        # Update calculations before generating files
        self.update_calculations()
        
        current_mode = self.mode.get()
        
        # Update settings from GUI based on current mode
        if current_mode == 'basic':
            # Only update basic server settings
            for key in self.basic_server:
                var_name = f'server_{key}'
                if hasattr(self, var_name):
                    var = getattr(self, var_name)
                    if hasattr(var, 'get'):
                        self.settings['ServerSettings'][key] = var.get()
            
            # Only update basic game settings
            for key in self.basic_game:
                var_name = f'game_{key}'
                if hasattr(self, var_name):
                    var = getattr(self, var_name)
                    if hasattr(var, 'get'):
                        self.settings['/script/shootergame.shootergamemode'][key] = var.get()
        else:
            # Update all settings for advanced mode
            for key in self.settings['ServerSettings']:
                var_name = f'server_{key}'
                if hasattr(self, var_name):
                    var = getattr(self, var_name)
                    if hasattr(var, 'get'):
                        self.settings['ServerSettings'][key] = var.get()

            for key in self.settings['/script/shootergame.shootergamemode']:
                var_name = f'game_{key}'
                if hasattr(self, var_name):
                    var = getattr(self, var_name)
                    if hasattr(var, 'get'):
                        self.settings['/script/shootergame.shootergamemode'][key] = var.get()

        try:
            # Generate GameUserSettings.ini
            config1 = configparser.ConfigParser(allow_no_value=True)
            config1.optionxform = str
            config1.add_section('ServerSettings')
            
            # Always include ActiveMods regardless of mode
            mods = self.mods_listbox.get(0, tk.END)
            self.settings['ServerSettings']['ActiveMods'] = ','.join(mods)
            
            if current_mode == 'basic':
                for key in self.basic_server:
                    value = self.settings['ServerSettings'].get(key, '')
                    config1.set('ServerSettings', key, str(value))
                # Always add ActiveMods
                config1.set('ServerSettings', 'ActiveMods', self.settings['ServerSettings']['ActiveMods'])
            else:
                for key, value in self.settings['ServerSettings'].items():
                    config1.set('ServerSettings', key, str(value))

            with open('GameUserSettings.ini', 'w') as f:
                config1.write(f)

            # Generate Game.ini
            config2 = configparser.ConfigParser(allow_no_value=True)
            config2.optionxform = str
            config2.add_section('/script/shootergame.shootergamemode')
            
            if current_mode == 'basic':
                for key in self.basic_game:
                    value = self.settings['/script/shootergame.shootergamemode'].get(key, '')
                    config2.set('/script/shootergame.shootergamemode', key, str(value))
            else:
                for key, value in self.settings['/script/shootergame.shootergamemode'].items():
                    config2.set('/script/shootergame.shootergamemode', key, str(value))

            with open('Game.ini', 'w') as f:
                config2.write(f)

            mode_text = "Basic" if current_mode == 'basic' else "Advanced"
            # Get the current working directory and absolute paths of the generated files
            current_dir = os.getcwd()
            game_user_settings_path = os.path.join(current_dir, 'GameUserSettings.ini')
            game_ini_path = os.path.join(current_dir, 'Game.ini')
            
            messagebox.showinfo("Success", 
                              f"INI files generated successfully in {mode_text} mode!\n\n"
                              f"Files saved to:\n{current_dir}\n\n"
                              f"Generated files:\n"
                              f"• GameUserSettings.ini\n"
                              f"• Game.ini\n\n"
                              f"Full paths:\n"
                              f"{game_user_settings_path}\n"
                              f"{game_ini_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate INI files: {str(e)}")

    def reset_to_defaults(self):
        # Reset mode to basic
        self.mode.set('basic')
        # Reset GUI controls to default values
        for section, settings in self.settings.items():
            prefix = 'server_' if section == 'ServerSettings' else 'game_'
            for key, default_value in settings.items():
                var_name = f'{prefix}{key}'
                if hasattr(self, var_name):
                    var = getattr(self, var_name)
                    if hasattr(var, 'set'):
                        var.set(default_value)
        # Clear mods list
        if hasattr(self, 'mods_listbox'):
            self.mods_listbox.delete(0, tk.END)
            self.settings['ServerSettings']['ActiveMods'] = ''
        # Repopulate tabs to reflect basic mode
        self.switch_mode()
        messagebox.showinfo("Reset", "All settings reset to defaults and mode set to Basic!")

if __name__ == '__main__':
    root = tk.Tk()
    app = ArkSettingsGenerator(root)
    root.mainloop()