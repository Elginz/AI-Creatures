# This is the Fitness Function for the advanced genetic algorithm

## Terrain Interaction-Based Fitness Functions 

------------------------------------------------------------------------
### How it works

How Your Current Fitness Function Works

The get_distance_travelled() function in your code determines fitness based only on the creature's start and end positions. It calculates:

Vertical Progress: How high the creature climbed (change in the Z-axis).
Horizontal Progress: How far the creature moved towards a target direction.
Combined Fitness (Default): A weighted sum of the two, rewarding creatures that both climb and move forward.
This function has no knowledge of the underlying physics, such as forces or friction.

How Your Proposed Fitness Functions Would Work

Your ideas describe more advanced, physics-based fitness functions. To implement them, you would need to extract detailed information from the PyBullet simulation at every step.

Contact Force Distribution: This would require you to use PyBullet's p.getContactPoints() function during the simulation to get the normalForce for every point where your creature touches the ground. You would then calculate the variance of these forces at the end to determine the fitness.

Grip Strength / Friction Utilization: This is even more complex and would require analyzing lateralFrictionForce1 and lateralFrictionForce2 from the p.getContactPoints() data and comparing it to the maximum possible friction.


1) Contact Force Distribution/Smoothness 

F = 1/(variance_of_contact_forces) 

Description: Encourages solutions that distribute contact forces more evenly among the climbing elements (e.g., legs, wheels), reducing stress on individual points and potentially improving grip.

Considerations: More applicable to multi-legged or multi-wheeled robots.

2) Grip Strength/Friction Utilization

F = sum of [(actual_friction_force)/(maximum_possible_friction_force)] for each contact point

Description: Rewards solutions that effectively utilize the available friction, maximizing grip on slippery or steep surfaces.

Considerations: Requires detailed simulation of friction models.

------------------------------------------------------------------------
<!-- Settings -->
Take note of the following:
- population size (35)
- initial Genome size (10)
- Mutation rate 
    point mutation rate: 0.1
    shrink mutation rate: 0.25
    grow mutation rate: 0.1
- No. of Generations (1000 avg)
------------------------------------------------------------------------
<!-- Result -->



-------- Additional Options on keeping the creature upright ------------

1. Expand Waveform Library

Introduce additional fundamental MotorType enums. Consider adding:

TRIANGLE: Provides a linear ramp up and down.
SAWTOOTH: Generates a signal that rises linearly and then sharply drops. These new waveforms can lead to different kinds of continuous, controlled, or jerky movements.

2. Implement Waveform Blending/Superposition

Instead of a binary choice between PULSE and SINE based on control_waveform, interpret control_waveform as a ratio to blend outputs from multiple motor types. For example, control_waveform could dictate a mix of sine and pulse, producing a more nuanced, hybrid movement.

3. Introduce State-Dependent or Non-Linear Output

Add internal state variables or non-linear transformations to the get_output method. For instance:

Accumulated Output: The motor's output could be influenced by a cumulative sum or average of past outputs, leading to "momentum" or "fatigue."
Thresholding/Clipping: Apply a non-linear function like tanh or a simple clamp to the final output, altering the intensity and range of movement. This adds complexity and dynamic behavior beyond simple periodic motion.