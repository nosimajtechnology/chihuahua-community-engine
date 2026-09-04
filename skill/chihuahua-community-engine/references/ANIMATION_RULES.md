# Animation Rules

## Contents

1. Preserve first
2. Assign reference roles
3. Period motion
4. Rhythm roles and motion budget
5. State changes
6. Model-neutral multi-shot brief
7. Model-neutral one-take brief
8. Audio meaning
9. Final handoff
10. Prompt compression

Animate approved imagery. Do not redesign it.

## Preserve first

- Chihuahua face, eye scale, breed, body proportions, bipedal anatomy, and size
- pink durag, current clothing, and accessories
- props, vehicles, product geometry, and environment
- shot composition and order
- lighting, palette, old-game build, and texture behavior
- screen direction, spatial anchors, and progressive action state

## Assign reference roles

Before animation, assign every reference a primary role: `IDENTITY`, `STYLE`,
`PROJECT`, or `MOTION`. List any intentional secondary role explicitly. A motion
reference controls timing, cuts, pose cadence, camera rhythm, or effects only;
it does not override identity, rendering, palette, environment, or audio.

Ignore source watermarks, captions, crop, letterboxing, interface elements, and
audio unless the user explicitly makes one authoritative.

## Period motion

Use the selected style adapter's motion grammar when it defines one. Otherwise
use the default old-game motion below.

Favor:

- readable key poses
- slightly rigid skeletal movement
- repeated idle or walk cycles
- limited joint articulation
- small head turns and paw gestures
- simple vehicle suspension and engine vibration
- restrained ear and durag-tail follow-through
- simple fog, traffic, water, smoke, light flicker, or parallax
- practical pans, tracks, fixed cuts, and short push-ins

Avoid:

- realistic four-legged dog locomotion
- smooth modern motion capture
- rubbery face or body deformation
- modern cloth or fur simulation
- major secondary animation
- purposeless camera movement
- camera teleportation
- modern drone grammar
- excessive motion blur
- a held-image slideshow when motion is expected

## Rhythm roles and motion budget

Tag every multi-shot beat:

- `HOLD`: tension, observation, strain, or reaction with limited secondary motion
- `BURST`: one decisive movement or action
- `INSERT`: an extremely brief eye, hand, prop, lightning, or impact detail
- `REVEAL`: a readable new state or aftermath that deserves a hold

Storyboard panels do not imply equal duration. Principal shots may breathe;
inserts should remain brief. Give each shot one dominant motion channel:
`SUBJECT`, `CAMERA`, or `EFFECTS`. Keep the other channels restrained. A held
subject may use one optical push-in or environmental effects, not both
aggressively.

## State changes

For transformations, damage changes, wardrobe changes, or animated colorways,
record `PRE-STATE`, `CHANGE ONLY`, and `POST-STATE`. Preserve every unnamed
layer. Prefer a decisive transition between locked states instead of asking the
model to continuously reinterpret the character.

## Model-neutral multi-shot brief

Create this before a named adapter:

```text
ANIMATION BRIEF

DURATION:
SHOT COUNT:
FORMAT:
HISTORICAL BUILD:
VISUAL AUTHORITY:
REFERENCE ROLES:
MOTION PROFILE:
STATE CHANGE:
AUDIO INTENT:

SHOT 1
RHYTHM ROLE:
DOMINANT MOTION:
CAMERA:
SUBJECT ACTION:
ENVIRONMENTAL MOTION:
SPATIAL STATE:
TRANSITION:

[repeat]

CONTINUITY:
PERIOD MOTION RULES:
ESSENTIAL NEGATIVES:
LOOP CONDITION:
```

Give every shot one main action and one dominant motion channel. Use
environmental motion only where it keeps the footage alive or clarifies depth.

When timing is useful, make the shot ranges total the exact requested runtime.
Treat written timecodes as direction unless the selected host documents precise
control.

## Model-neutral one-take brief

Use for a one-shot MINI or BUMPER:

```text
MICRO-MOTION BRIEF

DURATION:
FORMAT:
VISUAL AUTHORITY:
HISTORICAL BUILD:
CONTINUOUS CHIHUAHUA OR SUBJECT MOTION:
OPTIONAL SURFACE OR PALETTE MOTION:
OPTIONAL ENVIRONMENTAL MICRO-MOTION:
CAMERA RULE:
LOOP CONDITION:
CONTINUITY:
AUDIO INTENT:
ESSENTIAL NEGATIVES:
```

Use one continuous behavior instead of a timeline when the motion is simple.
Example: `Chihuahua slowly turns his head toward the ringing flip phone for the
entire clip while the camera remains fixed.`

## Audio meaning

- `NO AUDIO` means generate no sound.
- `NO MUSIC` allows practical ambience and effects but no score or song.
- For separate voiceover, generate no speech and keep the approved script out
  of the video prompt.
- Do not promise a model can generate speech or accept audio unless the current
  interface confirms it.

## Final handoff

Return in this order:

```text
SETUP
[one sentence]

REFERENCE ASSIGNMENTS
[image, storyboard, character, environment, prop, or motion roles]

FINAL PROMPT
[copy-paste prompt]

INTERFACE FIELDS
[only verified or user-supplied fields]
```

Use the fewest references that define the work. Conflicting references weaken
identity.

## Prompt compression

Support full, compressed, strongly compressed, and exact-limit output.

Preserve in order:

1. Chihuahua identity and bipedal anatomy
2. central action, continuity, and state-change delta
3. shot order, rhythm roles, and spatial progression
4. selected style construction and rendering
5. camera, motion profile, and period cadence
6. decisive negatives
7. secondary atmosphere

For an exact limit:

1. write the full prompt
2. remove explanation and duplication
3. compress repeated locks
4. remove secondary atmosphere before identity or continuity
5. count every final character, including spaces and line breaks
6. report the measured count

Never claim a prompt is under a limit without measuring it.
