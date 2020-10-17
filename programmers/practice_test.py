# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    counts = [0, 0, 0]
    supo_people = [
        [[1, 2, 3, 4, 5], 5],
        [[2, 1, 2, 3, 2, 4, 2, 5], 8],
        [[3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 10]
    ]

    len_supo_people = len(supo_people)
    for i, answer in enumerate(answers):
        for j in range(len_supo_people):
            if supo_people[j][0][i % supo_people[j][1]] == answer:
                counts[j] += 1

    max_count = max(counts)
    return [i + 1 for i in range(len(counts)) if counts[i] == max_count]
