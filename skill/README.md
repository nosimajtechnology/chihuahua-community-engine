# Skill source

`chihuahua-community-engine/` is the Skill exactly as ChatGPT sees it:
`SKILL.md`, `agents/openai.yaml`, and the `references/` it reads. This folder
is the source of truth. Edit these files, never a zip.

The installable zip is built from here:

```
python scripts/build_release.py
```

That validates the folder (one `SKILL.md` with `name` and `description`,
every link resolving, every file within the upload limits) and writes
`dist/chihuahua-community-engine.zip` — a zip whose only top-level entry is
this folder, which is the shape ChatGPT's **Skills → Create → Upload from
your computer** accepts. Pushing a `v*` tag runs the same build and attaches
the zip to a GitHub Release.

The character sheet in `references/` is the copy the Skill reads at run time.
The one in `/assets` is the same file, kept there so the README can show it.
