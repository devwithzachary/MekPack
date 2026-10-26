# 🚀 MekPack: Public Distribution & Publishing Guide

This guide outlines the end-to-end strategy, compliance checklist, and step-by-step procedures for publishing **MekPack: Future Frontiers** to public modpack catalogues and GitHub.

---

## 1. Distribution Platforms Overview

When ready to go public, MekPack should target three distribution channels:

| Platform | Format | Why It Matters | Audience Reach |
| :--- | :--- | :--- | :--- |
| **Modrinth** | `.mrpack` | Modern standard, open-source friendly, 100% compliant with creator licensing, built into modern launchers. | High (Prism, Modrinth App, ATLauncher) |
| **GitHub Releases** | `.mrpack` & `.zip` | Direct source distribution for power users, version history, issue tracking, and transparency. | Developers & Community |
| **CurseForge** | CurseForge ZIP | Legacy catalog with large audience, though requires strict project review. | High (CurseForge App users) |

---

## 2. Mod Licensing & Distribution Ethics

One of the greatest advantages of modern modpack distribution formats (`.mrpack`) is **strict license compliance**:

- **No Redistribution of Third-Party Code**: A `.mrpack` file contains **only metadata, hashes, and download links** (`modrinth.index.json`). It does **not** re-host or distribute companion mod JARs.
- **Creator Support**: When players install the `.mrpack` in their launcher, the client downloads each mod directly from the original author's official Modrinth page. This ensures all creators receive their rightful download credits and analytics.
- **Pack-Specific Overrides**: Custom configs (`config/`), the custom theme (`resourcepacks/`), and our native integration mod (`custom_mods/MekPackContent-26.3-0.0.1.jar`) are bundled in `overrides/`, which is the intended design for modpack customizations.

---

## 3. Pre-Flight Checklist (Initial 0.0.1 Release)

Complete these items before hitting "Publish":

- [x] **1. Transition Upstream Mekanism to Verified Branch Build**:
  - Currently, Mekanism 26.3 is built locally (`custom_mods/Mekanism-*.homebaked.jar`) ahead of its public release.
  - When the official Mekanism team publishes the public 26.3 release to Modrinth/CurseForge, running `python3 tools/update_mekanism.py` will automatically swap to official jars for v1.0.0.
- [ ] **2. Verify Packaging & Version String**:
  - In [tools/export_pack.py](file:///home/zachary/Code/MekPack/tools/export_pack.py), ensure `VERSION = "0.0.1"`.
- [ ] **3. Build Initial Release Packages**:
  ```bash
  python3 tools/export_pack.py
  ```
  Verify outputs in `dist/`:
  - `dist/MekPack-26.3-0.0.1.mrpack`
  - `dist/MekPack-26.3-0.0.1-Prism.zip`

---

## 4. Step-by-Step Platform Publishing

### Step 4.1: Publishing the Public GitHub Repository & Release

1. **Push Master to GitHub**:
   ```bash
   git remote add origin https://github.com/devwithzachary/MekPack.git
   git push -u origin master
   ```
2. **Tag the 0.0.1 Release**:
   ```bash
   git tag -a v0.0.1 -m "MekPack: Future Frontiers v0.0.1 Initial Release"
   git push origin v0.0.1
   ```
3. **Draft a GitHub Release**:
   - Go to `https://github.com/devwithzachary/MekPack/releases/new`.
   - Select tag `v0.0.1`.
   - Title: `MekPack: Future Frontiers 0.0.1 (Minecraft 26.3 NeoForge)`.
   - Description: Copy the summary from [README.md](file:///home/zachary/Code/MekPack/README.md) (featuring the Sovereign Spine overview, AI collaboration note, and mod credits).
   - **Attach Files**: Upload both `dist/MekPack-26.3-0.0.1.mrpack` and `dist/MekPack-26.3-0.0.1-Prism.zip`.

---

### Step 4.2: Submitting to Modrinth

Modrinth is the primary catalogue for modern Minecraft modpacks:

1. **Log In**: Go to [modrinth.com](https://modrinth.com/) and sign in with GitHub.
2. **Create Project**:
   - Click **Create Project** -> Select **Modpack**.
   - **Name**: `MekPack: Future Frontiers`
   - **Summary**: `A high-tech sci-fi industrial modpack centered around Mekanism on Minecraft 26.3 NeoForge with unified companion mod progression.`
   - **Categories / Tags**: `Tech`, `Progression`, `Quests`, `Automation`, `Sci-Fi`.
3. **Body / Description**:
   - Paste the contents of [README.md](file:///home/zachary/Code/MekPack/README.md).
   - Keep the AI collaboration disclosure and mod creator credits intact (Modrinth staff appreciates transparency).
4. **Artwork**:
   - Upload the 512×512 icon from your designer as the project avatar.
   - Upload the background banner.
5. **Publish Version**:
   - Click **Add Version**.
   - Version Number: `1.0.0`
   - Supported Loaders: `NeoForge`
   - Supported Minecraft Versions: `26.3`
   - Upload File: Select `dist/MekPack-26.3-1.0.0.mrpack`.
   - Modrinth will automatically scan `modrinth.index.json`, display all 44 companion mods on your project page, and submit the pack for a quick moderator review (usually approved within a few hours).

Once approved, players can install MekPack **directly from Prism Launcher or Modrinth App by searching "MekPack"**!

---

### Step 4.3: Submitting to CurseForge (Optional)

If you also wish to list on CurseForge:
1. Create a project under the **Modpacks -> Tech** category on CurseForge.
2. Paste the README description and credits.
3. Upload the export package or link back to your Modrinth/GitHub release.

---

## 5. Ongoing Maintenance & Post-Launch Workflow

### Updating Companion Mods
When mod updates are released on Modrinth:
```bash
python3 tools/mod_resolver.py
python3 tools/setup_instance.py
```
Test in Prism Launcher, then export:
```bash
python3 tools/export_pack.py
```

### Player Support & Issue Tracking
Direct players to your GitHub repository's **Issues** tab to report bugs, recipe balance suggestions, or quest flow ideas.
