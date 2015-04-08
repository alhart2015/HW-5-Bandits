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
        self.total_plays = 0
        self.c = 0.05
        self.d = 0.5
        self.epsilon = 1
        self.rewards = [0.0] * num_machines
        self.num_machines = num_machines


    def update_epsilon(self):

        if self.total_plays == 0:
            return

        val = (self.c*self.num_machines) / (self.d**2 * self.total_plays)
        if val < 1:
            self.epsilon = val
        else:
            self.epsilon = 1

    def select_machine(self):
        self.update_epsilon()
        max_reward = get_max_machine(self.rewards)
        # print max_reward, self.rewards
        r = random.random()
        if r < 1 - self.epsilon:
            return max_reward, 1.0
        else:
            # foi = random.randint(0, self.num_machines)
            # print 'num machines', self.num_machines
            # print 'o=ofiueh', foi
            # return foi, 0.0
            return random.randint(0, self.num_machines-1), 0.0
        

        # ucb_values = []
        # for machine in range(self.num_machines):
        #     ucb_values.append(self.expected_rewards[machine] + math.sqrt((2*math.log(self.total_plays))/self.num_plays[machine]))
        #     #ucb_values.append(math.log(self.total_plays))



        # return get_max_machine(ucb_values)

    def update_bandit(self, machine_just_played, reward):

        self.total_plays += 1
        self.rewards[machine_just_played] += reward

        # self.num_plays[machine_just_played] += 1.0
        # self.total_plays += 1.0
        # self.cumulative_rewards[machine_just_played] += reward
        # self.expected_rewards[machine_just_played] = self.cumulative_rewards[machine_just_played]/self.num_plays[machine_just_played]

        # return


    def play(self, slots):
        machine, r = self.select_machine()
        # print machine, r
        return slots.reward_dist[machine], r
            # p = random.random()
            # if p <= slots.reward_dist[machine]:
            #     return p, 1.0
            # else:
            #     return p, 0.0

def get_max_machine(array):
    return array.index(max(array))











