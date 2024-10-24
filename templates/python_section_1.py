from typing import Dict, List

import pandas as pd


def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    def reverse (lst,start, end,n):
        for i in range(n//2):
            lst[start] , lst[end] = lst[end],lst[start]
            start = start+1
            end = end-1
        
        return lst
  
    for i in range(0,len(lst),n):
        
        j = i+(n-1)
        if j > len(lst)-1:
            j = len(lst)-1 
        lst = reverse(lst,i,j,n) 

        """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.
    return lst

def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
  dic = {}
  for i in lst:
    if len(i) not in dic.keys():
      dic[len(i)] = [i]
    else:
      dic[len(i)].append(i)
  dic = dict(sorted(dic.items(),key = lambda x:x[0]))

   
  return dic

# def flatten_dict(nested_dict: Dict, sep: str = '.') -> Dict:
#     """
#     Flattens a nested dictionary into a single-level dictionary with dot notation for keys.
    
#     :param nested_dict: The dictionary object to flatten
#     :param sep: The separator to use between parent and child keys (defaults to '.')
#     :return: A flattened dictionary
#     """
#     # Your code here
#     return dict

def unique_permutations(nums: List[int]) -> List[List[int]]:
    from itertools import  permutations 
    lst = set(list(permutations(nums)))
    final = []
    for i in lst :
      final.append(list(i))

    return final

def find_all_dates(text: str) -> List[str]:
    import re

    pattern = r'[0-9]{2}-[0-9]{2}-[0-9]{4}|[0-9]{2}/[0-9]{2}/[0-9]{4}|[0-9]{4}\.[0-9]{2}\.[0-9]{2}'
    
    lst = re.findall(pattern, text)
    
    return lst 
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.
    
    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.


    """


# def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
#     """
#     Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
#     Args:
#         polyline_str (str): The encoded polyline string.

#     Returns:
#         pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
#     """
#     return pd.Dataframe()


def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
  
  import numpy as np
  trans = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      trans[j][i] = matrix[i][j]

  for i in range(len(trans)):
    trans[i][0] , trans[i][len(trans[0])-1] =  trans[i][len(trans[0])-1], trans[i][0]


  trans = np.array(trans)
  sum_rows = 0
  sum_cols = 0
  result = [[0 for j in range(len(trans[0]))] for i in range(len(trans))]
  for i in range (len(trans)):
    for j in range(len(trans[0])):
      sum_rows = sum(trans[i,:]) - trans[i][j]
      sum_cols = sum(trans[:,j]) - trans[i][j]
      result[i][j] = sum_rows + sum_cols
      sum_rows = 0
      sum_cols = 0
        # """
    # Rotate the given matrix by 90 degrees clockwise, then multiply each element 
    # by the sum of its original row and column index before rotation.
    
    # Args:
    # - matrix (List[List[int]]): 2D list representing the matrix to be transformed.
    
    # Returns:
    # - List[List[int]]: A new 2D list representing the transformed matrix.
    # """
    # # Your code here
  return result


# def time_check(df) -> pd.Series:
#     """
#     Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

#     Args:
#         df (pandas.DataFrame)

#     Returns:
#         pd.Series: return a boolean series
#     """
#     # Write your logic here

#     return pd.Series()


