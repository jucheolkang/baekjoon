import sys
roof0 = int(sys.stdin.readline())
roof1 = int(sys.stdin.readline())
note1 = list(map(int,sys.stdin.readline().split()))
roof2 = int(sys.stdin.readline())
note2 = list(map(int,sys.stdin.readline().split()))
note1.sort()
for j in range(roof0):
    for i in note2:

        start = 0
        end = len(note1)-1
        while start<=end:
            min = (start+end)//2
            if note1[min] == i:
                print("1")
                break
            elif note1[min] < i:
               start = min+1 
            elif note1[min] > i:
                end = min-1
        
        print("0")
    