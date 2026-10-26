# 🏆 MekPack: Custom Achievement Flow Blueprint

This blueprint outlines the custom progression tree that will guide players from **Tier 0 (Day One)** through **Endgame (Supercritical Phase Shifting & Antimatter)** with rewarding milestones along the way.

---

## 1. Visual & Audio Presentation

- **Tree Interface**: Rendered via `Better Advancements` for a smooth, full-screen, zoomable vector tech tree with customized line color accents matching Mekanism tier hues (Cyan, Red, Blue, Purple).
- **Celebration Banners**: Displayed using `Advancement Plaques` for dynamic, high-tech animated popups accompanied by subtle futuristic chimes.
- **Custom Background**: Dark carbon-fiber / quantum matrix grid backdrop (`mekpack:textures/gui/advancements/background.png`).

---

## 2. Master Progression Tree: 0 to Endgame

```mermaid
graph TD
    T0_Osmium["Tier 0: Future Prospecting<br/>Find Osmium Ore"] --> T1_Metallurgic["Tier 1: Smelting the Future<br/>Craft Metallurgic Infuser"]
    T1_Metallurgic --> T1_Steel["Tier 1: The Alloy Age<br/>Craft Steel Ingot"]
    T1_Steel --> T1_Circuit["Tier 1: Computational Logic<br/>Craft Basic Control Circuit"]
    
    %% Branch: CC Tweaked
    T1_Circuit -.-> B_CC["Branch: Telemetry Core<br/>Craft CC:Tweaked Computer"]
    %% Branch: Pipez
    T1_Circuit -.-> B_Pipez["Branch: High-Speed Conduits<br/>Craft Pipez Upgrades"]
    
    T1_Circuit --> T2_Enrichment["Tier 2: Chemical Multiplication<br/>Craft Enrichment Chamber"]
    T2_Enrichment --> T2_Infused["Tier 2: Infused Metallurgy<br/>Craft Infused Alloy & Adv. Circuit"]
    
    %% Branch: AE2
    T2_Infused -.-> B_AE2["Branch: The Digital Matrix<br/>Craft ME Controller & ME Drive"]
    
    T2_Infused --> T3_Purification["Tier 3: Gas Synthesis<br/>Electrolytic Separator & Purification"]
    T3_Purification --> T3_Reinforced["Tier 3: High-Grade Structural Tech<br/>Craft Reinforced Alloy & Elite Circuit"]
    
    %% Branch: DimStorage
    T3_Reinforced -.-> B_Dim["Branch: Dimensional Entanglement<br/>Craft DimStorage Frequency Chest"]
    
    T3_Reinforced --> T4_Fission["Tier 4: Splitting the Atom<br/>Build Industrial Fission Reactor"]
    T4_Fission --> T4_Turbine["Tier 4: Mega-Watt Generation<br/>Assemble Industrial Steam Turbine"]
    T4_Turbine --> T4_Atomic["Tier 4: Subatomic Engineering<br/>Craft Atomic Alloy & Ultimate Circuit"]
    
    %% Branch: Wormhole & Entangled
    T4_Atomic -.-> B_Wormhole["Branch: Spatial Wormholes<br/>Assemble Wormhole Portal Gate"]
    
    T4_Atomic --> T5_Fusion["Tier 5: Stellar Core<br/>Ignite Industrial Fusion Reactor"]
    T5_Fusion --> T5_SPS["Tier 5: Supercritical Reality<br/>Supercritical Phase Shifter (SPS)"]
    T5_SPS --> T5_Antimatter["Tier 5: Antimatter Synthesis<br/>Synthesize Antimatter Pellet"]
    T5_Antimatter --> T5_MekaSuit["Endgame: The Transcendent God<br/>Assemble Full MekaSuit System"]
    T5_Antimatter --> T5_QIO["Endgame: Post-Scarcity Grid<br/>Deploy QIO Quantum Frequency Storage"]
```

---

## 3. Detailed Milestones & Rewards Breakdown

### Tier 0: Ground Zero
- **`mekpack:root` (Welcome to Future Frontiers)**
  - *Task*: Enter the world.
  - *Reward*: MekPack Field Manual + 5x Torches + Canteen.
- **`mekpack:find_osmium` (The Blue Vein)**
  - *Task*: Mine Raw Osmium.
  - *Reward*: 8x Osmium Raw Ore + 50 XP.

### Tier 1: The Spark of Steel
- **`mekpack:craft_metallurgic_infuser` (The Heart of Metallurgy)**
  - *Task*: Craft the Metallurgic Infuser.
  - *Reward*: 16x Coal + 16x Redstone + 8x Enriched Iron.
- **`mekpack:craft_steel` (Tempered Ambition)**
  - *Task*: Smelt your first Steel Ingot.
  - *Reward*: 1x Steel Casing + 100 XP.
- **`mekpack:craft_basic_circuit` (Binary Inception)**
  - *Task*: Fabricate a Basic Control Circuit.
  - *Reward*: 2x Basic Control Circuits + 2x Energy Tablets.

### Tier 2: Kinetic Automation
- **`mekpack:craft_enrichment_chamber` (Molecular Multiplication)**
  - *Task*: Craft an Enrichment Chamber.
  - *Reward*: 4x Speed Upgrades + 4x Energy Upgrades.
- **`mekpack:craft_infused_alloy` (Alloy Dynamics)**
  - *Task*: Synthesize an Infused Alloy.
  - *Reward*: 4x Infused Alloys + 1x Basic Tier Installer.
- **`mekpack:ae2_inception` (Digital Genesis)**
  - *Task*: Craft an ME Controller using your Mekanism Steel Casing.
  - *Reward*: 1x ME Terminal + 2x 4k ME Storage Cells.

### Tier 3: Chemical Mastery
- **`mekpack:gas_infrastructure` (Elemental Partition)**
  - *Task*: Craft an Electrolytic Separator and store Hydrogen/Oxygen.
  - *Reward*: 1x Armored Jetpack + 1x Gas Tank.
- **`mekpack:craft_reinforced_alloy` (Reinforced Kinetics)**
  - *Task*: Synthesize a Reinforced Alloy.
  - *Reward*: 2x Advanced Tier Installers + 250 XP.
- **`mekpack:dim_frequency` (Cross-Planetary Frequency)**
  - *Task*: Bind a Dimensional Chest or Tank.
  - *Reward*: 1x Dim Core + 1x Teleportation Core.

### Tier 4: Nuclear Splendor
- **`mekpack:fission_reactor` (Chain Reaction)**
  - *Task*: Form a multiblock Fission Reactor.
  - *Reward*: Full Hazmat Suit + 16x Radioactive Waste Barrels + 500 XP.
- **`mekpack:industrial_turbine` (Megawatt Cyclone)**
  - *Task*: Assemble an Industrial Steam Turbine.
  - *Reward*: 4x Ultimate Energy Cubes + 4x Elite Tier Installers.
- **`mekpack:craft_atomic_alloy` (Atomic Harmony)**
  - *Task*: Synthesize an Atomic Alloy and Ultimate Control Circuit.
  - *Reward*: 2x Ultimate Tier Installers + 1000 XP.

### Tier 5: The Supercritical Frontier (Endgame)
- **`mekpack:stellar_fusion` (Harnessing the Sun)**
  - *Task*: Ignite a D-T Fusion Reactor with Laser Amplifiers.
  - *Reward*: 1x Quantum Entangloporter + 2000 XP.
- **`mekpack:sps_antimatter` (Beyond the Standard Model)**
  - *Task*: Form a Supercritical Phase Shifter (SPS) and produce 1x Antimatter Pellet.
  - *Reward*: 1x Antimatter Pellet + Creative Flight module base + 5000 XP.
- **`mekpack:mekasuit_god` (Transcendent Cybernetics)**
  - *Task*: Equip full MekaSuit with Laser Dissolution, Locomotion, and Solar Charging units.
  - *Reward*: Title "Cybernetic Sovereign" + Golden Star Trophy.

---

## 4. Implementation Phasing

1. **Phase 1 (Active)**: Establish modpack philosophy, developer guidelines, and the comprehensive recipe integration matrix.
2. **Phase 2 (Next)**: Implement the custom recipe overrides across `pipez`, `ae2`, `computercraft`, `dimstorage`, `entangled`, `wormhole`, `shrink`, `chunkloaders`, `trashcans`, and `movingelevators`.
3. **Phase 3**: Build and register the custom advancement datapack (`data/mekpack/advancement/...`) with Better Advancements and Advancement Plaques visual styling and custom loot tables.
