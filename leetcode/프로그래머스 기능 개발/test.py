def solution(progresses, speeds):
    answer = []
    maxVal = 0
    for idx, progress in enumerate(progresses):
        day = (100 - progress) / speeds[idx]
        if (100 - progress) % speeds[idx] != 0:
            day = round(day + 1)

        if maxVal < day:
            maxVal = day
            answer.append(1)
        else:
            answer[len(answer) - 1] += 1

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
