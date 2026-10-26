# ⚙️ MekPack: Recipe Customization & Datapack Technical Guide

This guide describes the technical architecture for authoring, testing, and packaging custom recipes and tags in **MekPack** on **Minecraft 26.3 (NeoForge)**.

---

## 1. Technical Architecture Overview

In Minecraft 26.3 NeoForge, recipes are resolved from data packs and mod resources using standard JSON schema specifications under `data/<namespace>/recipe/<recipe_name>.json`.

To keep the repository clean and ensure recipes are loaded seamlessly across singleplayer worlds, dedicated servers, and launcher exports, MekPack uses NeoForge's native **`lowcodefml`** mod loader:

1. **Development Source (`custom_content/`)**:
   - Contains raw, human-editable JSON recipe files, tags, loot tables, and advancements.
   - Includes `META-INF/neoforge.mods.toml` configured with `modLoader="lowcodefml"`.
2. **Automated Compilation & Packaging (`tools/build_content.py`)**:
   - Compiles `custom_content/` into `custom_mods/MekPackContent-26.3-0.0.1.jar`.
   - Automatically invoked by `tools/setup_instance.py` (for local play) and `tools/export_pack.py` (for release distribution).
   - Requires zero Java compilation; NeoForge's `lowcodefml` loads the data and resource structures natively into the game engine at startup.

---

## 2. Recipe File Structure & Schema Reference

### 2.1 Shaped Crafting Recipe
Example: Overriding `pipez:basic_upgrade` to require Mekanism's `basic_control_circuit` and `alloy_infused`.

Path: `data/pipez/recipe/basic_upgrade.json`

```json
{
  "type": "minecraft:crafting_shaped",
  "pattern": [
    "ANA",
    "NCN",
    "ANA"
  ],
  "key": {
    "A": "mekanism:alloy_infused",
    "C": "mekanism:basic_control_circuit",
    "N": "#c:nuggets/iron"
  },
  "result": {
    "id": "pipez:basic_upgrade",
    "count": 1
  }
}
```

### 2.2 Shapeless Crafting Recipe
Example: Standard Computer upgrading with Mekanism Steel and Circuit.

Path: `data/computercraft/recipe/computer_normal.json`

```json
{
  "type": "minecraft:crafting_shaped",
  "category": "redstone",
  "pattern": [
    "SSS",
    "SCS",
    "SGS"
  ],
  "key": {
    "S": "#c:ingots/steel",
    "C": "mekanism:basic_control_circuit",
    "G": "#c:glass_panes"
  },
  "result": {
    "id": "computercraft:computer_normal",
    "count": 1
  }
}
```

### 2.3 Mekanism Machine Recipes (Enrichment, Infusion, Crushing)
MekPack can also add custom recipes to Mekanism's own machines to process companion mod resources!

Example: Enriching Certus Quartz into Pure Certus Quartz in the Mekanism Enrichment Chamber:

Path: `data/mekanism/recipe/enriching/pure_certus.json`

```json
{
  "type": "mekanism:enriching",
  "input": {
    "count": 1,
    "item": "ae2:certus_quartz_crystal"
  },
  "output": {
    "count": 2,
    "id": "ae2:pure_certus_quartz_crystal"
  }
}
```

Example: Metallurgic Infusing Sky Stone with Redstone to create Fluix Crystals:

Path: `data/mekanism/recipe/metallurgic_infusing/fluix_from_skystone.json`

```json
{
  "type": "mekanism:metallurgic_infusing",
  "chemical_input": {
    "amount": 20,
    "tag": "mekanism:redstone"
  },
  "item_input": {
    "count": 1,
    "item": "ae2:sky_stone_block"
  },
  "output": {
    "count": 1,
    "id": "ae2:fluix_crystal"
  }
}
```

---

## 3. Unified Tag Standards (`c:`)

In NeoForge 26.3, all common item tags use the `#c:` namespace. Always prefer `#c:` tags over hardcoded vanilla items where applicable to ensure cross-mod interoperability:

- `#c:ingots/steel` (resolves `mekanism:ingot_steel`)
- `#c:ingots/osmium` (resolves `mekanism:ingot_osmium`)
- `#c:ingots/refined_obsidian` (resolves `mekanism:ingot_refined_obsidian`)
- `#c:ingots/refined_glowstone` (resolves `mekanism:ingot_refined_glowstone`)
- `#c:circuits/basic`, `#c:circuits/advanced`, `#c:circuits/elite`, `#c:circuits/ultimate`
- `#c:alloys/basic`, `#c:alloys/infused`, `#c:alloys/reinforced`, `#c:alloys/atomic`
- `#c:dusts/redstone`, `#c:dusts/glowstone`, `#c:dusts/diamond`

---

## 4. Verification & Testing Workflow

When developing and adding new recipe overrides:

1. **Write or Edit JSONs** in the content source directory.
2. **Sync Instance**:
   ```bash
   python3 tools/setup_instance.py
   ```
3. **Launch Testing Instance**:
   ```bash
   prismlauncher --launch MekPack-26.3
   ```
4. **In-game Check via JEI**:
   - Open inventory, search the companion mod item (e.g. `@pipez upgrade`).
   - Press `R` (recipes) on the item.
   - Confirm that the default recipe is completely replaced by the Mekanism-integrated recipe.
5. **Run Package Export**:
   ```bash
   python3 tools/export_pack.py
   ```
   Confirm that all new recipe assets are properly included in the distribution `.zip` and `.mrpack`.
