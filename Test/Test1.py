N = int(input())
for i in range(1,N+1):
    A,B = map(int,input().split())
    if (A == 1 and B == 2) or (A==2 and B == 3) or (A==3 and B ==1):
        print(f"#{i} B")
    else:
        print(f"#{i} A")


