def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
        elif s.isalnum():
            return False
    else:
        return False