# Style Adapter Router

Use a style adapter only when the user names it, uses a listed alias, supplies
its approved anchor, or clearly requests its visual target. Otherwise retain
the normal old-game build.

## Registered adapters

| Adapter | Aliases and cues | Reference |
| --- | --- | --- |
| `late-z-battle-cel-v1` | Late-Z Battle Cel, Buu-saga-inspired, mid-1990s DBZ-esque battle anime | [LATE_Z_BATTLE_CEL.md](style-adapters/LATE_Z_BATTLE_CEL.md) |
| `late-90s-ova-crime-action-v1` | Late-90s OVA Crime/Action, Yu Yu Hakusho-leaning broadcast cel, analog anime noir, grounded OVA action | [LATE_90S_OVA_CRIME_ACTION.md](style-adapters/LATE_90S_OVA_CRIME_ACTION.md) |

## Style selection menu

Present style choices only after the user selects a mode or the Engine infers
one from the idea. List `FLAGSHIP PS2 (DEFAULT)` first, then every registered
adapter using its display signifier and one short plain-language description.

`FLAGSHIP PS2` routes to [LOST_GAME_STYLE.md](LOST_GAME_STYLE.md). It remains
the default when the user says `default`, `PS2`, `flagship`, or simply asks to
continue after seeing the chooser. A named adapter routes to its registered
reference. Skip the menu when the user already chose a registered style or
supplied an approved style-specific project image.

## Selection rules

When an adapter is selected:

1. record its exact ID and version in project state
2. read only that adapter reference
3. use its bundled adapter character sheet as the style-specific character
   translation; use a bundled scene anchor only when the selected adapter
   explicitly declares one, and never let either replace the canonical identity
   sheet
4. let the adapter replace the default old-game rendering layer unless the user
   explicitly requests a hybrid
5. preserve the selected adapter through Genesis Frame, storyboard, animation
   brief, model packaging, and repair
6. after a generated project frame is approved, use that frame as the strongest
   project-specific visual authority while retaining the adapter rules
7. assign supplied videos or mixed-era references a declared role before use;
   a motion reference must not override identity, rendering, palette, or audio

Style adapters control rendering, palette behavior, camera grammar, motion
grammar, and style-local expression presets. Character identity remains under
`CHARACTER_LOCK.md`. Platform syntax remains under `MODEL_ADAPTERS.md`.

## Visible title signifier

After style selection, append the selected style signifier to every
creator-facing stage title. Use `FLAGSHIP PS2` for the default build or the
adapter's display signifier for a registered adapter. This keeps the selected
rendering system visible throughout the workflow.

Use:

```text
CHIHUAHUA COMMUNITY ENGINE · [ADAPTER DISPLAY SIGNIFIER]
GENESIS FRAME · [ADAPTER DISPLAY SIGNIFIER]
STORYBOARD · [ADAPTER DISPLAY SIGNIFIER]
ANIMATION PROMPT · [ADAPTER DISPLAY SIGNIFIER]
REPAIR · [ADAPTER DISPLAY SIGNIFIER]
```

Do not put a style-local expression preset in the title; state it separately in
the project lock only when useful.
