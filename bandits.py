'''
Explores algorithms for tackling the multi-armed bandit problem. Implements the
ucb1 and en_greedy algorithms presented by Auer et. al. at 

http://homes.di.unimi.it/~cesabian/Pubblicazioni/ml-02.pdf

Authors: Rich Korzelius and Alden Hart
3/31/2015
'''

def ucb1():
    '''Implements the ucb1 algorithm:

        Initialization: Play each machine once.
        Loop:
            Play machine j that maximizes xj + sqrt(2ln(n)/nj) where xj is the
            average reward obtained from machine j, nj is the number of times
            machine j has been played so far, and n is the overall number of
            plays done so far.

    Parameters:
        - Not sure

    Returns: a score????
    '''
    pass

def en_greedy(c, d):
    '''Implements the epsilon_n-greedy algorithm:

        Initialization: Define the sequence en in (0,1], n = 1, 2, ..., by:
            en = min{1, cK/d^2n}

        Loop: For each n = 1, 2, ... :
            - Let i_n be the machine with the highest current average reward
            - With probability 1-en play i_n, and with probability en play a 
                random arm 

    Parameters:
        c - float > 0
        d - float 0 < d < 1

    Returns: a score???
    '''
    pass

def main():
    pass

if __name__ == '__main__':
    main()
    