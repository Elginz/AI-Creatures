# This is the Fitness Function for the advanced genetic algorithm

## Sensory Fitness Iteration 

------------------------------------------------------------------------
### How it works

Of course. You've implemented a major and fascinating new feature: sensory input. Your creatures can now react to their environment—specifically, to their own orientation—to control their motors. This is a significant step up from running pre-programmed motor patterns.

Let's break down the differences file by file to see how you achieved this.

Summary of the Core Idea
The goal is to make creatures that can sense when they are tilted upwards (climbing a slope) and change their motor behavior in response. To do this, you've:

Added new genes to the DNA to control how a motor reacts to sensor data.

Created a new motor type that, instead of following a fixed pattern, takes a sensor value as input.

Hooked up a "sensor" in the simulation that measures the creature's pitch (its up/down tilt).

Fed this sensor value into the new motors to drive the creature's movement.

File-by-File Breakdown of Differences
Here are the specific changes you made in each file to implement this system.

1. genome.py — Defining the "Sensor Genes"
This file was changed to add the genetic material for the new sensory capabilities.

New Genes in get_gene_spec():

"sensor-gain": {"scale": 4.0}: You've added a "gain" gene. This will control how strongly the motor reacts to the sensor input. A high gain means a small tilt will cause a big motor response.

"sensor-bias": {"scale": 2.0}: You've added a "bias" gene. This adds a constant offset to the motor's output, allowing it to be active even when there is no sensor input.

Processing New Genes in get_gene_dict():

You added special logic to process these new genes. The code (gene[ind] - 0.5) * scale shifts the gene's value from a range of [0, scale] to [-scale/2, +scale/2]. This is crucial because it allows the gain and bias to be either positive or negative, giving the evolution more creative freedom.

Storing New Genes in URDFLink:

The URDFLink class constructor (__init__) and the genome_to_links method have been updated to accept and store sensor_gain and sensor_bias for each link.

2. creature.py — Creating the Sensor and the Reactive Motor
This file implements the logic for the creature to sense its orientation and for the motors to react to that sense.

New SENSOR_DRIVEN Motor Type:

The MotorType enum now includes SENSOR_DRIVEN.

The Motor class's __init__ method now uses the control_waveform gene to select one of three motor types, with SENSOR_DRIVEN being an option.

The Motor constructor now accepts and stores the gain and bias values from the genome.

Sensor-Driven Motor Logic in get_output():

The get_output method in the Motor class now accepts a sensor_value as an argument.

If the motor is SENSOR_DRIVEN, its output is calculated with the formula np.tanh(sensor_value * self.gain + self.bias). The tanh function is a great choice here as it squashes the output into a clean range between -1 and 1, preventing runaway motor values.

For the other motor types (PULSE, SINE), the logic remains the same, ignoring the sensor value.

Creature's Internal Sensor (update_sensors, get_pitch):

The Creature class now has a new variable, self.pitch, to store its current tilt.

A new method, update_sensors, takes the creature's orientation (as a quaternion) from the physics engine. It uses p.getEulerFromQuaternion to convert this into Euler angles and extracts the pitch (the rotation around the Y-axis).

A get_pitch method allows the simulation to retrieve this value.

3. simulation.py — Connecting the Sensor to the Motor in Real-Time
This file is the "glue" that connects the creature's physical state in the simulation to its brain (the sensor-driven motors).

Updating the Sensor in run_creature():

Inside the main simulation loop, after getting the creature's latest position and orientation (pos, orn), you now immediately call cr.update_sensors(orn). This ensures that every simulation step, the creature's internal sense of its own tilt is up-to-date.

Passing Sensor Data to Motors in update_motors():

This is the most critical change. Before updating the motors, the code now first asks the creature for its current pitch: pitch_value = cr.get_pitch().

It then loops through the motors and passes this pitch_value directly to each motor's get_output function: velocity = m.get_output(pitch_value).

In summary, you have successfully created a closed-loop system. The simulation tells the creature its orientation, the creature senses its pitch, and that pitch value is used to drive the motors, which in turn affects the creature's movement and new orientation in the simulation on the next step. This allows for the evolution of much more intelligent and reactive behaviors.




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
978 fittest: 264.041 mean: 20.734 mean links 14.0 max links 41
979 fittest: 264.22 mean: 29.712 mean links 17.0 max links 49
980 fittest: 264.22 mean: 10.248 mean links 19.0 max links 67
981 fittest: 264.22 mean: 12.59 mean links 20.0 max links 91
982 fittest: 264.22 mean: 10.119 mean links 17.0 max links 82
983 fittest: 264.22 mean: 11.118 mean links 16.0 max links 55
984 fittest: 264.22 mean: 11.098 mean links 14.0 max links 49
985 fittest: 264.22 mean: 13.906 mean links 16.0 max links 43
986 fittest: 264.22 mean: 11.9 mean links 17.0 max links 46
987 fittest: 264.22 mean: 11.938 mean links 13.0 max links 34
988 fittest: 264.22 mean: 12.858 mean links 15.0 max links 35
989 fittest: 264.22 mean: 17.056 mean links 15.0 max links 70
990 fittest: 264.22 mean: 18.149 mean links 17.0 max links 43
991 fittest: 264.22 mean: 14.822 mean links 14.0 max links 53
992 fittest: 264.22 mean: 14.217 mean links 21.0 max links 47
993 fittest: 264.22 mean: 10.972 mean links 17.0 max links 43
994 fittest: 264.22 mean: 11.338 mean links 17.0 max links 55
995 fittest: 264.22 mean: 17.022 mean links 15.0 max links 45
996 fittest: 264.22 mean: 10.419 mean links 15.0 max links 53
997 fittest: 264.22 mean: 16.554 mean links 18.0 max links 70
998 fittest: 264.22 mean: 19.225 mean links 16.0 max links 43
999 fittest: 264.22 mean: 9.909 mean links 15.0 max links 46
.
----------------------------------------------------------------------
Ran 1 test in 13692.926s




