import numpy as np


def matrix_multiplication(m1, m2):
    if multiplication_check([m1, m2]):
        return np.matmul(m1, m2)
    elif multiplication_check([m1, m2.T]):
        print('Result of multiplication obtained after transpose of matrix 2.')
        return np.matmul(m1, m2.T)
    elif multiplication_check([m1.T, m2]):
        print('Result of multiplication obtained after transpose of matrix 1.')
        return np.matmul(m1.T, m2)
    else:
        print('Matrices cannot be multiplied.')


def multiplication_check(m_list):
    result = True
    for i in range(len(m_list)-1):
        if m_list[i].shape[1] != m_list[i+1].shape[0]:
            result = False
    return result


def multiply_matrices(m_list):
    if multiplication_check(m_list):
        for i in range(len(m_list)-1):
            m_list[i+1] = matrix_multiplication(m_list[i], m_list[i+1])
        return m_list[-1]
    else:
        return


def compute_2d_distance(arr1, arr2):
    return np.linalg.norm(arr1-arr2)


def compute_multidimensional_distance(arr1, arr2):
    return compute_2d_distance(arr1, arr2)


def compute_pair_distances(arr):
    new_arr = np.zeros([arr.shape[0], arr.shape[0]])
    print(new_arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[0]):
            new_arr[i, j] = compute_2d_distance(arr[i], arr[j])
    return new_arr


if __name__ == "__main__":
    data = [[1, 2, 3], [4, 5, 6]]
    arr1 = np.array(data)
    arr2 = np.zeros([3, 2])+3
    arr3 = np.full([3, 2], 3)
    print('array 1\n', arr1)
    print('array 2\n', arr2)
    print('array 3\n', arr3)
