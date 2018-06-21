import sys
num_steps = int(sys.argv[1])

for i in range(num_steps):
    s = ""
    for j in range(num_steps-i-1):
        s += " "
    for j in range(i+1):
        s += "#"
    print(s)
