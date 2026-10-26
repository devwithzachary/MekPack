#!/usr/bin/env python3
"""
MekPack Content Builder
Packages custom_content/ into custom_mods/MekPackContent-26.3-1.0.0.jar
Uses NeoForge's native lowcodefml loader for zero-dependency runtime datapack/mod injection.
"""

import os
import zipfile
import shutil

SOURCE_DIR = "custom_content"
TARGET_JAR = "custom_mods/MekPackContent-26.3-0.0.1.jar"

def build_content_jar():
    if not os.path.exists(SOURCE_DIR):
        print(f"[SKIP] Source directory {SOURCE_DIR} does not exist yet.")
        return

    os.makedirs(os.path.dirname(TARGET_JAR), exist_ok=True)
    print(f"[BUILD] Packaging {SOURCE_DIR} -> {TARGET_JAR} ...")

    file_count = 0
    with zipfile.ZipFile(TARGET_JAR, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for f in files:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, SOURCE_DIR)
                z.write(full_path, rel_path)
                file_count += 1

    print(f"[SUCCESS] Packaged {file_count} files into {TARGET_JAR}")

if __name__ == "__main__":
    build_content_jar()
