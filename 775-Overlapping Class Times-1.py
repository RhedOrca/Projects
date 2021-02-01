classTimes = [(30, 75), (0, 50), (60, 150), (2, 10), (40, 70), (9, 200)]
maxLectures = 0
overlapRange = [0, 0]
for lecture1 in classTimes:
    currMax = 0
    overlapRange = [lecture1[0], lecture1[1]]
    for lecture2 in classTimes:
        start2 = lecture2[0]
        finish2 = lecture2[1]
        if start2 <= overlapRange[1] and finish2 >= overlapRange[0]:
            currMax += 1
            overlapRange[0] = max(overlapRange[0], start2)
            overlapRange[1] = min(overlapRange[1], finish2)
    if currMax > maxLectures:
        maxLectures = currMax

print("Minimum required classrooms is " + str(maxLectures))

