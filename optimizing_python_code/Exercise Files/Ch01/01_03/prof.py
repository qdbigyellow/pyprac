"""Example using cProfile"""
from login import login
from random import random


def gen_cases(n):
    """Generate tests cases"""
    for i in range(n):
        if random() > 0.1:  # 90% of logins are OK
            yield ('daffy', 'rabbit season')
        else:
            if random() < 0.2:   # less than 20% of NOK login is because of no user
                yield ('tweety', 'puddy tat')  # no such user
            else:               
                yield ('daffy', 'duck season')


def bench_login(cases):
    """Benchmark login with test cases"""
    for user, passwd in cases:
        login(user, passwd)


if __name__ == '__main__':
    n = 1000
    cases = list(gen_cases(n))
    
    if 0:
        bench_login(cases)   # run the code  
    
    if 0:
        import cProfile
        cProfile.run('bench_login(cases)')  # run the code  with profile

    if 0:
        import cProfile
        # python -m pstats profile.out  to analysis the output file. 
        # or 
        # use snakeviz module to visual. 
        cProfile.run('bench_login(cases)', filename='profile.out')  # run the code with proile result in file


# Use Ipython


# %run -n prof.py
# case = list(gen_cases(1000))
# %prun bench_login(cases)
# %prun ?
# %prun -s cumulative bench_login(cases)