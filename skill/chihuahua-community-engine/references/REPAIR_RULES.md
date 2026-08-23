# Repair Rules

## Contents

1. Response shape
2. Priority order
3. Narrow repair syntax
4. Common failures
5. Escalate only when necessary

Repair the smallest failed layer. Preserve everything that already works.

## Response shape

Use plain language:

```text
PROBLEM
[one short diagnosis]

FIX
[the minimum important corrections]

RETRY
[copy-paste correction or corrected generation instruction]
```

Do not replace the whole idea when one face, limb, prop, shot, or rendering
layer failed.

## Priority order

1. Chihuahua becomes four-legged
2. Chihuahua identity or breed changes
3. extra limbs, duplicate body, or duplicate Chihuahua
4. durag disappears, changes color, or loses knot/tails
5. body proportions or scale drift
6. image becomes too modern
7. storyboard or action continuity breaks
8. eyes deform, shrink, multiply, or point incorrectly
9. clothing changes unexpectedly
10. props, product, vehicle, or environment mutate
11. motion becomes too realistic or camera becomes too modern

Identity and anatomy outrank decoration.

## Narrow repair syntax

```text
LOCK:
[approved face, identity, clothing, environment, light, camera, composition,
old-game rendering, and every correct element]

CHANGE ONLY:
[one failed layer]

DO NOT CHANGE:
[all protected layers]
```

## Common failures

### He turned into a normal dog or has four legs

State:

```text
Keep the same tiny Chihuahua identity, face, eyes, fur, durag, clothing, and
environment. Change only the body interpretation: he is upright and bipedal,
with one compact torso, exactly two short hind legs below it, and exactly two
small forearms with paw-like hands at the shoulders. No forelegs on the ground,
no quadrupedal spine, no ordinary-dog stance, no extra limbs.
```

### Extra limbs or duplicated body parts

Lock the correct head, torso, outfit, pose, crop, and environment. Specify one
head, one torso, two forearms, two hind legs, and no hidden or duplicated limbs.
If a table, pool edge, or vehicle hides the body, ask the model to keep the
hidden anatomy coherent rather than inventing another leg set.

### Face changed

Use the canonical character sheet and latest approved image as face authority. Lock eye
size and spacing, short muzzle, nose scale, ear shape, fur tone, head-to-body
ratio, and expression range. Change only the failed face.

### Durag changed

Lock faded dusty-pink color, forehead band, rear knot, and hanging tails. If
only color should animate, change the surface hue without changing mesh, knot,
tails, seams, fit, lighting, or any unrelated color.

### Too modern

Correct the asset and render construction, not only the filter:

- lower geometry and facial detail
- use small painted textures
- use baked or vertex lighting and crude shadows
- remove PBR, reflections, depth of field, volumetrics, smooth fur, and modern
  camera polish
- restore practical 4:3 in-engine composition

Do not hide the failure with more pixelation, VHS noise, scanlines, or a CRT
border.

### Eyes deform

Lock two large dark glossy eyes with the same size, placement, forward-facing
orientation, and simple reflections as the authority. Change only the failed
eye region. Do not change the muzzle, ears, durag, expression, or camera.

### One storyboard shot is wrong

Name the shot. Lock all other panels, panel grid, chronology, assets, geography,
lighting, build, and screen direction. Regenerate only the failed panel or
replace it while preserving its exact action state.

### Car, product, or prop changes

Repeat its silhouette, color, scale, side, orientation, wear, and position in
the affected shot. Keep every unrelated character and environment layer locked.

### Bumper jumps, stops, or reverses

Remove timecodes, destination angles, checkpoints, and staged poses. Use one
constant behavior for the entire clip. State: `one continuous uncut take;
constant speed and one direction; no stopping, snapping, reversing, jumping,
or recentering.`

### Camera moves instead of the model

State: `The model rotates. The camera remains completely fixed. The crop,
scale, horizon, and background do not move.`

### Video becomes a slideshow

Keep the storyboard and identity. Add one purposeful action source to each shot
and restrained environmental or camera motion. Do not redesign frames or add
unrelated activity.

## Escalate only when necessary

Regenerate the full frame or sequence only when the whole build is incoherent,
the approved authority is unusable, or several locked layers contradict one
another. Explain the conflict in one sentence before restarting.
