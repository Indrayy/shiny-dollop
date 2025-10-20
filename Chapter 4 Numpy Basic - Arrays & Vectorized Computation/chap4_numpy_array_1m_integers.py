import numpy as np
my_array = np.arange(1_000_000) 
#  Creating a large array with 1 million elements  
my_list = list(range(1_000_000))
#  Creating a large list with 1 million elements    

%timeit my_array2 = my_array * 2
715 µs ± 13.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit my_list2 = [x * 2 for x in my_list]
48.03 s ± 298 ms per loop (mean ± std. dev. of 7 runs, 10 loop each)
