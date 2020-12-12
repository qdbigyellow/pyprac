* Always have *measurable* performance goal before optimize
* Maybe update hardware is easier.
* Profile the code before 

* Use real data to measure
* Anti-virum may give penalty to performance.
* Have test beforehand
* Know when to measure the performance.

**time** module & **timeit module**
    * from time import perf_counter
    * timeit can evalute the code inside the function call. The code is the argument of timeit()

**cProfile** is the Deterministic Profilers
check the exec 01_04. 

a) python -m cProfile prof.py


b)   import cProfile
     cProfile.run('function(*args)', )
   python prof.py

c) Run code pstats module to display
     import cProfile
     cProfile.run('function(*args)', filename='profile.out')
   python prof.py
   python -m pstats profile.out

   in the debugger 
     1. stats 10
     2. sort cumtime
     3. stats 10
use snakeviz prof.out can visual the result in web


 d) ipython
    %run -n prof.py
    %cases = list(gen_cases(1000))
    %prun bench_login(bench_login(cases))

**line_profile** : Do line proile in the fine granularity.  Need pip install
**kernprof**:  A CLI program. 
**@profile** to mark the code to profile. 
  1. decorate the function with @profile
  2. kernprof -l prof.py  => prof.py.lprof   # create the profile
  3. python -m line_profiler prof.py.lprof   # visual the result

ipython version
    1. remove the @profile decorator
    2. %run -n prof.py   # load the code without running
    3. case = list(gen_cases(1000))  # generate test data
    4. %load_ext line_profiler   # load the external package
    5. %lprun -f login bench_login(casese)   # lprun is line proflier run,  -f with function name to profile, bench_login is the function to run.



**tracemalloc** 
check which line of you code genereate the data.  

import tracemalloc
tracemalloc.start()
run_code(...)
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno')[:10]:
    print(stat)


**memory_profiler** to check which part use most of memory
meomry profile also use **@profile** to identify the function be profiled
python -m momory_profiler prof.py

**mprof run sos.py**  genereate the profile data.
time base memory profileing,  check if the memory continously growing.
**remove decorator**
mprof run prof.py  => genereate a dat file
mprof plot file.dat


