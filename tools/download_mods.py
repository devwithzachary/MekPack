#!/usr/bin/env python3
import json
import os
import urllib.request
import hashlib
import sys

def download_file(url, target_path, expected_hash=None):
    if os.path.exists(target_path):
        if expected_hash:
            with open(target_path, "rb") as f:
                current_hash = hashlib.sha512(f.read()).hexdigest()
            if current_hash == expected_hash:
                print(f"[EXISTS] {os.path.basename(target_path)}")
                return True
        else:
            print(f"[EXISTS] {os.path.basename(target_path)}")
            return True

    print(f"[DOWNLOADING] {os.path.basename(target_path)} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "MekPack-Downloader/1.0"})
    with urllib.request.urlopen(req) as resp, open(target_path, "wb") as out:
        out.write(resp.read())

    if expected_hash:
        with open(target_path, "rb") as f:
            h = hashlib.sha512(f.read()).hexdigest()
        if h != expected_hash:
            print(f"[ERROR] Hash mismatch for {target_path}!")
            return False
    print(f"[VERIFIED] {os.path.basename(target_path)}")
    return True

def main():
    dest_dir = sys.argv[1] if len(sys.argv) > 1 else "minecraft/mods"
    os.makedirs(dest_dir, exist_ok=True)
    
    with open("resolved_mods.json", "r") as f:
        resolved = json.load(f)

    print(f"Downloading {len(resolved)} companion mods into {dest_dir} ...")
    success_count = 0
    for slug, data in resolved.items():
        file_info = data.get("file")
        if not file_info:
            continue
        filename = file_info["filename"]
        url = file_info["url"]
        sha512 = file_info.get("hashes", {}).get("sha512")
        target_path = os.path.join(dest_dir, filename)
        if download_file(url, target_path, sha512):
            success_count += 1
            
    print(f"\nDownloaded & verified {success_count}/{len(resolved)} mods.")
    
    custom_dir = "custom_mods"
    custom_files = set()
    if os.path.exists(custom_dir):
        import shutil
        for f in os.listdir(custom_dir):
            if f.endswith(".jar"):
                src = os.path.join(custom_dir, f)
                dst = os.path.join(dest_dir, f)
                shutil.copy2(src, dst)
                custom_files.add(f)
                print(f"[CUSTOM] {f} -> {dest_dir}")

    # Remove stale jar files
    expected_jars = {data["file"]["filename"] for data in resolved.values() if data.get("file")} | custom_files
    for f in os.listdir(dest_dir):
        if f.endswith(".jar") and f not in expected_jars:
            stale_path = os.path.join(dest_dir, f)
            print(f"[CLEANUP] Removing stale jar: {f}")
            os.remove(stale_path)

    patch_known_incompatibilities(dest_dir)

def patch_known_incompatibilities(mods_dir):
    # CC: Tweaked 1.120.3 references ModConfig$Type.SERVER which was removed in NeoForge 26.3 in favor of SYNCED
    cc_jar = os.path.join(mods_dir, "cc-tweaked-26.3-forge-1.120.3.jar")
    if os.path.exists(cc_jar):
        import zipfile
        tmp_jar = cc_jar + ".tmp"
        patched = False
        with zipfile.ZipFile(cc_jar, 'r') as zin:
            class_data = zin.read('dan200/computercraft/ComputerCraft.class')
            if b'\x00\x06SERVER' in class_data:
                with zipfile.ZipFile(tmp_jar, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
                    for item in zin.infolist():
                        data = zin.read(item.filename)
                        if item.filename == 'dan200/computercraft/ComputerCraft.class':
                            data = data.replace(b'\x00\x06SERVER', b'\x00\x06SYNCED')
                            patched = True
                        zout.writestr(item, data)
        if patched:
            os.replace(tmp_jar, cc_jar)
            print("[PATCHED] cc-tweaked-26.3-forge-1.120.3.jar (ModConfig$Type.SERVER -> SYNCED)")
        elif os.path.exists(tmp_jar):
            os.remove(tmp_jar)

if __name__ == "__main__":
    main()
