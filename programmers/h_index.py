# https://programmers.co.kr/learn/courses/30/lessons/42747#
def solution(citations):
    citations = sorted(citations)
    len_citations = len(citations)

    for i in range(len_citations):
        if citations[i] >= len_citations - i:
            return len_citations - i
    return 0
