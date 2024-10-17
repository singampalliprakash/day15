def apples(n,k):
    return k%n
n=int(input("enter the number of students:"))
k=int(input("enter the number of apples:"))
remainder=apples(n,k)
print(remainder)