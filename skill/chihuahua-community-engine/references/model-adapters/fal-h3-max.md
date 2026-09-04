# fal.ai MiniMax H3 Max Adapter

Use this adapter for `H3 Max`, `fal H3`, `I2V`, `T2V`, `R2V`, `Classic
Control`, `Direct Explore`, or `Character Lock`. Apply the canonical Chihuahua
lock, selected style adapter, approved continuity, and model-neutral animation
brief first. This file changes route, prompt structure, reference packaging, and
verified fal.ai fields only.

## Live routes

| Creation route | fal.ai endpoint | Source authority |
| --- | --- | --- |
| CLASSIC CONTROL | `minimax/h3-max/image-to-video` | approved Genesis Frame |
| DIRECT EXPLORE | `minimax/h3-max/text-to-video` | text prompt only |
| CHARACTER LOCK | `minimax/h3-max/reference-to-video` | selected character sheet; Late-Z sheet alone by default when Late-Z is active |

A request for the classic first-frame-to-storyboard flow already means CLASSIC
CONTROL. If a user asks to explore or iterate freely, recommend DIRECT EXPLORE.
If they want recognizable Chihuahua without a fixed opening frame, recommend
CHARACTER LOCK. Ask the compact chooser from `SKILL.md` only when video intent
is ambiguous.

## Optimize the seed before prompting

Preserve the premise and every explicit non-negotiable. Improve only its staging:

1. put a readable visual hook in the opening second
2. create a visible cause -> escalation -> payoff
3. use one dominant subject action and one camera purpose per beat
4. sequence actions that would be confusing or anatomically difficult if simultaneous
5. end on a resolved image, reaction, reveal, loop point, or intentional cliffhanger

For a 15-second action scene, prefer about 4-5 principal shots with only brief
impact or detail inserts. Do not give every shot equal duration. Avoid passive
openings, repetitive angles, slideshow pacing, impossible paw/object contact,
quadrupedal action drift, and an unresolved final beat.

For transformations, state `PRE-STATE -> physical impact or occlusion bridge ->
POST-STATE`. Never request continuous liquid morphing of the face, breed, body,
eyes, muzzle, durag, paws, or clothing.

If the seed is loose and the route is DIRECT EXPLORE, offer at most three
meaningfully different T2V-ready concepts. If the seed is clear, silently
optimize one direction and continue.

## Model-aware staging

Exploit H3 Max for coherent short action, explicit camera movement, chronological
multi-shot prompting, physical transitions, and multimodal role assignment.
Reduce risk by simplifying crowded choreography, overlapping limb actions,
tiny continuity-dependent props, dense dialogue, frequent costume changes,
long chains of cuts, or conflicting camera commands.

Timecodes are narrative guidance, not guaranteed frame-accurate edit points.
Cover the entire requested duration with non-overlapping blocks. Each block
contains camera, Chihuahua or subject action, environmental response, and the
physical transition into the next beat.

## Common prompt order

```text
[duration, aspect, one-line premise, selected rendering lock]

[R2V ONLY: REFERENCE ASSIGNMENTS]

IDENTITY INVARIANTS:
[protected Chihuahua traits and current wardrobe/state]

0.0-[time]s — [camera]; [subject action]; [environment]; [transition]
[continue through the full duration]

AUDIO:
[dialogue, effects, ambience, music, NO MUSIC, or NO AUDIO]

CONTINUITY / DO NOT:
[short decisive failure prevention]
```

Use direct concrete verbs. Describe how cuts, wipes, impacts, occlusions, or
camera passes cause transitions. Do not stack contradictory aesthetic labels.
When a broadcast-cel style is active, use its exact rendering and temporal rules,
not generic `modern anime`, `smooth animation`, or `glossy cinematic` language.

## CLASSIC CONTROL — I2V

Create and approve the Genesis Frame with GPT Image 2, then create and approve
the storyboard. Send only the Genesis Frame to `image_url` as the literal first
frame. The I2V output inherits its aspect ratio. Use `end_image_url` only when
the user deliberately approves an exact ending frame.

The storyboard is planning authority for shot order, composition, geography,
action states, rhythm, and transitions. Do not upload a contact sheet by
default: translate it into the chronological prompt. Keep appearance wording
compact because the approved frame carries identity and rendering; spend prompt
budget on bipedal motion, contact points, camera, continuity, and endpoint.

If the opening frame is wrong, repair it before video. If motion fails but the
frame is right, revise only the motion/camera language or simplify the failed
beat.

## DIRECT EXPLORE — T2V

Use `text-to-video` with no references of any modality. The prompt must describe
Chihuahua completely enough to stand alone:

```text
The protagonist is the same tiny tan Chihuahua mascot, upright and bipedal,
with a compact pear-shaped torso, short hind legs and flat paws, short forearms
with paw-like hands, a large Chihuahua head, upright triangular ears, short
narrow muzzle, tiny black nose, and oversized round dark glossy eyes. He wears
a faded dusty-pink durag with the band across his forehead, knot behind his
head, and two hanging tails. Preserve his very small stature, head-to-body
ratio, canine anatomy, simple construction, and exact silhouette in every shot.
```

Then state the selected style's rendering, capture, cadence, camera, and
exclusions in text. T2V is for breadth, not canonical certainty; briefly label
identity as interpretive. If identity or bipedal anatomy repeatedly drifts,
recommend CHARACTER LOCK or CLASSIC CONTROL instead of making the prompt longer
and more conflicted.

## CHARACTER LOCK — R2V

When Late-Z is active, use this default package:

```text
Image 1 = ../../assets/style-adapters/late-z-battle-cel/chihuahua-character-sheet-v1.jpeg;
sole default reference and complete authority for Chihuahua identity, face,
bipedal anatomy, proportions, durag, palette, linework, cel shading, and Late-Z
broadcast rendering.
```

Begin every default Late-Z R2V prompt with:

```text
#Image1 is the sole visual reference and complete authority for the character's
identity, facial construction, anatomy, costume, proportions, palette, linework
and Late-Z rendering. Preserve the same character throughout every angle. Do
not show the sheet, turnaround layout, white background or multiple copies of
the character.
```

Do not also upload the canonical Chihuahua sheet, the scene anchor, raw
broadcast frames, or other internal construction assets. Add another reference
only when the user explicitly requests it, the scene requires another
character, prop, vehicle, environment, motion, or audio authority, or a failed
generation needs a narrow identity or anatomy repair. Keep the Late-Z sheet as
`Image 1`, assign each added reference one narrow role, and never say to blend
all references. Mention only reference slots that are actually used.

Outside Late-Z, preserve the existing default order:

```text
Image 1 = ../chihuahua-character-sheet.png; immutable Chihuahua identity,
breed, face, eye scale, bipedal construction, proportions, fur, durag, and silhouette.
Image 2 = selected adapter-specific Chihuahua sheet when the selected adapter's
existing architecture requires it; translation and era treatment only.
```

For Late-90s OVA, Image 2 is
`../../assets/style-adapters/late-90s-ova-crime-action/chihuahua-character-sheet-v1.png`.
Add further image, video, or audio references only when materially needed and
assign each one a narrow role. In the copy-paste prompt call inputs according
to their actual list order. A host UI may display the same tokens with `#` or
`@`; preserve ordering and roles.

Use the fewest references that fully define the scene. Never say `blend all
references`. Reference images, videos, and audio together may total at most 12
files in the current fal.ai schema. Reference videos must each be 2-15 seconds
with at most 15 seconds combined. Reference audio must be 2-15 seconds with at
most 15 seconds combined and cannot be the only reference modality.

## Verified fal.ai fields

- `duration`: integer seconds; current H3 Max range is 5-15
- `resolution`: `768P` default; use `480P` only for cheaper/faster drafts
- `prompt_expansion_mode`: `balanced` for iteration; offer `quality` for finals
- `aspect_ratio` for T2V: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, or `9:16`
- `aspect_ratio` for R2V: the same choices plus `adaptive`
- I2V aspect follows `image_url`; `end_image_url` is optional
- keep `enable_safety_checker: true`

Prefer `4:3` for Late-Z, Late-90s OVA, or flagship PS2 T2V/R2V unless the
project requires another format. Do not claim 2K, a hidden camera control, or
another field not present in the current endpoint schema.

## Delivery

```text
ROUTE: [CLASSIC CONTROL / DIRECT EXPLORE / CHARACTER LOCK]
SETUP: [endpoint and what to upload, or NO REFERENCES]
REFERENCES: [ordered narrow roles; omit for T2V]
PROMPT: [copy-paste prompt]
FIELDS: [duration, resolution, expansion mode, ratio when applicable]
RISK / NEXT MOVE: [one short note only when useful]
```

For repair, keep the seed premise, route, reference order, identity, approved
state, and style locked. Change only the failed action, camera, transition,
audio, or continuity clause. A route change is explicit: T2V -> R2V for identity
or bipedal drift; R2V -> CLASSIC CONTROL when opening composition or exact
geography must be locked.
