# Animation Rules

## Contents

1. Preserve first
2. Period motion
3. Model-neutral multi-shot brief
4. Model-neutral one-take brief
5. Audio meaning
6. Final handoff
7. Prompt compression

Animate approved imagery. Do not redesign it.

## Preserve first

- Chihuahua face, eye scale, breed, body proportions, bipedal anatomy, and size
- pink durag, current clothing, and accessories
- props, vehicles, product geometry, and environment
- shot composition and order
- lighting, palette, old-game build, and texture behavior
- screen direction, spatial anchors, and progressive action state

## Period motion

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

## Model-neutral multi-shot brief

Create this before a named adapter:

```text
ANIMATION BRIEF

DURATION:
SHOT COUNT:
FORMAT:
HISTORICAL BUILD:
VISUAL AUTHORITY:
AUDIO INTENT:

SHOT 1
CAMERA:
CHIHUAHUA ACTION:
ENVIRONMENTAL MOTION:
SPATIAL STATE:
TRANSITION:

[repeat]

CONTINUITY:
PERIOD MOTION RULES:
ESSENTIAL NEGATIVES:
LOOP CONDITION:
```

Give every shot one main action and one dominant camera idea. Use environmental
motion only where it keeps the footage alive or clarifies depth.

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
2. central action and continuity
3. shot order and spatial progression
4. old-game construction and rendering
5. camera and period motion
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
