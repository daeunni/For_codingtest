## Minimum button for T time
T = int(input())
origin_T = T

second = [300, 60, 10]  # second
count = []  # push count list

for time in second:
    count.append(T // time)
    T = T % time  # remain

# can't make
if origin_T == sum([x * y for x, y in zip(second, count)]):
    print (count[0], count[1], count[2])

else:
    print (-1)