def recur(n):
    if n < 1:
        return n
    else:
        return n + recur(n-1)

n = int(input("Enter number :"))
print(recur (n))