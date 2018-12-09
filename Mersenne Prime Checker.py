import time

def MersennePrime(pm=3):
    mp = (2 ** pm) - 1
    print(pm)
    print(mp)
    while True:
        pm = pm + 1
        print(mp)


def LucasLehmerSequence(n=4):
    lls = (n ** 2) - 2 # Calculates the 2nd digit of the Lucas-Lehmer Sequence.
    print(n)
    print(lls)
    while True:
        n = lls
        lls = (n ** 2) - 2
        print(lls)


def Checker(pm_n=1):
    n=4
    pm=3
    start = time.time()
    mp = (2 ** pm) - 1
    while True:
        lls = (n ** 2) - 2
        n = lls # Updates the value of n to be = the previous sequence entry.
        lls = (n ** 2) - 2
        pm = pm + 1 # Adds 1 to the power of the Mersenne.
        mp = (2 ** pm) - 1
        if (lls % mp) == 0: # If nth in sequence has a remainder of 0 when / by the nth Mersenne it is a Mersenne Prime.
            print(mp, ' is a Mersenne prime. Yay!')
        else:
            print(mp, ' is sadly not a Mersenne prime. :(')

    end = time.time()
    print(end - start)



print(Checker())
