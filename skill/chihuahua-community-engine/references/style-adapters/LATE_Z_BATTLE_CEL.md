# Late-Z Battle Cel Adapter v1.2

## Contents

1. Purpose and activation
2. Reference assignments
3. Reference-role firewall
4. Rendering lock
5. Chihuahua translation
6. Expression preset
7. Camera and composition
8. Temporal rhythm
9. Motion profiles
10. Exclusions
11. Repair checks

## Purpose and activation

Adapter ID: `late-z-battle-cel-v1`

Adapter version: `1.2`

Display signifier: `LATE-Z BATTLE CEL`

Use for Chihuahua images and cinematics that request Late-Z Battle Cel,
Buu-saga-inspired, mid-1990s DBZ-esque battle anime, or the bundled approved
anchor. This is a render-and-motion adapter. It replaces the default PS2 build
while active; do not mix cel animation with 3D game rendering unless the user
explicitly requests a hybrid.

The adapter borrows period visual grammar only. Do not add franchise
characters, costumes, symbols, attacks, locations, logos, or story canon unless
the user separately requests them.

## Reference assignments

- `../../assets/style-adapters/late-z-battle-cel/chihuahua-character-sheet-v1.jpeg`
  is the bundled Late-Z translation reference for neutral front,
  three-quarter, profile, and rear construction; tan cel palette; dusty-pink
  durag geometry; line economy; simplified fur treatment; and the
  `BATTLE_INTENSE` eyelid-aperture variant. Its SHA-256 is
  `1587dd003cac4b1e54a3ca0f09df55d1a17569ef1cfb675610b6ac816df3bc87`.
- `../../assets/style-adapters/late-z-battle-cel/chihuahua-anchor-v1.png` is the
  approved scene-level reference for atmospheric palette, grain, cel shadows,
  weather, and battle-frame treatment.
- `../chihuahua-character-sheet.png` remains the immutable authority for breed,
  face DNA, eye scale and spacing, muzzle, ears, bipedal anatomy, stature, tan
  fur, and dusty-pink durag.
- A user-approved project image outranks the bundled anchor for that project's
  wardrobe, environment, lighting, pose, and continuity.

When image tooling accepts multiple references, assign the canonical character
sheet to underlying identity, the bundled Late-Z sheet to adapter-specific
character translation, and the scene anchor to rendering/atmosphere when its
role is useful. Never ask either adapter asset to replace the canonical sheet.

Exception for H3 Max R2V: upload only the bundled Late-Z character sheet as
`Image 1` by default. For that route, it is the consolidated authority for
identity, proportions, face, anatomy, costume, palette, linework, cel shading,
and broadcast rendering. Do not also attach the canonical sheet, scene anchor,
or raw broadcast captures unless the user requests them, the scene needs a
separate narrow authority, or a failed result needs a targeted repair.

## Reference-role firewall

Assign every supplied reference a primary role before generation:

- **IDENTITY:** canonical Chihuahua sheet or approved project Chihuahua
- **STYLE:** bundled Late-Z character sheet, approved adapter anchor, and
  target-era cel references
- **PROJECT:** approved frame or storyboard controlling current continuity
- **MOTION:** clips controlling only timing, cuts, camera rhythm, pose cadence,
  or effects behavior

A mixed-era, differently cropped, or off-target animation clip may be useful as
MOTION authority without becoming STYLE authority. Do not inherit its character
designs, costumes, anatomy, palette, aura colors, locations, logos, crop,
letterboxing, watermark, captions, or audio. Reference audio is non-authoritative
unless the user explicitly assigns it an audio role.

## Rendering lock

- original 4:3 mid-1990s television-cel presentation
- confident dark brown-black ink contours, thicker on the outer silhouette and
  thinner on sparse interior marks
- clean simplified forms with two opaque cel values and an occasional third
  highlight; hard-edged shadow shapes and no soft character gradients
- tan fur translated into warm ochre base, pale beige light, and muted umber
  shadow planes; little or no individual fur hatching
- dusty-pink durag translated into rose base, maroon shadow, and restrained pale
  salmon highlight while preserving band, knot, and two tails
- hand-painted backgrounds built from broad opaque shapes, sparse cracks and
  atmospheric color recession rather than dense digital detail
- very light fine analog cel-photography grain, most visible in sky midtones and
  flat paint regions, with restrained broadcast softness and minute color bleed
- grain must remain subordinate to the drawing: no obvious noise effect
- in animation, grain behaves as a stable finishing texture rather than crawling,
  boiling, or redrawing independently every frame

## Chihuahua translation

Keep the exact tiny tan Chihuahua, upright and bipedal, with compact torso,
short limbs, paw-like hands, large ears, short muzzle, tiny nose, oversized dark
eyes, and dusty-pink durag. Preserve canine facial structure and small scale.
Do not give him human musculature, human hands, human eye whites, spiked hair,
or a generic anime-human body.

The normal expression keeps the canonical round visible eye shape. Use the
style-local preset below only for an intense battle expression or when the user
requests the approved-anchor look.

## Expression preset: BATTLE_INTENSE

Preserve exactly two oversized eyes in their canonical positions and at their
canonical scale. Change only the visible eyelid aperture:

- horizontally compressed angular almond or wedge shape
- upper lids descend sharply toward pointed inner corners
- firmer, flatter lower lids
- short bold brow or tension creases directly above the eyes
- nearly black canine fill with dark-brown tone and one small hard white cel
  highlight per eye
- direct, fiercely determined gaze; exhausted but unbroken

Do not add bright irises, large white sclera, extra eyelids, human eye anatomy,
or a permanent angry redesign. Keep the muzzle, nose, ears, mouth, and head
construction unchanged.

## Camera and composition

Favor original-TV-anime framing:

- tense close-ups and medium close-ups for strain or decision
- low three-quarter views and restrained dutch angles for confrontation
- wide aftermath frames that hold small characters against painted terrain
- strong asymmetry, foreground rocks or debris, and clear silhouettes
- practical pans, short push-ins, snap reframes, and decisive cuts

Create dynamism primarily through contrast between compositions: wide frame,
tight strain close-up, extreme detail insert, release, reaction, and aftermath.
Do not solve a static sequence by moving the camera constantly.

Keep 4:3 unless the user explicitly requests another delivery format. Avoid
modern shallow depth of field, glossy lens effects, floating drone movement,
or constant camera motion.

## Temporal rhythm

For MINI, SCENE, BUMPER, or FAKE AD animation briefs:

- use held key poses with limited secondary motion, then short decisive bursts
- let principal shots breathe; do not assign every storyboard panel equal time
- tag each shot as `HOLD`, `BURST`, `INSERT`, or `REVEAL`
- use visibly stepped character-pose changes and repeated drawings rather than
  perfectly smooth interpolation; effects may update faster than the character
- give each shot one dominant motion channel: subject, camera, or effects
- during a held pose, move only restrained effects or one short optical push-in
- favor hard cuts; use a very brief high-contrast or white impact cel only when
  transformation or contact needs punctuation
- use brief hand-drawn smears, speed lines, impact frames, debris or rain
  accents only when the action needs them
- let durag tails, rain, dust, clothing, and background effects move
  economically; do not simulate them with modern fluid physics
- keep facial acting sparse: eye aperture, brow crease, head angle, jaw set,
  and small mouth changes
- preserve the approved cel palette, grain, contour weight, and hard shadows
  through every storyboard panel and generated shot
- keep held contours and cel-shadow geometry stable; no line boil, facial
  redrawing, elastic zooming, or drifting anatomy

The model adapter still controls Seedance, Kling, or generic platform syntax.
This adapter controls the intended visual and motion result.

## Motion profiles

### POWER_UP_TRANSFORM

Build the sequence from discrete states:

1. establish the intact pre-transformation state
2. hold a strain pose while weather, dust, debris, or aura pressure escalates
3. tighten through a restrained push-in or progressively closer hard cuts
4. use one very brief impact or silhouette insert
5. hard-cut to the completed post-transformation state
6. hold the reveal, then show the opponent reaction or environmental aftermath

Record:

```text
PRE-STATE:
CHANGE ONLY:
POST-STATE:
```

The transformation delta controls only the named changes. Preserve identity,
anatomy, proportions, clothing construction, durag geometry, position, and
environment unless named. Never gradually morph the face, body, eyes, or durag
between states.

### IMPACT_MELEE

Use a readable chain: launch, approach silhouette, one strike, very brief
contact insert, follow-through, opponent reaction, aftermath. Use one clear
attack path per principal shot. Do not ask for an extended exchange, multiple
simultaneous attacks, or prolonged overlapping limbs. Preserve exactly one
head, one torso, two forearms, and two hind legs per character through contact.

For an 8-15 second sequence, prefer 4-5 principal shots plus no more than two
brief inserts. Treat written durations as rhythm guidance rather than guaranteed
frame-accurate control.

## Exclusions

- no modern glossy digital-anime finish or remaster coloring
- no airbrushed character gradients, bloom, volumetric light, lens flare, or
  cinematic depth of field
- no 3D, CGI, PS2 render, modern low-poly homage, or photoreal fur
- no heavy grain, VHS noise, scanlines, dust, scratches, film burns, chromatic
  aberration, sepia cast, vignette, CRT border, or compression blocks
- no dense fur strokes or painterly hatching used to fake age
- no franchise character traits, spiked transformation hair, colored battle
  irises, logos, subtitles, HUD, or watermark by default
- no constant camera motion, equal-duration montage rhythm, smooth
  transformation morph, crawling grain, line boil, or modern fluid interpolation

## Repair checks

Repair only the failed layer:

- **too clean:** add a very light fine cel-photography grain and restrained
  broadcast softness; do not change palette, linework, lighting, or composition
- **too painterly:** remove fur hatching and soft blends; restore broad opaque
  paint planes and hard-edged shadows
- **eyes too round during `BATTLE_INTENSE`:** reshape only the visible aperture;
  preserve eye scale, spacing, dark fill, muzzle, ears, and camera
- **eyes become human:** remove bright irises and large white sclera; restore
  oversized dark canine fill and small hard highlights
- **identity drifts:** restore the character sheet's breed, proportions,
  bipedal anatomy, short limbs, muzzle, ears, tan fur, and complete pink durag
- **fake aging becomes obvious:** reduce grain and remove VHS, scratches,
  scanlines, borders, or color casts
- **camera feels stiff:** add shot-scale contrast, one restrained push-in, or a
  decisive cut; do not add continuous orbiting or random handheld movement
- **transformation morphs:** restore locked pre- and post-states; bridge them
  only with effects and a brief hard-cut impact insert
- **held drawing crawls:** stabilize contour, face, cel shadows, and grain;
  animate only the declared dominant motion channel
- **melee creates extra limbs:** reduce the shot to one readable strike and one
  attack path; restore the exact limb count before adding effects
