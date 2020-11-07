# https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    possble_skill_tree = len(skill_trees)
    for skill_tree in skill_trees:
        skill_list = list(skill)
        for s in skill_tree:
            if s in skill and s != skill_list.pop(0):
                possble_skill_tree -= 1
                break
    return possble_skill_tree
