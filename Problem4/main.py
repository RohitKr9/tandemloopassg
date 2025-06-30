l1 = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9]
n = int(input("Enter the Number of elements :"))

l2 = []
while n:
    l2.append(int(input()))
    n -= 1

print(l2)
ans = {}
for i in l1:
    count = 0
    for j in l2:
        if(j%i == 0):
            count += 1
    ans[i] = count

print(ans)