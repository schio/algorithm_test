"""
https://programmers.co.kr/learn/courses/30/lessons/42579
"""
def solution(genres, plays):
    from collections import defaultdict
    each_play_cnt = defaultdict(list)
    genres_cnt = defaultdict(int)
    
    for i in range(len(genres)):
        genres_cnt[genres[i]] += plays[i]
        each_play_cnt[genres[i]].append((plays[i], i))
        
    
    answer = []
    for genres_key, _ in sorted(genres_cnt.items(), key=lambda x: x[1], reverse=True):
        for plays_key in sorted(each_play_cnt[genres_key], key=lambda x: x[0],  reverse=True)[:2]:
            answer.append(plays_key[1])
    
    return answer