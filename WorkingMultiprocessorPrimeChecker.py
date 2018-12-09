def Checker(pm_n=(2, 4)):
    pm, n = pm_n
    lls = (n ** 2 - 2)
    lls = n
    lls = (n ** 2 - 2)
    mp  = (2 ** pm - 1)
    pm = pm + 1
    mp  = (2 ** pm - 1)
    if lls % mp == 0:
        print(mp, 'is a Mersenne Prime. Yay! :D')
    else:
        print(mp, 'is not a Mersenne Prime. Awww :(')


if __name__ == '__main__':
    from multiprocessing import Pool
    with Pool(2) as pool:
        pm1 = 2
        n1 = 4
        pm2 = 3
        n2 = (n1 ** 2 - 2)
        result = pool.map(Checker, [(pm1, n1), (pm2, n2)])
        print(result)
        while True:
            pm1 = pm2 + 1
            n1 = (n2 ** 2 - 2)
            pm2 = pm1 + 1
            n2 = (n1 ** 2 - 2)
            result = pool.map(Checker, [(pm1, n1), (pm2, n2)])
            print(result)
