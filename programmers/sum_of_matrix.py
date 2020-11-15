# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    import numpy as np
    return (np.array(arr1) + np.array(arr2)).tolist()
