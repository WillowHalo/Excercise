file = open("StudentExercise.csv")
next(file)
out = {
    "Excercise":[],
    "TV":[],
    "Height":[],
    "Weight":[],
    "Siblings":[],
    "BirthOrder":[],
    "VerbalSAT":[],
    "MathSAT":[],
    "SAT":[],
    "GPA":[],
    "Pulse":[],
    "Piercings":[]
    }

def clean(string):
    try:
        output = float(string)
    except:
        output = None
    return output

def average(lis):
    return sum(lis)/len(lis)

def prop_above(lis):
    avg = average(lis)
    total = 0
    for item in lis:
        if item>avg:
            total += 1
    return total

def median(lis):
    lis.sort()
    ln = len(lis)
    print(ln//2,round(ln/2-.5))
    output = lis[ln//2:round(ln/2+.5)]
    print(output)
    return average(output)

print("od",median([-5, 6, 200]))
print("ev",median([1, 200, 202, 3000000]))

for p in file:
    line = p.split()
    n = 0
    for cat in out:
        addon = clean(line[n])
        if addon != None:
            out[cat].append(addon)
        n += 1
    

# get excerise number
