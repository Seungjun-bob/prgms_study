def solution(phone_number):
    num_list = list(phone_number)
    num_list.reverse()
    for i in range(4, len(num_list)):
        num_list[i] = '*'
    num_list.reverse()
    return ''.join(num_list)