ls=[]
n=int(input("Enter limit:"))
for i in range(n):
    ls.append(int(input("Enter element: ")))
print("Unsorted list: ",ls)
for i in range(n):
    for j in range(i+1,n):
        if ls[i]>ls[j]:
            temp=ls[i]
            ls[i]=ls[j]
            ls[j]=temp
print("Sorted list",ls)


output:
Enter limit:5
Enter element: 12
Enter element: 13
Enter element: 14
Enter element: 15
Enter element: 16
Unsorted list:  [12, 13, 14, 15, 16]
Sorted list [12, 13, 14, 15, 16]
