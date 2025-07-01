<h1 align="center"> Mountain Climbing Creatures </h1>


## Introduction
The goal of this project is to adapt the existing evolutionary algorithm so the creatures can
evolve to attempt the task of climbing a mountain. Several methods were developed for the
creatures to progressively learn and adapt to efficiently to climb the mountain.
Through iterative testing and evolution, the aim is to witness the emergence of creatures that
demonstrate the remarkable ability to climb the mountain, showcasing the genetic algorithms
in evolving solutions to complex problems.

Overview of the Genetic Algorithm
The creature's fitness function would need to be changed for it to climb the mountain. A first
genetic algorithm is created so that the creature's distance travelled would include its
weighted vertical distance.
The following are the mutation mechanisms:
- Population
- Generation
- Grow Mutation Rate

Additional experiments such as changes to the motor classes or further add ons include:
- Triangle and Sawtooth waveforms
- State-dependent or Nonlinear
- Sensory Inputs

Fitness Evaluation
The initial fitness of the creature is dependent on its vertical and horizontal distance
travelled. A metric is used to assess each creature’s efficiency and overall furthest distance.
It’s combined fitness is evaluated in the formula:

<h5 align="center"> Combined Fitness = 0.7 x Vertical Distance + 0.3 x Horizontal Distance </h1>
