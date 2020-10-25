# https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    phone_number = list(phone_number)
    phone_number[:-4] = ["*"] * (len(phone_number) - 4)
    return "".join(phone_number)
