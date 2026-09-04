# Cinematic Modes

## Contents

1. Shared first-frame rule
2. MINI
3. SCENE
4. BUMPER
5. FAKE AD

Use this file for MINI, SCENE, BUMPER, and FAKE AD. Keep each format at the
smallest useful scale.

## Shared first-frame rule

Use `references/chihuahua-character-sheet.png` as the automatic identity
authority for every first frame in MINI, SCENE, BUMPER, and FAKE AD. Supply it
as an image reference whenever the generation tool supports references.

For a new visual build, create one strong first frame before expansion. It sets:

- Chihuahua identity, clothing, and scale
- props and vehicles
- environment and spatial anchors
- time, weather, lighting, and palette
- console build and rendering fidelity
- tone and camera potential

Do not expand a visibly wrong first frame. After approval, preserve it as the
project's visual authority.

## MINI

Purpose: one simple animated Chihuahua moment.

Defaults:

- 4-8 seconds
- 1-3 shots
- one action or reaction
- simple camera and easy motion
- no extra lore or subplot

Examples:

- Chihuahua slowly opens the refrigerator at 3 AM.
- Chihuahua notices someone across the diner.
- Chihuahua answers his flip phone beside a pool.

Use a one-take Micro-Motion Brief when one shot is strongest. For 2-3 shots,
write a compact continuous shot plan. Use a visual storyboard only when it will
meaningfully improve continuity or the user asks for one.

Good MINI progression:

1. readable starting state
2. one action or discovery
3. reaction, reveal, or loop point

Avoid multiple locations, several props changing hands, long dialogue, or an
action that cannot read in the runtime.

## SCENE

Purpose: a short connected cinematic.

Defaults:

- 8-15 seconds
- 4-6 shots
- one clear premise
- one continuous location or motivated movement between connected spaces
- progressive action
- payoff, interruption, reveal, decision, or cliffhanger

When concept development is needed, offer no more than three concise routes.
Each route contains:

- premise
- main visual
- progression
- ending

If the user's premise is already strong, do not make them choose from options.
Optimize one direction and continue through the selected creation route.

For CLASSIC CONTROL, create the Genesis Frame, obtain approval, create a clean
continuous storyboard using `STORYBOARD_RULES.md`, then build the model-neutral
Animation Brief and H3 Max I2V prompt. Upload the Genesis Frame as the opening
frame; the storyboard is planning authority and is not uploaded by default.

For DIRECT EXPLORE, skip image generation and references and build a fully
descriptive H3 Max T2V concept. For CHARACTER LOCK, skip the Genesis Frame and
use the selected character sheet as H3 Max R2V authority. When Late-Z is active,
the approved Late-Z sheet is `Image 1` and the only default uploaded reference.
Read `model-adapters/fal-h3-max.md` for exact packaging.

## BUMPER

Purpose: a short loopable intermission, station ID, menu artifact, strange
portrait, loading fragment, or character showcase.

Defaults:

- 4-10 seconds; use 6 seconds when unspecified
- one approved image
- one continuous uncut take
- one primary persistent motion
- no more than two subtle supporting motion layers
- fixed camera by default
- 4:3 historical framing when appropriate
- no generated dialogue, music, or text by default

Useful types:

- rotating model viewer
- character-select idle
- loading-screen fragment
- station ident
- strange portrait
- empty environmental loop
- technical-difficulties artifact
- micro-advertisement with no full script

Workflow:

```text
IDEA OR APPROVED STILL -> FIRST FRAME IF NEEDED -> APPROVAL
-> MICRO-MOTION LOCK -> MODEL PROMPT
```

If the user supplies an approved still, skip redundant research and
regeneration. Use it as identity, render, environment, framing, and start-state
authority.

Describe motion as continuous behavior:

- `slowly and steadily for the entire clip`
- `one continuous uncut take`
- `constant speed in one direction`
- `the model rotates; the camera remains fixed`
- `change only the approved texture color`

Avoid timecodes, checkpoints, staged poses, and several camera moves for a
simple loop. These often create jumping or stopping.

Micro-Motion Lock:

```text
SOURCE:
DURATION:
VISUAL AUTHORITY:
PRIMARY SUBJECT MOTION:
SURFACE OR PALETTE MOTION:
ENVIRONMENTAL MICRO-MOTION:
CAMERA:
LOOP CONDITION:
AUDIO INTENT:
TEXT INTENT:
DO NOT CHANGE:
```

## FAKE AD

Purpose: a sincere fictional commercial that exists inside the Chihuahua
world.

Defaults:

- 8-15 seconds
- 4-6 shots
- absurd product or service treated as real
- immediate visual cold open
- high product readability
- no generated text inside images by default
- no music by default
- optional narrator starting after the opening image

Use these gates only as needed:

1. commercial concept
2. narrator script, if narration is used
3. narration route
4. first frame
5. storyboard
6. animation package

Do not bury a beginner in all six gates at once. Reveal only the current step.

Commercial concept:

```text
PRODUCT OR SERVICE:
FICTIONAL COMPANY:
CAMPAIGN OR TAGLINE:
ABSURD CLAIM:
SETTING:
TONE:
DURATION AND SHOTS:
NARRATION:
```

Invent only missing fields. Offer 2-3 concepts only when asked or when the raw
idea genuinely needs development.

For a 15-second narrated ad, target roughly 30-45 spoken words. This is a pacing
guide, not a model limit. Prefer:

1. problem or declaration
2. product name
3. absurd but sincere benefit
4. proof, feature, model, or variant
5. fictional company tag

Narration routes:

- `IN_MODEL`: include exact approved copy only when the selected host exposes
  reliable speech controls
- `SEPARATE`: prohibit generated dialogue in the video prompt and return a
  clean voiceover script plus voice brief
- `NONE`: tell the story with action, ambience, effects, and later-added text
- `AUTO`: choose separate voiceover when behavior is unknown or voice quality
  matters

For separate voiceover, never repeat the script in the video prompt. Leave
visual breathing room for it.

Default ad shot grammar:

1. silent visual hook or problem
2. first clear product/service reveal
3. proof, feature, or character use
4. absurd escalation
5. prestige close-up or reaction
6. hero finish and fictional corporate tag for editing

Keep the product stable between shots. If it changes color, change only the
surface or approved colorway—not its geometry, fit, knot, seams, or scale.

After the primary ad, offer related stills only if useful: hero portrait,
fictional magazine image, product detail, colorway card, package shot, or audio-
only version. Do not force campaign expansion.
