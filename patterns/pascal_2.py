def nth_row(n):
    ans = 1
    print(ans,end=" ")
    for i in range(1,n):
        ans = ans * (n-i)
        ans = ans//i
        print(ans,end=" ")
    
row = int(input("Enter the row you want to print : "))
nth_row(row)