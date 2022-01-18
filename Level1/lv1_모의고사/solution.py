def solution(answers):

    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_score = 0
    b_score = 0
    c_score = 0
    score = []
    answer = []
    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            a_score +=1
        if b[i%len(b)] == answers[i]:
            b_score +=1
        if c[i%len(c)] == answers[i]:
            c_score +=1
    score.append(a_score)
    score.append(b_score)
    score.append(c_score)
    maxscore = max(score)
    
    for i in range(3):
        if score[i] == maxscore:
            answer.append(i+1)
    return answer