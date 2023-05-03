def single_list(lists):
   """
   takes list of lists as input and returns a single list of all values with 
   nans removed

   dependencies: numpy
   """
   import numpy as np

   solo =  [x for xs in lists for x in xs
          if not(np.isnan(x)).any() == True]
   return solo