# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    len_prices = len(prices)
    answer = [0] * len_prices
    for i in range(len_prices - 1):
        for j in range(i, len_prices - 1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer
