# MekPack: Future Frontiers

A sci-fi tech modpack for **Minecraft 26.3 (NeoForge 26.3.0.110)** built around **Mekanism 10.8**. Instead of letting companion mods compete with or skip Mekanism's tech tree, MekPack ties Applied Energistics 2, Pipez, CC: Tweaked, SecurityCraft, dimensional storage, and portals directly into Mekanism progression.

> **Note on AI Assistance:** MekPack is a personal passion project maintained with **AI assistance** for updating mod packages, resolving version and dependency conflicts, managing startup and crash errors, and wiring configs, custom recipes, and quests on the cutting-edge Minecraft 26.3 ecosystem.

---

## How to Try It

### Option 1: Import a Release (Recommended)
1. Download the latest release from [GitHub Releases](https://github.com/devwithzachary/MekPack/releases):
   - `MekPack-26.3-0.0.3.mrpack` for Prism Launcher, Modrinth App, or ATLauncher.
   - `MekPack-26.3-0.0.3-Prism.zip` for a self-contained Prism Launcher import.
2. In your launcher, click **Add Instance -> Import** and select the downloaded file.
3. Make sure **Java 25** is selected and **6-8 GB of RAM** is allocated.
4. Launch the game and open the **Theseus Quest Book** to follow the 6-tier progression tree.

### Option 2: Build and Run from Source
```bash
git clone https://github.com/devwithzachary/MekPack.git
cd MekPack
python3 tools/setup_instance.py
```
This links `config/` and `resourcepacks/` into `minecraft/`, generates the quest and advancement trees, builds the custom content pack, and downloads all 49 companion mods from Modrinth with SHA-512 verification. You can then point Prism Launcher or MultiMC at the directory and launch with NeoForge `26.3.0.110` and Java 25.

---

## What's Inside the Pack

### Mekanism at the Center
- **Mekanism, Generators, Tools, and Additions**: 5x ore processing, Digital Miner, Fission and Fusion Reactors, Industrial Turbine, Supercritical Phase Shifter (SPS), Antimatter synthesis, QIO storage, and the MekaSuit.
- Because Mekanism does not yet have an official public release for Minecraft 26.3 on Modrinth, MekPack currently bundles dev builds compiled from Mekanism's upstream `26.3` branch.

### Guided 6-Tier Quest Progression
- **Theseus Quests**: Every player receives the **Theseus Quest Book** automatically on joining a world, with a 6-chapter, 33-milestone quest tree, automatic item-collection tasks, item and XP rewards, and branching wings for companion mods.
- **Advancement Plaques**: Celebration plaques still appear for vanilla and mod advancements, while progression stays centered on the Theseus Quest Book:
  - **Tier 0 - Ground Zero**: Osmium prospecting and basic Heat Generators.
  - **Tier 1 - The Spark of Steel**: Metallurgic Infuser, Steel, Basic Control Circuits, Wind Turbines, Pipez, CC: Tweaked, Moving Elevators, and Chunk Loaders.
  - **Tier 2 - Kinetic Automation**: Enrichment Chamber (2x ore), Infused Alloys, Advanced Circuits, AE2 ME Controller and basic storage, and SecurityCraft keypads.
  - **Tier 3 - Chemical Digitization**: Electrolytic Separator, Purification Chamber (3x ore), Reinforced Alloys, Elite Circuits, Digital Miner, and DimStorage.
  - **Tier 4 - Nuclear Power & Relays**: Fission Reactor, Industrial Turbine, Atomic Alloys, Ultimate Circuits, Entangled blocks, and Wormhole portals.
  - **Tier 5 - Supercritical Frontier**: Fusion Reactor, SPS Antimatter production, MekaSuit, QIO Drive Array, and Shrink.

### Companion Tech & Logistics
- **Applied Energistics 2 (`ae2`)**: ME Networks, autocrafting, spatial storage, and wireless bridges gated behind Mekanism alloys and circuits.
- **CC: Tweaked (`cc-tweaked`)**: Programmable Lua computers and monitors, including a built-in Mekanism reactor and energy matrix telemetry script (`config/cc-tweaked/scripts/mek_monitor.lua`).
- **Pipez**: High-throughput item, fluid, gas, and energy pipes with tiered upgrades matching Mekanism circuits.
- **SecurityCraft**: Keypads, retinal scanners, laser grids, and reinforced base defenses.
- **Moving Elevators, DimStorage, Entangled, Wormhole, Shrink, Chunk Loaders, Trash Cans, and Item Collectors**: Base transit, cross-dimensional storage and teleportation, shrinking, and automation utilities.

### Worldgen & Exploration
- **The Lost Cities**: Procedural abandoned metropolis dimension with skyscrapers, highways, and subways.
- **Terralith & Tectonic**: Overworld terrain and biome overhaul with dramatic cliffs, calderas, and valleys.
- **Incendium & Nullscape**: Overhauled Nether and End dimensions.
- **Structory & Structory Towers**: Scattered ruins, outposts, and transmission towers.

### Performance, Visuals & Quality of Life
- **Sodium & Iris**: High-performance rendering with shader pack support.
- **Lithium, FerriteCore, ImmediatelyFast, Entity Culling, More Culling, and Dynamic FPS**: Memory and frame-rate optimizations.
- **JEI, Jade, Xaero's Minimap, Xaero's World Map, and AppleSkin**: Recipe lookup, machine/chemical HUD tooltips, mapping, and saturation display.

---

## Project Layout, Tools & Documentation

```text
├── config/              # Curated mod and Theseus Quests configurations
├── resourcepacks/       # Optional resource packs
├── custom_content/      # Custom recipes, advancements, and reward loot tables
├── custom_mods/         # Upstream Mekanism 26.3 builds & MekPackContent jar
├── tools/               # Python scripts for resolving, building, and exporting
├── docs/                # Design, recipe, and distribution documentation
├── instance.cfg         # Prism Launcher instance config
├── mmc-pack.json        # Component versions (Minecraft 26.3, NeoForge 26.3.0.110)
├── resolved_mods.json   # Pinned Modrinth manifest with SHA-512 hashes
└── minecraft/           # [Gitignored] Local test instance directory
```

Key scripts in `tools/`:
- `python3 tools/setup_instance.py`: Sets up `minecraft/` for local testing.
- `python3 tools/mod_resolver.py` & `python3 tools/download_mods.py`: Resolves compatible Modrinth `26.3` NeoForge mods and downloads them with SHA-512 verification.
- `python3 tools/generate_theseus_quests.py` & `python3 tools/generate_advancements.py`: Regenerates the 33-milestone quest book and advancement tree.
- `python3 tools/update_mekanism.py`: Checks Modrinth for an official 26.3 Mekanism release or rebuilds from the upstream `26.3` branch.
- `python3 tools/export_pack.py`: Exports `.mrpack` and Prism `.zip` release bundles into `dist/`.

Further documentation:
- [Changelog](CHANGELOG.md)
- [AI & Contributor Guidelines](AGENTS.md)
- [Modpack Philosophy](docs/MODPACK_PHILOSOPHY.md)
- [Companion Mod Integration Matrix](docs/INTEGRATION_MATRIX.md)
- [Recipe Customization Guide](docs/RECIPE_CUSTOMIZATION_GUIDE.md)
- [Custom Achievement Flow Blueprint](docs/ACHIEVEMENT_FLOW_BLUEPRINT.md)
- [Public Distribution & Publishing Guide](docs/DISTRIBUTION_GUIDE.md)

---

## Credits & Acknowledgements

MekPack relies on the work of the Minecraft modding community. Thank you to every developer and contributor whose mods make this pack possible:

### Industrial Core
- **Mekanism, Generators, Tools & Additions**: Created by [Aidancbrady](https://aidancbrady.com/mekanism/), [Thommy101](https://github.com/Thommy101), [Thiakil](https://github.com/thiakil), [pupnewfster](https://github.com/pupnewfster), [dizzyd](https://github.com/dizzyd), with contributions from unpairedbracket, CyanideX, Ridanisaurus, and the Mekanism community.

### Automation, Networking & Logistics
- **Applied Energistics 2 (`ae2`)**: Created by [Team AppliedEnergistics](https://appliedenergistics.org/) (shartte, yueh, and contributors).
- **ComputerCraft: Tweaked (`cc-tweaked`)**: Created by [Daniel Ratcliffe](https://tweaked.cc/) (DanTwoHundred), maintained by Aaron Mills and SquidDev.
- **Pipez**: Created by [Max Henkel](https://www.curseforge.com/minecraft/mc-mods/pipez).
- **DimStorage**: Created by [Edivad99](https://github.com/Edivad99) (with special thanks to Thegaarnik).
- **Entangled**: Created by [SuperMartijn642](https://www.curseforge.com/minecraft/mc-mods/entangled).
- **Wormhole (Portals)**: Created by [SuperMartijn642](https://www.curseforge.com/minecraft/mc-mods/wormhole-portals).
- **Moving Elevators**: Created by [SuperMartijn642](https://www.curseforge.com/minecraft/mc-mods/moving-elevators).
- **Chunk Loaders**: Created by [SuperMartijn642](https://www.curseforge.com/minecraft/mc-mods/chunk-loaders).
- **Trash Cans & Item Collectors**: Created by [SuperMartijn642](https://www.curseforge.com/minecraft/mc-mods/trash-cans).
- **Shrink**: Created by [Gigabit101](https://gigabit101.net/mods/Shrink).
- **SecurityCraft**: Created by [Geforce](https://discord.gg/U8DvBAW), bl4ckscor3, Redstone_Dubstep, and ChainmailPickaxe.

### Worldgen, Dimensions & Structures
- **The Lost Cities**: Created by [McJty](http://github.com/McJtyMods/LostCities/).
- **Terralith, Incendium, Nullscape, Structory & Structory Towers**: Created by [Stardust Labs](https://www.stardustlabs.net/) (Starmute, catter1, Botany, TheKingWhale, Rei_the_Goat, runcows).
- **Tectonic**: Created by [Apollo](https://modrinth.com/mod/tectonic).

### Performance, Rendering & Engine
- **Sodium & Lithium**: Created by [JellySquid (jellysquid3)](https://github.com/CaffeineMC), IMS212, 2No2Name, and contributors.
- **Iris**: Created by [coderbot](https://github.com/IrisShaders/Iris), IMS212, and the Iris team.
- **ImmediatelyFast**: Created by [RaphiMC (RK_01)](https://github.com/RaphiMC/ImmediatelyFast).
- **FerriteCore**: Created by [malte0811](https://github.com/malte0811/FerriteCore).
- **Entity Culling**: Created by [tr7zw](https://modrinth.com/mod/entityculling).
- **More Culling**: Created by [FX - PR0CESS](https://modrinth.com/mod/moreculling) and 1Foxy2.
- **Dynamic FPS**: Created by [juliand665 & LostLuma](https://dapprgames.com/mods).

### Quests, HUD, Diagnostics & Utilities
- **Theseus Quests**: Created by [johardt](https://modrinth.com/mod/theseus-quests) (forked from Terrarium's Heracles / Odyssey Quests).
- **Just Enough Items (JEI)** & **MezzConfig**: Created by [mezz](https://www.curseforge.com/minecraft/mc-mods/jei).
- **Jade**: Created by [Snownee](https://www.curseforge.com/minecraft/mc-mods/jade) (with credits to TehNut, ProfMobius, and kalkafox).
- **Better Advancements**: Created by [way2muchnoise](https://www.curseforge.com/minecraft/mc-mods/better-advancements).
- **Advancement Plaques**: Created by [Grend_G](https://modrinth.com/mod/advancement-plaques).
- **AppleSkin**: Created by [squeek502](https://github.com/squeek502/AppleSkin).
- **Xaero's Minimap & World Map**: Created by [xaero96](https://channillo.com/authors/xaero96/).

### APIs & Companion Libraries
- **Curios API**: Created by [TheIllusiveC4 (C4)](https://github.com/TheIllusiveC4/Curios).
- **Architectury API & Cloth Config**: Created by [shedaniel](https://github.com/shedaniel).
- **Yet Another Config Lib (YACL)**: Created by [isXander](https://github.com/isXander).
- **Resourceful Lib**: Created by [Team Resourceful](https://modrinth.com/mod/resourceful-lib).
- **SuperMartijn642's Core & Config Libs**: Created by [SuperMartijn642](https://github.com/SuperMartijn642).
- **Forge Config API Port**: Created by [Fuzs](https://modrinth.com/mod/forge-config-api-port).
- **GuideME**: Created by [shartte](https://github.com/AppliedEnergistics/GuideME/).
- **EdivadLib**: Created by [Edivad99](https://github.com/Edivad99).
- **Polylib**: Created by [CreeperHost](https://minetogether.io).
- **Iceberg** & **Lithostitched**: Created by their respective Modrinth authors.
