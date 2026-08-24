# Lost-Game Style Rules

## Contents

1. Default build
2. PS2 construction
3. Optional adjacent builds
4. Character and environment construction
5. Camera behavior
6. Modern exclusions
7. Optional screenshot grounding

Make every result look like raw real-time footage from one coherent old console
game. Build the old game first. Treat “retro” as a consequence, not a filter.

## Default build

When the user gives no era, use:

```text
BUILD: mid-generation PS2-style in-engine cutscene, approximately 2004
PRESENTATION: practical urban/open-world game camera
HISTORICAL FRAME: 4:3
CHARACTERS: simplified low-detail meshes, rigid faces and slightly stiff animation
TEXTURES: small, blurry or lightly pixelated photographic/painted maps
LIGHTING: baked or vertex-lit with limited dynamic shadows
ENVIRONMENT: modular, sparse-to-moderate density, visible LOD and modest draw distance
MATERIALS: simple diffuse color with crude highlights; no modern PBR
```

Use a modern delivery canvas only when requested. Preserve 4:3 composition
inside it when historical framing matters.

## PS2 construction

Favor:

- obvious low-detail polygon construction
- simplified faces, paws, clothing, vehicles, and props
- painted seams, folds, labels, and surface detail
- 128-256px hero textures only where useful; smaller textures elsewhere
- repeated level pieces and low-detail background objects
- baked light, vertex color, blob or crude projected shadows
- rigid facial changes and limited joint articulation
- modest fog, short-to-medium draw distance, and visible LOD
- practical pans, push-ins, tracks, and fixed-angle cuts
- restrained aliasing and capture softness

## Optional adjacent builds

Use these only when the idea or user points there:

### PS1, approximately 1998-2000

- very crude faceted meshes
- 32-128px unfiltered textures
- affine texture warping and swimming
- vertex snapping and slight polygon jitter
- broad Gouraud gradients
- ordered dithering and jagged edges
- tiny environments, heavy fog, simple blob shadows
- very stiff animation and fixed or crude practical cameras

### Early sixth generation, approximately 2000-2003

- cleaner low-poly geometry than PS1
- simple skeletal animation
- 128-256px textures where appropriate
- basic dynamic shadows and simple specular highlights
- larger but still clearly limited environments
- no modern lighting stack

### Dreamcast-like arcade clean

- bright clean arcade presentation
- readable silhouettes and saturated baked color
- simple specular response
- low tracking cameras and strong parallax
- early-sixth-generation geometry without modern detail

## Character and environment construction

Build Chihuahua as a crude game asset from the start. Do not create a detailed
modern dog and pixelate it afterward.

Build locations from:

- large simple floor and wall meshes
- repeated modular architecture
- angular curves
- simple skyboxes
- flat or crossed-plane foliage
- low-detail furniture and vehicles
- sparse crowds and repeated NPC types
- painted detail instead of dense geometry

Leave negative space. Old games did not fill every surface with props.

## Camera behavior

Favor:

- fixed practical cuts
- low ground-level angles
- high overheads
- profile and rear-follow views
- short push-ins
- simple pans and basic tracking
- occasional dutch angle
- a strong foreground object when it clarifies depth

Use one reason per angle: reveal space, clarify action, show scale, protect
continuity, or land the payoff. Dynamic does not mean random.

Avoid repeated centered eye-level medium shots, drone-like gliding, excessive
handheld shake, shallow modern depth of field, or glossy commercial camera
movement.

## Modern exclusions

Use only the decisive exclusions for the likely failure:

- no Unreal Engine or modern AAA look
- no modern Blender low-poly homage
- no concept art or illustration
- no modern animated-film mascot design
- no dense fur strands, skin detail, or sculpted anatomy
- no PBR, ray tracing, global illumination, ambient occlusion, or realistic reflections
- no modern soft shadows, volumetric light, bloom, or cinematic depth of field
- no smooth cloth, fur, or facial simulation
- no fake VHS or CRT effect used to hide modern assets
- no heavy filter applied over a modern render
- no HUD, caption, logo, or text unless requested

Positive construction instructions come first. Do not bury the scene under a
large negative list.

## Optional screenshot grounding

When the user names a specific original game, platform, or year and visual
search is available, inspect authentic original-release gameplay or in-engine
cutscene screenshots before the first image. Use one primary title and no more
than two close period comparisons. Exclude remasters, mods, altered ports,
promotional renders, fan art, and AI images.

Use screenshots only to confirm rendering density, textures, lighting, camera,
fog, shadows, and hardware limits. Do not copy their character, location,
composition, or story.

Keep this invisible or summarize it in one short line. Do not delay a beginner
with research details. If reliable evidence is unavailable, use the internal
build above and say so only when relevant.
