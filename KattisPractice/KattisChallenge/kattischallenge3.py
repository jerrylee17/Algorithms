import math
"""
class car:
    # name = name
    # price = price
    # puc = pick up price
    # cpk = cost per kilo
    def __init__(self, name, p, puc, cpk):
        self.name = name
        self.price = p
        self.puc = puc
        self.cpk = cpk
"""

class spy:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.car = None

class log:
    '''
        events:
            p - pra --> name of car
            r - pra --> distance of curr car
            a - pra --> accident
    '''
    def __init__(self, time, spy, event, pra):
        self.time = time
        self.spy = spy
        self.event = event
        self.pra = pra
        
testcases = int(input())

for i in range(testcases):
    theinput = input().split(' ')
    m = int(theinput[0])    #cars
    n = int(theinput[1])    #events
    cars, logs, spies = {}, [], []
    # 1 car is a dictionary
    # cars object set up
    for j in range(m):
        # obj = car(input().split(' '))
        userIn = input().split(' ')
        cars[userIn[0]] = [int(userIn[1]), int(userIn[2]), int(userIn[3])]
    # logs set up
    for j in range(n):
        obj = input().split(' ')
        obj = log(obj[0], obj[1], obj[2], obj[3])
        logs.append(obj)
    # sort logs by spy name, then time
    logs.sort(key = lambda x: (x.spy, int(x.time)))
    # [print(log.spy, log.time, log.event, log.pra) for log in logs]
    # make spies
    """
    allNames = sorted(list(set([x.name for x in logs])))
    for name in range(len(allNAmes)):
        mySpy = spy(name, 0)
        spies.append(mySpy)
    """
    # traverse logs
    currSpy, currTime, currLog = None, None, None
    allNames = set()
    mySpy = None
    """
    check if spy is new.
	YES -   add his name to allNames
                must be "p" assign him a car
                make spy object
        NO -
            Check if spy inconsistent
                YES - continue
            Check event type
                if p:
                    spy.car = pra
                    cost += puc
                if r:
                    cost += cpk*pra
                if a:
                    cost += math.ceil(price*pra/100)
    """
    for i in range(len(logs)):
        currLog = logs[i]
        currSpy, currTime = currLog.spy, currLog.time
        # check if spy is new
        if currSpy not in allNames:
            allNames.add(currSpy)
            if currLog.event != "p":
                spies.append(spy(currSpy, "INCONSISTENT"))
                continue
            else:
                # get car pick up cost
                carCost = cars[currLog.pra][1]
                spies.append(spy(currSpy, carCost))
                spies[-1].car = currLog.pra
                continue
        # check if spy is inconsistent
        if spies[-1].cost == "INCONSISTENT":
            continue
        # check if spy has car
        if spies[-1].car == None:
            if currLog.event == "p":
                spies[-1].car = currLog.pra
                spies[-1].cost += cars[currLog.pra][1]
            else:
                spies[-1].cost = "INCONSISTENT"
        elif currLog.event == "p":
            spies[-1].cost = "INCONSISTENT"
        elif currLog.event == "r":
            spies[-1].cost += cars[spies[-1].car][2] * int(currLog.pra)
            spies[-1].car = None
        elif currLog.event == "a":
            spies[-1].cost += math.ceil(cars[spies[-1].car][0] * int(currLog.pra) / 100)

    spies.sort(key = lambda x: x.name)
    for i in range(len(spies)):
        if spies[i].car != None:
            spies[i].cost = "INCONSISTENT"
        print(spies[i].name + " " + str(spies[i].cost))
