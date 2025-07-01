# Fitness function for genetic algo


## Progress-Based Fitness function 

<!-- THIS IS THE RESULT -->
997 fittest: 2.36 mean: 0.478 mean links 44.0 max links 130
[SKIP] Creature has too many links (135), skipping.
998 fittest: 2.36 mean: 0.331 mean links 37.0 max links 135
[SKIP] Creature has too many links (103), skipping.
[SKIP] Creature has too many links (127), skipping.
999 fittest: 2.36 mean: 0.588 mean links 39.0 max links 127


Take note of the following:
- population size (20)

- initial Genome size (10)

- Mutation rate 
    point mutation rate: 0.1
    shrink mutation rate: 0.25
    grow mutation rate: 0.1

- No. of Generations (1000 avg)

- Average fitness value (0.151)

- Best fitness value (1.082)

997 fittest: 1.082 mean: 0.35 mean links 9.0 max links 27
998 fittest: 1.082 mean: 0.149 mean links 8.0 max links 16
999 fittest: 1.082 mean: 0.151 mean links 6.0 max links 10

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
