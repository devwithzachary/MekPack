#!/usr/bin/env python3
"""
MekPack FTB Quests Generator
Generates full quest hierarchy for FTB Quests (v13 schema) under config/ftbquests/quests/:
- data.json5
- chapter_groups.json5
- chapters/
  - 00_ground_zero.json5
  - 01_the_spark_of_steel.json5
  - 02_kinetic_automation.json5
  - 03_chemical_digitization.json5
  - 04_nuclear_power.json5
  - 05_supercritical_frontier.json5
- lang/en_us/
  - en_us.json5

Enforces the Mekanism Sovereign Spine architecture across all 6 tiers:
All external companion mods (AE2, Pipez, ComputerCraft, DimStorage, Entangled, Wormhole,
SecurityCraft, Moving Elevators, Shrink) branch directly off their corresponding Mekanism tier.
"""

import os
import json
import hashlib
from typing import Dict, List, Any, Optional

QUESTS_DIR = "config/ftbquests/quests"
CHAPTERS_DIR = os.path.join(QUESTS_DIR, "chapters")
LANG_DIR = os.path.join(QUESTS_DIR, "lang", "en_us")

def make_hex_id(seed: str) -> str:
    """Generate a deterministic, positive 63-bit hex ID from a unique seed string."""
    h = hashlib.sha256(seed.encode("utf-8")).digest()[:8]
    val = int.from_bytes(h, "big") & 0x7FFFFFFFFFFFFFFF
    if val < 2:
        val += 2
    return f"{val:016X}"

def write_json5(filepath: str, data: Any):
    """Write formatted JSON5 (standard JSON is fully valid JSON5)."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

def generate_quests():
    print("[INIT] Generating MekPack FTB Quests...")
    os.makedirs(CHAPTERS_DIR, exist_ok=True)
    os.makedirs(LANG_DIR, exist_ok=True)

    group_id = make_hex_id("group:sovereign_spine")
    lang_entries: Dict[str, Any] = {}

    # 1. data.json5
    data_json = {
        "version": 13,
        "default_reward_team": False,
        "default_consume_items": False,
        "default_autoclaim_rewards": "disabled",
        "default_quest_shape": "circle",
        "default_quest_disable_jei": False,
        "drop_loot_crates": False,
        "emergency_items_cooldown": 300,
        "disable_gui": False,
        "grid_scale": 0.5,
        "pause_game": False,
        "lock_message": "",
        "progression_mode": "linear",
        "detection_delay": 20,
        "show_lock_icons": True,
        "drop_book_on_death": False,
        "hide_excluded_quests": False,
        "fallback_locale": "en_us",
        "verify_on_load": True,
        "suppress_all_autoclaiming": False
    }
    write_json5(os.path.join(QUESTS_DIR, "data.json5"), data_json)

    # 2. chapter_groups.json5
    chapter_groups_json = {
        "chapter_groups": [
            {
                "id": group_id
            }
        ]
    }
    write_json5(os.path.join(QUESTS_DIR, "chapter_groups.json5"), chapter_groups_json)
    lang_entries[f"chapter_group.{group_id}.title"] = "MekPack: Sovereign Spine"

    # Chapter definitions
    chapters_meta = [
        {
            "id_seed": "chapter:00_ground_zero",
            "filename": "00_ground_zero",
            "order_index": 0,
            "title": "Tier 0: Ground Zero",
            "subtitle": "Osmium prospecting & the first thermal spark",
            "icon": "mekanism:raw_osmium"
        },
        {
            "id_seed": "chapter:01_the_spark_of_steel",
            "filename": "01_the_spark_of_steel",
            "order_index": 1,
            "title": "Tier 1: The Spark of Steel",
            "subtitle": "Metallurgic infusion, steel alloy, & early infrastructure",
            "icon": "mekanism:steel_casing"
        },
        {
            "id_seed": "chapter:02_kinetic_automation",
            "filename": "02_kinetic_automation",
            "order_index": 2,
            "title": "Tier 2: Kinetic Automation",
            "subtitle": "Enrichment, advanced circuits, & digital ME storage inception",
            "icon": "mekanism:alloy_infused"
        },
        {
            "id_seed": "chapter:03_chemical_digitization",
            "filename": "03_chemical_digitization",
            "order_index": 3,
            "title": "Tier 3: Chemical Digitization",
            "subtitle": "Electrolytic gases, 3x tri-ore refinement, & autonomic excavation",
            "icon": "mekanism:alloy_reinforced"
        },
        {
            "id_seed": "chapter:04_nuclear_power",
            "filename": "04_nuclear_power",
            "order_index": 4,
            "title": "Tier 4: Nuclear Criticality & Relays",
            "subtitle": "Fission reactors, steam turbines, wormholes, & quantum logic",
            "icon": "mekanismgenerators:fission_reactor_casing"
        },
        {
            "id_seed": "chapter:05_supercritical_frontier",
            "filename": "05_supercritical_frontier",
            "order_index": 5,
            "title": "Tier 5: Supercritical Frontier",
            "subtitle": "Fusion energy, antimatter synthesis, QIO post-scarcity, & MekaSuit",
            "icon": "mekanism:pellet_antimatter"
        }
    ]

    chapter_id_map: Dict[str, str] = {}
    for ch in chapters_meta:
        cid = make_hex_id(ch["id_seed"])
        chapter_id_map[ch["filename"]] = cid
        lang_entries[f"chapter.{cid}.title"] = ch["title"]
        lang_entries[f"chapter.{cid}.chapter_subtitle"] = ch["subtitle"]

    # 3. Quest Definitions across the 6 Chapters
    # Keys map to seed identifiers used for deterministic hex IDs.
    quest_defs = [
        # ==========================================
        # CHAPTER 0: GROUND ZERO
        # ==========================================
        {
            "key": "root",
            "chapter": "00_ground_zero",
            "title": "MekPack: Future Frontiers",
            "subtitle": "Welcome to the Sovereign Industrial Spine",
            "desc": [
                "Welcome to MekPack: Future Frontiers.",
                "",
                "Mekanism serves as the non-bypassable industrial backbone of this world. Every companion mod—from Applied Energistics 2 and Pipez to ComputerCraft and DimStorage—is synchronized with your industrial advancement.",
                "",
                "Forge your path from planetary prospecting through advanced chemical processing to supercritical reality."
            ],
            "icon": "mekanism:steel_casing",
            "shape": "hexagon",
            "size": 1.5,
            "x": -3.0,
            "y": 0.0,
            "dependencies": [],
            "tasks": [
                {
                    "type": "checkmark",
                    "title": "Initialize Sovereign Spine"
                }
            ],
            "rewards": [
                {"type": "item", "id": "minecraft:torch", "count": 16},
                {"type": "item", "id": "minecraft:bread", "count": 8},
                {"type": "item", "id": "minecraft:compass", "count": 1},
                {"type": "xp", "xp": 50}
            ]
        },
        {
            "key": "find_osmium",
            "chapter": "00_ground_zero",
            "title": "The Blue Vein",
            "subtitle": "Prospect planetary Osmium deposits",
            "desc": [
                "Osmium is the primary elemental catalyst for all Mekanism metallurgy.",
                "",
                "Venture into subterranean caverns to extract Raw Osmium. You will require steady veins of Osmium to synthesize alloys, basic casings, and structural components."
            ],
            "icon": "mekanism:raw_osmium",
            "shape": "circle",
            "size": 1.2,
            "x": 0.0,
            "y": 0.0,
            "dependencies": ["root"],
            "tasks": [
                {"type": "item", "id": "mekanism:raw_osmium", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:raw_osmium", "count": 8},
                {"type": "xp", "xp": 50}
            ]
        },
        {
            "key": "heat_generator",
            "chapter": "00_ground_zero",
            "title": "Thermal Inception",
            "subtitle": "Harness early combustible and passive heat",
            "desc": [
                "Every machine requires sustained electrical power.",
                "",
                "The Heat Generator burns combustible materials (coal, charcoal, wood) to generate Joule energy. Placing lava adjacent to the Heat Generator provides additional passive thermal output."
            ],
            "icon": "mekanismgenerators:heat_generator",
            "shape": "square",
            "size": 1.2,
            "x": 3.0,
            "y": 0.0,
            "dependencies": ["find_osmium"],
            "tasks": [
                {"type": "item", "id": "mekanismgenerators:heat_generator", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "minecraft:coal", "count": 16},
                {"type": "item", "id": "minecraft:redstone", "count": 16},
                {"type": "xp", "xp": 50}
            ]
        },

        # ==========================================
        # CHAPTER 1: THE SPARK OF STEEL
        # ==========================================
        {
            "key": "metallurgic_infuser",
            "chapter": "01_the_spark_of_steel",
            "title": "The Heart of Metallurgy",
            "subtitle": "Infuse base metals with elemental catalysts",
            "desc": [
                "The Metallurgic Infuser is the cornerstone of early industrialization.",
                "",
                "By infusing Iron with Carbon (Coal or Charcoal), you produce Enriched Iron—the mandatory precursor to forged Steel."
            ],
            "icon": "mekanism:metallurgic_infuser",
            "shape": "square",
            "size": 1.3,
            "x": -4.0,
            "y": 0.0,
            "dependencies": ["heat_generator"],
            "tasks": [
                {"type": "item", "id": "mekanism:metallurgic_infuser", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:enriched_iron", "count": 8},
                {"type": "item", "id": "minecraft:redstone", "count": 32},
                {"type": "xp", "xp": 100}
            ]
        },
        {
            "key": "steel_ingot",
            "chapter": "01_the_spark_of_steel",
            "title": "Tempered Ambition",
            "subtitle": "Forge high-strength structural Steel",
            "desc": [
                "Infuse Enriched Iron a second time with Carbon to create Steel Dust, then smelt it into Steel Ingots.",
                "",
                "Steel is required for heavy machinery frames, modular casings, and all companion mod entry-level hardware."
            ],
            "icon": "mekanism:ingot_steel",
            "shape": "circle",
            "size": 1.0,
            "x": -1.5,
            "y": 0.0,
            "dependencies": ["metallurgic_infuser"],
            "tasks": [
                {"type": "item", "id": "mekanism:ingot_steel", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:ingot_steel", "count": 8},
                {"type": "item", "id": "mekanism:steel_casing", "count": 1},
                {"type": "xp", "xp": 100}
            ]
        },
        {
            "key": "basic_control_circuit",
            "chapter": "01_the_spark_of_steel",
            "title": "Computational Logic",
            "subtitle": "Synthesize the Basic Control Circuit",
            "desc": [
                "By infusing Osmium Ingots with Redstone, you craft the Basic Control Circuit.",
                "",
                "This circuit represents the computational foundation of Tier 1. It unlocks kinetic machinery, automation conduits, computers, and vertical transit."
            ],
            "icon": "mekanism:basic_control_circuit",
            "shape": "square",
            "size": 1.3,
            "x": 1.0,
            "y": 0.0,
            "dependencies": ["steel_ingot"],
            "tasks": [
                {"type": "item", "id": "mekanism:basic_control_circuit", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:basic_control_circuit", "count": 2},
                {"type": "item", "id": "mekanism:energy_tablet", "count": 2},
                {"type": "xp", "xp": 150}
            ]
        },
        {
            "key": "wind_generator",
            "chapter": "01_the_spark_of_steel",
            "title": "High-Altitude Kinetic Harvest",
            "subtitle": "Sustainable atmospheric wind power",
            "desc": [
                "Tired of feeding coal to your generators?",
                "",
                "The Wind Generator harnesses atmospheric flow. Deploy it at high altitudes for significantly multiplied power production."
            ],
            "icon": "mekanismgenerators:wind_generator",
            "shape": "circle",
            "size": 1.1,
            "x": 4.0,
            "y": 0.0,
            "dependencies": ["basic_control_circuit"],
            "tasks": [
                {"type": "item", "id": "mekanismgenerators:wind_generator", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:basic_energy_cube", "count": 1},
                {"type": "xp", "xp": 150}
            ]
        },
        {
            "key": "branch_pipez",
            "chapter": "01_the_spark_of_steel",
            "title": "High-Throughput Conduits",
            "subtitle": "Steel-reinforced logistical routing",
            "desc": [
                "Companion Integration: Pipez",
                "",
                "Construct Pipez conduits using Steel Casings and Basic Control Circuits. Automated item, fluid, and energy transport connects your industrial machinery."
            ],
            "icon": "pipez:item_pipe",
            "shape": "circle",
            "size": 1.0,
            "x": 1.0,
            "y": -2.5,
            "dependencies": ["basic_control_circuit"],
            "tasks": [
                {"type": "item", "id": "pipez:item_pipe", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "pipez:energy_pipe", "count": 16},
                {"type": "item", "id": "pipez:wrench", "count": 1},
                {"type": "xp", "xp": 100}
            ]
        },
        {
            "key": "branch_cc_tweaked",
            "chapter": "01_the_spark_of_steel",
            "title": "Telemetry Core",
            "subtitle": "Programmable logic and industrial automation",
            "desc": [
                "Companion Integration: CC: Tweaked",
                "",
                "Assemble a ComputerCraft computer mainframe driven by Steel and Control Circuits. Monitor energy levels, reactor telemetry, and automated factories via Lua scripts."
            ],
            "icon": "computercraft:computer_normal",
            "shape": "circle",
            "size": 1.0,
            "x": 1.0,
            "y": 2.5,
            "dependencies": ["basic_control_circuit"],
            "tasks": [
                {"type": "item", "id": "computercraft:computer_normal", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "computercraft:cable", "count": 16},
                {"type": "xp", "xp": 100}
            ]
        },
        {
            "key": "branch_moving_elevators",
            "chapter": "01_the_spark_of_steel",
            "title": "Vertical Transit",
            "subtitle": "Multi-floor elevator elevators for complex compounds",
            "desc": [
                "Companion Integration: Moving Elevators",
                "",
                "Construct Elevator Controllers to build multi-floor freight and personnel elevators throughout your vertical bases."
            ],
            "icon": "movingelevators:elevator_block",
            "shape": "circle",
            "size": 1.0,
            "x": 3.0,
            "y": 2.5,
            "dependencies": ["basic_control_circuit"],
            "tasks": [
                {"type": "item", "id": "movingelevators:elevator_block", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "movingelevators:display_block", "count": 2},
                {"type": "item", "id": "movingelevators:button_block", "count": 2},
                {"type": "xp", "xp": 100}
            ]
        },

        # ==========================================
        # CHAPTER 2: KINETIC AUTOMATION
        # ==========================================
        {
            "key": "enrichment_chamber",
            "chapter": "02_kinetic_automation",
            "title": "Molecular Multiplication (2x)",
            "subtitle": "Double planetary ore yields & refine catalysts",
            "desc": [
                "The Enrichment Chamber achieves 2x ore multiplication by molecular compression.",
                "",
                "It also enriches redstone, coal, and diamond into ultra-dense compressed forms, multiplying infuser efficiency eightfold."
            ],
            "icon": "mekanism:enrichment_chamber",
            "shape": "square",
            "size": 1.3,
            "x": -3.0,
            "y": 0.0,
            "dependencies": ["basic_control_circuit"],
            "tasks": [
                {"type": "item", "id": "mekanism:enrichment_chamber", "count": 1}
            ],
            "rewards": [
                {
                    "type": "item",
                    "id": "mekanism:upgrade",
                    "count": 4,
                    "components": {"mekanism:upgrade_type": "mekanism:speed"}
                },
                {
                    "type": "item",
                    "id": "mekanism:upgrade",
                    "count": 4,
                    "components": {"mekanism:upgrade_type": "mekanism:energy"}
                },
                {"type": "xp", "xp": 200}
            ]
        },
        {
            "key": "infused_alloy",
            "chapter": "02_kinetic_automation",
            "title": "Alloy Dynamics",
            "subtitle": "Infuse Iron with enriched Redstone",
            "desc": [
                "Infusing Iron with Redstone in the Metallurgic Infuser synthesizes Infused Alloy.",
                "",
                "This intermediate alloy is required for machine upgrades, Tier Installers, and Advanced Control Circuits."
            ],
            "icon": "mekanism:alloy_infused",
            "shape": "circle",
            "size": 1.1,
            "x": 0.0,
            "y": 0.0,
            "dependencies": ["enrichment_chamber"],
            "tasks": [
                {"type": "item", "id": "mekanism:alloy_infused", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:alloy_infused", "count": 4},
                {"type": "item", "id": "mekanism:basic_tier_installer", "count": 1},
                {"type": "xp", "xp": 200}
            ]
        },
        {
            "key": "advanced_control_circuit",
            "chapter": "02_kinetic_automation",
            "title": "Advanced Silicon Architecture",
            "subtitle": "Upgrade basic logic with Infused Alloys",
            "desc": [
                "By infusing Basic Control Circuits with Infused Alloys, you advance to Tier 2 computational architecture.",
                "",
                "Advanced Control Circuits unlock high-capacity Energy Cubes, digital storage controllers, and secure biometric facilities."
            ],
            "icon": "mekanism:advanced_control_circuit",
            "shape": "square",
            "size": 1.3,
            "x": 3.0,
            "y": 0.0,
            "dependencies": ["infused_alloy"],
            "tasks": [
                {"type": "item", "id": "mekanism:advanced_control_circuit", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:advanced_control_circuit", "count": 2},
                {"type": "item", "id": "mekanism:advanced_tier_installer", "count": 1},
                {"type": "xp", "xp": 250}
            ]
        },
        {
            "key": "branch_ae2_controller",
            "chapter": "02_kinetic_automation",
            "title": "The Digital Matrix",
            "subtitle": "Construct the ME Controller Mainframe",
            "desc": [
                "Companion Integration: Applied Energistics 2",
                "",
                "Under the Sovereign Spine directive, AE2 mainframes require Steel Casings and Advanced Control Circuits.",
                "",
                "Assemble the ME Controller to digitize matter into crystalline energy storage grids."
            ],
            "icon": "ae2:controller",
            "shape": "square",
            "size": 1.2,
            "x": 3.0,
            "y": -2.5,
            "dependencies": ["advanced_control_circuit"],
            "tasks": [
                {"type": "item", "id": "ae2:controller", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "ae2:drive", "count": 1},
                {"type": "item", "id": "ae2:terminal", "count": 1},
                {"type": "item", "id": "ae2:item_storage_cell_4k", "count": 2},
                {"type": "xp", "xp": 250}
            ]
        },
        {
            "key": "branch_securitycraft",
            "chapter": "02_kinetic_automation",
            "title": "Biometric Security",
            "subtitle": "Fortify your base with keypads and reinforced locks",
            "desc": [
                "Companion Integration: SecurityCraft",
                "",
                "Construct Keypads, Retinal Scanners, and Indestructible Iron Doors using Advanced Control Circuits to secure your compound against intrusion."
            ],
            "icon": "securitycraft:keypad_item",
            "shape": "circle",
            "size": 1.0,
            "x": 3.0,
            "y": 2.5,
            "dependencies": ["advanced_control_circuit"],
            "tasks": [
                {"type": "item", "id": "securitycraft:keypad_item", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "securitycraft:retinal_scanner", "count": 1},
                {"type": "item", "id": "securitycraft:door_indestructible_iron_item", "count": 1},
                {"type": "xp", "xp": 150}
            ]
        },

        # ==========================================
        # CHAPTER 3: CHEMICAL DIGITIZATION
        # ==========================================
        {
            "key": "electrolytic_separator",
            "chapter": "03_chemical_digitization",
            "title": "Elemental Partition",
            "subtitle": "Electrolyze water into pressurized Hydrogen and Oxygen",
            "desc": [
                "The Electrolytic Separator dissociates water molecules into pure Hydrogen and Oxygen gas.",
                "",
                "Oxygen fuels advanced tri-ore chemical purification, while Hydrogen powers jetpacks and advanced chemical injection synthesis."
            ],
            "icon": "mekanism:electrolytic_separator",
            "shape": "circle",
            "size": 1.1,
            "x": -5.0,
            "y": 0.0,
            "dependencies": ["advanced_control_circuit"],
            "tasks": [
                {"type": "item", "id": "mekanism:electrolytic_separator", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:basic_chemical_tank", "count": 1},
                {"type": "item", "id": "mekanism:jetpack_armored", "count": 1},
                {"type": "xp", "xp": 250}
            ]
        },
        {
            "key": "purification_chamber",
            "chapter": "03_chemical_digitization",
            "title": "Tri-Ore Refining (3x)",
            "subtitle": "Oxygen-injected ore multiplication",
            "desc": [
                "Inject pressurized Oxygen into Raw Ores within the Purification Chamber to achieve 3x tri-chemical yield multiplication.",
                "",
                "This marks your transition into heavy chemical engineering."
            ],
            "icon": "mekanism:purification_chamber",
            "shape": "square",
            "size": 1.3,
            "x": -2.5,
            "y": 0.0,
            "dependencies": ["electrolytic_separator"],
            "tasks": [
                {"type": "item", "id": "mekanism:purification_chamber", "count": 1}
            ],
            "rewards": [
                {
                    "type": "item",
                    "id": "mekanism:upgrade",
                    "count": 4,
                    "components": {"mekanism:upgrade_type": "mekanism:speed"}
                },
                {
                    "type": "item",
                    "id": "mekanism:upgrade",
                    "count": 4,
                    "components": {"mekanism:upgrade_type": "mekanism:chemical"}
                },
                {"type": "xp", "xp": 300}
            ]
        },
        {
            "key": "reinforced_alloy",
            "chapter": "03_chemical_digitization",
            "title": "Reinforced Kinetics",
            "subtitle": "Infuse alloys with pulverized Diamond",
            "desc": [
                "Infusing Infused Alloy with Diamond dust produces ultra-dense Reinforced Alloy.",
                "",
                "Reinforced Alloys withstand the intense chemical stress of elite manufacturing and Tier 3 installations."
            ],
            "icon": "mekanism:alloy_reinforced",
            "shape": "circle",
            "size": 1.1,
            "x": 0.0,
            "y": 0.0,
            "dependencies": ["purification_chamber"],
            "tasks": [
                {"type": "item", "id": "mekanism:alloy_reinforced", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:alloy_reinforced", "count": 4},
                {"type": "item", "id": "mekanism:advanced_tier_installer", "count": 2},
                {"type": "xp", "xp": 300}
            ]
        },
        {
            "key": "elite_control_circuit",
            "chapter": "03_chemical_digitization",
            "title": "Quantum Computation Matrix",
            "subtitle": "Fabricate Elite Control Circuits",
            "desc": [
                "Combining Advanced Circuits with Reinforced Alloys yields the Elite Control Circuit.",
                "",
                "This computational milestone unlocks cross-dimensional logistics, the Digital Miner, and early nuclear infrastructure."
            ],
            "icon": "mekanism:elite_control_circuit",
            "shape": "square",
            "size": 1.3,
            "x": 2.5,
            "y": 0.0,
            "dependencies": ["reinforced_alloy"],
            "tasks": [
                {"type": "item", "id": "mekanism:elite_control_circuit", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:elite_control_circuit", "count": 2},
                {"type": "item", "id": "mekanism:elite_tier_installer", "count": 1},
                {"type": "xp", "xp": 350}
            ]
        },
        {
            "key": "digital_miner",
            "chapter": "03_chemical_digitization",
            "title": "Autonomic Planetary Excavation",
            "subtitle": "Precision underground digital quarrying",
            "desc": [
                "The Digital Miner revolutionizes resource gathering.",
                "",
                "Using teleportation beam matrices and tag-filtered quarry logic, it selectively mines valuable ores underground without leaving catastrophic craters."
            ],
            "icon": "mekanism:digital_miner",
            "shape": "square",
            "size": 1.4,
            "x": 5.0,
            "y": 0.0,
            "dependencies": ["elite_control_circuit"],
            "tasks": [
                {"type": "item", "id": "mekanism:digital_miner", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:basic_energy_cube", "count": 1},
                {"type": "item", "id": "mekanism:teleportation_core", "count": 1},
                {"type": "xp", "xp": 400}
            ]
        },
        {
            "key": "branch_dimstorage",
            "chapter": "03_chemical_digitization",
            "title": "Cross-Planetary Frequency",
            "subtitle": "Infinite-range frequency synchronized storage",
            "desc": [
                "Companion Integration: DimStorage",
                "",
                "Construct Dimensional Chests and Tanks using Elite Control Circuits and Teleportation Cores.",
                "",
                "Transmit items and fluids across infinite dimensions on synchronized frequency color channels."
            ],
            "icon": "dimstorage:dimensional_chest",
            "shape": "circle",
            "size": 1.1,
            "x": 2.5,
            "y": -2.5,
            "dependencies": ["elite_control_circuit"],
            "tasks": [
                {"type": "item", "id": "dimstorage:dimensional_chest", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "dimstorage:dim_core", "count": 1},
                {"type": "item", "id": "dimstorage:dim_wall", "count": 4},
                {"type": "xp", "xp": 250}
            ]
        },

        # ==========================================
        # CHAPTER 4: NUCLEAR POWER & RELAYS
        # ==========================================
        {
            "key": "fission_reactor",
            "chapter": "04_nuclear_power",
            "title": "Splitting the Atom",
            "subtitle": "Multiblock Fission Reactor criticality",
            "desc": [
                "Construct the multiblock Fission Reactor to induce nuclear fission.",
                "",
                "WARNING: Nuclear operations generate intense ionizing radiation and toxic Nuclear Waste. Wear a full Hazmat Suit and store waste strictly in Radioactive Waste Barrels."
            ],
            "icon": "mekanismgenerators:fission_reactor_casing",
            "shape": "square",
            "size": 1.3,
            "x": -4.5,
            "y": 0.0,
            "dependencies": ["digital_miner"],
            "tasks": [
                {"type": "item", "id": "mekanismgenerators:fission_reactor_casing", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:hazmat_mask", "count": 1},
                {"type": "item", "id": "mekanism:hazmat_gown", "count": 1},
                {"type": "item", "id": "mekanism:hazmat_pants", "count": 1},
                {"type": "item", "id": "mekanism:hazmat_boots", "count": 1},
                {"type": "item", "id": "mekanism:radioactive_waste_barrel", "count": 16},
                {"type": "xp", "xp": 500}
            ]
        },
        {
            "key": "industrial_turbine",
            "chapter": "04_nuclear_power",
            "title": "Megawatt Cyclone",
            "subtitle": "Colossal kinetic steam condensation",
            "desc": [
                "Route superheated steam from your Fission Reactor into an Industrial Turbine multiblock.",
                "",
                "The turbine converts thermal energy into millions of Joules while condensing steam back into recirculating reactor water."
            ],
            "icon": "mekanismgenerators:turbine_casing",
            "shape": "square",
            "size": 1.3,
            "x": -1.5,
            "y": 0.0,
            "dependencies": ["fission_reactor"],
            "tasks": [
                {"type": "item", "id": "mekanismgenerators:turbine_casing", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:ultimate_energy_cube", "count": 1},
                {"type": "item", "id": "mekanism:elite_tier_installer", "count": 2},
                {"type": "xp", "xp": 600}
            ]
        },
        {
            "key": "atomic_alloy",
            "chapter": "04_nuclear_power",
            "title": "Subatomic Engineering",
            "subtitle": "Infuse alloys with Refined Obsidian dust",
            "desc": [
                "Infusing Reinforced Alloy with Refined Obsidian dust in the Metallurgic Infuser yields Atomic Alloy.",
                "",
                "Atomic Alloy is the pinnacle of physical metallurgy, required for the Ultimate Control Circuit and relativistic endgame engineering."
            ],
            "icon": "mekanism:alloy_atomic",
            "shape": "circle",
            "size": 1.2,
            "x": 1.5,
            "y": 0.0,
            "dependencies": ["industrial_turbine"],
            "tasks": [
                {"type": "item", "id": "mekanism:alloy_atomic", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:alloy_atomic", "count": 4},
                {"type": "item", "id": "mekanism:ultimate_tier_installer", "count": 2},
                {"type": "xp", "xp": 700}
            ]
        },
        {
            "key": "ultimate_control_circuit",
            "chapter": "04_nuclear_power",
            "title": "Transcendent Logic Core",
            "subtitle": "Apex computational technology",
            "desc": [
                "Combining Elite Control Circuits with Atomic Alloys fabricates the Ultimate Control Circuit.",
                "",
                "This apex processor drives spatial entanglement, wormhole portal gateways, and D-T fusion reactors."
            ],
            "icon": "mekanism:ultimate_control_circuit",
            "shape": "square",
            "size": 1.4,
            "x": 4.5,
            "y": 0.0,
            "dependencies": ["atomic_alloy"],
            "tasks": [
                {"type": "item", "id": "mekanism:ultimate_control_circuit", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:ultimate_control_circuit", "count": 2},
                {"type": "item", "id": "mekanism:teleportation_core", "count": 1},
                {"type": "xp", "xp": 800}
            ]
        },
        {
            "key": "branch_entangled",
            "chapter": "04_nuclear_power",
            "title": "Spatial Entanglement",
            "subtitle": "Quantum pairing between containers and machines",
            "desc": [
                "Companion Integration: Entangled",
                "",
                "Craft Entangled Blocks and Binders using Atomic Alloys and Ultimate Circuits.",
                "",
                "Bind machines or inventories across reality so they share the exact same physical and digital space."
            ],
            "icon": "entangled:block",
            "shape": "circle",
            "size": 1.1,
            "x": 4.5,
            "y": -2.5,
            "dependencies": ["ultimate_control_circuit"],
            "tasks": [
                {"type": "item", "id": "entangled:block", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "entangled:item", "count": 1},
                {"type": "item", "id": "mekanism:alloy_atomic", "count": 4},
                {"type": "xp", "xp": 500}
            ]
        },
        {
            "key": "branch_wormhole",
            "chapter": "04_nuclear_power",
            "title": "Stargate Gateway",
            "subtitle": "Interdimensional personnel stargates",
            "desc": [
                "Companion Integration: Wormhole",
                "",
                "Construct Portal Stabilizers and Target Devices powered by Ultimate Control Circuits.",
                "",
                "Establish permanent, instantaneous wormhole gates across distant outposts and dimensions."
            ],
            "icon": "wormhole:portal_stabilizer",
            "shape": "circle",
            "size": 1.1,
            "x": 4.5,
            "y": 2.5,
            "dependencies": ["ultimate_control_circuit"],
            "tasks": [
                {"type": "item", "id": "wormhole:portal_stabilizer", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "wormhole:portal_frame", "count": 4},
                {"type": "item", "id": "wormhole:advanced_target_device", "count": 1},
                {"type": "xp", "xp": 500}
            ]
        },

        # ==========================================
        # CHAPTER 5: SUPERCRITICAL FRONTIER
        # ==========================================
        {
            "key": "fusion_reactor",
            "chapter": "05_supercritical_frontier",
            "title": "Harnessing the Sun",
            "subtitle": "Ignite sustained D-T thermonuclear fusion",
            "desc": [
                "Assemble the Fusion Reactor multiblock and inject deuterium-tritium fuel.",
                "",
                "Ignite the core using a focused gigajoule pulse from Laser Amplifiers to achieve sustained stellar fusion and near-infinite power generation."
            ],
            "icon": "mekanismgenerators:fusion_reactor_controller",
            "shape": "gear",
            "size": 1.4,
            "x": -4.0,
            "y": 0.0,
            "dependencies": ["ultimate_control_circuit"],
            "tasks": [
                {"type": "item", "id": "mekanismgenerators:fusion_reactor_controller", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:quantum_entangloporter", "count": 1},
                {"type": "xp", "xp": 1500}
            ]
        },
        {
            "key": "sps_multiblock",
            "chapter": "05_supercritical_frontier",
            "title": "Supercritical Phase Shifter",
            "subtitle": "Relativistic matter particle accelerator",
            "desc": [
                "Construct the massive Supercritical Phase Shifter (SPS) multiblock accelerator.",
                "",
                "Supercharge the ring with Supercharged Coils and relativistic energy to polarize nuclear waste into supercritical gas."
            ],
            "icon": "mekanism:sps_casing",
            "shape": "square",
            "size": 1.3,
            "x": -1.0,
            "y": 0.0,
            "dependencies": ["fusion_reactor"],
            "tasks": [
                {"type": "item", "id": "mekanism:sps_casing", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:supercharged_coil", "count": 4},
                {"type": "xp", "xp": 2000}
            ]
        },
        {
            "key": "antimatter_pellet",
            "chapter": "05_supercritical_frontier",
            "title": "Beyond the Standard Model",
            "subtitle": "Synthesize relativistic Antimatter Pellets",
            "desc": [
                "Crystallize supercritical antimatter gas into stable Antimatter Pellets.",
                "",
                "Antimatter represents the absolute pinnacle of technological achievement, unlocking post-scarcity QIO storage, cybernetic MekaSuits, and quantum dimensional manipulation."
            ],
            "icon": "mekanism:pellet_antimatter",
            "shape": "gear",
            "size": 1.5,
            "x": 2.0,
            "y": 0.0,
            "dependencies": ["sps_multiblock"],
            "tasks": [
                {"type": "item", "id": "mekanism:pellet_antimatter", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:pellet_antimatter", "count": 1},
                {"type": "xp", "xp": 5000}
            ]
        },
        {
            "key": "mekasuit",
            "chapter": "05_supercritical_frontier",
            "title": "Cybernetic Sovereign",
            "subtitle": "The ultimate modular powered exosuit",
            "desc": [
                "Construct the MekaSuit body armor forged from HD enhanced plates, antimatter, and ultimate circuits.",
                "",
                "Install modules like the Gravitational Modulating Unit to gain creative flight, absolute environmental immunity, and God-tier mobility."
            ],
            "icon": "mekanism:mekasuit_bodyarmor",
            "shape": "gear",
            "size": 1.4,
            "x": 5.0,
            "y": -1.8,
            "dependencies": ["antimatter_pellet"],
            "tasks": [
                {"type": "item", "id": "mekanism:mekasuit_bodyarmor", "count": 1}
            ],
            "rewards": [
                {
                    "type": "item",
                    "id": "mekanism:module",
                    "count": 1,
                    "components": {
                        "mekanism:module_type": "mekanism:gravitational_modulating_unit",
                        "minecraft:rarity": "epic"
                    }
                },
                {"type": "xp", "xp": 5000}
            ]
        },
        {
            "key": "qio_drive",
            "chapter": "05_supercritical_frontier",
            "title": "Post-Scarcity Quantum Grid",
            "subtitle": "Store billions of items on quantum frequencies",
            "desc": [
                "Deploy the QIO Drive Array and Supermassive Storage Drives.",
                "",
                "Quantum frequency storage transcends physical drives, providing limitless capacity, instantaneous cross-dimensional access, and seamless dashboard telemetry."
            ],
            "icon": "mekanism:qio_drive_array",
            "shape": "gear",
            "size": 1.4,
            "x": 5.0,
            "y": 1.8,
            "dependencies": ["antimatter_pellet"],
            "tasks": [
                {"type": "item", "id": "mekanism:qio_drive_array", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:qio_drive_supermassive", "count": 1},
                {"type": "xp", "xp": 5000}
            ]
        },
        {
            "key": "branch_shrink",
            "chapter": "05_supercritical_frontier",
            "title": "Subatomic Dimension",
            "subtitle": "Personal subatomic quantum resizing",
            "desc": [
                "Companion Integration: Shrink",
                "",
                "Under the Sovereign Spine directive, personal resizing technology demands Antimatter Pellets and Ultimate Circuits.",
                "",
                "Compress your avatar to subatomic scale to explore compact circuitry or expand for titan stature."
            ],
            "icon": "shrink:shrinking_device",
            "shape": "diamond",
            "size": 1.2,
            "x": 2.0,
            "y": -2.5,
            "dependencies": ["antimatter_pellet"],
            "tasks": [
                {"type": "item", "id": "shrink:shrinking_device", "count": 1}
            ],
            "rewards": [
                {"type": "item", "id": "mekanism:pellet_antimatter", "count": 2},
                {"type": "xp", "xp": 2500}
            ]
        }
    ]

    # Pre-map all quest keys to their hex IDs
    quest_id_map: Dict[str, str] = {q["key"]: make_hex_id(f"quest:{q['key']}") for q in quest_defs}

    # Group quests by chapter
    chapter_quests: Dict[str, List[Dict[str, Any]]] = {ch["filename"]: [] for ch in chapters_meta}

    for q in quest_defs:
        qid = quest_id_map[q["key"]]
        dep_hex_list = [quest_id_map[d] for d in q["dependencies"] if d in quest_id_map]

        # Register localization keys
        lang_entries[f"quest.{qid}.title"] = q["title"]
        lang_entries[f"quest.{qid}.quest_subtitle"] = q["subtitle"]
        lang_entries[f"quest.{qid}.quest_desc"] = q["desc"]

        # Tasks
        task_list = []
        for idx, t in enumerate(q["tasks"]):
            tid = make_hex_id(f"task:{q['key']}:{idx}")
            if t["type"] == "checkmark":
                task_list.append({
                    "id": tid,
                    "type": "checkmark",
                    "title": t.get("title", "Checkmark")
                })
            elif t["type"] == "item":
                item_obj: Dict[str, Any] = {"id": t["id"]}
                task_entry: Dict[str, Any] = {
                    "id": tid,
                    "type": "item",
                    "item": item_obj
                }
                if t.get("count", 1) > 1:
                    task_entry["count"] = t["count"]
                task_list.append(task_entry)

        # Rewards
        reward_list = []
        for idx, r in enumerate(q["rewards"]):
            rid = make_hex_id(f"reward:{q['key']}:{idx}")
            if r["type"] == "item":
                item_obj = {"id": r["id"]}
                if "components" in r:
                    item_obj["components"] = r["components"]
                reward_entry: Dict[str, Any] = {
                    "id": rid,
                    "type": "item",
                    "item": item_obj
                }
                if r.get("count", 1) > 1:
                    reward_entry["count"] = r["count"]
                reward_list.append(reward_entry)
            elif r["type"] == "xp":
                reward_list.append({
                    "id": rid,
                    "type": "xp",
                    "xp": r["xp"]
                })

        quest_json: Dict[str, Any] = {
            "id": qid,
            "x": float(q["x"]),
            "y": float(q["y"]),
            "shape": q.get("shape", "circle"),
            "size": float(q.get("size", 1.0)),
            "tasks": task_list,
            "rewards": reward_list
        }
        if dep_hex_list:
            quest_json["dependencies"] = dep_hex_list

        chapter_quests[q["chapter"]].append(quest_json)

    # Write each chapter file
    for ch in chapters_meta:
        fname = ch["filename"]
        cid = chapter_id_map[fname]
        chapter_json = {
            "id": cid,
            "group": group_id,
            "order_index": ch["order_index"],
            "filename": fname,
            "icon": {
                "id": ch["icon"]
            },
            "default_quest_shape": "",
            "quests": chapter_quests[fname]
        }
        write_json5(os.path.join(CHAPTERS_DIR, f"{fname}.json5"), chapter_json)
        print(f"[CHAPTER] Wrote {fname}.json5 ({len(chapter_quests[fname])} quests)")

    # 4. Write lang/en_us/en_us.json5
    write_json5(os.path.join(LANG_DIR, "en_us.json5"), lang_entries)
    print(f"[LANG] Wrote {len(lang_entries)} translation strings to lang/en_us/en_us.json5")

    print(f"[SUCCESS] FTB Quests generation complete! Total quests: {len(quest_defs)}")

if __name__ == "__main__":
    generate_quests()
