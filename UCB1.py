"""
UCB1 implementation of the K-armed bandit problem

Author: Rich Korzelius and Alden Hart
"""

import random
import math
import Slots

machines = Slots.Slots

class Bandit(machines):
	"""
	Implements the behavior of a K-armed bandit using the UCB1 algorithm
	that learns which slot machine is the optimal choice based on its past
	choices.

	Attributes
		total_plays = total number of rounds played

		num_plays = array of integers representing the number of number plays
		of plays on the machine corresponding to each index

		expected_rewards = array representing the expected reward for the machine
		corresponding to each index
	"""

	def __init__(self, num_machines):
		self.total_plays = 0.0
		self.num_plays = [0.0 for machine in range(num_machines)]
		self.cumulative_rewards = [0.0 for machine in range(num_machines)]
		self.expected_rewards = [0.0 for machine in range(num_machines)]
		self.num_machines = num_machines


	def initialize(self, slots):
		for machine in range(self.num_machines):
			p, reward = play(machine, slots)
			self.total_plays += 1.0
			self.num_plays[machine] += 1.0
			self.cumulative_rewards[machine] += reward
			self.expected_rewards[machine] = self.cumulative_rewards[machine]/self.num_plays[machine]

		return

	def select_machine(self):
		ucb_values = []
		for machine in range(self.num_machines):
			ucb_values.append(self.expected_rewards[machine] + math.sqrt((2*math.log(self.total_plays))/self.num_plays[machine]))
			#ucb_values.append(math.log(self.total_plays))

		return get_max_machine(ucb_values)

	def update_bandit(self, machine_just_played, reward):
		self.num_plays[machine_just_played] += 1.0
		self.total_plays += 1.0
		self.cumulative_rewards[machine_just_played] += reward
		self.expected_rewards[machine_just_played] = self.cumulative_rewards[machine_just_played]/self.num_plays[machine_just_played]

		return

def get_max_machine(array):
	return array.index(max(array))

def play(machine, slots):
		p = random.random()
		if p <= slots.reward_dist[machine]:
			return p, 1.0
		else:
			return p, 0.0











