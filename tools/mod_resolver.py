#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
import sys

TARGET_MC = "26.3"
TARGET_LOADER = "neoforge"

CANDIDATES = [
    # Core Tech & Sci-Fi
    "ae2",
    "cc-tweaked",
    "pipez",
    "security-craft",
    "moving-elevators",
    "dimstorage",
    "entangled",
    "wormhole",
    "shrink",
    "chunk-loaders",
    "trash-cans",
    "item-collectors",
    
    # UI & Diagnostics
    "jei",
    "jade",
    "xaeros-minimap",
    "xaeros-world-map",
    "appleskin",
    "better-advancements",
    "advancement-plaques",
    
    # Optimization & Engine
    "sodium",
    "iris",
    "ferrite-core",
    "lithium",
    "immediatelyfast",
    "entityculling",
    "moreculling",
    "dynamic-fps",
    
    # Common Libs & APIs
    "curios",
    "architectury-api",
    "cloth-config",
    "yacl",
    "supermartijn642s-config-lib",
    "supermartijn642s-core-lib",
    "edivadlib",
    "polylib",
    "guideme",
    "forge-config-api-port",
    "iceberg",
    "lithostitched",

    # Sci-Fi Worldgen, Dimensions & Structures
    "the-lost-cities",
    "terralith",
    "tectonic",
    "nullscape",
    "incendium",
    "structory",
    "structory-towers"
]

def check_project(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version"
    req = urllib.request.Request(url, headers={"User-Agent": "MekPack-Resolver/1.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        return {"slug": slug, "error": str(e)}

    # Find matching version - first prefer TARGET_LOADER
    for v in data:
        game_versions = v.get("game_versions", [])
        loaders = v.get("loaders", [])
        if TARGET_MC in game_versions and TARGET_LOADER in loaders:
            files = v.get("files", [])
            jar_files = [f for f in files if f["filename"].endswith(".jar") and not any(x in f["filename"].lower() for x in ["fabric", "quilt"])]
            cand_files = jar_files if jar_files else files
            primary_file = next((f for f in cand_files if f.get("primary")), cand_files[0] if cand_files else None)
            if primary_file:
                return {
                    "slug": slug,
                    "version_number": v["version_number"],
                    "name": v["name"],
                    "file": primary_file,
                    "dependencies": v.get("dependencies", [])
                }

    # Fallback to datapack if no loader jar exists
    for v in data:
        game_versions = v.get("game_versions", [])
        loaders = v.get("loaders", [])
        if TARGET_MC in game_versions and "datapack" in loaders:
            files = v.get("files", [])
            primary_file = next((f for f in files if f.get("primary")), files[0] if files else None)
            if primary_file:
                return {
                    "slug": slug,
                    "version_number": v["version_number"],
                    "name": v["name"],
                    "file": primary_file,
                    "dependencies": v.get("dependencies", [])
                }


    return {"slug": slug, "not_found": True}

if __name__ == "__main__":
    results = {}
    for slug in CANDIDATES:
        res = check_project(slug)
        if "file" in res and res["file"]:
            print(f"[FOUND] {slug} -> {res['file']['filename']}")
            results[slug] = res
        else:
            print(f"[MISSING/OTHER] {slug}: {res}")
    
    with open("resolved_mods.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResolved {len(results)}/{len(CANDIDATES)} mods for {TARGET_LOADER} {TARGET_MC}.")
