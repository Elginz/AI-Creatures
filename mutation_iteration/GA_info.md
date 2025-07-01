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
    point mutation rate: (INDEPENDENT VARIABLE)
    shrink mutation rate: 0.25
    grow mutation rate: 0.1
- No. of Generations (1000)

------------------------------------------------------------------------

### Grow Mutation Rate (0.01)
<!-- Result -->
997 fittest: 2.21 mean: 0.284 mean links 67.0 max links 337
[SKIP] Creature has too many links (136), skipping.
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (118), skipping.
[SKIP] Creature has too many links (111), skipping.
[SKIP] Creature has too many links (136), skipping.
998 fittest: 2.21 mean: 0.364 mean links 55.0 max links 136
[SKIP] Creature has too many links (129), skipping.
[SKIP] Creature has too many links (239), skipping.
[SKIP] Creature has too many links (115), skipping.
[SKIP] Creature has too many links (111), skipping.
[SKIP] Creature has too many links (117), skipping.
[SKIP] Creature has too many links (167), skipping.
999 fittest: 2.21 mean: 0.241 mean links 54.0 max links 239
.
----------------------------------------------------------------------
Ran 1 test in 22369.799s


------------------------------------------------------------------------

### Grow Mutation Rate (0.1)
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

### Grow Mutation Rate (0.25)
<!-- Result -->
996 fittest: 2.741 mean: 0.331 mean links 49.0 max links 245
[SKIP] Creature has too many links (133), skipping.
[SKIP] Creature has too many links (135), skipping.
[SKIP] Creature has too many links (297), skipping.
[SKIP] Creature has too many links (121), skipping.
997 fittest: 2.741 mean: 0.31 mean links 46.0 max links 297
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (132), skipping.
[SKIP] Creature has too many links (516), skipping.
[SKIP] Creature has too many links (127), skipping.
998 fittest: 2.741 mean: 0.345 mean links 58.0 max links 516
[SKIP] Creature has too many links (111), skipping.
999 fittest: 2.741 mean: 0.27 mean links 29.0 max links 111
.
----------------------------------------------------------------------
Ran 1 test in 21101.217s


------------------------------------------------------------------------

