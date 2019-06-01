N = int(input())
arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))

prev = 0
result = abs(arr1[0] - arr2[0]) #base case

for i in range(1,N):
    vert = result + abs(arr1[i] - arr2[i])
    horz = prev + abs(arr1[i] - arr1[i-1]) + abs(arr2[i] - arr2[i-1]) 
    prev = result
    result = max(vert,horz)

print("Max Sum : ",result)