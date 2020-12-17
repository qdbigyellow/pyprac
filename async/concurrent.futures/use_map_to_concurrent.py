# from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import urllib

# multiprocessing.dummy use thread not process. 
p = ThreadPool(1)

urls = [
    'http://www.python.org',
    'http://www.python.org/about',
    'http://www.python.org/doc',
    'http://www.python.org/download',
    'http://www.python.org/getit',
    'http://www.python.org/community',
    'http://www.python.org/jobs',
    'https://pypi.org/',
    'http://www.python.org/psf'
]

result = p.map(urllib.request.urlopen, urls)
p.close()
p.join()


## in Ipython
## %%timeit -n10 -r10
## %run use_map_to_concurrent.py
## ..
## ..
