# https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    result_tree = [0]
    for num in numbers:
        tree = []
        for tree_num in result_tree:
            tree.append(tree_num + num)
            tree.append(tree_num - num)
        result_tree = tree
    return result_tree.count(target)
