# This is the main functions. 

import genome 
from xml.dom.minidom import getDOMImplementation
from enum import Enum
import numpy as np

class MotorType(Enum):
    PULSE = 1
    SINE = 2

class Motor:
    def __init__(self, control_waveform, control_amp, control_freq):
        if control_waveform <= 0.5:
            self.motor_type = MotorType.PULSE
        else:
            self.motor_type = MotorType.SINE
        self.amp = control_amp
        self.freq = control_freq
        self.phase = 0

    def get_output(self):
        self.phase = (self.phase + self.freq) % (np.pi * 2)
        if self.motor_type == MotorType.PULSE:
            output = 1 if self.phase < np.pi else -1
        else:
            output = np.sin(self.phase)
        return output 

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