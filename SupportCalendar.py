from datetime import datetime, timedelta
import random
import camelcase, numpy


def numToDay(day, month, year):
    date = datetime(year, month, day)
    num = date.weekday()
    arr = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return arr[num]


def isWeekday(day, month, year): # Checks if day is a working day (weekday)
    date = datetime(year, month, day)
    if date.weekday() > 4:
        return False
    else:
        return True
        
def isIndianHoliday(day, month, year): # Checks if day is a Indian Holiday


    for x in range(0,len(IndiaHoliday)):
        if day == IndiaHoliday[x].getDay():
            if month == IndiaHoliday[x].getMonth():
                if year == IndiaHoliday[x].getYear():
                    return True
                else:
                    return False




def isUSAHoliday(day, month, year): # Checks if day is a USA Holiday
    for x in range(0, len(USAHoliday)):
        if day == USAHoliday[x].getDay():
            if month == USAHoliday[x].getMonth():
                if year == USAHoliday[x].getYear():
                    return True
                else:
                    return False




def isIndianTeamOff(): # True if the Indian team is off
    counter = 0


    for x in range(0,len(IndiaEmployee)):
        if IndiaEmployee[x].getCanWork() == False:
            counter = counter + 1
    if counter == len(IndiaEmployee):
        return True
    else:
        return False


def isUSATeamOff(): # True if USA team is off
    counter = 0


    for x in range(0, len(USAEmployee)):
        if USAEmployee[x].getCanWork() == False:
            counter = counter + 1
    if counter == len(USAEmployee):
        return True
    else:
        return False
        


class Holiday: # Class for Holiday Object
    def __init__(self, y, m, d, c):
        self.year = y
        self.month = m
        self.day = d
        self.country = c
    
    def isWeekday(self):
        date = datetime(self.year, self.month, self.day)
        if date.weekday() > 4:
            return False
        else:
            return True


    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.year


class Employee:


    def __init__(self, n, c):
        self.name = n
        self.country = c
        self.canWork = True
        self.rank = 0


    def changeCanWork(self):
        if self.canWork == True:
            canWork = False
        else:
            self.canWork = True
    def getRank(self):
        return self.rank
    
    def getCanWork(self):
        return self.canWork


    def getName(self):
        return self.name


    def incrementRank(self):
        self.rank = self.rank + 1


# All the employees 
a  = Employee("a", "India")
b = Employee("b", "India")
c = Employee("c", "India")
d = Employee("d", "India")
e = Employee("e", "India")


f = Employee("f", "USA")
g = Employee("g", "USA")
h = Employee("h", "USA")
i = Employee("i", "USA")
j = Employee("j", "USA")


# All the random Holiday objects
h1 = Holiday(2021, 7, 16, "India")
h2 = Holiday(2021, 7, 23, "India")
h3 = Holiday(2021, 7, 24, "India")
h4 = Holiday(2021, 7, 19, "India")
h5 = Holiday(2021, 7, 20, "India")


h6 = Holiday(2021, 7, 14, "USA")
h7 = Holiday(2021, 7, 20, "USA")
h8 = Holiday(2021, 7, 20, "USA")
h9 = Holiday(2021, 7, 20, "USA")
h10 = Holiday(2021, 7, 20, "USA")


# popoulate two region specific arrays with employees
IndiaEmployee = [a, b, c, d, e]
USAEmployee = [f, g, h, i, j]
# popoulate two region specific arrays with holidays 
IndiaHoliday = [h1, h2, h3, h4, h5]
USAHoliday = [h6, h7, h8, h9, h10]




for x in range(90):


    day = int((datetime.now() + timedelta(x)).strftime('%d'))
    month = int((datetime.now() + timedelta(x)).strftime('%m'))
    year = int((datetime.now() + timedelta(x)).strftime('%Y'))


    if isWeekday(day, month, year): # If day is working day, set all employees to canwork
        for x in range(0, len(IndiaEmployee)):
            IndiaEmployee[x].canWork = True
        for x in range(0, len(USAEmployee)):
            USAEmployee[x].canWork = True


    if isWeekday(day, month, year) == False: # if day is not a working day, set all employees to cannot work
        for x in range(0, len(IndiaEmployee)):
            IndiaEmployee[x].canWork = False
        for x in range(0, len(USAEmployee)):
            USAEmployee[x].canWork = False
        print("WEEKEND ON " + str(day) + "/" + str(month) + "/" + str(year))
        print("ALL SUPPORT UNAVAILIBLE")


    else:
        if isIndianHoliday(day, month, year) and isUSAHoliday(day, month, year): # If both teams are off on holiday, nobody can work
            print(str(day) + "/" + str(month) + "/" + str(year))
            print("BOTH TEAM ARE OFF")
            print("ALL SUPPORT UNAVAILIBLE")


        else:
            if isIndianHoliday(day, month, year): # if it is an Indian holiday, set all Indian employees to cannot work
                for x in range(0, len(IndiaEmployee)):
                    IndiaEmployee[x].canWork = False
                print('INDIA TEAM WILL BE OFF ON ' + str(day) + "/" + str(month) + "/" + str(year))
                print('USA TEAM WILL TAKE OVER')


            else:
                if isUSAHoliday(day, month, year): # if it is an USA holiday, set all USA employees to cannot work
                    for x in range(0, len(USAEmployee)):
                        USAEmployee[x].canWork = False
                    print("USA TEAM WILL BE OFF ON " + str(day) + "/" + str(month) + "/" + str(year))
                    print("INDIA TEAM WILL TAKE OVER")
        


    if isWeekday(day, month, year) and (not isUSAHoliday(day, month, year) or not isIndianHoliday(day, month, year)): # If day is a working day


        print("")                                               # Indian Support Teams gets outputted
        print(str(day) + "/" + str(month) + "/" + str(year) + " -- " + numToDay(day, month, year))
        print("~~ SUPORT FOR TODAY~~ ")


        if not isIndianTeamOff():  # If Indian Team is working


            primaryChoice = random.choice(IndiaEmployee) # Random primary India employee 


            while True: # check if primary is eligible to work, and if not, change primary choice to an eligible employee
                if primaryChoice.canWork:
                    break;
                else:
                    lowestRank = IndiaEmployee[0].getRank()
                    for x in len(IndiaEmployee):
                        if IndiaEmployee[x].getRank() < lowestRank:
                            lowestRank = IndiaEmployee[x].getRank
                    for x in len(IndiaEmployee):
                        if IndiaEmployee[x].getRank == lowestRank:
                            primaryChoice = IndiaEmployee[x]
                   
                   
                   # primaryChoice = random.choice(IndiaEmployee)


            secondaryChoice = random.choice(IndiaEmployee) # Random secondary India employee


            while True: # If secondarychoicename is equal to primary name, then pick new object from India employee list
                if secondaryChoice != primaryChoice and secondaryChoice.canWork:
                    break 
               
                else:
                    secondaryChoice = random.choice(IndiaEmployee)


            
            print("INDIA PRIMARY: " + primaryChoice.getName())
            print("INDIA SECONDARY: " + secondaryChoice.getName())


            for x in range(0, len(IndiaEmployee)): # For loop traverses through employee list and increments rank by 1
                if primaryChoice == IndiaEmployee[x]:
                    IndiaEmployee[x].incrementRank()
                




        if not isUSATeamOff():




            primaryChoice = random.choice(USAEmployee) # Random primary USA Employee


            while True:
                if primaryChoice.getCanWork():
                    break 
                else:
                    lowestRank = USAEmployee[0].getRank()
                    for x in len(USAEmployee):
                        if USAEmployee[x].getRank() < lowestRank:
                            lowestRank = USAEmployee[x].getRank
                    for x in len(USAEmployee):
                        if USAEmployee[x].getRank == lowestRank:
                            primaryChoice = USAEmployee[x]




                    #primaryChoice = random.choice(USAEmployee) 
            
            secondaryChoice = random.choice(USAEmployee)


            while True:
                if secondaryChoice != primaryChoice and secondaryChoice.getCanWork():
                    break
                else:
                    secondaryChoice = random.choice(USAEmployee)
            
            print("")
            print("USA PRIMARY: " + primaryChoice.getName())
            print("USA SECONDARY: " + secondaryChoice.getName())


            for x in range(0, len(USAEmployee)): # For loop traverses through employee list and increments rank by 1
                if primaryChoice == USAEmployee[x]:
                    USAEmployee[x].incrementRank()
            




    print("~~~~~~~~~~~~~~~~~~~~~")
    print("")
         
melcase, numpy




def numToDay(day, month, year):
    date = datetime(year, month, day)
    num = date.weekday()
    arr = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return arr[num]


def isWeekday(day, month, year): # Checks if day is a working day (weekday)
    date = datetime(year, month, day)
    if date.weekday() > 4:
        return False
    else:
        return True
        
def isIndianHoliday(day, month, year): # Checks if day is a Indian Holiday


    for x in range(0,len(IndiaHoliday)):
        if day == IndiaHoliday[x].getDay():
            if month == IndiaHoliday[x].getMonth():
                if year == IndiaHoliday[x].getYear():
                    return True
                else:
                    return False




def isUSAHoliday(day, month, year): # Checks if day is a USA Holiday
    for x in range(0, len(USAHoliday)):
        if day == USAHoliday[x].getDay():
            if month == USAHoliday[x].getMonth():
                if year == USAHoliday[x].getYear():
                    return True
                else:
                    return False




def isIndianTeamOff(): # True if the Indian team is off
    counter = 0


    for x in range(0,len(IndiaEmployee)):
        if IndiaEmployee[x].getCanWork() == False:
            counter = counter + 1
    if counter == len(IndiaEmployee):
        return True
    else:
        return False


def isUSATeamOff(): # True if USA team is off
    counter = 0


    for x in range(0, len(USAEmployee)):
        if USAEmployee[x].getCanWork() == False:
            counter = counter + 1
    if counter == len(USAEmployee):
        return True
    else:
        return False
        


class Holiday: # Class for Holiday Object
    def __init__(self, y, m, d, c):
        self.year = y
        self.month = m
        self.day = d
        self.country = c
    
    def isWeekday(self):
        date = datetime(self.year, self.month, self.day)
        if date.weekday() > 4:
            return False
        else:
            return True


    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.year


class Employee:


    def __init__(self, n, c):
        self.name = n
        self.country = c
        self.canWork = True
        self.rank = 0


    def changeCanWork(self):
        if self.canWork == True:
            canWork = False
        else:
            self.canWork = True
    def getRank(self):
        return self.rank
    
    def getCanWork(self):
        return self.canWork


    def getName(self):
        return self.name


    def incrementRank(self):
        self.rank = self.rank + 1


# All the employees 
a  = Employee("a", "India")
b = Employee("b", "India")
c = Employee("c", "India")
d = Employee("d", "India")
e = Employee("e", "India")


f = Employee("f", "USA")
g = Employee("g", "USA")
h = Employee("h", "USA")
i = Employee("i", "USA")
j = Employee("j", "USA")


# All the random Holiday objects
h1 = Holiday(2021, 7, 16, "India")
h2 = Holiday(2021, 7, 23, "India")
h3 = Holiday(2021, 7, 24, "India")
h4 = Holiday(2021, 7, 19, "India")
h5 = Holiday(2021, 7, 20, "India")


h6 = Holiday(2021, 7, 14, "USA")
h7 = Holiday(2021, 7, 20, "USA")
h8 = Holiday(2021, 7, 20, "USA")
h9 = Holiday(2021, 7, 20, "USA")
h10 = Holiday(2021, 7, 20, "USA")


# popoulate two region specific arrays with employees
IndiaEmployee = [a, b, c, d, e]
USAEmployee = [f, g, h, i, j]
# popoulate two region specific arrays with holidays 
IndiaHoliday = [h1, h2, h3, h4, h5]
USAHoliday = [h6, h7, h8, h9, h10]




for x in range(90):


    day = int((datetime.now() + timedelta(x)).strftime('%d'))
    month = int((datetime.now() + timedelta(x)).strftime('%m'))
    year = int((datetime.now() + timedelta(x)).strftime('%Y'))


    if isWeekday(day, month, year): # If day is working day, set all employees to canwork
        for x in range(0, len(IndiaEmployee)):
            IndiaEmployee[x].canWork = True
        for x in range(0, len(USAEmployee)):
            USAEmployee[x].canWork = True


    if isWeekday(day, month, year) == False: # if day is not a working day, set all employees to cannot work
        for x in range(0, len(IndiaEmployee)):
            IndiaEmployee[x].canWork = False
        for x in range(0, len(USAEmployee)):
            USAEmployee[x].canWork = False
        print("WEEKEND ON " + str(day) + "/" + str(month) + "/" + str(year))
        print("ALL SUPPORT UNAVAILIBLE")


    else:
        if isIndianHoliday(day, month, year) and isUSAHoliday(day, month, year): # If both teams are off on holiday, nobody can work
            print(str(day) + "/" + str(month) + "/" + str(year))
            print("BOTH TEAM ARE OFF")
            print("ALL SUPPORT UNAVAILIBLE")


        else:
            if isIndianHoliday(day, month, year): # if it is an Indian holiday, set all Indian employees to cannot work
                for x in range(0, len(IndiaEmployee)):
                    IndiaEmployee[x].canWork = False
                print('INDIA TEAM WILL BE OFF ON ' + str(day) + "/" + str(month) + "/" + str(year))
                print('USA TEAM WILL TAKE OVER')


            else:
                if isUSAHoliday(day, month, year): # if it is an USA holiday, set all USA employees to cannot work
                    for x in range(0, len(USAEmployee)):
                        USAEmployee[x].canWork = False
                    print("USA TEAM WILL BE OFF ON " + str(day) + "/" + str(month) + "/" + str(year))
                    print("INDIA TEAM WILL TAKE OVER")
        


    if isWeekday(day, month, year) and (not isUSAHoliday(day, month, year) or not isIndianHoliday(day, month, year)): # If day is a working day


        print("")                                               # Indian Support Teams gets outputted
        print(str(day) + "/" + str(month) + "/" + str(year) + " -- " + numToDay(day, month, year))
        print("~~ SUPORT FOR TODAY~~ ")


        if not isIndianTeamOff():  # If Indian Team is working


            primaryChoice = random.choice(IndiaEmployee) # Random primary India employee 


            while True: # check if primary is eligible to work, and if not, change primary choice to an eligible employee
                if primaryChoice.canWork:
                    break;
                else:
                    lowestRank = IndiaEmployee[0].getRank()
                    for x in len(IndiaEmployee):
                        if IndiaEmployee[x].getRank() < lowestRank:
                            lowestRank = IndiaEmployee[x].getRank
                    for x in len(IndiaEmployee):
                        if IndiaEmployee[x].getRank == lowestRank:
                            primaryChoice = IndiaEmployee[x]
                   
                   
                   # primaryChoice = random.choice(IndiaEmployee)


            secondaryChoice = random.choice(IndiaEmployee) # Random secondary India employee


            while True: # If secondarychoicename is equal to primary name, then pick new object from India employee list
                if secondaryChoice != primaryChoice and secondaryChoice.canWork:
                    break 
               
                else:
                    secondaryChoice = random.choice(IndiaEmployee)


            
            print("INDIA PRIMARY: " + primaryChoice.getName())
            print("INDIA SECONDARY: " + secondaryChoice.getName())


            for x in range(0, len(IndiaEmployee)): # For loop traverses through employee list and increments rank by 1
                if primaryChoice == IndiaEmployee[x]:
                    IndiaEmployee[x].incrementRank()
                




        if not isUSATeamOff():




            primaryChoice = random.choice(USAEmployee) # Random primary USA Employee


            while True:
                if primaryChoice.getCanWork():
                    break 
                else:
                    lowestRank = USAEmployee[0].getRank()
                    for x in len(USAEmployee):
                        if USAEmployee[x].getRank() < lowestRank:
                            lowestRank = USAEmployee[x].getRank
                    for x in len(USAEmployee):
                        if USAEmployee[x].getRank == lowestRank:
                            primaryChoice = USAEmployee[x]




                    #primaryChoice = random.choice(USAEmployee) 
            
            secondaryChoice = random.choice(USAEmployee)


            while True:
                if secondaryChoice != primaryChoice and secondaryChoice.getCanWork():
                    break
                else:
                    secondaryChoice = random.choice(USAEmployee)
            
            print("")
            print("USA PRIMARY: " + primaryChoice.getName())
            print("USA SECONDARY: " + secondaryChoice.getName())


            for x in range(0, len(USAEmployee)): # For loop traverses through employee list and increments rank by 1
                if primaryChoice == USAEmployee[x]:
                    USAEmployee[x].incrementRank()
            




    print("~~~~~~~~~~~~~~~~~~~~~")
    print("")
