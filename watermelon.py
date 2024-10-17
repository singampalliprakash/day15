w=int(input("enter the weight of watermelon:"))
if(w%2!=0):
    print("no it is odd")
else:
    x=w//2
    if(x%2==0):
        print("yes,brother1 gets",+x)
        print("yes,brother2 gets",+x)
    else:
        print("yes,brother1 gets",x-1)
        print("brother2 gets",x+1)