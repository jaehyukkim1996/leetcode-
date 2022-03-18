def solution(progresses, speeds):
    # Basic set up, how many days required to finish
    maxVal = 0
    answer = []
    for i in range(len(progresses)):
        division = (100 - progresses[i]) % speeds[i]
        daysFinish = (100 - progresses[i]) / speeds[i]
        # round off
        if division != 0:
            daysFinish +=1
            daysFinish = round(daysFinish)
        else:
            daysFinish = round(daysFinish)

        if maxVal < daysFinish:
            maxVal = daysFinish
            answer.append(1)
        else:
            answer[len(answer) - 1] += 1

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))



