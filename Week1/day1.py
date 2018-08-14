def hoursInAYear(year):
    days = 0
    if(year%4==0):
        if(year%100==0 and year%400 ==0):
        	days = 366
    else:
    	days = 365

    if(days is 366):
        hours = 366*24
    else:
        hours = 365*24
    print('The number of hours in the year ',year,' are ',hours)


def isLeapYear(year):
    days = 0
    if(year%4==0):
        if(year%100 ==0 and year%400==0):
            days = 366
    else:
        days = 365
		
    if(days == 366):
        return 1
    else:
        return 0

def minutesInADecade():
    year = int(input("Please enter starting year"))
    count = 0
    for x in range(year,year+10):
        temp = isLeapYear(x)
        count+=temp
    leapYears = count
    nonLeapYears = 10-count
    minutes = leapYears*366*24*60+nonLeapYears*365*24*60
    print('Minutes in the decade from ',year,' to ',year+9,' is ',minutes)

def ageInSeconds():
    age = int(input("Please enter your age in years"))
    seconds = age*365.25*24*60*60
    print('Age in seconds is ',seconds)

def findAndreeasAge():
    seconds = 486180000
    age = (((seconds/60)/60)/24)/365.25
    print("Andreaa's age is ",age)

def timeout32bit():
    total = 2**31
    days = (((total/1000)/60)/60)/24
    print('Number of days it takes for a 32-bit system to timeout if it has a bug with integer overflow is ',days)

def timeout64bit():
    total = 2**63
    days = (((total/1000)/60)/60)/24
    print('Number of days it takes for a 32-bit system to timeout if it has a bug with integer overflow is ',days)






year = int(input('Please enter a year '))
hoursInAYear(year)
minutesInADecade()
ageInSeconds()
findAndreeasAge()
timeout32bit()
timeout64bit()