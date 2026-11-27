#!/usr/bin/env python3
"""
MekPack Theseus Quests Generator
Generates the 6-tier Mekanism Sovereign Spine quest tree in Heracles/Theseus JSON format
under config/theseus/:
- groups.txt
- group_settings.json
- quests/<chapter_dir>/<quest_id>.json
"""

import os
import json

THESEUS_DIR = "config/theseus"
QUESTS_DIR = os.path.join(THESEUS_DIR, "quests")

GROUPS = [
    ("Tier 0: Ground Zero", "tier0_ground_zero", "mekanism:raw_osmium"),
    ("Tier 1: The Spark of Steel", "tier1_spark_of_steel", "mekanism:metallurgic_infuser"),
    ("Tier 2: Kinetic Automation", "tier2_kinetic_automation", "mekanism:enrichment_chamber"),
    ("Tier 3: Chemical Digitization", "tier3_chemical_digitization", "mekanism:purification_chamber"),
    ("Tier 4: Nuclear Power & Relays", "tier4_nuclear_power", "mekanismgenerators:fission_reactor_casing"),
    ("Tier 5: Supercritical Frontier", "tier5_supercritical_frontier", "mekanism:pellet_antimatter"),
]

BG_DEFAULT = "theseus:textures/gui/quest_backgrounds/default.png"
BG_HEX = "theseus:textures/gui/quest_backgrounds/hexagons.png"
BG_GEAR = "theseus:textures/gui/quest_backgrounds/gears.png"
BG_DIAMOND = "theseus:textures/gui/quest_backgrounds/diamonds.png"
BG_OCTAGON = "theseus:textures/gui/quest_backgrounds/octagons.png"


def make_quest(
    quest_id,
    chapter_dir,
    group_name,
    pos,
    title,
    subtitle,
    description,
    icon,
    tasks,
    rewards=None,
    dependencies=None,
    bg=BG_DEFAULT,
    unlock_toast=False,
):
    data = {
        "display": {
            "icon": {"type": "theseus:item", "item": icon},
            "icon_background": bg,
            "title": title,
            "subtitle": subtitle,
            "description": description if isinstance(description, list) else [description],
            "groups": {group_name: {"position": list(pos)}},
        },
        "tasks": tasks,
        "rewards": rewards or {},
    }
    if dependencies:
        data["dependencies"] = dependencies
    if unlock_toast:
        data["settings"] = {"unlockNotification": True}

    out_dir = os.path.join(QUESTS_DIR, chapter_dir)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{quest_id}.json"), "w") as f:
        json.dump(data, f, indent=2)


def item_task(key, title, item_id, amount=1):
    return {
        key: {
            "type": "theseus:item",
            "title": title,
            "icon": {"type": "theseus:item", "item": item_id},
            "item": item_id,
            "amount": amount,
            "collection": "automatic",
        }
    }


def item_rewards(items, xp=0):
    rewards = {}
    for idx, entry in enumerate(items):
        item_id, count = entry[0], entry[1]
        r = {
            "type": "theseus:item",
            "title": f"{count}x {item_id.split(':')[-1].replace('_', ' ').title()}",
            "item": {"id": item_id, "count": count},
        }
        if len(entry) > 2 and entry[2]:
            r["item"]["components"] = entry[2]
        rewards[f"item_{idx}"] = r
    if xp > 0:
        rewards["xp"] = {
            "type": "theseus:xp",
            "title": f"{xp} XP",
            "xptype": "points",
            "amount": xp,
        }
    return rewards


def generate_all():
    os.makedirs(QUESTS_DIR, exist_ok=True)

    # 1. groups.txt
    with open(os.path.join(THESEUS_DIR, "groups.txt"), "w") as f:
        f.write("\n".join(g[0] for g in GROUPS) + "\n")

    # 2. group_settings.json
    settings = {}
    for name, _, icon in GROUPS:
        settings[name] = {
            "icon": icon,
            "iconEnabled": True,
            "background": "",
            "backgroundOpacity": 100,
        }
    with open(os.path.join(THESEUS_DIR, "group_settings.json"), "w") as f:
        json.dump(settings, f, indent=2)

    # ---------------- TIER 0: GROUND ZERO ----------------
    g0, d0, _ = GROUPS[0]
    make_quest(
        "welcome", d0, g0, (0, 0),
        "MekPack: Future Frontiers",
        "Tier 0 — The Sovereign Industrial Spine",
        [
            "Welcome to MekPack. Mekanism is the central, non-bypassable industrial spine of this world.",
            "Every companion mod (AE2, Pipez, CC:Tweaked, DimStorage, Entangled, Shrink) is tied to Mekanism progression.",
            "Click the checkmark below to claim your starter supplies and begin prospecting."
        ],
        "mekanism:steel_casing",
        {"ready": {"type": "theseus:check", "title": "Acknowledge Briefing", "icon": {"type": "theseus:item", "item": "mekanism:steel_casing"}}},
        item_rewards([("minecraft:torch", 16), ("minecraft:bread", 8), ("minecraft:compass", 1)], xp=50),
        bg=BG_HEX,
    )
    make_quest(
        "find_osmium", d0, g0, (150, 0),
        "The Blue Vein",
        "Tier 0 — Osmium Prospecting",
        "Prospect underground deposits and mine Raw Osmium—the lifeblood of Mekanism metallurgy.",
        "mekanism:raw_osmium",
        item_task("osmium", "Mine Raw Osmium", "mekanism:raw_osmium", 8),
        item_rewards([("mekanism:raw_osmium", 8)], xp=50),
        dependencies=["welcome"],
    )
    make_quest(
        "heat_generator", d0, g0, (300, 0),
        "Thermal Inception",
        "Tier 0 — First Power",
        "Construct a Heat Generator to produce your first Forge Energy (FE) from fuel or adjacent lava.",
        "mekanismgenerators:heat_generator",
        item_task("heat_gen", "Craft Heat Generator", "mekanismgenerators:heat_generator"),
        item_rewards([("minecraft:coal", 16), ("minecraft:redstone", 16)], xp=50),
        dependencies=["find_osmium"],
        bg=BG_GEAR,
    )

    # ---------------- TIER 1: THE SPARK OF STEEL ----------------
    g1, d1, _ = GROUPS[1]
    make_quest(
        "metallurgic_infuser", d1, g1, (0, 0),
        "The Heart of Metallurgy",
        "Tier 1 — Alloy & Steel Synthesis",
        "Build the Metallurgic Infuser to infuse Redstone, Carbon, and Diamond into base metals.",
        "mekanism:metallurgic_infuser",
        item_task("infuser", "Craft Metallurgic Infuser", "mekanism:metallurgic_infuser"),
        item_rewards([("mekanism:enriched_iron", 8), ("minecraft:redstone", 32)], xp=100),
        dependencies=["heat_generator"],
        bg=BG_HEX,
        unlock_toast=True,
    )
    make_quest(
        "steel_ingot", d1, g1, (150, 0),
        "Tempered Ambition",
        "Tier 1 — Industrial Steel",
        "Infuse Iron with Coal/Carbon twice and smelt the resulting Steel Dust into Steel Ingots.",
        "mekanism:ingot_steel",
        item_task("steel", "Smelt Steel Ingots", "mekanism:ingot_steel", 8),
        item_rewards([("mekanism:ingot_steel", 8), ("mekanism:steel_casing", 1)], xp=100),
        dependencies=["metallurgic_infuser"],
    )
    make_quest(
        "basic_control_circuit", d1, g1, (300, 0),
        "Computational Logic",
        "Tier 1 — Basic Circuits",
        "Infuse Osmium with Redstone in the Metallurgic Infuser to fabricate Basic Control Circuits.",
        "mekanism:basic_control_circuit",
        item_task("circuit", "Craft Basic Control Circuit", "mekanism:basic_control_circuit", 2),
        item_rewards([("mekanism:basic_control_circuit", 2), ("mekanism:energy_tablet", 2)], xp=150),
        dependencies=["steel_ingot"],
        bg=BG_HEX,
    )
    make_quest(
        "wind_generator", d1, g1, (450, 0),
        "High-Altitude Kinetic Harvest",
        "Tier 1 — Clean Renewable Power",
        "Deploy a Wind Generator at high altitude for continuous passive energy generation.",
        "mekanismgenerators:wind_generator",
        item_task("wind", "Craft Wind Generator", "mekanismgenerators:wind_generator"),
        item_rewards([("mekanism:basic_energy_cube", 1)], xp=150),
        dependencies=["basic_control_circuit"],
        bg=BG_GEAR,
    )
    make_quest(
        "branch_pipez", d1, g1, (300, -110),
        "High-Throughput Conduits",
        "Tier 1 Wing — Pipez Logistics",
        "Craft Steel-reinforced Pipez to automate item, fluid, and energy transport.",
        "pipez:item_pipe",
        item_task("pipez", "Craft Item Pipes", "pipez:item_pipe", 8),
        item_rewards([("pipez:energy_pipe", 16), ("pipez:wrench", 1)], xp=100),
        dependencies=["basic_control_circuit"],
    )
    make_quest(
        "branch_cc_tweaked", d1, g1, (450, -110),
        "Telemetry Core",
        "Tier 1 Wing — CC: Tweaked",
        "Assemble a CC: Tweaked Computer to run Lua automation and Mekanism telemetry scripts.",
        "computercraft:computer_normal",
        item_task("pc", "Craft Computer", "computercraft:computer_normal"),
        item_rewards([("computercraft:cable", 16)], xp=100),
        dependencies=["basic_control_circuit"],
    )
    make_quest(
        "branch_moving_elevators", d1, g1, (300, 110),
        "Vertical Transit",
        "Tier 1 Wing — Moving Elevators",
        "Construct a multi-floor Elevator Controller for your industrial compound.",
        "movingelevators:elevator_block",
        item_task("elev", "Craft Elevator Controller", "movingelevators:elevator_block"),
        item_rewards([("movingelevators:display_block", 2), ("movingelevators:button_block", 2)], xp=100),
        dependencies=["basic_control_circuit"],
    )

    # ---------------- TIER 2: KINETIC AUTOMATION ----------------
    g2, d2, _ = GROUPS[2]
    make_quest(
        "enrichment_chamber", d2, g2, (0, 0),
        "Molecular Multiplication",
        "Tier 2 — 2x Ore Processing",
        "Double raw ore yields and enrich Infuser materials (Redstone, Carbon, Diamond) with the Enrichment Chamber.",
        "mekanism:enrichment_chamber",
        item_task("enrich", "Craft Enrichment Chamber", "mekanism:enrichment_chamber"),
        item_rewards([
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:speed"}),
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:energy"}),
        ], xp=200),
        dependencies=["basic_control_circuit"],
        bg=BG_GEAR,
        unlock_toast=True,
    )
    make_quest(
        "infused_alloy", d2, g2, (150, 0),
        "Alloy Dynamics",
        "Tier 2 — Infused Alloy",
        "Infuse Iron with Redstone to synthesize Infused Alloys for Tier 2 machinery.",
        "mekanism:alloy_infused",
        item_task("alloy", "Synthesize Infused Alloy", "mekanism:alloy_infused", 8),
        item_rewards([("mekanism:alloy_infused", 4), ("mekanism:basic_tier_installer", 1)], xp=200),
        dependencies=["enrichment_chamber"],
    )
    make_quest(
        "advanced_control_circuit", d2, g2, (300, 0),
        "Advanced Silicon Architecture",
        "Tier 2 — Advanced Circuits",
        "Upgrade Basic Circuits with Infused Alloys into Advanced Control Circuits.",
        "mekanism:advanced_control_circuit",
        item_task("adv_circuit", "Craft Advanced Control Circuit", "mekanism:advanced_control_circuit", 2),
        item_rewards([("mekanism:advanced_control_circuit", 2), ("mekanism:advanced_tier_installer", 1)], xp=250),
        dependencies=["infused_alloy"],
        bg=BG_HEX,
    )
    make_quest(
        "branch_ae2_controller", d2, g2, (300, -110),
        "The Digital Matrix",
        "Tier 2 Wing — Applied Energistics 2",
        "Construct the ME Controller mainframe powered by Steel Casings and Advanced Circuits.",
        "ae2:controller",
        item_task("ctrl", "Craft ME Controller", "ae2:controller"),
        item_rewards([("ae2:drive", 1), ("ae2:terminal", 1), ("ae2:item_storage_cell_4k", 2)], xp=250),
        dependencies=["advanced_control_circuit"],
        bg=BG_DIAMOND,
    )
    make_quest(
        "branch_securitycraft", d2, g2, (300, 110),
        "Biometric Security",
        "Tier 2 Wing — SecurityCraft",
        "Secure your industrial compound with Circuit-driven Keypads and Laser Grids.",
        "securitycraft:keypad_item",
        item_task("keypad", "Craft Keypad", "securitycraft:keypad_item"),
        item_rewards([("securitycraft:retinal_scanner", 1), ("securitycraft:door_indestructible_iron_item", 1)], xp=150),
        dependencies=["advanced_control_circuit"],
    )

    # ---------------- TIER 3: CHEMICAL DIGITIZATION ----------------
    g3, d3, _ = GROUPS[3]
    make_quest(
        "electrolytic_separator", d3, g3, (0, 0),
        "Elemental Partition",
        "Tier 3 — Hydrogen & Oxygen",
        "Split water into pressurized Hydrogen and Oxygen using the Electrolytic Separator.",
        "mekanism:electrolytic_separator",
        item_task("sep", "Craft Electrolytic Separator", "mekanism:electrolytic_separator"),
        item_rewards([("mekanism:basic_chemical_tank", 1), ("mekanism:jetpack_armored", 1)], xp=250),
        dependencies=["advanced_control_circuit"],
        bg=BG_GEAR,
        unlock_toast=True,
    )
    make_quest(
        "purification_chamber", d3, g3, (150, 0),
        "Tri-Ore Refining (3x)",
        "Tier 3 — Chemical Ore Processing",
        "Inject Oxygen into raw ores inside the Purification Chamber for 3x ore multiplication.",
        "mekanism:purification_chamber",
        item_task("purify", "Craft Purification Chamber", "mekanism:purification_chamber"),
        item_rewards([
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:speed"}),
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:chemical"}),
        ], xp=300),
        dependencies=["electrolytic_separator"],
        bg=BG_GEAR,
    )
    make_quest(
        "reinforced_alloy", d3, g3, (300, 0),
        "Reinforced Kinetics",
        "Tier 3 — Reinforced Alloy",
        "Infuse Infused Alloys with Diamond to forge ultra-dense Reinforced Alloys.",
        "mekanism:alloy_reinforced",
        item_task("reinf", "Synthesize Reinforced Alloy", "mekanism:alloy_reinforced", 8),
        item_rewards([("mekanism:alloy_reinforced", 4), ("mekanism:advanced_tier_installer", 2)], xp=300),
        dependencies=["purification_chamber"],
    )
    make_quest(
        "elite_control_circuit", d3, g3, (450, 0),
        "Quantum Computation Matrix",
        "Tier 3 — Elite Circuits",
        "Fabricate Elite Control Circuits using Reinforced Alloys.",
        "mekanism:elite_control_circuit",
        item_task("elite_c", "Craft Elite Control Circuit", "mekanism:elite_control_circuit", 2),
        item_rewards([("mekanism:elite_control_circuit", 2), ("mekanism:elite_tier_installer", 1)], xp=350),
        dependencies=["reinforced_alloy"],
        bg=BG_HEX,
    )
    make_quest(
        "digital_miner", d3, g3, (600, 0),
        "Autonomic Planetary Excavation",
        "Tier 3 — Digital Miner",
        "Construct the Digital Miner to extract target underground ores automatically.",
        "mekanism:digital_miner",
        item_task("miner", "Craft Digital Miner", "mekanism:digital_miner"),
        item_rewards([("mekanism:basic_energy_cube", 1), ("mekanism:teleportation_core", 1)], xp=400),
        dependencies=["elite_control_circuit"],
        bg=BG_DIAMOND,
    )
    make_quest(
        "branch_dimstorage", d3, g3, (450, -110),
        "Cross-Planetary Frequency",
        "Tier 3 Wing — DimStorage",
        "Link wireless cross-dimensional storage channels with Dimensional Chests and Tanks.",
        "dimstorage:dimensional_chest",
        item_task("dim", "Craft Dimensional Chest", "dimstorage:dimensional_chest"),
        item_rewards([("dimstorage:dim_core", 1), ("dimstorage:dim_wall", 4)], xp=250),
        dependencies=["elite_control_circuit"],
    )

    # ---------------- TIER 4: NUCLEAR POWER & RELAYS ----------------
    g4, d4, _ = GROUPS[4]
    make_quest(
        "fission_reactor", d4, g4, (0, 0),
        "Splitting the Atom",
        "Tier 4 — Fission Reactor",
        "Assemble an Industrial Multiblock Fission Reactor to generate Polonium, Plutonium, and superheated steam.",
        "mekanismgenerators:fission_reactor_casing",
        item_task("fission", "Craft Fission Reactor Casings", "mekanismgenerators:fission_reactor_casing", 16),
        item_rewards([
            ("mekanism:hazmat_mask", 1),
            ("mekanism:hazmat_gown", 1),
            ("mekanism:hazmat_pants", 1),
            ("mekanism:hazmat_boots", 1),
            ("mekanism:radioactive_waste_barrel", 16),
        ], xp=500),
        dependencies=["digital_miner"],
        bg=BG_OCTAGON,
        unlock_toast=True,
    )
    make_quest(
        "industrial_turbine", d4, g4, (150, 0),
        "Megawatt Cyclone",
        "Tier 4 — Industrial Turbine",
        "Condense reactor steam through an Industrial Turbine for colossal power output.",
        "mekanismgenerators:turbine_casing",
        item_task("turbine", "Craft Turbine Casings", "mekanismgenerators:turbine_casing", 16),
        item_rewards([("mekanism:ultimate_energy_cube", 1), ("mekanism:elite_tier_installer", 2)], xp=600),
        dependencies=["fission_reactor"],
        bg=BG_GEAR,
    )
    make_quest(
        "atomic_alloy", d4, g4, (300, 0),
        "Subatomic Engineering",
        "Tier 4 — Atomic Alloy",
        "Infuse Reinforced Alloys with Refined Obsidian to forge Atomic Alloys.",
        "mekanism:alloy_atomic",
        item_task("atomic", "Synthesize Atomic Alloy", "mekanism:alloy_atomic", 8),
        item_rewards([("mekanism:alloy_atomic", 4), ("mekanism:ultimate_tier_installer", 2)], xp=700),
        dependencies=["industrial_turbine"],
    )
    make_quest(
        "ultimate_control_circuit", d4, g4, (450, 0),
        "Transcendent Logic Core",
        "Tier 4 — Ultimate Circuits",
        "Fabricate the Ultimate Control Circuit—the apex of computational technology.",
        "mekanism:ultimate_control_circuit",
        item_task("ult_c", "Craft Ultimate Control Circuit", "mekanism:ultimate_control_circuit", 2),
        item_rewards([("mekanism:ultimate_control_circuit", 2), ("mekanism:teleportation_core", 1)], xp=800),
        dependencies=["atomic_alloy"],
        bg=BG_HEX,
    )
    make_quest(
        "branch_entangled", d4, g4, (450, -110),
        "Spatial Entanglement",
        "Tier 4 Wing — Entangled",
        "Bind machines and containers instantaneously across reality with Entangled Blocks.",
        "entangled:block",
        item_task("ent", "Craft Entangled Block", "entangled:block"),
        item_rewards([("entangled:item", 1), ("mekanism:alloy_atomic", 4)], xp=500),
        dependencies=["ultimate_control_circuit"],
    )
    make_quest(
        "branch_wormhole", d4, g4, (450, 110),
        "Stargate Gateway",
        "Tier 4 Wing — Wormhole Portals",
        "Deploy an interdimensional Wormhole Portal Stabilizer powered by quantum circuits.",
        "wormhole:portal_stabilizer",
        item_task("worm", "Craft Portal Stabilizer", "wormhole:portal_stabilizer"),
        item_rewards([("wormhole:portal_frame", 4), ("wormhole:advanced_target_device", 1)], xp=500),
        dependencies=["ultimate_control_circuit"],
    )

    # ---------------- TIER 5: SUPERCRITICAL FRONTIER ----------------
    g5, d5, _ = GROUPS[5]
    make_quest(
        "fusion_reactor", d5, g5, (0, 0),
        "Harnessing the Sun",
        "Tier 5 — D-T Fusion Reactor",
        "Ignite a D-T Fusion Reactor with high-energy Laser Amplifiers for near-limitless energy.",
        "mekanismgenerators:fusion_reactor_controller",
        item_task("fusion", "Craft Fusion Reactor Controller", "mekanismgenerators:fusion_reactor_controller"),
        item_rewards([("mekanism:quantum_entangloporter", 1)], xp=1500),
        dependencies=["ultimate_control_circuit"],
        bg=BG_OCTAGON,
        unlock_toast=True,
    )
    make_quest(
        "sps_multiblock", d5, g5, (150, 0),
        "Supercritical Phase Shifter",
        "Tier 5 — SPS Accelerator",
        "Construct the colossal SPS particle accelerator to polarize Polonium into Antimatter.",
        "mekanism:sps_casing",
        item_task("sps", "Craft SPS Casings", "mekanism:sps_casing", 16),
        item_rewards([("mekanism:supercharged_coil", 4)], xp=2000),
        dependencies=["fusion_reactor"],
        bg=BG_OCTAGON,
    )
    make_quest(
        "antimatter_pellet", d5, g5, (300, 0),
        "Beyond the Standard Model",
        "Tier 5 — Antimatter Synthesis",
        "Synthesize a stable Antimatter Pellet from relativistic particle collisions.",
        "mekanism:pellet_antimatter",
        item_task("anti", "Synthesize Antimatter Pellet", "mekanism:pellet_antimatter"),
        item_rewards([("mekanism:pellet_antimatter", 1)], xp=5000),
        dependencies=["sps_multiblock"],
        bg=BG_DIAMOND,
    )
    make_quest(
        "mekasuit", d5, g5, (450, -110),
        "Cybernetic Sovereign",
        "Tier 5 — MekaSuit Power Armor",
        "Assemble the MekaSuit modular power armor system.",
        "mekanism:mekasuit_bodyarmor",
        item_task("suit", "Craft MekaSuit Bodyarmor", "mekanism:mekasuit_bodyarmor"),
        item_rewards([
            ("mekanism:module", 1, {
                "mekanism:module_type": "mekanism:gravitational_modulating_unit",
                "minecraft:rarity": "epic",
            })
        ], xp=5000),
        dependencies=["antimatter_pellet"],
        bg=BG_DIAMOND,
    )
    make_quest(
        "qio_drive", d5, g5, (450, 0),
        "Post-Scarcity Quantum Grid",
        "Tier 5 — QIO Storage",
        "Deploy a QIO Drive Array to store billions of items on subatomic quantum frequencies.",
        "mekanism:qio_drive_array",
        item_task("qio", "Craft QIO Drive Array", "mekanism:qio_drive_array"),
        item_rewards([("mekanism:qio_drive_supermassive", 1)], xp=5000),
        dependencies=["antimatter_pellet"],
        bg=BG_DIAMOND,
    )
    make_quest(
        "branch_shrink", d5, g5, (450, 110),
        "Subatomic Dimension",
        "Tier 5 Wing — Shrink",
        "Compress your physical form to microscopic scale with the Personal Shrinking Device.",
        "shrink:shrinking_device",
        item_task("shrink", "Craft Personal Shrinking Device", "shrink:shrinking_device"),
        item_rewards([("mekanism:pellet_antimatter", 2)], xp=2500),
        dependencies=["antimatter_pellet"],
        bg=BG_DIAMOND,
    )

    print("[SUCCESS] Generated 33 Theseus Quests across 6 Sovereign Spine chapters in config/theseus/.")


if __name__ == "__main__":
    generate_all()

