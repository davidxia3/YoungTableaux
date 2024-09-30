from sympy.utilities.iterables import partitions
import math

def hook_length_product(sympy_partition):
  
    partition_list = []
    for part_size, frequency in sympy_partition.items():
        partition_list.extend([part_size] * frequency)

    partition_list.sort(reverse=True)

    hook_length_product = 1

    for i, row_length in enumerate(partition_list):
        for j in range(row_length):
            right = row_length - j - 1  
            below = sum(1 for k in range(i + 1, len(partition_list)) if partition_list[k] > j) 
            hook_len = right + below + 1 

            hook_length_product *= hook_len

    return hook_length_product

