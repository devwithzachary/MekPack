#!/usr/bin/env python3
"""
MekPack Exporter
Generates:
1. Distributable Prism Launcher / MultiMC importable ZIP.
2. Modrinth .mrpack format bundle with metadata and index.
"""

import os
import json
import zipfile
import hashlib
import glob

PACK_NAME = "MekPack"
VERSION = "0.0.1"
MC_VERSION = "26.3"
LOADER_VERSION = "26.3.0.95"

DEFAULT_OPTIONS = """resourcePacks:["vanilla"]
incompatibleResourcePacks:[]
fovEffectScale:1.0
darknessEffectScale:1.0
glintSpeed:0.5
glintStrength:0.75
preferredGraphicsBackend:"opengl"
startedCleanly:true
onboardAccessibility:false
"""

def add_dir_to_zip(z, src_dir, zip_prefix):
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            full_path = os.path.join(root, f)
            rel = os.path.relpath(full_path, src_dir)
            target = os.path.join(zip_prefix, rel)
            z.write(full_path, target)

def create_prism_zip():
    zip_filename = f"dist/{PACK_NAME}-{MC_VERSION}-{VERSION}-Prism.zip"
    os.makedirs("dist", exist_ok=True)
    print(f"Creating Prism Launcher pack: {zip_filename} ...")
    
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as z:
        # Instance definitions
        z.write("mmc-pack.json", "mmc-pack.json")
        z.write("instance.cfg", "instance.cfg")
        if os.path.exists("icon.png"):
            z.write("icon.png", "icon.png")
            
        # Default options.txt
        z.writestr("minecraft/options.txt", DEFAULT_OPTIONS)

        # Configs & Resourcepacks
        add_dir_to_zip(z, "config", "minecraft/config")
        add_dir_to_zip(z, "resourcepacks", "minecraft/resourcepacks")

        # Custom mods (homebaked Mekanism)
        if os.path.exists("custom_mods"):
            add_dir_to_zip(z, "custom_mods", "minecraft/mods")
            
        # If companion mods exist locally in minecraft/mods, include them so the Prism zip is immediately playable offline
        if os.path.exists("minecraft/mods"):
            custom_files = set(os.listdir("custom_mods")) if os.path.exists("custom_mods") else set()
            for f in os.listdir("minecraft/mods"):
                if f.endswith(".jar") and f not in custom_files and not f.startswith("Mekanism"):
                    full = os.path.join("minecraft/mods", f)
                    z.write(full, f"minecraft/mods/{f}")
                
    print(f"Successfully built: {zip_filename} ({os.path.getsize(zip_filename) // (1024*1024)} MB)")
    return zip_filename

def create_modrinth_pack():
    mrpack_filename = f"dist/{PACK_NAME}-{MC_VERSION}-{VERSION}.mrpack"
    os.makedirs("dist", exist_ok=True)
    print(f"Creating Modrinth .mrpack: {mrpack_filename} ...")

    with open("resolved_mods.json", "r") as f:
        resolved = json.load(f)

    files_list = []
    for slug, data in resolved.items():
        finfo = data.get("file")
        if not finfo:
            continue
        files_list.append({
            "path": f"mods/{finfo['filename']}",
            "hashes": finfo.get("hashes", {}),
            "env": {
                "client": "required",
                "server": "required"
            },
            "downloads": [finfo["url"]],
            "fileSize": finfo.get("size", 0)
        })

    index_data = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": VERSION,
        "name": f"{PACK_NAME} 26.3",
        "summary": "Sci-Fi tech modpack focused around Mekanism on Minecraft 26.3 NeoForge",
        "files": files_list,
        "dependencies": {
            "minecraft": MC_VERSION,
            "neoforge": LOADER_VERSION
        }
    }

    with zipfile.ZipFile(mrpack_filename, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("modrinth.index.json", json.dumps(index_data, indent=2))
        z.writestr("overrides/options.txt", DEFAULT_OPTIONS)

        # Overrides: configs, resourcepacks, and homebaked Mekanism jars
        add_dir_to_zip(z, "config", "overrides/config")
        add_dir_to_zip(z, "resourcepacks", "overrides/resourcepacks")
        if os.path.exists("custom_mods"):
            add_dir_to_zip(z, "custom_mods", "overrides/mods")

    print(f"Successfully built: {mrpack_filename} ({os.path.getsize(mrpack_filename) // 1024} KB)")
    return mrpack_filename

if __name__ == "__main__":
    import subprocess, sys

    adv_gen = os.path.join("tools", "generate_advancements.py")
    if os.path.exists(adv_gen):
        subprocess.check_call([sys.executable, adv_gen])

    content_builder = os.path.join("tools", "build_content.py")
    if os.path.exists(content_builder):
        subprocess.check_call([sys.executable, content_builder])

    create_prism_zip()
    create_modrinth_pack()
    print("\nExport completed! Release artifacts ready in dist/")
