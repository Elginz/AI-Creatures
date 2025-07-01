# This is the Fitness Function for the advanced genetic algorithm

##  State-Dependent or Non-Linear Output Fitness Functions 

------------------------------------------------------------------------
### How it works

3. Introduce State-Dependent or Non-Linear Output
Add internal state variables or non-linear transformations to the get_output method. For instance:

Accumulated Output: The motor's output could be influenced by a cumulative sum or average of past outputs, leading to "momentum" or "fatigue."

Thresholding/Clipping: Apply a non-linear function like tanh or a simple clamp to the final output, altering the intensity and range of movement.
This adds complexity and dynamic behavior beyond simple periodic motion.

✅ Internal state (accumulated_output) — mimicking momentum or fatigue.

✅ Non-linear transformation (tanh) — modeling saturation behavior.


Original idea:
# output = amplitude * sin(freq * t + phase)

Output is purely periodic — repeats forever in a smooth, predictable wave.

No memory of past outputs — no notion of fatigue or momentum.

Easy to simulate, but not biologically realistic or expressive.



Your enhanced version:
# raw_output = amplitude * sin(freq * time + phase)
# accumulated_output += raw_output
# accumulated_output = clip(accumulated_output, -10, 10)
# final_output = tanh(accumulated_output)

Here’s what that changes:

1. Adds State / Memory
Each motor now remembers past activity.

Like a real muscle, strong repeated movements "build up" — the motor has momentum.

If a joint keeps flexing in one direction, that direction gains bias due to accumulation.

2. Adds Fatigue-like Behavior
tanh() introduces a saturation effect: once the output is too strong, it plateaus.

This means the motor becomes less responsive at high effort, simulating fatigue or limits.

3. Non-Linear Dynamics
Instead of smooth sine waves, output becomes skewed or distorted.

Result: robots or creatures might move more jerkily, or more stably, depending on genome tuning.


✅ Summary: What this change does
Adds internal memory to motor output.

Simulates fatigue, saturation, and momentum.

Produces non-linear, more life-like motion.

Opens the door for emergent behavior in evolved creatures.






🧠 Optional Ideas for Further Biological Plausibility
If you want to take it further:

1. Decay in accumulated output (simulating fatigue recovery):
# At each step, slowly reduce accumulated fatigue
self.accumulated_output *= 0.99

2. Different non-linearities:
final_output = math.atan(self.accumulated_output)  # Smoother saturation

3. Velocity adaptation (derivative effect):
Track how fast the output changes and reduce amplitude:
self.prev_output = getattr(self, 'prev_output', 0)
velocity = raw_output - self.prev_output
self.prev_output = raw_output
final_output = math.tanh(self.accumulated_output - 0.5 * velocity)



------------------------------------------------------------------------
<!-- Settings -->
Take note of the following:
- population size (35)
- initial Genome size (10)
- Mutation rate 
    point mutation rate: 0.1
    shrink mutation rate: 0.25
    grow mutation rate: 0.25
- No. of Generations (1000 avg)
------------------------------------------------------------------------
<!-- Result -->

996 fittest: 2.627 mean: 0.204 mean links 48.0 max links 180
[SKIP] Creature has too many links (148), skipping.
[SKIP] Creature has too many links (118), skipping.
[SKIP] Creature has too many links (177), skipping.
[SKIP] Creature has too many links (180), skipping.
[SKIP] Creature has too many links (154), skipping.
[SKIP] Creature has too many links (136), skipping.
997 fittest: 2.627 mean: 0.371 mean links 58.0 max links 180
[SKIP] Creature has too many links (154), skipping.
[SKIP] Creature has too many links (101), skipping.
998 fittest: 2.627 mean: 0.338 mean links 46.0 max links 154
[SKIP] Creature has too many links (196), skipping.
[SKIP] Creature has too many links (119), skipping.
[SKIP] Creature has too many links (111), skipping.
[SKIP] Creature has too many links (155), skipping.
[SKIP] Creature has too many links (185), skipping.
[SKIP] Creature has too many links (357), skipping.
999 fittest: 2.627 mean: 0.283 mean links 69.0 max links 357
.
----------------------------------------------------------------------
Ran 1 test in 14488.603s


Best result: csv 876 fittest: 2.627 mean: 0.329 mean links 68.0 max links 529
