file = open("numbers.txt", "r")
lines=file.readlines()[1:]
lines = [i.strip("\n") for i in lines]
count = 0
for x in lines:
    line = x.split()
    count=0
    for i in line:
        if str(int(i)+1) in line:
            count+=abs(line.index(i)-line.index(str(int(i)+1)))
    print(count)