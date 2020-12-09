'''
non-preemptive priority scheduling
'''

import heapq


class Process:
    '''Information of process start time and burst time'''

    start = False
    finished = False
    # startTime = 0
    # finishTime = 0
    # responseTime = 0
    # completionTime = 0
    # waitingTime = 0
    # turnAround = 0

    def __init__(self, processNumber, arrival, burst, priority):
        self.processNumber = processNumber
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.priority = priority


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
processDictionary = {}

# Getting user input
if (n == 1):
    processCount = int(input("Enter the number of processes: "))
    for i in range(processCount):
        print("Enter the arrival and burst time of process ", i+1)
        processInfo = input().split()
        processArrival = int(processInfo[0])
        processBurst = int(processInfo[1])
        processPriority = int(processInfo[2])
        processObj = Process(i+1, processArrival,
                             processBurst, processPriority)
        processList.append(processObj)
        processDictionary.setdefault(processPriority, []).append(processObj)
        heapq.heappush(processRemaining, (processPriority, processObj))
# Reading from the file
elif (n == 2):
    f = open("ps.txt", "r")
    processCount = int(f.readline())
    for i in range(processCount):
        processInfo = f.readline().split()
        processArrival = int(processInfo[0])
        processBurst = int(processInfo[1])
        processPriority = int(processInfo[2])
        processObj = Process(i+1, processArrival,
                             processBurst, processPriority)
        processList.append(processObj)
        processDictionary.setdefault(processPriority, []).append(processObj)
        heapq.heappush(processRemaining, (processPriority, processObj))
else:
    raise Exception("Selected mode should be between 1 and 2")
# printing the processes information
questionHeader = ["process no.", "start", "burst", "priority"]
questionTable = [questionHeader]
for process in processList:
    tableRow = [process.processNumber, process.arrival,
                process.burst, process.priority]
    questionTable.append(tableRow)
drawTable(questionTable)
print()
# doing non-preemptive priority scheduling algorithm
print("Grant Chart:")
cpuClock = 0
while(processRemaining):
    temp = heapq.heappop(processRemaining)
    process = temp[1]
    process.startTime = cpuClock
    print(process.burst*str(process.processNumber), end="")
    cpuClock += process.burst
    process.finishTime = cpuClock
    process.responseTime = process.burst
    process.turnAround = cpuClock-process.arrival
    process.waitingTime = cpuClock - \
        process.arrival - process.burst

print('\n')

# printing the result table
headerList = ["Process no.", "Arrival", "Burst", "Priority", "Start",
              "Finish", "Response", "Turnaround", "Waiting"]
table = [headerList]

for process in processList:
    tableRow = [process.processNumber, process.arrival, process.burst, process.priority,
                process.startTime, process.finishTime, process.responseTime,
                process.turnAround, process.waitingTime]
    table.append(tableRow)

drawTable(table)
print()
print("Average Turnaroud Time: ", avgTurnAroundTime(processList))
print("Average Waiting Time: ", avgWaitingTime(processList))
print()
