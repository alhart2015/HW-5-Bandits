"""
Tests the E_Greedy Bandit

Author: Rich Korzelius
"""

import E_Greedy
import Slots
import random
import math
import matplotlib.pyplot as plt
# from E_Greedy import play

OPTIMAL_MACHINE = 0
NUM_PLAYS = 10**5

def test_eps(slots, bandit):
    cumulative_regret = 0.0
    cumulative_regret_array = []
    percentage_optimal_play_array = []
    total_plays = 0.0
    num_optimal_plays = 0.0

    for i in range(NUM_PLAYS):

        machine_to_play, reward = bandit.select_machine()
        # machine_to_play, reward = bandit.play(slots)
        # print 'machine to play, reward', machine_to_play, reward
        bandit.update_bandit(machine_to_play, reward)
        p = slots.reward_dist[machine_to_play]
        # print 'p', p
        # print

        total_plays += 1.0

        if machine_to_play == OPTIMAL_MACHINE:
            num_optimal_plays += 1.0


        if p <= slots.reward_dist[OPTIMAL_MACHINE]:
            actual_regret = 1.0 - reward
        else:
            actual_regret = 0.0 - reward

        cumulative_regret += actual_regret
        cumulative_regret_array.append(cumulative_regret)

        percentage_optimal_play = num_optimal_plays/total_plays * 100.0
        percentage_optimal_play_array.append(percentage_optimal_play)

    return cumulative_regret, cumulative_regret_array, percentage_optimal_play, percentage_optimal_play_array

def main():
    
    DIST_1 = [0.9, 0.6]
    DIST_3 = [0.55, 0.45]
    DIST_11 = [0.9, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
    # DIST_13 = [0.9, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
    DIST_14 = [0.55, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45]

    # ^^ is there a reason you didn't use these?

    #DIST_1 = [0.9, 0.6]
    #DIST_3 = [0.55, 0.45]
    #DIST_11 = [0.9, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
    #DIST_13 = [0.9, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]

    # ^^ is there a reason you didn't use these?
    
    bandit_1 = E_Greedy.Bandit(len(DIST_1))
    slots_1 = Slots.Slots(DIST_1)
    # bandit_1.initialize(slots_1)

    # bandit_1 = E_Greedy.Bandit(2)
    # slots_1 = Slots.Slots([0.9, 0.6])
    # bandit_1.initialize(slots_1)

    bandit_3 = E_Greedy.Bandit(len(DIST_3))
    slots_3 = Slots.Slots(DIST_3)
    # bandit_3.initialize(slots_3)

    # bandit_3 = E_Greedy.Bandit(2)
    # slots_3 = Slots.Slots([0.55, 0.45])
    # bandit_3.initialize(slots_3)

    bandit_11 = E_Greedy.Bandit(len(DIST_11))
    slots_11 = Slots.Slots(DIST_11)
    # bandit_11.initialize(slots_11)

    # bandit_11 = E_Greedy.Bandit(10)
    # slots_11 = Slots.Slots([0.9, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6])
    # bandit_11.initialize(slots_11)

    bandit_14 = E_Greedy.Bandit(len(DIST_14))
    slots_14 = Slots.Slots(DIST_14)
    # bandit_14.initialize(slots_14)

    # bandit_13 = E_Greedy.Bandit(10)
    # slots_13 = Slots.Slots([0.9, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8])
    # bandit_13.initialize(slots_13)

    cumulative_regret_1, cumulative_regret_array_1, percentage_optimal_play_1, percentage_optimal_play_array_1 = test_eps(slots_1, bandit_1)
    cumulative_regret_3, cumulative_regret_array_3, percentage_optimal_play_3, percentage_optimal_play_array_3 = test_eps(slots_3, bandit_3)
    cumulative_regret_11, cumulative_regret_array_11, percentage_optimal_play_11, percentage_optimal_play_array_11 = test_eps(slots_11, bandit_11)
    cumulative_regret_14, cumulative_regret_array_14, percentage_optimal_play_14, percentage_optimal_play_array_14 = test_eps(slots_14, bandit_14)

    print 'Bandit 1 - Percentage of optimal plays: ' + str(percentage_optimal_play_1)
    print 'Bandit 1 - Cumulative Regret: ' + str(cumulative_regret_1)
    print
    print 'Bandit 3 - Percentage of optimal plays: ' + str(percentage_optimal_play_3)
    print 'Bandit 3 - Cumulative Regret: ' + str(cumulative_regret_3)
    print
    print 'Bandit 11 - Percentage of optimal plays: ' + str(percentage_optimal_play_11)
    print 'Bandit 11 - Cumulative Regret: ' + str(cumulative_regret_11)
    print
    print 'Bandit 14 - Percentage of optimal plays: ' + str(percentage_optimal_play_14)
    print 'Bandit 14 - Cumulative Regret: ' + str(cumulative_regret_14)

    plt.plot(cumulative_regret_array_1, label='Bandit 1')
    plt.plot(cumulative_regret_array_3, label='Bandit 3')
    plt.plot(cumulative_regret_array_11, label='Bandit 11')
    plt.plot(cumulative_regret_array_14, label='Bandit 14')
    plt.ylabel('Cumulative Regret')
    plt.xlabel('Plays')
    plt.title('Cumulative Regret over time')
    plt.legend()
    plt.show()

    plt.plot(percentage_optimal_play_array_1, label='Bandit 1')
    plt.plot(percentage_optimal_play_array_3, label='Bandit 3')
    plt.plot(percentage_optimal_play_array_11, label='Bandit 11')
    plt.plot(percentage_optimal_play_array_14, label='Bandit 14')
    plt.ylabel('Percentage of optimal plays')
    plt.xlabel('Plays')
    plt.title('Percentage of optimal plays over time')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    main()