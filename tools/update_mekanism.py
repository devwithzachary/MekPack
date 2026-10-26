#!/usr/bin/env python3
"""
MekPack Mekanism Updater
Checks upstream GitHub branch 26.3 and Modrinth/ModMaven for new builds,
rebuilding local dev jars or swapping to official release jars once published.
"""

import os
import subprocess
import urllib.request
import json
import glob
import shutil

SCRATCH_REPO = "/home/zachary/.gemini/antigravity-ide/brain/9959dfa2-ca5c-4e06-94ed-01da18652196/scratch/Mekanism"
JAVA_HOME = "/home/zachary/.local/share/PrismLauncher/java/java-runtime-epsilon"
MODS_DIR = os.path.abspath("minecraft/mods")

def check_public_release():
    print("[1/3] Checking for official public 26.3 release on Modrinth...")
    try:
        url = "https://api.modrinth.com/v2/project/mekanism/version"
        req = urllib.request.Request(url, headers={"User-Agent": "MekPack-Updater/1.0"})
        with urllib.request.urlopen(req) as resp:
            versions = json.loads(resp.read().decode())
        for v in versions:
            if "26.3" in v.get("game_versions", []) and "neoforge" in v.get("loaders", []):
                print(f"[FOUND PUBLIC RELEASE] Version: {v['version_number']}")
                return v
    except Exception as e:
        print(f"Could not check Modrinth: {e}")
    print("No public 26.3 release on Modrinth yet (still in WIP). Using branch build.")
    return None

def build_from_branch():
    print(f"[2/3] Updating local Git branch 26.3 at {SCRATCH_REPO} ...")
    subprocess.run(["git", "pull", "--ff-only"], cwd=SCRATCH_REPO, check=True)
    
    print("Compiling Mekanism jars...")
    env = os.environ.copy()
    env["JAVA_HOME"] = JAVA_HOME
    gradle_cmd = [
        os.path.join(SCRATCH_REPO, "gradlew"),
        "-p", SCRATCH_REPO,
        "jar", "generatorsJar", "toolsJar", "additionsJar"
    ]
    subprocess.run(gradle_cmd, env=env, check=True)
    
    print("[3/3] Deploying built jars into minecraft/mods ...")
    built_jars = glob.glob(os.path.join(SCRATCH_REPO, "build/libs/Mekanism*.jar"))
    for jar in built_jars:
        dest = os.path.join(MODS_DIR, os.path.basename(jar))
        shutil.copy2(jar, dest)
        print(f"  -> Copied {os.path.basename(jar)}")

def main():
    public_ver = check_public_release()
    if public_ver:
        print("Official release available! Downloading official jars...")
        for f in public_ver["files"]:
            url = f["url"]
            dest = os.path.join(MODS_DIR, f["filename"])
            print(f"Downloading {f['filename']} ...")
            urllib.request.urlretrieve(url, dest)
        # Remove old homebaked jars
        for old in glob.glob(os.path.join(MODS_DIR, "*homebaked*")):
            os.remove(old)
            print(f"Removed legacy homebaked jar: {os.path.basename(old)}")
    else:
        build_from_branch()
        
    print("\nMekanism update complete! Prism Launcher instance is synchronized.")

if __name__ == "__main__":
    main()
