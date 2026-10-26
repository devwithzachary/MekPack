#!/usr/bin/env python3
"""
MekPack Advancement & Loot Table Generator
Generates:
- custom_content/data/mekpack/advancement/...
- custom_content/data/mekpack/loot_table/rewards/...
- custom_content/data/mekpack/loot_tables/rewards/... (dual mirror for compatibility)

Compatible with Minecraft 26.3 / NeoForge 26.3.0.95.
Uses 26.3 modifier schemas and Mekanism DataComponent schemas for upgrades and modules.
"""

import os
import json
import shutil

ADV_DIR = "custom_content/data/mekpack/advancement"
LOOT_DIR = "custom_content/data/mekpack/loot_table/rewards"
LOOT_DIR_LEGACY = "custom_content/data/mekpack/loot_tables/rewards"

os.makedirs(ADV_DIR, exist_ok=True)
os.makedirs(LOOT_DIR, exist_ok=True)
os.makedirs(LOOT_DIR_LEGACY, exist_ok=True)

def create_loot_table(loot_id, items):
    entries = []
    for item_spec in items:
        item = item_spec[0]
        count = item_spec[1]
        components = item_spec[2] if len(item_spec) > 2 else None
        
        entry = {
            "type": "minecraft:item",
            "name": item
        }
        
        modifiers = []
        functions = []
        if count > 1:
            modifiers.append({
                "type": "minecraft:set_count",
                "count": count
            })
            functions.append({
                "function": "minecraft:set_count",
                "count": count
            })
        if components:
            modifiers.append({
                "type": "minecraft:set_components",
                "components": components
            })
            functions.append({
                "function": "minecraft:set_components",
                "components": components
            })
            
        if modifiers:
            entry["modifier"] = modifiers
        if functions:
            entry["functions"] = functions
            
        entries.append(entry)
    
    loot_data = {
        "type": "minecraft:advancement_reward",
        "pools": [
            {
                "rolls": 1,
                "entries": entries
            }
        ]
    }
    
    for base_dir in [LOOT_DIR, LOOT_DIR_LEGACY]:
        path = os.path.join(base_dir, f"{loot_id}.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(loot_data, f, indent=2)

def create_advancement(rel_path, parent, title, desc, icon, frame, trigger_item, exp=0, loot_items=None, is_root=False):
    loot_id = rel_path.replace("/", "_")
    loot_tables = []
    if loot_items:
        create_loot_table(loot_id, loot_items)
        loot_tables.append(f"mekpack:rewards/{loot_id}")

    adv_data = {
        "display": {
            "icon": {
                "id": icon
            },
            "title": {
                "text": title
            },
            "description": {
                "text": desc
            },
            "frame": frame,
            "show_toast": True,
            "announce_to_chat": frame in ["goal", "challenge"]
        }
    }

    if is_root:
        adv_data["display"]["background"] = "minecraft:textures/gui/advancements/backgrounds/stone.png"
        adv_data["criteria"] = {
            "tick": {
                "trigger": "minecraft:tick"
            }
        }
    else:
        adv_data["parent"] = f"mekpack:{parent}"
        adv_data["criteria"] = {
            "has_item": {
                "trigger": "minecraft:inventory_changed",
                "conditions": {
                    "items": [
                        {
                            "items": trigger_item
                        }
                    ]
                }
            }
        }

    rewards = {}
    if exp > 0:
        rewards["experience"] = exp
    if loot_tables:
        rewards["loot"] = loot_tables
    if rewards:
        adv_data["rewards"] = rewards

    full_path = os.path.join(ADV_DIR, f"{rel_path}.json")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(adv_data, f, indent=2)

def generate_all():
    # ----------------- ROOT -----------------
    create_advancement(
        rel_path="root",
        parent=None,
        title="MekPack: Future Frontiers",
        desc="Welcome to the Sovereign Industrial Spine. Forge your path from primitive metallurgy to supercritical reality.",
        icon="mekanism:steel_casing",
        frame="task",
        trigger_item=None,
        exp=50,
        loot_items=[("minecraft:torch", 16), ("minecraft:bread", 8), ("minecraft:compass", 1)],
        is_root=True
    )

    # ----------------- TIER 0: GROUND ZERO -----------------
    create_advancement(
        rel_path="tier0/find_osmium",
        parent="root",
        title="The Blue Vein",
        desc="Prospect and mine Raw Osmium from planetary deposits.",
        icon="mekanism:raw_osmium",
        frame="task",
        trigger_item="mekanism:raw_osmium",
        exp=50,
        loot_items=[("mekanism:raw_osmium", 8)]
    )

    create_advancement(
        rel_path="tier0/heat_generator",
        parent="tier0/find_osmium",
        title="Thermal Inception",
        desc="Harness passive and burning thermal energy using the Heat Generator.",
        icon="mekanismgenerators:heat_generator",
        frame="task",
        trigger_item="mekanismgenerators:heat_generator",
        exp=50,
        loot_items=[("minecraft:coal", 16), ("minecraft:redstone", 16)]
    )

    # ----------------- TIER 1: THE SPARK OF STEEL -----------------
    create_advancement(
        rel_path="tier1/metallurgic_infuser",
        parent="tier0/heat_generator",
        title="The Heart of Metallurgy",
        desc="Construct the Metallurgic Infuser to infuse elements into base metals.",
        icon="mekanism:metallurgic_infuser",
        frame="goal",
        trigger_item="mekanism:metallurgic_infuser",
        exp=100,
        loot_items=[("mekanism:enriched_iron", 8), ("minecraft:redstone", 32)]
    )

    create_advancement(
        rel_path="tier1/steel_ingot",
        parent="tier1/metallurgic_infuser",
        title="Tempered Ambition",
        desc="Smelt Enriched Iron into durable Steel Ingots.",
        icon="mekanism:ingot_steel",
        frame="task",
        trigger_item="mekanism:ingot_steel",
        exp=100,
        loot_items=[("mekanism:ingot_steel", 8), ("mekanism:steel_casing", 1)]
    )

    create_advancement(
        rel_path="tier1/basic_control_circuit",
        parent="tier1/steel_ingot",
        title="Computational Logic",
        desc="Fabricate a Basic Control Circuit using Infused Osmium.",
        icon="mekanism:basic_control_circuit",
        frame="goal",
        trigger_item="mekanism:basic_control_circuit",
        exp=150,
        loot_items=[("mekanism:basic_control_circuit", 2), ("mekanism:energy_tablet", 2)]
    )

    create_advancement(
        rel_path="tier1/wind_generator",
        parent="tier1/basic_control_circuit",
        title="High-Altitude Kinetic Harvest",
        desc="Deploy a Wind Generator at high altitude for sustained clean energy.",
        icon="mekanismgenerators:wind_generator",
        frame="task",
        trigger_item="mekanismgenerators:wind_generator",
        exp=150,
        loot_items=[("mekanism:basic_energy_cube", 1)]
    )

    # Branches off Tier 1
    create_advancement(
        rel_path="tier1/branch_pipez",
        parent="tier1/basic_control_circuit",
        title="High-Throughput Conduits",
        desc="Craft Steel-Reinforced Pipes to automate item, fluid, and energy transport.",
        icon="pipez:item_pipe",
        frame="task",
        trigger_item="pipez:item_pipe",
        exp=100,
        loot_items=[("pipez:energy_pipe", 16), ("pipez:wrench", 1)]
    )

    create_advancement(
        rel_path="tier1/branch_cc_tweaked",
        parent="tier1/basic_control_circuit",
        title="Telemetry Core",
        desc="Assemble a CC: Tweaked Computer running logic circuits.",
        icon="computercraft:computer_normal",
        frame="task",
        trigger_item="computercraft:computer_normal",
        exp=100,
        loot_items=[("computercraft:cable", 16)]
    )

    create_advancement(
        rel_path="tier1/branch_moving_elevators",
        parent="tier1/basic_control_circuit",
        title="Vertical Transit",
        desc="Construct a multi-floor Elevator Controller for your industrial compound.",
        icon="movingelevators:elevator_block",
        frame="task",
        trigger_item="movingelevators:elevator_block",
        exp=100,
        loot_items=[("movingelevators:display_block", 2), ("movingelevators:button_block", 2)]
    )

    # ----------------- TIER 2: KINETIC AUTOMATION -----------------
    create_advancement(
        rel_path="tier2/enrichment_chamber",
        parent="tier1/basic_control_circuit",
        title="Molecular Multiplication",
        desc="Double raw ore yields and refine elements with the Enrichment Chamber.",
        icon="mekanism:enrichment_chamber",
        frame="goal",
        trigger_item="mekanism:enrichment_chamber",
        exp=200,
        loot_items=[
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:speed"}),
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:energy"})
        ]
    )

    create_advancement(
        rel_path="tier2/infused_alloy",
        parent="tier2/enrichment_chamber",
        title="Alloy Dynamics",
        desc="Infuse Iron with Redstone to synthesize Infused Alloys.",
        icon="mekanism:alloy_infused",
        frame="task",
        trigger_item="mekanism:alloy_infused",
        exp=200,
        loot_items=[("mekanism:alloy_infused", 4), ("mekanism:basic_tier_installer", 1)]
    )

    create_advancement(
        rel_path="tier2/advanced_control_circuit",
        parent="tier2/infused_alloy",
        title="Advanced Silicon Architecture",
        desc="Upgrade basic logic with Infused Alloys into Advanced Control Circuits.",
        icon="mekanism:advanced_control_circuit",
        frame="goal",
        trigger_item="mekanism:advanced_control_circuit",
        exp=250,
        loot_items=[("mekanism:advanced_control_circuit", 2), ("mekanism:advanced_tier_installer", 1)]
    )

    # Branches off Tier 2
    create_advancement(
        rel_path="tier2/branch_ae2_controller",
        parent="tier2/advanced_control_circuit",
        title="The Digital Matrix",
        desc="Construct the ME Controller mainframe powered by Steel Casings and Advanced Circuits.",
        icon="ae2:controller",
        frame="goal",
        trigger_item="ae2:controller",
        exp=250,
        loot_items=[("ae2:drive", 1), ("ae2:terminal", 1), ("ae2:item_storage_cell_4k", 2)]
    )

    create_advancement(
        rel_path="tier2/branch_securitycraft",
        parent="tier2/advanced_control_circuit",
        title="Biometric Security",
        desc="Secure your industrial compound with Circuit-driven Keypads and Laser Grids.",
        icon="securitycraft:keypad_item",
        frame="task",
        trigger_item="securitycraft:keypad_item",
        exp=150,
        loot_items=[("securitycraft:retinal_scanner", 1), ("securitycraft:door_indestructible_iron_item", 1)]
    )

    # ----------------- TIER 3: CHEMICAL DIGITIZATION -----------------
    create_advancement(
        rel_path="tier3/electrolytic_separator",
        parent="tier2/advanced_control_circuit",
        title="Elemental Partition",
        desc="Split water into pressurized Hydrogen and Oxygen with the Electrolytic Separator.",
        icon="mekanism:electrolytic_separator",
        frame="task",
        trigger_item="mekanism:electrolytic_separator",
        exp=250,
        loot_items=[("mekanism:basic_chemical_tank", 1), ("mekanism:jetpack_armored", 1)]
    )

    create_advancement(
        rel_path="tier3/purification_chamber",
        parent="tier3/electrolytic_separator",
        title="Tri-Ore Refining (3x)",
        desc="Inject Oxygen into raw ore to achieve 3x tri-chemical multiplication.",
        icon="mekanism:purification_chamber",
        frame="goal",
        trigger_item="mekanism:purification_chamber",
        exp=300,
        loot_items=[
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:speed"}),
            ("mekanism:upgrade", 4, {"mekanism:upgrade_type": "mekanism:chemical"})
        ]
    )

    create_advancement(
        rel_path="tier3/reinforced_alloy",
        parent="tier3/purification_chamber",
        title="Reinforced Kinetics",
        desc="Infuse Alloys with Diamond to forge ultra-dense Reinforced Alloys.",
        icon="mekanism:alloy_reinforced",
        frame="task",
        trigger_item="mekanism:alloy_reinforced",
        exp=300,
        loot_items=[("mekanism:alloy_reinforced", 4), ("mekanism:advanced_tier_installer", 2)]
    )

    create_advancement(
        rel_path="tier3/elite_control_circuit",
        parent="tier3/reinforced_alloy",
        title="Quantum Computation Matrix",
        desc="Fabricate Elite Control Circuits using Reinforced Alloys.",
        icon="mekanism:elite_control_circuit",
        frame="goal",
        trigger_item="mekanism:elite_control_circuit",
        exp=350,
        loot_items=[("mekanism:elite_control_circuit", 2), ("mekanism:elite_tier_installer", 1)]
    )

    create_advancement(
        rel_path="tier3/digital_miner",
        parent="tier3/elite_control_circuit",
        title="Autonomic Planetary Excavation",
        desc="Construct the Digital Miner to extract target underground ores automatically.",
        icon="mekanism:digital_miner",
        frame="goal",
        trigger_item="mekanism:digital_miner",
        exp=400,
        loot_items=[("mekanism:basic_energy_cube", 1), ("mekanism:teleportation_core", 1)]
    )

    # Branches off Tier 3
    create_advancement(
        rel_path="tier3/branch_dimstorage",
        parent="tier3/elite_control_circuit",
        title="Cross-Planetary Frequency",
        desc="Link wireless cross-dimensional storage channels with Dimensional Chests and Tanks.",
        icon="dimstorage:dimensional_chest",
        frame="task",
        trigger_item="dimstorage:dimensional_chest",
        exp=250,
        loot_items=[("dimstorage:dim_core", 1), ("dimstorage:dim_wall", 4)]
    )

    # ----------------- TIER 4: NUCLEAR POWER & SPATIAL RELAYS -----------------
    create_advancement(
        rel_path="tier4/fission_reactor",
        parent="tier3/digital_miner",
        title="Splitting the Atom",
        desc="Assemble an Industrial Multiblock Fission Reactor and achieve nuclear criticality.",
        icon="mekanismgenerators:fission_reactor_casing",
        frame="goal",
        trigger_item="mekanismgenerators:fission_reactor_casing",
        exp=500,
        loot_items=[
            ("mekanism:hazmat_mask", 1),
            ("mekanism:hazmat_gown", 1),
            ("mekanism:hazmat_pants", 1),
            ("mekanism:hazmat_boots", 1),
            ("mekanism:radioactive_waste_barrel", 16)
        ]
    )

    create_advancement(
        rel_path="tier4/industrial_turbine",
        parent="tier4/fission_reactor",
        title="Megawatt Cyclone",
        desc="Condense reactor steam through an Industrial Turbine for colossal power output.",
        icon="mekanismgenerators:turbine_casing",
        frame="goal",
        trigger_item="mekanismgenerators:turbine_casing",
        exp=600,
        loot_items=[("mekanism:ultimate_energy_cube", 1), ("mekanism:elite_tier_installer", 2)]
    )

    create_advancement(
        rel_path="tier4/atomic_alloy",
        parent="tier4/industrial_turbine",
        title="Subatomic Engineering",
        desc="Infuse Reinforced Alloys with Refined Obsidian to forge Atomic Alloys.",
        icon="mekanism:alloy_atomic",
        frame="task",
        trigger_item="mekanism:alloy_atomic",
        exp=700,
        loot_items=[("mekanism:alloy_atomic", 4), ("mekanism:ultimate_tier_installer", 2)]
    )

    create_advancement(
        rel_path="tier4/ultimate_control_circuit",
        parent="tier4/atomic_alloy",
        title="Transcendent Logic Core",
        desc="Fabricate the Ultimate Control Circuit—the apex of computational technology.",
        icon="mekanism:ultimate_control_circuit",
        frame="goal",
        trigger_item="mekanism:ultimate_control_circuit",
        exp=800,
        loot_items=[("mekanism:ultimate_control_circuit", 2), ("mekanism:teleportation_core", 1)]
    )

    # Branches off Tier 4
    create_advancement(
        rel_path="tier4/branch_entangled",
        parent="tier4/ultimate_control_circuit",
        title="Spatial Entanglement",
        desc="Bind machines and containers instantaneously across reality with Entangled Blocks.",
        icon="entangled:block",
        frame="task",
        trigger_item="entangled:block",
        exp=500,
        loot_items=[("entangled:item", 1), ("mekanism:alloy_atomic", 4)]
    )

    create_advancement(
        rel_path="tier4/branch_wormhole",
        parent="tier4/ultimate_control_circuit",
        title="Stargate Gateway",
        desc="Deploy an interdimensional Wormhole Portal Stabilizer powered by quantum circuits.",
        icon="wormhole:portal_stabilizer",
        frame="task",
        trigger_item="wormhole:portal_stabilizer",
        exp=500,
        loot_items=[("wormhole:portal_frame", 4), ("wormhole:advanced_target_device", 1)]
    )

    # ----------------- TIER 5: SUPERCRITICAL FRONTIER (ENDGAME) -----------------
    create_advancement(
        rel_path="tier5/fusion_reactor",
        parent="tier4/ultimate_control_circuit",
        title="Harnessing the Sun",
        desc="Ignite a D-T Fusion Reactor with high-energy Laser Amplifiers.",
        icon="mekanismgenerators:fusion_reactor_controller",
        frame="challenge",
        trigger_item="mekanismgenerators:fusion_reactor_controller",
        exp=1500,
        loot_items=[("mekanism:quantum_entangloporter", 1)]
    )

    create_advancement(
        rel_path="tier5/sps_multiblock",
        parent="tier5/fusion_reactor",
        title="Supercritical Phase Shifter",
        desc="Construct the colossal SPS particle accelerator to polarize matter.",
        icon="mekanism:sps_casing",
        frame="goal",
        trigger_item="mekanism:sps_casing",
        exp=2000,
        loot_items=[("mekanism:supercharged_coil", 4)]
    )

    create_advancement(
        rel_path="tier5/antimatter_pellet",
        parent="tier5/sps_multiblock",
        title="Beyond the Standard Model",
        desc="Synthesize a stable Antimatter Pellet from relativistic particle collisions.",
        icon="mekanism:pellet_antimatter",
        frame="challenge",
        trigger_item="mekanism:pellet_antimatter",
        exp=5000,
        loot_items=[("mekanism:pellet_antimatter", 1)]
    )

    create_advancement(
        rel_path="tier5/mekasuit",
        parent="tier5/antimatter_pellet",
        title="Cybernetic Sovereign",
        desc="Assemble the complete MekaSuit modular power armor system.",
        icon="mekanism:mekasuit_bodyarmor",
        frame="challenge",
        trigger_item="mekanism:mekasuit_bodyarmor",
        exp=5000,
        loot_items=[
            ("mekanism:module", 1, {
                "mekanism:module_type": "mekanism:gravitational_modulating_unit",
                "minecraft:rarity": "epic"
            })
        ]
    )

    create_advancement(
        rel_path="tier5/qio_drive",
        parent="tier5/antimatter_pellet",
        title="Post-Scarcity Quantum Grid",
        desc="Deploy a QIO Drive Array to store billions of items on subatomic quantum frequencies.",
        icon="mekanism:qio_drive_array",
        frame="challenge",
        trigger_item="mekanism:qio_drive_array",
        exp=5000,
        loot_items=[("mekanism:qio_drive_supermassive", 1)]
    )

    create_advancement(
        rel_path="tier5/branch_shrink",
        parent="tier5/antimatter_pellet",
        title="Subatomic Dimension",
        desc="Compress your physical form to microscopic scale with the Quantum Shrinking Device.",
        icon="shrink:shrinking_device",
        frame="task",
        trigger_item="shrink:shrinking_device",
        exp=2500,
        loot_items=[("mekanism:pellet_antimatter", 2)]
    )

    print("[SUCCESS] Advancements and Loot Tables generated successfully.")

if __name__ == "__main__":
    generate_all()
