# 🧩 MekPack: Companion Mod Integration Matrix

This document provides the item-by-item integration matrix connecting all companion mods into the **Mekanism Sovereign Spine**.

---

## 1. Applied Energistics 2 (`ae2`)

AE2 is the premier digital storage and autocrafting system. In vanilla AE2, all processors, controllers, and drives are made with Certus Quartz, Fluix, and vanilla ingots. In MekPack, AE2's digital hardware requires Mekanism control circuits, steel casings, and alloys.

| AE2 Component | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Logic Processor** | Gold Ingot + Silicon + Redstone | **Basic Control Circuit** + Printed Silicon + Redstone | **Tier 1** | Anchors digital logic directly to Mekanism's basic circuit manufacturing. |
| **Calculation Processor** | Pure Certus + Silicon + Redstone | **Advanced Control Circuit** + Printed Calculation + Redstone | **Tier 2** | Gates math coprocessing behind tier 2 enrichment and alloy fabrication. |
| **Engineering Processor** | Diamond + Silicon + Redstone | **Elite Control Circuit** + Printed Engineering + Redstone | **Tier 3** | High-level engineering requires Mekanism's chemical injection tier circuits. |
| **ME Controller** | Fluix Block + Pure Certus + Sky Stone | **Steel Casing** + 4x **Advanced Control Circuits** + 2x Fluix Block + 2x **Infused Alloy** | **Tier 2** | The main network mainframe demands industrial structural casing and alloys. |
| **ME Drive** | Chest + 2x Engineering Processor + Iron | **Steel Casing** + 2x **Calculation Processors** + 4x **Steel Ingots** | **Tier 2** | Storage arrays require heavy steel chassis. |
| **Spatial IO Port & Pylon** | Fluix Glass + Eye of Ender + Iron | **Teleportation Core** + **Atomic Alloy** + Spatial Cell casing | **Tier 4** | Pocket dimension manipulation is equivalent to quantum teleportation. |
| **Dense Energy Cell** | 8x Energy Cell + Calculation Processor | 4x **Basic Energy Cubes** + **Reinforced Alloy** + Calculation Processor | **Tier 3** | Massive power storage leverages Mekanism energy cube tech. |

---

## 2. Pipez (`pipez`)

Pipez offers extreme transfer rates in a single block. Default recipes use only iron ingots and redstone, completely invalidating Mekanism logistical pipes. In MekPack, Pipez upgrades require Mekanism Control Circuits and Alloys.

| Pipez Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Item / Fluid / Energy / Gas Pipe** | 6x Iron + 2x Redstone + 1x Item | 6x **Steel Ingots** + 2x **Enriched Iron** + 1x Center Material | **Tier 1** | Requires basic industrial metallurgy rather than cheap raw iron. |
| **Basic Upgrade** | 4x Iron + 4x Iron Nuggets + 1x Redstone | 4x **Infused Alloy** + 1x **Basic Control Circuit** + 4x Steel Nuggets | **Tier 2** | Early throughput boost requires basic circuit gating. |
| **Improved Upgrade** | 4x Gold + Basic Upgrade | 4x **Reinforced Alloy** + 1x **Advanced Control Circuit** + Basic Upgrade | **Tier 3** | Medium throughput requires chemical enrichment and advanced circuits. |
| **Advanced Upgrade** | 4x Diamond + Improved Upgrade | 4x **Atomic Alloy** + 1x **Elite Control Circuit** + Improved Upgrade | **Tier 4** | High throughput demands nuclear-tier atomic alloys. |
| **Ultimate Upgrade** | 4x Netherite + Advanced Upgrade | 2x **Refined Obsidian Ingot** + 1x **Ultimate Control Circuit** + 1x **Teleportation Core** + Advanced Upgrade | **Tier 4+** | Infinite throughput requires teleportation core technology. |

---

## 3. Dimensional Storage (`dimstorage`)

DimStorage provides instant interdimensional wireless chest and tank frequency syncing.

| DimStorage Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Dim Core** | 4x Iron + 4x Redstone + 1x Diamond | 1x **Teleportation Core** + 4x **Refined Obsidian** + 4x **Advanced Control Circuit** | **Tier 3/4** | Dimensional frequency linking is a high-level quantum feat. |
| **Dim Wall** | 8x Iron + 1x Dim Core | 8x **Steel Ingots** + 1x Dim Core | **Tier 3** | Structural integrity for quantum containment fields. |
| **Dimensional Chest** | Chest + Dim Walls + Dim Core | **Personal Chest** + 4x **Reinforced Alloy** + 1x Dim Core | **Tier 3** | Merges Mekanism personal chest security with quantum frequencies. |
| **Dimensional Tank** | Glass + Dim Walls + Dim Core | **Basic Fluid Tank** + 4x **Reinforced Alloy** + 1x Dim Core | **Tier 3** | Upgrades Mekanism pressurized fluid tanks for interdimensional transfer. |

---

## 4. Entangled (`entangled`)

Entangled allows binding any block tile entity (even complex modded machines) directly to another block across any distance or dimension.

| Entangled Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Entangled Block** | 4x Ender Pearl + 4x Obsidian + Chest | 1x **Steel Casing** + 2x **Atomic Alloy** + 2x **Teleportation Cores** + 4x **Refined Obsidian** | **Tier 4** | Quantum block linking requires Mekanism teleportation cores and atomic alloys. |
| **Entangled Binder** | 4x Ender Pearl + 4x Iron + 1x Diamond | 1x **Atomic Alloy** + 1x **Teleportation Core** + 2x **Refined Glowstone Ingot** | **Tier 4** | Handheld frequency calibrator requires quantum materials. |

---

## 5. Wormhole (`wormhole`)

Wormhole provides dimensional stargates and player teleportation portals.

| Wormhole Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Portal Stabilizer** | 4x Iron + 4x Copper + 1x Eye of Ender | 1x **Steel Casing** + 2x **Teleportation Cores** + 2x **Elite Control Circuits** + 4x **Steel Plates/Ingots** | **Tier 4** | Gateway stabilization requires industrial structural casings and dual quantum cores. |
| **Portal Frame** | 8x Iron + 1x Redstone | 8x **Steel Ingots** + 1x **Infused Alloy** | **Tier 2** | High-durability structural frame. |
| **Advanced Target Device** | 4x Gold + 4x Redstone + Ender Pearl | 1x **Energy Tablet** + 1x **Advanced Control Circuit** + 2x **Refined Glowstone** | **Tier 3** | Dimensional coordinate telemetry requires Mekanism portable energy storage. |

---

## 6. ComputerCraft: Tweaked (`cc-tweaked`)

CC: Tweaked supercomputers provide automation and Lua telemetry scripting for reactors and matrix storage.

| CC: Tweaked Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Computer** | 7x Stone + 1x Redstone + 1x Glass Pane | 1x **Steel Casing** + 1x **Basic Control Circuit** + 2x **Enriched Iron** + 1x Glass Pane | **Tier 1** | Prevents crafting computers on minute 1 with cobblestone; requires basic steel fabrication. |
| **Advanced Computer** | 7x Gold + 1x Computer | 1x Standard Computer + 2x **Advanced Control Circuits** + 2x **Infused Alloy** + 4x Gold | **Tier 2** | Color displays and high clock speeds require tier 2 circuits and alloys. |
| **Pocket Computer** | 7x Gold + 1x Apple / Glass + Redstone | 1x **Energy Tablet** + 1x **Advanced Control Circuit** + 2x **Steel Ingots** | **Tier 2** | Handheld computing is battery-driven via Mekanism Energy Tablets. |
| **Turtles (Robits / Automata)** | Computer + 7x Iron + Chest | 1x Standard Computer + 1x **Robit** (or 2x **Basic Control Circuits** + 4x Steel) | **Tier 2** | Mobile robotic automation ties into Mekanism robotics. |

---

## 7. SecurityCraft (`securitycraft`)

SecurityCraft provides retinal scanners, keypads, laser grids, and unbreakable reinforced containment blocks.

| SecurityCraft Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Keypad / Retinal Scanner** | 8x Stone/Iron + Redstone | 1x **Basic/Advanced Control Circuit** + 1x **Steel Casing** + Redstone | **Tier 1/2** | High-tech biometric security requires digital control circuits. |
| **Laser Block** | 4x Iron + 4x Redstone + Glass | 1x **Laser Core / Laser** + 1x **Steel Casing** + 2x **Infused Alloy** | **Tier 2** | Integrates with Mekanism's own laser emitter optics. |
| **Reinforced Door / Safe** | 6x Iron + Redstone | 4x **Steel Ingots** + 2x **Enriched Iron** + 1x **Basic Control Circuit** | **Tier 1** | Blast-resistant industrial security structures. |

---

## 8. Moving Elevators (`movingelevators`)

Futuristic skyscraper and multi-floor facility transit.

| Moving Elevators Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Elevator Controller** | 6x Iron + 2x Redstone + 1x Piston | 1x **Steel Casing** + 1x **Basic Control Circuit** + 2x **Enriched Iron** + 1x Piston | **Tier 1** | Heavy industrial elevator hoisting requires steel framing and logic control. |
| **Elevator Display** | 8x Iron + 1x Glass Pane | 4x **Steel Ingots** + 1x **Enriched Iron** + 1x Glass Pane | **Tier 1** | Consistent sci-fi steel aesthetic. |

---

## 9. Shrink (`shrink`)

Personal quantum resizing device allowing the player to enter micro-conduits and compact base layouts.

| Shrink Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Personal Shrinking Device** | 4x Iron + 1x Ender Pearl + Glass + Button | 1x **Energy Tablet** + 1x **Teleportation Core** + 2x **Atomic Alloy** + 1x Glass | **Tier 4** | Subatomic spatial alteration is a premier tier 4 quantum breakthrough. |

---

## 10. Chunk Loaders (`chunkloaders`)

Autonomous persistent chunk loading across all planetary dimensions.

| Chunk Loader Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Single Chunk Loader** | 4x Iron + 4x Obsidian + Pearl | 1x **Steel Casing** + 1x **Basic Control Circuit** + 2x **Infused Alloy** | **Tier 1** | Local automation persistence. |
| **Basic Chunk Loader (3x3)** | Single Loader + Iron + Gold | Single Loader + 2x **Advanced Control Circuits** + 2x **Reinforced Alloy** | **Tier 2** | Factory floor chunk loading. |
| **Advanced Chunk Loader (5x5)**| Basic Loader + Diamond + Obsidian | Basic Loader + 2x **Elite Control Circuits** + 2x **Atomic Alloy** | **Tier 3** | Sprawling multi-machine industrial complex. |
| **Ultimate Chunk Loader (7x7)** | Advanced Loader + Netherite | Advanced Loader + 1x **Ultimate Control Circuit** + 1x **Teleportation Core** | **Tier 4** | Megabase and planetary telemetry coverage. |

---

## 11. Trash Cans (`trashcans`)

Automated voiding of industrial byproducts and excess materials.

| Trash Can Item | Default Recipe | MekPack Integrated Recipe | Required Tier | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Item / Liquid Trash Can** | 4x Cobblestone + 4x Iron + Lava/Chest | 1x **Steel Casing** + 4x **Steel Ingots** + Lava Bucket / Void Basin | **Tier 1** | Heavy industrial incinerator basin. |
| **Energy Trash Can** | 4x Redstone + 4x Iron + Obsidian | 1x **Basic Energy Cube** + 1x **Steel Casing** + 2x **Infused Alloy** | **Tier 2** | High-capacity electrical ground sink. |
| **Ultimate Trash Can** | Item + Liquid + Energy Trash Can | 1x Item + 1x Liquid + 1x Energy + 1x **Elite Control Circuit** | **Tier 3** | Universal automated waste disposal facility. |
