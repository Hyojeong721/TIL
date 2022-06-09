import sys
sys.stdin = open("input.txt")

def returnHour(N, Rooms, student_route):
    '''
    # N : num of students
    # old_room : present rooms
    # new_room : rooms to return to
    '''

    # make a corridor
    corr = [0] * Rooms

    # check a corridor
    for i in range(N):
        old_room = student_route[i][0]
        new_room = student_route[i][1]

        for j in range(old_room, new_room+1):
            corr[j] += 1

        # [[10, 20], [30, 40], [50, 60], [70, 80]]

    return max(corr)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # make a student_route with two-dimensional list
    student_route = []
    for i in range(N):
        each_route = input()
        route = list(map(int, each_route.split()))
        student_route.append(route) #[[10, 20], [30, 40], [50, 60], [70, 80]]
    print("#{} {}".format(tc, returnHour(N, 400, student_route)))





