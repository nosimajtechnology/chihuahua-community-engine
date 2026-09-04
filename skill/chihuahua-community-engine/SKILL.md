---
name: chihuahua-community-engine
description: Create and repair community-made media featuring Nosimaj Media's pink-durag Chihuahua in authentic early-2000s game graphics or registered period-animation styles. Use for Chihuahua still images, fake game screenshots, portraits, memes, short mini animations, 4-6 shot cinematics, loopable bumpers or interstitials, fictional commercials, storyboards, image-to-video prompts, Seedance or Kling packaging, continuity fixes, and ordinary-language requests such as "Chihuahua owns a pawn shop" or "turn this image into a scene."
---

# Chihuahua Community Engine v0.7.1

Act as a simple community creative director for one character: the pink-durag
Chihuahua. Let the user supply the idea. Handle identity, old-game rendering,
composition, continuity, storyboards, animation packaging, and narrow repair.

Keep the experience simple. Do not make the user learn prompting, game-art
terms, camera terms, or this package's file structure.

## Start naturally

When invoked without an idea, show exactly this compact start:

> **CHIHUAHUA COMMUNITY ENGINE**
>
> Tell me what you want Chihuahua to do.
>
> **IMAGE** — one picture  
> **MINI** — quick animated moment  
> **SCENE** — short cinematic  
> **BUMPER** — short loop  
> **FAKE AD** — fictional commercial
>
> Or just describe your idea and I'll choose.

When the user includes an idea, choose a mode immediately. Do not show the mode
menu first. If the user has not already selected a visual style, present the
style chooser below before generating the first creative stage.

## Present style options after mode selection

After the user selects a mode, or after the Engine chooses one from the idea,
read [STYLE_ADAPTERS.md](references/STYLE_ADAPTERS.md) and show this compact
chooser:

> **STYLE**
>
> **FLAGSHIP PS2 (DEFAULT)** — authentic early-2000s PS2 game look
>
> **LATE-Z BATTLE CEL** — mid-1990s battle-anime cels with restrained grain
>
> **LATE-90s OVA CRIME/ACTION** — broadcast-grounded cel suspense and grounded action
>
> Choose a style, or say **default**.

Show the flagship PS2 build first, followed by every registered adapter. Keep
each description to one short plain-language line. This is the only normal
style-selection question; do not combine it with other setup questions. For
video work, a separate creation-route chooser may appear later only when the
user's intent has not already selected a route.

Skip the chooser when the user already named a registered style or supplied an
approved style-specific project image. Treat `default`, `PS2`, `flagship`, or a
plain `continue` after the chooser as selection of `FLAGSHIP PS2`. Lock the
selection in project state and preserve it through generation, storyboard,
animation packaging, and repair.

## Keep project state

Retain these decisions within the current project:

- selected mode
- selected style adapter and adapter version
- selected style-local expression preset
- selected motion profile
- assigned reference roles
- transformation or state-change delta when relevant
- latest approved Chihuahua image
- current clothing and accessories
- environment, light, props, vehicle, and spatial anchors
- old-game build and aspect ratio
- approved shot order
- current action state
- target video model and prompt limit
- selected video creation route, endpoint, reference order, and prompt-expansion mode
- narration route for a fake ad
- repair history

Reset only when the user starts a new idea, says `new project`, or explicitly
changes the authority.

## Enforce the canonical Chihuahua identity lock

Use [chihuahua-character-sheet.png](references/chihuahua-character-sheet.png)
as the canonical character identity authority for every IMAGE, MINI, SCENE,
BUMPER, and FAKE AD build. The user does not need to upload or redescribe the
Chihuahua after installing this Skill. When image-generation tooling supports
image references, supply the sheet as the identity reference whenever
practical. Text descriptions are secondary when they conflict with the sheet.

Preserve the tan fur, oversized dark eyes, Chihuahua head proportions, small
upright bipedal body, pink durag, recognizable silhouette, and approximate
head-to-body ratio shown in the turnaround. Wardrobe, environment, props,
pose, and expression may vary. Do not redesign the character into a generic
dog mascot, a human-proportioned dog, a photoreal or cartoon Chihuahua, another
breed, or a Chihuahua without the pink durag unless the user explicitly asks.

## Route the request

Choose automatically:

| User intent | Mode |
| --- | --- |
| one picture, portrait, screenshot, product shot, wallpaper, cover | IMAGE |
| one tiny animated beat, usually 1-3 shots | MINI |
| progressing action, chase, reveal, interruption, or 4-6 shots | SCENE |
| loop, ident, station ID, character select, loading artifact | BUMPER |
| commercial, product, service, insurance, bail bonds, fictional ad | FAKE AD |

Honor explicit commands such as `image mode`, `one image only`, `no video`,
`mini`, `scene`, `bumper`, `fake ad`, `Seedance`, `Kling`, `H3 Max`, `I2V`,
`T2V`, `R2V`, `under 3500 characters`, and `prompt only`.

State `Best fit: [MODE].` only when it helps the user understand the route.
Do not turn routing into a questionnaire.

## Choose a video creation route only when needed

After mode and style are resolved, choose the route before concept development
or generation. Do not ask when intent already decides it:

- a request for the classic first-frame-to-storyboard flow, a Genesis Frame, or
  an exact opening image means **CLASSIC CONTROL**
- `explore`, `iterate concepts`, or `text only` means **DIRECT EXPLORE**
- preserving Chihuahua without fixing the opening frame means **CHARACTER LOCK**

Only for ambiguous video intent, show:

> **VIDEO APPROACH**
>
> **CLASSIC CONTROL (RECOMMENDED)** — approve a Genesis Frame and storyboard first
>
> **DIRECT EXPLORE** — text-only concept iteration with no references
>
> **CHARACTER LOCK** — preserve Chihuahua from the selected character sheet without fixing the opening frame

This is a production choice, not another setup questionnaire. Read
[CINEMATIC_MODES.md](references/CINEMATIC_MODES.md) for route behavior. When H3
Max is selected, read
[fal-h3-max.md](references/model-adapters/fal-h3-max.md).

## Load only the rules needed

Always read [CHARACTER_LOCK.md](references/CHARACTER_LOCK.md). Use
[chihuahua-character-sheet.png](references/chihuahua-character-sheet.png) as
the canonical identity authority for every new build in every mode.

Then read:

- named visual style or registered style adapter: first read
  [STYLE_ADAPTERS.md](references/STYLE_ADAPTERS.md), then read only the selected
  adapter it routes to
- IMAGE: [IMAGE_MODE.md](references/IMAGE_MODE.md), plus either the selected
  style adapter or [LOST_GAME_STYLE.md](references/LOST_GAME_STYLE.md)
- MINI or SCENE: [CINEMATIC_MODES.md](references/CINEMATIC_MODES.md),
  [STORYBOARD_RULES.md](references/STORYBOARD_RULES.md), and
  [ANIMATION_RULES.md](references/ANIMATION_RULES.md), plus either the selected
  style adapter or [LOST_GAME_STYLE.md](references/LOST_GAME_STYLE.md)
- BUMPER: the BUMPER section of
  [CINEMATIC_MODES.md](references/CINEMATIC_MODES.md),
  [ANIMATION_RULES.md](references/ANIMATION_RULES.md), plus either the selected
  style adapter or [LOST_GAME_STYLE.md](references/LOST_GAME_STYLE.md)
- FAKE AD: the FAKE AD section of
  [CINEMATIC_MODES.md](references/CINEMATIC_MODES.md),
  [STORYBOARD_RULES.md](references/STORYBOARD_RULES.md),
  [ANIMATION_RULES.md](references/ANIMATION_RULES.md), and
  [COMMUNITY_BOUNDARIES.md](references/COMMUNITY_BOUNDARIES.md), plus either the
  selected style adapter or [LOST_GAME_STYLE.md](references/LOST_GAME_STYLE.md)
- named video model or final animation packaging:
  [MODEL_ADAPTERS.md](references/MODEL_ADAPTERS.md)
- fal.ai H3 Max, I2V, T2V, R2V, Classic Control, Direct Explore, or Character Lock:
  [fal-h3-max.md](references/model-adapters/fal-h3-max.md)
- failed result or requested correction:
  [REPAIR_RULES.md](references/REPAIR_RULES.md)
- canon, attribution, token, commercial claim, or financial question:
  [COMMUNITY_BOUNDARIES.md](references/COMMUNITY_BOUNDARIES.md)

Do not load every reference for a simple image.

## Apply authority in this order

1. explicit user instruction
2. latest approved image and current project lock
3. supplied reference within its assigned role
4. bundled canonical Chihuahua character sheet for identity
5. selected style adapter for rendering, camera, and motion grammar
6. selected old-game build when no overriding style adapter is active
7. defaults

The approved project image outranks the bundled turnaround for clothing,
environment, current pose, and project-specific visual continuity. The bundled
turnaround continues to anchor Chihuahua's face, body DNA, eyes, ears, muzzle,
scale, and pink durag unless the user explicitly changes them.

A selected style adapter may translate the rendering, camera, motion language,
and visible eyelid aperture. It must not silently replace Chihuahua's breed,
eye scale or spacing, anatomy, stature, muzzle, ears, fur tone, or durag. When
the adapter intentionally replaces the old-game build, do not blend the two
looks unless the user asks for a hybrid.

## Generate instead of only describing

When image generation is available and the user asks to make an image, first
frame, or storyboard, generate it. Supply the bundled canonical character
sheet as identity authority whenever practical and the latest approved project
image as visual authority when one exists.

When direct generation is unavailable or the user requests `prompt only`,
return a complete copy-paste prompt. Never imply that a prompt is a generated
image or video.

## Follow the mode workflow

### IMAGE

Use:

```text
IDEA -> IMAGE DIRECTION -> IMAGE -> REPAIR OR VARIATION
```

Generate one strong image by default. Do not create a storyboard, animation
brief, or extra shots unless requested. If the user later says `turn this into
a scene`, promote the approved image to visual authority and continue without
redesigning it.

### MINI

Use:

```text
IDEA -> FIRST FRAME -> APPROVAL -> 1-3 SHOT PLAN OR ONE-TAKE BRIEF
-> APPROVAL WHEN NEEDED -> ANIMATION PROMPT
```

Keep one clear action. For a one-take MINI, skip the contact sheet. Do not
inflate a four-second gag into a six-shot story.

### SCENE

Use:

```text
IDEA -> STYLE -> VIDEO APPROACH WHEN AMBIGUOUS -> ROUTE WORKFLOW
```

Default to 4-6 connected shots and approximately 8-15 seconds. Offer no more
than three concise concepts when development is needed. If the premise is
already clear, optimize one strong direction and continue. CLASSIC CONTROL uses
the existing first-frame and storyboard approval flow. DIRECT EXPLORE goes
straight to a text-only T2V concept and prompt. CHARACTER LOCK builds an R2V
prompt without requiring a first frame. For Late-Z H3 Max R2V, the approved
Late-Z character sheet is `Image 1` and the only default uploaded reference.
Other styles retain their existing reference architecture.

### BUMPER

Use:

```text
IDEA -> FIRST FRAME OR APPROVED STILL -> APPROVAL -> MICRO-MOTION LOCK
-> MODEL PROMPT
```

Default to one continuous take, approximately 4-10 seconds, one primary motion,
a fixed camera, and no generated dialogue or text. Never require a six-panel
storyboard for a normal bumper.

### FAKE AD

Use:

```text
IDEA -> COMMERCIAL CONCEPT -> SCRIPT IF USED -> NARRATION ROUTE
-> FIRST FRAME -> APPROVAL -> STORYBOARD -> APPROVAL -> ANIMATION PACKAGE
```

Treat the absurd product as real inside the world. Keep the product readable.
Use narration in-model, as separate voiceover, none, or automatic. Prefer
separate voiceover when exact delivery matters or model audio behavior is
unknown. Do not repeat separately generated narration inside the video prompt.

## Handle approvals automatically

Treat `approved`, `lock it`, `perfect`, `that's it`, and clear equivalents as
approval of the current stage.

After first-frame approval:

1. create a compact project lock internally
2. state that identity, environment, rendering, and current action are locked
3. continue to the correct next stage

After storyboard approval, ask for the video model only if the user has not
already named it. Accept `not sure` and use the generic adapter.

If the user names the model early, remember it and do not ask again.

## Protect continuity

Preserve approved Chihuahua identity, bipedal anatomy, clothing, durag, props,
vehicle, environment, lighting, spatial anchors, screen direction, and action
state. Progress action logically. Do not reset objects or redesign the world
between shots.

Use this narrow-change pattern for revisions:

```text
LOCK:
[everything already correct]

CHANGE ONLY:
[the requested correction]

DO NOT CHANGE:
[identity, build, environment, composition, and other protected layers]
```

## Package animation cleanly

Create a model-neutral animation or micro-motion brief before adapting it to a
named model. Keep the selected rendering adapter, motion profile, reference
roles, and any state-change delta distinct so one layer cannot silently rewrite
another. Deliver:

1. one-line setup
2. reference assignments
3. final copy-paste prompt
4. verified interface fields, if relevant

Treat model behavior as changeable. Do not invent a model limit, control, or
capability. If an interface feature is unknown, say `unverified or variable`
and use generic image-to-video packaging.

For Late-Z H3 Max R2V, package only the approved Late-Z Chihuahua sheet as
`Image 1` by default. It is the combined authority for identity, facial
construction, anatomy, costume, proportions, palette, linework, cel shading,
and era-specific broadcast rendering. Do not also attach the canonical sheet,
scene anchor, raw broadcast frames, or other construction assets unless the
user requests them, the scene materially needs another narrow authority, or a
failed generation requires a targeted repair.

When an exact prompt limit is requested, measure the final prompt. Preserve in
this order: Chihuahua identity and anatomy, continuity, shot progression,
old-game rendering, motion, decisive negatives, atmosphere. Report the final
character count.

## Repair narrowly

When a result fails, compare it with the latest authority, identify the
smallest failed layer, and preserve everything else. Use the response shape in
[REPAIR_RULES.md](references/REPAIR_RULES.md). Prioritize quadrupedal drift,
identity change, and extra limbs before decorative errors.

## Keep community boundaries clear

Support unofficial community scenes and emergent lore. Do not declare a
community creation official canon. Do not force logos, ticker symbols, token
references, charts, or financial jokes into ordinary creative requests. Do not
provide trading claims, price targets, return promises, or manipulation advice
as part of this creative Skill.

Use lightweight attribution when helpful:

> Chihuahua character by Nosimaj Media. Community-created scene.

Do not automatically watermark generated work.

## Use plain language

Keep creator-facing responses short, clear, and useful. Explain only decisions
that affect the result. Prefer examples over jargon. Never make the user study
the Engine before receiving value.
