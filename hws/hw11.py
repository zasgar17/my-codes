# 1
# import numpy as np

# one_dimensional_array = np.array([1, 2, 3, 4]) 

# N = int(np.sqrt(len(one_dimensional_array)))
# if N * N == len(one_dimensional_array):
#     matrix = one_dimensional_array.reshape(N, N)
#     print("Yeni Matrix:")
#     print(matrix)
# else:
#     print("emeliyyat mumkun olmadi")
    
# 2
# import numpy as np
# integer_array = np.array([1, 2, 3, 4, 5])
# string_array = integer_array.astype(str)
# print("Integer Array:")
# print(integer_array)
# print("\nString Array:")
# print(string_array)

# 3
# import numpy as np
# integer_array = np.array([123, 45, 678, 90, 555])
# def digit_sum(n):
#     return sum(map(int, str(n)))
# sum_of_digits = np.array([digit_sum(num) for num in integer_array])
# max_sum_index = np.argmax(sum_of_digits)
# integer_with_max_sum = integer_array[max_sum_index]
# print("Given Integer Array:", integer_array)
# print("Integer with Maximum Sum of Digits:", integer_with_max_sum)

# 4
# import numpy as np
# array = np.array([1, 2, 0, 4, 5])
# non_zero = np.all(array != 0)

# if non_zero:
#     print("Every element in the array is non-zero.")
# else:
#     print("There is at least one zero element in the array.")

# 5
# import numpy as np
# array = np.array([0, 2, 0, 4, 5])
# count=0
# if 0 in array:
#     count+=1
#     print(count)
# all_zero = np.all(array == 0)

# if all_zero:
#     print("Every element in the array is zero.")
# else:
#     print("There is at least one non-zero element in the array.")

# 6
# import numpy as np

# arr = np.array([3, 7, 2, 9, 1, 4, 6, 8, 5])
# arr_sum = np.sum(arr)
# arr_max = np.max(arr)
# arr_min = np.min(arr)

# print("Array: ", arr)
# print("Sum: ", arr_sum)
# print("Maximum: ", arr_max)
# print("Minimum: ", arr_min)

# 7
# import numpy as np

# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(np.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print("Matrix:")
# print(matrix)
# //7
# import numpy as np
# arr=np.array([4,7,3,9,11])
# prime_sum=0


# for n in arr:
#     check=True
    
#     for i in range(2, int(n**0.5) + 1): 
#         if n % i == 0:
#             check=False
#     if check:
#         prime_sum +=n       
# print(prime_sum)

# 8
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
column_vector = matrix[:, 0]

print("Verilen Matrix:")
print(matrix)

print("\nİlk Sütun Vektoru:")
print(column_vector)

# 9
# import numpy as np

# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# diaq_1 = matrix[[:, 0], [1:, 1], []

# print("Verilen Matrix:")
# print(matrix)
