class Process:
    '''Information of process start time and burst time'''

    start = False
    # startTime = 0
    # finishTime = 0
    # responseTime = 0
    # completionTime = 0
    # waitingTime = 0
    # turnAround = 0

    def __init__(self, processNumber, arrival, burst):
        self.processNumber = processNumber
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.startTime = arrival


def drawTable(table):
    # header
    lengthList = []
    sumOfLengths = 0
    for item in table[0]:
        print(item, end="|")
        sumOfLengths += len(item) + 1
        lengthList.append(len(item))
    print()
    print(sumOfLengths*"-")

    # row entries
    table.pop(0)
    for row in table:
        for i in range(len(row)):
            output = "{0:^" + str(lengthList[i]) + "}"
            print(output.format(row[i]), end="|")
        print()


def getArrivalTime(obj):
    return obj.arrival


def avgTurnAroundTime(processList):
    sum = 0
    for process in processList:
        sum += process.turnAround
    return sum/len(processList)


def avgWaitingTime(processList):
    sum = 0
    for process in processList:
        sum += process.waitingTime
    return sum / len(processList)


# Select how to get data
print("Select an input mode:")
print("Press 1 to read user input")
print("Press 2 to read from file")
n = int(input())

processList = []
processRemaining = []

# Getting user input
if (n == 1):
    processCount = int(input("Enter the number of processes: "))
    for i in range(processCount):
        print("Enter the arrival and burst time of process ", i+1)
        processInfo = input().split()
        processArrival = int(processInfo[0])
        processBurst = int(processInfo[1])
        processObj = Process(i+1, processArrival, processBurst)
        processList.append(processObj)
        processRemaining.append(processObj)
    timeQuantum = int(input("Enter the time quantum: "))
# Reading from the file
elif (n == 2):
    f = open("roundrobin.txt", "r")
    processCount = int(f.readline())
    for i in range(processCount):
        processInfo = f.readline().split()
        processArrival = int(processInfo[0])
        processBurst = int(processInfo[1])
        processObj = Process(i+1, processArrival, processBurst)
        processList.append(processObj)
        processRemaining.append(processObj)
    timeQuantum = int(f.readline())
else:
    raise Exception("Selected mode should be between 1 and 2")
# Reverse sorting to ensure first come first serve when the burst time is equal
processRemaining.sort(key=getArrivalTime, reverse=False)
# printing the processes information
questionHeader = ["process no.", "start", "burst"]
questionTable = [questionHeader]
for process in processList:
    tableRow = [process.processNumber, process.arrival,
                process.burst]
    questionTable.append(tableRow)
drawTable(questionTable)
print()
# doing preemptive sjf or srtf algorithm
print("Grant Chart:")
cpuClock = 0
while (len(processRemaining) > 0):
    for process in processRemaining.copy():
        if (process.remaining > timeQuantum):
            if (process.start == False):
                process.startTime = cpuClock
                process.start = True
            process.remaining -= timeQuantum
            print(timeQuantum*str(process.processNumber), end="")
            cpuClock += timeQuantum
        else:
            if (process.start == False):
                process.startTime = cpuClock
                process.start = True
            print(process.remaining*str(process.processNumber), end="")
            cpuClock += process.remaining
            process.finishTime = cpuClock
            process.remaining = 0
            process.responseTime = process.startTime - process.arrival
            process.turnAround = process.finishTime - process.arrival
            process.waitingTime = process.finishTime - process.arrival - process.burst
            processRemaining.remove(process)
print("\n")
# printing the result table
headerList = ["Process no.", "Arrival", "Burst", "Start",
              "Finish", "Response", "Turnaround", "Waiting"]
table = [headerList]

for process in processList:
    tableRow = [process.processNumber, process.arrival, process.burst,
                process.startTime, process.finishTime, process.responseTime,
                process.turnAround, process.waitingTime]
    table.append(tableRow)

drawTable(table)
print()
print("Average Turnaroud Time: ", avgTurnAroundTime(processList))
print("Average Waiting Time: ", avgWaitingTime(processList))
print()
