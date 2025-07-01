# Introduce State-Dependent or Non-Linear Output
# Add internal state variables or non-linear transformations to the get_output method. For instance:

# Accumulated Output: The motor's output could be influenced by a cumulative sum or average of past outputs, leading to "momentum" or "fatigue."

# Thresholding/Clipping: Apply a non-linear function like tanh or a simple clamp to the final output, altering the intensity and range of movement.
# This adds complexity and dynamic behavior beyond simple periodic motion.


import genome 
from xml.dom.minidom import getDOMImplementation
from enum import Enum
import numpy as np
import math

class MotorType(Enum):
    PULSE = 1
    SINE = 2

class Motor:
    def __init__(self, frequency=1.0, amplitude=1.0, phase=0.0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.time = 0
        # Internal state for simulating momentum effects
        self.accumulated_output = 0 

    def step(self):
        # increments the motor's internal time counter
        self.time += 1

    def get_output(self):
        # Basic sine wave output based on internal clock
        raw_output = self.amplitude * math.sin(self.frequency * self.time + self.phase)

        # Accumulate for fatigue/momentum effect
        self.accumulated_output += raw_output

        # Normalize accumulated output such as keeping it within a range)
        self.accumulated_output = max(min(self.accumulated_output, 10), -10)

        # Apply tanh to simulate saturation/fatigue
        final_output = math.tanh(self.accumulated_output)

        return final_output


class Creature:
    def __init__(self, gene_count):
        self.spec = genome.Genome.get_gene_spec()
        self.dna = genome.Genome.get_random_genome(len(self.spec), gene_count)
        self.flat_links = None
        self.exp_links = None
        self.motors = None
        self.start_position = None
        self.last_position = None

    def get_flat_links(self):
        if self.flat_links is None:
            gdicts = genome.Genome.get_genome_dicts(self.dna, self.spec)
            self.flat_links = genome.Genome.genome_to_links(gdicts)
        return self.flat_links

    def get_expanded_links(self):
        self.get_flat_links()
        if self.exp_links is not None:
            return self.exp_links
        exp_links = [self.flat_links[0]]
        genome.Genome.expandLinks(self.flat_links[0], self.flat_links[0].name, self.flat_links, exp_links)
        self.exp_links = exp_links
        return self.exp_links

    def to_xml(self):
        self.get_expanded_links()
        domimpl = getDOMImplementation()
        adom = domimpl.createDocument(None, "start", None)
        robot_tag = adom.createElement("robot")
        robot_tag.setAttribute("name", "pepe")
        for link in self.exp_links:
            robot_tag.appendChild(link.to_link_element(adom))
        for i, link in enumerate(self.exp_links):
            if i == 0:
                continue  # skip the root node
            robot_tag.appendChild(link.to_joint_element(adom))
        return '<?xml version="1.0"?>' + robot_tag.toprettyxml()

    def get_motors(self):
        self.get_expanded_links()
        if self.motors is None:
            self.motors = [Motor(l.control_waveform, l.control_amp, l.control_freq)
                           for l in self.exp_links[1:]]
        return self.motors

    def update_position(self, pos):
        if self.start_position is None:
            self.start_position = pos
            if not hasattr(self, 'position_history'):
                self.position_history = []
        else:
            self.last_position = pos
        if hasattr(self, 'position_history'):
            self.position_history.append(pos)

    def get_distance_travelled(self, fitness_type="combined", target_direction=(1, 0), weights=(0.7, 0.3)):
        if self.start_position is None or self.last_position is None:
            return 0
        p1 = np.asarray(self.start_position)
        p2 = np.asarray(self.last_position)
        if fitness_type == "vertical":
            return max(p2[2] - p1[2], 0)
        elif fitness_type == "horizontal":
            horizontal = np.array([p2[0] - p1[0], p2[1] - p1[1]], dtype=np.float64)
            dir_vec = np.array(target_direction, dtype=np.float64)
            dir_vec /= np.linalg.norm(dir_vec) if np.linalg.norm(dir_vec) > 0 else 1.0
            return max(np.dot(horizontal, dir_vec), 0)
        elif fitness_type == "combined":
            w1, w2 = weights
            vertical = max(p2[2] - p1[2], 0)
            horizontal = np.array([p2[0] - p1[0], p2[1] - p1[1]], dtype=np.float64)
            dir_vec = np.array(target_direction, dtype=np.float64)
            dir_vec /= np.linalg.norm(dir_vec) if np.linalg.norm(dir_vec) > 0 else 1.0
            horizontal_progress = max(np.dot(horizontal, dir_vec), 0)
            return w1 * vertical + w2 * horizontal_progress
        elif fitness_type == "euclidean":
            return np.linalg.norm(p2 - p1)
        else:
            raise ValueError(f"Unknown fitness_type: {fitness_type}")

    def get_vertical_progress(self):
        return self.get_distance_travelled(fitness_type="vertical")

    def get_horizontal_progress(self, target_direction=(1, 0)):
        return self.get_distance_travelled(fitness_type="horizontal", target_direction=target_direction)

    def get_combined_fitness(self, w1=0.7, w2=0.3, target_direction=(1, 0)):
        return self.get_distance_travelled(fitness_type="combined", target_direction=target_direction, weights=(w1, w2))

    def get_max_height_achieved(self):
        if hasattr(self, 'position_history') and self.position_history:
            max_height = max(pos[2] for pos in self.position_history)
            return max(max_height - self.start_position[2], 0)
        return self.get_vertical_progress()

    def update_dna(self, dna):
        self.dna = dna
        self.flat_links = None
        self.exp_links = None
        self.motors = None
        self.start_position = None
        self.last_position = None