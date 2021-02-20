intervals = [
   [-412, -83],
   [301, 405],
   [-297, 472],
   [413, 464],
   [107, 272]
]


def sum_of_intervals(intervals):
    i = 0
    while i < len(intervals):
        j = i + 1
        while j < len(intervals):
            end_of_first = intervals[i][1]
            begining_of_next = intervals[j][0]
            if begining_of_next in range(intervals[i][0], intervals[i][1]):
                if intervals[j][1] > intervals[i][1]:
                    inserted = [intervals[i][0], intervals[j][1]]
                    intervals[i] = inserted
                del intervals[j]
                j = 0
            j += 1
        i += 1
    sum = 0
    for interval in intervals:
        sum = sum + abs(interval[1]-interval[0])
    return sum

a = sum_of_intervals(intervals)

print(a)
