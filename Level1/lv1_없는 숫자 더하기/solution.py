def solution(numbers):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = sorted(numbers)
    for i in numbers:
        if i in num:
            num.remove(i)
        
    return sum(num)