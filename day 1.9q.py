time=int(input())
entry=list(map(int,input().split()))
exit=list(map(int,input().split()))
present=0
total_guests=0
for i in range(time):
    Present+=entry[i]-exit[i]
    if Total_guests<present:
        Total_guests=present
print(Total_guests,end=' ')
