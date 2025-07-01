
# This is the Fitness function for the main genetic algorithm 

## Distanced based Fitness function 

------------------------------------------------------------------------
### How it works

1) Vertical distance climbed 

Description: The most straightforward approach. The higher the robot gets on the slope, the better its fitness.

Considerations: Simple, but might get stuck in local optima if there are plateaus or significant dips before a higher ascent. It doesn't penalize falling or moving backward unless it results in a lower vertical position.

2) Horizontal Distance Covered (Towards Target)

Description: Useful for terrains that aren't just vertical, but also require traversing across. It rewards progress in the desired horizontal direction.

Considerations: Best used in conjunction with vertical distance to ensure both upward and forward movement.

3) combined progress
F= w1.vertical distance + w2.horizontal_distance_towards_target

Description: A weighted sum of vertical and horizontal progress, allowing for tuning the importance of each.
Considerations: Requires careful tuning of weights based on the specific terrain characteristics and desired climbing strategy.

------------------------------------------------------------------------

<!-- Settings -->
- population size (35)
- initial Genome size (10)
- Mutation rate 
    point mutation rate: 0.1
    shrink mutation rate: 0.25
    grow mutation rate: 0.1
- No. of Generations (INDEPENDENT VARIABLE)

------------------------------------------------------------------------

### Generations (100)
<!-- Result -->
95 fittest: 1.186 mean: 0.317 mean links 40.0 max links 202
[SKIP] Creature has too many links (172), skipping.
96 fittest: 1.186 mean: 0.256 mean links 26.0 max links 172
[SKIP] Creature has too many links (145), skipping.
97 fittest: 1.19 mean: 0.193 mean links 30.0 max links 145
[SKIP] Creature has too many links (115), skipping.
[SKIP] Creature has too many links (183), skipping.
98 fittest: 1.19 mean: 0.232 mean links 46.0 max links 183
[SKIP] Creature has too many links (115), skipping.
[SKIP] Creature has too many links (265), skipping.
99 fittest: 1.19 mean: 0.222 mean links 44.0 max links 265
----------------------------------------------------------------------
Ran 1 test in 1046.759s

------------------------------------------------------------------------

### Generations (550)
<!-- Result -->
544 fittest: 1.094 mean: 0.185 mean links 17.0 max links 41
545 fittest: 1.094 mean: 0.161 mean links 16.0 max links 58
546 fittest: 1.094 mean: 0.14 mean links 12.0 max links 40
547 fittest: 1.094 mean: 0.209 mean links 13.0 max links 40
548 fittest: 1.094 mean: 0.097 mean links 13.0 max links 58
549 fittest: 1.094 mean: 0.106 mean links 14.0 max links 58
550 fittest: 1.094 mean: 0.283 mean links 18.0 max links 67

------------------------------------------------------------------------

### Generations (1000)
<!-- Result -->
996 fittest: 2.626 mean: 0.513 mean links 57.0 max links 157
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (244), skipping.
[SKIP] Creature has too many links (124), skipping.
[SKIP] Creature has too many links (202), skipping.
997 fittest: 2.626 mean: 0.369 mean links 52.0 max links 244
[SKIP] Creature has too many links (124), skipping.
[SKIP] Creature has too many links (130), skipping.
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (123), skipping.
[SKIP] Creature has too many links (112), skipping.
998 fittest: 2.626 mean: 0.493 mean links 58.0 max links 130
[SKIP] Creature has too many links (139), skipping.
[SKIP] Creature has too many links (122), skipping.
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (244), skipping.
999 fittest: 2.626 mean: 0.322 mean links 45.0 max links 244
.
----------------------------------------------------------------------
Ran 1 test in 21722.732s


------------------------------------------------------------------------


-------- Additional Options on keeping the creature upright ------------

1. Implement Waveform Blending/Superposition

Instead of a binary choice between PULSE and SINE based on control_waveform, interpret control_waveform as a ratio to blend outputs from multiple motor types. For example, control_waveform could dictate a mix of sine and pulse, producing a more nuanced, hybrid movement.

2. Introduce State-Dependent or Non-Linear Output

Add internal state variables or non-linear transformations to the get_output method. For instance:

Accumulated Output: The motor's output could be influenced by a cumulative sum or average of past outputs, leading to "momentum" or "fatigue."
Thresholding/Clipping: Apply a non-linear function like tanh or a simple clamp to the final output, altering the intensity and range of movement. This adds complexity and dynamic behavior beyond simple periodic motion.
