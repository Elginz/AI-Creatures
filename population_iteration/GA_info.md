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
- population size (INDEPENDENT VARIABLE)
- initial Genome size (10)
- Mutation rate 
    point mutation rate: 0.1
    shrink mutation rate: 0.25
    grow mutation rate: 0.1
- No. of Generations (1000 avg)

------------------------------------------------------------------------

### Population (20)
<!-- Result -->

997 fittest: 2.36 mean: 0.478 mean links 44.0 max links 130
[SKIP] Creature has too many links (135), skipping.
998 fittest: 2.36 mean: 0.331 mean links 37.0 max links 135
[SKIP] Creature has too many links (103), skipping.
[SKIP] Creature has too many links (127), skipping.
999 fittest: 2.36 mean: 0.588 mean links 39.0 max links 127

------------------------------------------------------------------------

### Population (35)
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

------------------------------------------------------------------------

### Population (50)
<!-- Result -->
997 fittest: 2.394 mean: 0.196 mean links 56.0 max links 244
[SKIP] Creature has too many links (135), skipping.
[SKIP] Creature has too many links (130), skipping.
[SKIP] Creature has too many links (109), skipping.
[SKIP] Creature has too many links (135), skipping.
[SKIP] Creature has too many links (127), skipping.
[SKIP] Creature has too many links (171), skipping.
[SKIP] Creature has too many links (166), skipping.
[SKIP] Creature has too many links (130), skipping.
998 fittest: 2.394 mean: 0.156 mean links 53.0 max links 171
[SKIP] Creature has too many links (175), skipping.
[SKIP] Creature has too many links (166), skipping.
[SKIP] Creature has too many links (175), skipping.
[SKIP] Creature has too many links (135), skipping.
[SKIP] Creature has too many links (171), skipping.
[SKIP] Creature has too many links (130), skipping.
[SKIP] Creature has too many links (130), skipping.
[SKIP] Creature has too many links (243), skipping.
999 fittest: 2.394 mean: 0.321 mean links 68.0 max links 243

Ran 1 test in 28896.227s

------------------------------------------------------------------------

