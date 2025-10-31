file = open("StudentExercise.csv")
##next(file)
##out = {
##    "Excercise":[],
##    "TV":[],
##    "Height":[],
##    "Weight":[],
##    "Siblings":[],
##    "BirthOrder":[],
##    "VerbalSAT":[],
##    "MathSAT":[],
##    "SAT":[],
##    "GPA":[],
##    "Pulse":[],
##    "Piercings":[]
##    }
##true_set = []
##def clean(string):
##    try:
##        output = float(string)
##    except:
##        output = None
##    return output
##
##def average(lis):
##    return sum(lis)/len(lis)
##
##def prop_above(lis):
##    avg = average(lis)
##    total = 0
##    for item in lis:
##        if item>avg:
##            total += 1
##    return total
##
##def median(lis):
##    lis.sort()
##    ln = len(lis)
##    print(ln//2,round(ln/2+1))
##    output = [ lis[ln//2], lis[round(ln/2+.5)] ]
##    print(output)
##    
##    return average(output)
##
##print("od",median([-1, 6, 200]))
##print("ev",median([1, 200, 202, 3000000]))
##
##for i in file:
##    line = i.split()
##    truset = []
##    n = 0
##    for cat in out:
##        addon = clean(line[n])
##        if addon != None:
##            out[cat].append(addon)
##        truset.append(addon)
##        n += 1
##    true_set.append(truset)

from numpy import array as ray
from matplotlib import pyplot as plot

data = []

def clean(string):
    try:
        out = float(string)
    except:
        out = string
    return out

for i in file:
    line = i.split(",")
    out = []
    for pie in line:
        out.append(clean(pie))
    data.append(out)

ex = [] # kill top
for row in data:
    for col in row:
        ex.append(1)
data = ray(data)

def median(lis):
    if len(lis)%2 == 0:
        pass
    else:
        pass
    return out

def average(lis):
    return sum(lis)/len(lis)

def prop_above(lis):
    avg = average(lis)
    total = 0
    for item in lis:
        if item>avg:
            total += 1
    return total
print((data[0, :]))
plot()
# get excerise number
