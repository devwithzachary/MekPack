#!/usr/bin/env python3
"""
MekPack Instance Setup Script
Configures the local test environment (minecraft/) for Prism Launcher / MultiMC:
1. Links root config/ -> minecraft/config
2. Links root resourcepacks/ -> minecraft/resourcepacks
3. Configures default options.txt with the custom theme enabled
4. Invokes download_mods.py to download companion mods and sync custom_mods/
"""

import os
import sys
import subprocess
import shutil
import re

def setup_instance():
    os.makedirs("minecraft", exist_ok=True)

    # 1. Symlink config
    config_link = os.path.join("minecraft", "config")
    if not os.path.islink(config_link):
        if os.path.exists(config_link):
            shutil.rmtree(config_link)
        os.symlink("../config", config_link)
        print("[LINK] minecraft/config -> ../config")

    # 2. Symlink resourcepacks
    rp_link = os.path.join("minecraft", "resourcepacks")
    if not os.path.islink(rp_link):
        if os.path.exists(rp_link):
            shutil.rmtree(rp_link)
        os.symlink("../resourcepacks", rp_link)
        print("[LINK] minecraft/resourcepacks -> ../resourcepacks")

    # 3. Ensure options.txt exists with default vanilla resourcepacks
    options_file = os.path.join("minecraft", "options.txt")
    vanilla_rp = 'resourcePacks:["vanilla"]'
    if os.path.exists(options_file):
        with open(options_file, "r") as f:
            content = f.read()
        if "resourcePacks:" not in content:
            content += f"\n{vanilla_rp}\n"
        else:
            content = re.sub(r'resourcePacks:\[.*?\]', vanilla_rp, content)
        with open(options_file, "w") as f:
            f.write(content)
    else:
        with open(options_file, "w") as f:
            f.write(f"{vanilla_rp}\nincompatibleResourcePacks:[]\n")
    print("[CONFIG] Ensured default vanilla loading screen & resourcepacks in minecraft/options.txt")

    # 4. Generate Advancements
    adv_gen = os.path.join("tools", "generate_advancements.py")
    if os.path.exists(adv_gen):
        subprocess.check_call([sys.executable, adv_gen])

    # 5. Build custom content mod jar
    content_builder = os.path.join("tools", "build_content.py")
    if os.path.exists(content_builder):
        subprocess.check_call([sys.executable, content_builder])

    # 6. Run download_mods.py
    subprocess.check_call([sys.executable, "tools/download_mods.py"])
    print("\nInstance ready for Prism Launcher testing!")

if __name__ == "__main__":
    setup_instance()
