# ⚡ MekPack: Future Frontiers (Minecraft 26.3)

A high-tech, futuristic sci-fi modpack centered around **Mekanism 10.8** on **Minecraft 26.3 (NeoForge)**.

Built in preparation for the official public release of Mekanism 26.3, equipped with local dev builds from the upstream repository and a curated suite of sci-fi tech, automation, planetary world generation, optimization, and QoL companion mods.

> ⚡ **The Sovereign Spine Directive**: Unlike loose kitchen-sink modpacks, MekPack binds every companion mod directly into Mekanism's technological progression. You cannot bypass Mekanism with external mods; Applied Energistics 2, Pipez, ComputerCraft, and quantum dimensional logistics all demand proportional Mekanism alloys, control circuits, and industrial machinery.
> 
> Detailed documentation:
> - 📜 [Modpack Philosophy & Core Tenets](docs/MODPACK_PHILOSOPHY.md)
> - 🧩 [Companion Mod Integration Matrix](docs/INTEGRATION_MATRIX.md)
> - ⚙️ [Recipe Customization & Technical Guide](docs/RECIPE_CUSTOMIZATION_GUIDE.md)
> - 🏆 [Custom Achievement Flow Blueprint](docs/ACHIEVEMENT_FLOW_BLUEPRINT.md)
> - 🚀 [Public Distribution & Publishing Guide](docs/DISTRIBUTION_GUIDE.md)
> - 🤖 [AI & Contributor Core Guidelines](AGENTS.md)

---

## 🚀 Key Features & Mod Suite

### 1. The Core Industrial Engine: Mekanism
- **Mekanism (Core)**: 5x Chemical Ore Processing, Digital Miner, Supercritical Phase Shifter (SPS), Antimatter generation, QIO Quantum Storage, and MekaSuit modular armor.
- **Mekanism Generators**: Advanced Solar Generators, Wind Turbines, Gas-Burning Generators, Industrial Fission & Fusion Reactors, and Turbine assemblies.
- **Mekanism Tools**: Refined Obsidian, Osmium, Lapis, and Glowstone tools and armors.
- **Mekanism Additions**: Baby skeletons, voice dispensers, and colorful plastic building blocks.

### 2. Automation & Sci-Fi Systems
- **Applied Energistics 2 (`ae2`)**: ME Network, Quantum Network Bridges, Spatial Storage, Autocrafting, and ME Terminals.
- **CC: Tweaked**: Programmable Lua supercomputers and monitors. Includes a built-in Mekanism reactor & energy matrix telemetry script (`config/cc-tweaked/scripts/mek_monitor.lua`).
- **SecurityCraft**: High-security facilities, laser tripwires, retinal scanners, keypad doors, bounce pads, and alarm systems.
- **Moving Elevators**: Multi-floor futuristic elevators with call buttons and speed control.
- **Pipez**: High-throughput item, fluid, gas, and energy transport cables.
- **DimStorage & Entangled & Wormhole**: Quantum frequency interdimensional tanks, chests, and portal networks.
- **Shrink**: Personal quantum resizing gadget for inspecting microcircuits and compact base routing.
- **Chunk Loaders**: Persistent industrial chunk loading across dimensions.
- **Trash Cans & Item Collectors**: Automated waste voiding and vacuum pickup.

### 3. Sci-Fi Worldgen, Dimensions & Structures
- **The Lost Cities**: Massive procedural abandoned cyberpunk metropolis dimension with skyscrapers, highways, subways, and ruins ripe for industrial reclamation.
- **Terralith & Tectonic**: Dramatic planetary terrain overhaul featuring colossal cliffs, volcanic calderas, underground rivers, and exotic biomes tailored for epic factories.
- **Incendium**: Nether technological and pipeline overhaul featuring mechanical magma facilities, geothermal vents, and infernal research ruins.
- **Nullscape**: The End transformed into an alien void frontier with floating crystal spires, nebula skies, and hazardous terrain.
- **Structory & Structory Towers**: Atmospheric outpost ruins, antenna arrays, transmission towers, and remote relay stations scattered across planets.

### 4. Visuals, Optimization & HUD
- **Sodium & Iris**: Next-generation rendering engine with high-performance shader pack support.
- **FerriteCore, Lithium, ImmediatelyFast, More Culling, Entity Culling**: Extreme performance optimizations ensuring smooth 144+ FPS even with massive automated factories.
- **Just Enough Items (JEI)** & **Jade**: Full chemical, fluid, energy, and block state HUD inspections.
- **Xaero's Minimap & World Map**: High-tech radar and planetary mapping.
- **Curios API & Companion Libraries**: Accessory slots for jetpacks and scuba gear, plus required runtime libraries (ForgeConfigAPIPort, SuperMartijn642's Config & Core Libs, EdivadLib, PolyLib, GuideME).

### 5. Progression & Quest System
- **Better Advancements & Advancement Plaques**: Structured 6-chapter sci-fi progression tree with full-screen zoomable interface, custom line links, inventory shortcut button, and animated celebration plaques upon completing milestones.
- **MekPack Sovereign Spine**: 33 milestones guiding you from Tier 0 Osmium prospecting through to Tier 5 Supercritical SPS Antimatter synthesis, with companion mod wings (AE2, Pipez, ComputerCraft, SecurityCraft, DimStorage, Entangled, Wormhole, Shrink) and custom reward loot tables.
- **FTB Quests Standby**: Standby generator (`tools/generate_quests.py`) ready for deployment once an official 26.3 FTB build is released.

---

## 📁 Repository Structure

The repository is organized strictly as a clean modpack source distribution:

```
├── config/              # Curated mod configurations
├── resourcepacks/       # User resourcepacks directory
├── custom_content/      # Data pack recipes, advancements, loot tables
├── custom_mods/         # Mekanism & MekPackContent jars
├── tools/               # Automation & maintenance scripts
├── instance.cfg         # Prism Launcher instance configuration
├── mmc-pack.json        # Component versions (MC 26.3, NeoForge 26.3.0.95)
├── resolved_mods.json   # Mod manifest with SHA-512 hashes and download URLs
└── minecraft/           # [GITIGNORED] Local test environment & runtime files
```

The runtime testing folder `minecraft/` is completely excluded from git tracking to prevent save games, logs, player caches, or binary jars from bloating the repo.

---

## 🎮 Playing & Testing via Prism Launcher

The modpack repository is pre-configured and directly linked to your local Prism Launcher:

- **Instance Name**: `MekPack 26.3 (Sci-Fi Edition)`
- **Instance Folder**: `~/.local/share/PrismLauncher/instances/MekPack-26.3`
- **Configured Java**: Microsoft Java 25.0.1 LTS (`java-runtime-epsilon`)
- **Memory**: 8 GB Allocated (Optimized G1GC args configured)

### Setup Local Environment
If setting up a fresh clone, run:
```bash
python3 tools/setup_instance.py
```
This automatically symlinks `config/` and `resourcepacks/`, links custom Mekanism builds, compiles custom datapack content, and downloads all companion mods.

### Launching
- **GUI**: Open Prism Launcher and double-click **MekPack 26.3 (Sci-Fi Edition)**.
- **CLI**:
  ```bash
  prismlauncher --launch MekPack-26.3
  ```

---

## 🛠️ Management & Automation Tools

In `tools/`:

### 1. Setup Instance (`tools/setup_instance.py`)
Prepares the local test environment (`minecraft/`) with symlinks to `config/` and `resourcepacks/`, downloads all companion mods, copies custom Mekanism builds, and applies compatibility patches.

### 2. Update Mekanism (`tools/update_mekanism.py`)
Checks upstream GitHub (`mekanism/Mekanism` branch `26.3`) and Modrinth:
- While 26.3 is in development: pulls latest commits and recompiles the local jars into `custom_mods/`.
- When the Mekanism team publishes the official public 26.3 build: automatically downloads official release jars, verifies hashes, and cleans up dev jars.
```bash
python3 tools/update_mekanism.py
```

### 3. Export for Release (`tools/export_pack.py`)
Builds distributable release packages directly into `dist/`:
- `MekPack-26.3-0.0.1-Prism.zip`: Importable by Prism Launcher, MultiMC, or ATLauncher.
- `MekPack-26.3-0.0.1.mrpack`: Modrinth modpack format with hash manifests.
```bash
python3 tools/export_pack.py
```

### 4. Progression & Advancements Generation (`tools/generate_advancements.py`)
Generates the synced datapack advancements and reward loot tables across all 6 progression tiers:
```bash
python3 tools/generate_advancements.py
```

### 5. Mod Resolver & Downloader (`tools/mod_resolver.py` & `tools/download_mods.py`)
Resolves candidate companion mods from Modrinth for NeoForge 26.3, checks dependencies, and downloads them with SHA-512 validation.

---

## 💡 About This Project & AI Collaboration

This modpack has long been a dream project of mine, but finding the extensive time required to balance recipes, tune configurations, and architect progression alongside daily life has always been a barrier. With the emergence of modern AI coding assistants, I was finally able to bring this vision into reality within what little free time I have.

MekPack is primarily crafted for my own personal enjoyment and love for Mekanism's industrial depth. However, my sincere hope is that other players who appreciate tightly-integrated sci-fi tech progression and challenging automation will find as much fun playing it as I had putting it together.

I fully recognize and respect that some in the gaming and modding community have reservations or concerns regarding the use of AI tools in creative projects. AI was utilized here not to replace human creativity or cut corners, but rather as an interactive engineering co-pilot—accelerating the repetitive mechanics of configuration scripting, tag synchronization, and recipe wiring so that a cohesive, polished modpack could be realized.

---

## 🙏 Credits & Acknowledgements

MekPack would not exist without the incredible dedication, ingenuity, and passion of the Minecraft modding community. We extend our deepest gratitude to every developer, artist, and contributor whose work powers this experience:

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

### HUD, Diagnostics & Utilities
- **Just Enough Items (JEI)**: Created by [mezz](https://www.curseforge.com/minecraft/mc-mods/jei).
- **Jade**: Created by [Snownee](https://www.curseforge.com/minecraft/mc-mods/jade) (with credits to TehNut, ProfMobius, and kalkafox).
- **Better Advancements**: Created by [way2muchnoise](https://www.curseforge.com/minecraft/mc-mods/better-advancements).
- **Advancement Plaques**: Created by [Grend_G](https://modrinth.com/mod/advancement-plaques).
- **AppleSkin**: Created by [squeek502](https://github.com/squeek502/AppleSkin).
- **Xaero's Minimap & World Map**: Created by [xaero96](https://channillo.com/authors/xaero96/).

### APIs & Companion Libraries
- **Curios API**: Created by [TheIllusiveC4 (C4)](https://github.com/TheIllusiveC4/Curios).
- **Architectury API & Cloth Config**: Created by [shedaniel](https://github.com/shedaniel).
- **Yet Another Config Lib (YACL)**: Created by [isXander](https://github.com/isXander).
- **SuperMartijn642's Core & Config Libs**: Created by [SuperMartijn642](https://github.com/SuperMartijn642).
- **Forge Config API Port**: Created by [Fuzs](https://modrinth.com/mod/forge-config-api-port).
- **GuideME**: Created by [shartte](https://github.com/AppliedEnergistics/GuideME/).
- **EdivadLib**: Created by [Edivad99](https://github.com/Edivad99).
- **Polylib**: Created by [CreeperHost](https://minetogether.io).
