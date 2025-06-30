import math
#x = None
while True:
    try:
        x = int(input("Enter an Integer"))
        if x%2 == 0:
            x = x-1
        break
    except ValueError as e:
        print(f"Please input again an positive integer {e}")

def sequenceprint(x):
    j = 1
    for i in range(x):
        print(j, end=" ")
        j += 2
    print('\n')

print(x)
sequenceprint(x)