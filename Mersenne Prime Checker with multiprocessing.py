# Each thread will check it's own number for Mersenne Primality


def Checker(pm_n=(2, 4)):
    pm, n = pm_n
    lls = (n ** 2 - 2) # Lucas-Lehmer Sequence
    lls = n
    lls = (n ** 2 - 2)
    mp  = (2 ** pm - 1) # Formula for Mersenne Primes
    pm = pm + 1
    mp  = (2 ** pm - 1)
    if lls % mp == 0: # The actual checking.
        print(mp, 'is a Mersenne Prime.')
    else:
        print(mp, 'is not a Mersenne Prime.')

        
# The Multiprocessing; works for 4 Processors, add additional 'pm' and 'n' etc and change the 4 in 'Pool(4)' to your Processor quantity.
if __name__ == '__main__':
    from multiprocessing import Pool
    with Pool(4) as pool: # Creates a 'Pool' of tasks from which each Processor will work on and output independently.
        pm1 = 2
        n1 = 4
        pm2 = 3
        n2 = (n1 ** 2 - 2)
        pm3 = 4
        n3 = (n2 ** 2 - 2)
        pm4 = 5
        n4 = (n3 ** 2 - 2)
        result = pool.map(Checker, [(pm1, n1), (pm2, n2), (pm3, n3), (pm4, n4)])
        print(result)
        while True:
            pm1 = pm4 + 1
            n1 = (n4 ** 2 - 2)
            pm2 = pm1 + 1
            n2 = (n1 ** 2 - 2)
            pm3 = pm2 + 1
            n3 = (n2 ** 2 - 2)
            pm4 = pm3 + 1
            n4 = (n3 ** 2 - 2)
            result = pool.map(Checker, [(pm1, n1), (pm2, n2), (pm3, n3), (pm4, n4)])
            print(result)
