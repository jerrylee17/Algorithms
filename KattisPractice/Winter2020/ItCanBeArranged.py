import math
tc = int(input())


def solve(m, courses, cleanMatrix):
    # Sort by start time
    courses.sort(key=lambda x: (x[0], x[1]))
    currRooms = 0
    maxRooms = 0
    # [ID, Endtime, RoomsRequired]
    endTimes = []
    for c in courses:
        # Check currently occupied courses
        for i, times in enumerate([e.copy() for e in endTimes]):
            # Start time of course is greater than
            # End time + clean time
            # Basically has the course ended + been cleaned
            if c[0] >= times[1] + cleanMatrix[times[0]][c[3]]:
                # Free the rooms
                currRooms -= times[2]
                # Remove the occupied course
                endTimes.remove(times)
        # Calculate required rooms
        roomsRequired = math.ceil(c[2] / m)
        # Occupy those required rooms
        currRooms += roomsRequired
        # Add current course to occupied list
        endTimes.append([c[3], c[1]+1, roomsRequired])
        # Set max room
        maxRooms = max(maxRooms, currRooms)
    return maxRooms


for case in range(tc):
    # courses, capacity of room
    n, m = list(map(int, input().split(' ')))
    # start, end, # of registered students, ID
    courses = []
    for i in range(n):
        courseInfo = list(map(int, input().split(' ')))
        courseInfo.append(i)
        courses.append(courseInfo)
    cleanMatrix = []
    for i in range(n):
        clean = list(map(int, input().split(' ')))
        cleanMatrix.append(clean)
    result = solve(m, courses, cleanMatrix)
    print(f'Case {case+1}: {result}')
