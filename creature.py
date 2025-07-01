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
            return 1 if self.phase < np.pi else -1
        else:
            return np.sin(self.phase)

class Creature:
    def __init__(self, gene_count):
        self.spec = genome.Genome.get_gene_spec()
        self.dna = genome.Genome.get_random_genome(len(self.spec), gene_count)
        self.flat_links = None
        self.exp_links = None
        self.motors = None
        self.start_position = None
        self.last_position = None
        self.position_history = []

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
                continue
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
        self.last_position = pos
        self.position_history.append(pos)

    def get_total_path_length(self):
        """Compute total movement path length based on position history."""
        if len(self.position_history) < 2:
            return 0.0
        total = 0.0
        for i in range(1, len(self.position_history)):
            p1 = np.array(self.position_history[i - 1])
            p2 = np.array(self.position_history[i])
            total += np.linalg.norm(p2 - p1)
        return total

    def get_vertical_progress(self):
        if self.start_position is None or self.last_position is None:
            return 0.0
        return max(self.last_position[2] - self.start_position[2], 0.0)

    def get_horizontal_distance_to_center(self, target_center=(0, 0)):
        if self.last_position is None:
            return float('inf')
        pos_xy = np.array(self.last_position[:2])
        center = np.array(target_center)
        return np.linalg.norm(pos_xy - center)

    def get_stability_fitness(self, target_center=(0, 0)):
        """Calculate a penalized fitness score for stability, size, and efficiency."""
        if self.start_position is None or self.last_position is None:
            return 0.0

        vertical_gain = self.get_vertical_progress()

        # Reward being closer to the center at the end
        approach_center = max(0, 10.0 - self.get_horizontal_distance_to_center(target_center))

        total_path = self.get_total_path_length()
        useful_motion = vertical_gain + approach_center
        excess_movement = max(0, total_path - useful_motion)
        excess_penalty = excess_movement * 0.005  # motion inefficiency penalty

        # Penalize for having too many links
        num_links = len(self.get_expanded_links())
        size_penalty = max(0, (num_links - 6)) * 0.5

        # Final score formula
        score = (
            2.0 * vertical_gain +
            0.4 * approach_center -
            excess_penalty -
            size_penalty
        )
        return score

    def update_dna(self, dna):
        self.dna = dna
        self.flat_links = None
        self.exp_links = None
        self.motors = None
        self.start_position = None
        self.last_position = None
        self.position_history = []

