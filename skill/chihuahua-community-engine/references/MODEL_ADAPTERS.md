# Model Adapters

## Contents

1. Shared preparation
2. Seedance
3. Kling
4. Generic image-to-video
5. Final delivery

Keep the core Chihuahua, storyboard, continuity, and old-game rules independent
from any one video model. Treat model interfaces and limits as changeable.

## fal.ai MiniMax H3 Max

For H3 Max, I2V, T2V, R2V, Classic Control, Direct Explore, or Character Lock,
read [fal-h3-max.md](model-adapters/fal-h3-max.md). That adapter controls route
selection, reference order, seed optimization, prompt structure, and verified
fal.ai fields. It may translate packaging but cannot override Chihuahua
identity, approved continuity, or the selected style adapter.

## Shared preparation

Before adapting, require:

- approved image or storyboard when available
- compact project lock
- model-neutral Animation Brief or Micro-Motion Brief
- reference-role map and selected motion profile when relevant
- explicit pre-state, change-only delta, and post-state for transformations
- requested duration and aspect ratio
- audio intent
- prompt packaging level or exact limit

Use the fewest references that fully define the work. Assign every reference
one primary role: identity, style, storyboard order, environment, prop/vehicle,
or motion. A motion reference cannot silently become rendering or audio
authority.

For Late-Z H3 Max R2V, the fewest complete package is one file: the approved
Late-Z Chihuahua sheet as `Image 1`. It replaces the normal canonical-plus-style
video package for this route only. Add a narrowly assigned reference only when
the user asks for it, the scene materially requires it, or a failed generation
needs a targeted repair; keep the Late-Z sheet first and omit unused slots.

## Seedance

Prefer reference-to-video when the current interface allows it.

Useful role pattern:

```text
@Image 1 = ordered storyboard or shooting plan
@Image 2 = immutable Chihuahua identity and approved rendering authority
@Image 3 = environment authority, only when needed
@Image 4 = decisive prop or vehicle, only when needed
```

When the current interface accepts a video reference, label it `motion cadence
only`. Ignore its characters, rendering, palette, crop, watermark, captions,
and audio unless the user explicitly assigns another role.

For BUMPER or one-shot MINI, use one approved still rather than a contact sheet.

Prompt order:

1. duration, format, and story intent
2. reference assignments
3. Chihuahua identity and bipedal lock
4. historical rendering contract
5. compact project lock
6. state-change lock when relevant
7. selected motion profile, rhythm roles, and dominant motion channels
8. chronological shot plan, or one continuous motion for BUMPER
9. continuity and spatial restrictions
10. audio intent
11. decisive negatives

Use explicit shot order and plain time ranges when helpful. Do not assume
frame-exact timecode control. Do not give every panel equal duration: principal
shots may hold while impact or detail inserts remain brief. If the board becomes
a collage, repeat the order in text or animate shots separately from the same
lock.

If the interface supports audio, still state the exact desired route. Use
`NO MUSIC` for ambience/effects without a score and `NO AUDIO` for silence.

## Kling

When the current interface provides a bound character/Element feature, bind
Chihuahua as the most fragile identity. Use the approved first frame or clean
storyboard as the environment and visual anchor.

Useful authority pattern:

```text
CHARACTER OR ELEMENT = immutable Chihuahua identity
START FRAME OR IMAGE = environment, lighting, palette, and rendering authority
SHOT PLAN = chronological motion authority
```

When Custom Multi-Shot or an equivalent current control is available, place
shot order and durations there and keep global identity/rendering negatives in
the main prompt. When it is unavailable or unverified, use a Genesis Frame and
generate one shot per clip if necessary.

Prompt order:

1. format and duration
2. character and image authority
3. Chihuahua identity, anatomy, and main action
4. environment and spatial relationships
5. historical rendering contract
6. shot plan or one-take behavior
7. continuity
8. audio
9. decisive negatives

Do not claim a named control exists in the user's host unless it is visible or
verified. If the user simply says `Kling`, return the strongest model-neutral
prompt plus concise setup guidance.

## Generic image-to-video

Use the strongest route actually supported:

1. approved ordered storyboard
2. approved first frame
3. text-only project lock

Text-only has the highest continuity risk. Say so briefly only when useful.

Generic prompt order:

```text
INPUT AUTHORITY
REFERENCE ROLES
FORMAT AND DURATION
CHIHUAHUA IDENTITY AND BIPEDAL LOCK
HISTORICAL RENDERING CONTRACT
PROJECT LOCK
STATE CHANGE
MOTION PROFILE AND RHYTHM ROLES
GLOBAL CAMERA AND MOTION
SHOT PLAN OR CONTINUOUS ONE-TAKE MOTION
CONTINUITY
AUDIO
ESSENTIAL NEGATIVES
```

If multi-shot behavior is unknown, do not promise that a contact sheet will be
read in order. Offer one-shot generation from the same lock as the reliable
fallback.

## Final delivery

Return:

```text
SETUP
[what to upload and which mode to choose]

REFERENCE ASSIGNMENTS
[ordered roles]

FINAL COPY-PASTE PROMPT
[adapted prompt]

INTERFACE FIELDS
[only fields confirmed by the user or current interface]
```

For an exact character limit, measure the final copy-paste prompt after all
compression and report the count.
