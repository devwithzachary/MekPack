# ⚡ MekPack: Future Frontiers — AI & Contributor Core Guidelines

Welcome to the **MekPack** repository. This document defines the non-negotiable architectural principles, progression rules, and coding standards for all AI sessions and human contributors working on this modpack.

---

## 🏛️ 1. The Core Philosophy: "Mekanism Sovereign Spine"

MekPack is **not** a loose kitchen-sink modpack where mods compete or allow players to skip progression.

> **THE SOVEREIGN SPINE DIRECTIVE:**  
> **Mekanism is the central, non-bypassable industrial spine of MekPack.**  
> Every external mod (Applied Energistics 2, Pipez, ComputerCraft, DimStorage, Entangled, Wormhole, SecurityCraft, Moving Elevators, Shrink, Chunk Loaders, Trash Cans) must tie directly into Mekanism progression. A player must **never** be able to use a companion mod to trivialize, circumvent, or bypass Mekanism technology tiers.

### Rules of Engagement for Mod Integration
1. **No Cheap Shortcuts**: If a companion mod offers high-utility logistics, storage, chunk loading, or automation (e.g. Pipez, DimStorage, AE2), its crafting recipes must demand proportional Mekanism materials (Alloys, Control Circuits, Steel Casings, Teleportation Cores).
2. **Synchronized Tiers**: Upgrades in companion mods must mirror Mekanism tiers:
   - Basic Tier -> Basic Control Circuit + Infused Alloy
   - Advanced Tier -> Advanced Control Circuit + Reinforced Alloy
   - Elite Tier -> Elite Control Circuit + Atomic Alloy
   - Ultimate Tier -> Ultimate Control Circuit + Teleportation Core / Antimatter
3. **Mekanism Machinery Precedence**: Processing tasks that Mekanism specializes in (ore multiplication, gas synthesis, chemical injection, nuclear physics) belong to Mekanism. Companion mods enhance interface, transport, telemetry, and base building—they do not replace Mekanism factories.

---

## 📊 2. The 6-Tier Progression Hierarchy

Any new recipe, advancement, or configuration change must be placed within one of these 6 explicit progression tiers:

| Tier | Name | Mekanism Foundation | Companion Mod Capabilities Unlocked |
| :--- | :--- | :--- | :--- |
| **Tier 0** | **Ground Zero** | Osmium prospecting, Bronze/Osmium tools, Heat Generator | Basic early-game manual tools; no automated routing or wireless storage. |
| **Tier 1** | **The Spark of Steel** | Metallurgic Infuser, Enriched Iron, Steel Casing, Basic Control Circuits, Wind Turbines | Basic Pipez, CC:Tweaked normal computers, Moving Elevators, Single/Basic Chunk Loaders. |
| **Tier 2** | **Kinetic Automation** | Enrichment Chamber, Crusher, Infused Alloy, Advanced Control Circuits, Energy Tablets | Improved Pipez upgrades, AE2 Fluix & Quartz processing, Basic AE2 Terminals & Drives (1k/4k), SecurityCraft Keypads. |
| **Tier 3** | **Chemical Digitization** | Purification Chamber, Electrolytic Separator, Reinforced Alloy, Elite Control Circuits | Advanced Pipez upgrades, AE2 ME Controller, Autocrafting (Molecular Assemblers), DimStorage dimensional chests/tanks. |
| **Tier 4** | **Nuclear Power & Relays** | Chemical Injection, Fission Reactor, Industrial Turbine, Atomic Alloy, Ultimate Control Circuits | Ultimate Pipez upgrades, AE2 Dense Cells (64k/256k), Entangled blocks/binders, Wormhole portals, Advanced Security lasers. |
| **Tier 5** | **Supercritical Frontier** | Fusion Reactor, Supercritical Phase Shifter (SPS), Antimatter Pellets, QIO Storage, MekaSuit | Shrink quantum resizing gadget, AE2 Spatial Storage, Quantum Entangloporters, Post-scarcity total automation. |

---

## 🛠️ 3. Recipe Modification Standards & Architecture

### Environment
- **Minecraft Version**: `26.3`
- **Mod Loader**: `NeoForge 26.3.0.95`
- **Tag Conventions**: Use unified Common Tags (`#c:ingots/steel`, `#c:dusts/refined_obsidian`, `#c:circuits/basic`, etc.) alongside Mekanism identifiers (`mekanism:basic_control_circuit`, `mekanism:alloy_infused`, `mekanism:steel_casing`).

### Recipe Storage & Packaging
- Custom recipes and datapack enhancements are housed in custom mod packages or global datapack directories that are automatically synced by `tools/setup_instance.py` and exported by `tools/export_pack.py`.
- Always verify recipes against existing mod namespaces (`ae2`, `pipez`, `computercraft`, `dimstorage`, `entangled`, `wormhole`, `shrink`, `chunkloaders`, `trashcans`, `movingelevators`).
- Never delete or modify vanilla or modded items destructively without providing clear JEI visibility and replacement recipes.

---

## 🏆 4. Quest Line & Progression Architecture

MekPack powers its structured sci-fi progression tree through **Better Advancements** (`BetterAdvancements-NeoForge-26.3-0.6.0.81.jar`) and **Advancement Plaques** (`AdvancementPlaques-26.3-neoforge-1.7.3.jar`), packaged into `custom_mods/MekPackContent-26.3-0.0.1.jar` by `tools/generate_advancements.py` and `tools/build_content.py`:
1. **Interactive Quest Chapters**:
   - `00_ground_zero`: Tier 0 - Ground Zero (Welcome, Osmium Prospecting, Heat Generation)
   - `01_the_spark_of_steel`: Tier 1 - The Spark of Steel (Metallurgic Infuser, Steel, Basic Circuits, Wind Turbines, Pipez, CC:Tweaked, Moving Elevators)
   - `02_kinetic_automation`: Tier 2 - Kinetic Automation (Enrichment Chamber 2x, Infused Alloy, Advanced Circuits, AE2 Controller Inception, SecurityCraft)
   - `03_chemical_digitization`: Tier 3 - Chemical Digitization (Electrolytic Separator, Purification Chamber 3x, Reinforced Alloy, Elite Circuits, Digital Miner, DimStorage)
   - `04_nuclear_power`: Tier 4 - Nuclear Power & Relays (Fission Multiblock, Industrial Turbine, Atomic Alloy, Ultimate Circuits, Entangled, Wormholes)
   - `05_supercritical_frontier`: Tier 5 - Supercritical Frontier (Fusion Reactor, SPS Multiblock, Antimatter Pellets, MekaSuit, QIO Drive Array, Shrink)
2. **Visual & Interactive Interface**: Better Advancements replaces the vanilla screen with a high-resolution, zoomable, dark sci-fi tree with custom line connections and node badges. Advancement Plaques triggers full-screen animated fanfare plaques and particles upon completing milestone quests.
3. **Branching Milestone Wings**: External companion mods branch directly off their corresponding Mekanism tier requirements.
4. **Tangible Rewards**: Quests grant meaningful tier materials (alloys, circuit kits, machine upgrades, energy tablets, radioactive waste management equipment) via custom datapack loot tables.
5. **FTB Quests Standby**: FTB Quests / Library 26.1 causes critical SDL/Wayland and GuiGraphics render pipeline crashes in Minecraft 26.3. The deterministic FTB tree generator (`tools/generate_quests.py`) remains preserved for when FTB releases an official 26.3-compatible build.

---

## 🤖 5. Mandatory Checklist for Future AI Sessions

Before completing any task in this workspace:
- [ ] **Verify Mekanism Anchor**: Does this change allow any player to bypass Mekanism? If yes, adjust recipes immediately.
- [ ] **Preserve Repository Cleanliness**: `minecraft/` is local runtime and gitignored; changes must be made in `config/`, `resourcepacks/`, `custom_mods/`, or `tools/`.
- [ ] **Check Tooling Compatibility**: Ensure changes are recognized and correctly packaged by `tools/setup_instance.py` and `tools/export_pack.py`.
- [ ] **Document Updates**: Record all modified recipes in `docs/INTEGRATION_MATRIX.md` and keep docs synchronized.
