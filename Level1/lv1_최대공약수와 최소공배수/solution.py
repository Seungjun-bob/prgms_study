def solution(n, m):
    gcd = 0
    lcm = 0
    for i in range(1,n+1):
        if n%i == 0:
            if m%i ==0:
                gcd = i
    if gcd == 1:
        lcm = m*n
    else: 
        lcm = (m*n) // gcd

    return [gcd,lcm]