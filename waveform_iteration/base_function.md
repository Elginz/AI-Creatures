# This is the Fitness Function for the advanced genetic algorithm

## Waveform Library Fitness Functions 

------------------------------------------------------------------------
### How it works


Sawtooth/Triangle Wave: Provides a linear ramp up and down, which can simulate different kinds of sustained movements or contractions.


1. Expand Waveform Library

Introduce additional fundamental MotorType enums. Consider adding:

TRIANGLE: Provides a linear ramp up and down.
SAWTOOTH: Generates a signal that rises linearly and then sharply drops. These new waveforms can lead to different kinds of continuous, controlled, or jerky movements.


1. Expansion of the MotorType Enum

The first step was to formally define the new motor types within the program's logical framework.

What was done: The MotorType enum was expanded to include two new members: TRIANGLE and SAWTOOTH.

# Previous Version
# class MotorType(Enum):
#     PULSE = 1
#     SINE = 2

# Updated Version
class MotorType(Enum):
    PULSE = 1
    SINE = 2
    TRIANGLE = 3
    SAWTOOTH = 4

2. Re-mapping the Genetic Input in the Motor Constructor

With the new motor types defined, the next step was to allow the creature's genetic code (dna) to select them.

What was done: The constructor (__init__) for the Motor class was modified. The logic that interprets the control_waveform gene—a floating-point number between 0.0 and 1.0—was changed from a binary if/else statement to a multi-tiered if/elif/else structure.

# Previous Version
# if control_waveform <= 0.5:
#     self.motor_type = MotorType.PULSE
# else:
#     self.motor_type = MotorType.SINE

# Updated Version
if control_waveform < 0.25:
    self.motor_type = MotorType.PULSE
elif control_waveform < 0.5:
    self.motor_type = MotorType.SINE
elif control_waveform < 0.75:
    self.motor_type = MotorType.TRIANGLE
else:
    self.motor_type = MotorType.SAWTOOTH

Technical Detail: This change partitions the continuous [0.0, 1.0) output range of the control_waveform gene into four equal, distinct segments. This allows a single gene to express four different phenotypes (motor types), significantly increasing the exploratory power of the genetic algorithm without altering the underlying genome structure. The algorithm can now evolve creatures that utilize these more complex movement patterns.



3. Implementing New Waveform Generation Logic

The final and most critical step was to implement the mathematical logic to generate the new waveforms in the get_output method of the Motor class.

What was done: Two new conditional blocks were added to the get_output method, one for MotorType.TRIANGLE and one for MotorType.SAWTOOTH.

Technical Detail:

Phase Calculation: The core of the motor's operation is the self.phase variable, which is advanced by self.freq on each call and wraps around at 2 pi. This continuous, cyclical phase is the input for all waveform calculations.

Triangle Wave Implementation:

The phase is first normalized to a range of [0.0, 2.0) by calculating p_norm = self.phase / np.pi. This simplifies the math for creating a linear wave.
For the first half of the cycle (p_norm < 1.0), the output is calculated using the linear equation 1.0 - 2.0 * p_norm. This creates a line that descends from 1 to -1 as p_norm goes from 0 to 1.
For the second half (p_norm >= 1.0), the output is -1.0 + 2.0 * (p_norm - 1.0). This creates a line that ascends from -1 back to 1 as p_norm goes from 1 to 2. The result is a smooth, continuous triangle wave.
Sawtooth Wave Implementation:

A sawtooth wave is a simple linear ramp from -1 to 1. This is achieved with the single equation output = (self.phase / np.pi) - 1.0.
As self.phase ramps from 0 to 2
pi, the output ramps linearly from -1 to 1. The "sharp drop" characteristic of the wave is handled implicitly by the modulo operation in the phase update line (self.phase = (self.phase + self.freq) % (np.pi * 2)), which causes the phase to instantly reset to 0, and thus the output to reset to -1.
Amplitude Application: In the updated code, the base waveform (ranging from -1 to 1) is calculated first, and the motor's amplitude (self.amp) is applied universally at the end (return output * self.amp). This is slightly cleaner than applying it in each if block.

In summary, these modifications provide a richer set of primitive behaviors for the genetic algorithm to work with, enabling the evolution of more complex and potentially more effective locomotion strategies without requiring any changes to other files like genome.py or the simulation environment itself.

    

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

996 fittest: 2.186 mean: 0.352 mean links 108.0 max links 405
[SKIP] Creature has too many links (256), skipping.
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (256), skipping.
[SKIP] Creature has too many links (171), skipping.
[SKIP] Creature has too many links (202), skipping.
[SKIP] Creature has too many links (283), skipping.
[SKIP] Creature has too many links (148), skipping.
[SKIP] Creature has too many links (122), skipping.
[SKIP] Creature has too many links (148), skipping.
997 fittest: 2.186 mean: 0.39 mean links 82.0 max links 283
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (247), skipping.
[SKIP] Creature has too many links (265), skipping.
[SKIP] Creature has too many links (121), skipping.
[SKIP] Creature has too many links (256), skipping.
998 fittest: 2.186 mean: 0.35 mean links 62.0 max links 265
[SKIP] Creature has too many links (190), skipping.
[SKIP] Creature has too many links (122), skipping.
[SKIP] Creature has too many links (149), skipping.
999 fittest: 2.186 mean: 0.352 mean links 42.0 max links 190
.
----------------------------------------------------------------------
Ran 1 test in 19127.892s


974 fittest: 2.186 mean: 0.378 mean links 60.0 max links 364

Best: 974.csv






