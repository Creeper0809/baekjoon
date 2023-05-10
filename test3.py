from collections import deque


def solution(progresses, speeds):
    answer = []
    temp_list = [[progresses[i],speeds[i]] for i in range(len(progresses))]
    queue = deque(temp_list)
    time = 1
    while queue:
        correct = 0
        while queue and queue[0][0] + queue[0][1] * time >= 100:
            correct += 1
            queue.popleft()
        if correct != 0:
            answer.append(correct)
        time += 1
    return answer


print(*solution([93,30,55],[1,30,5]), sep=", ")