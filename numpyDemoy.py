import  numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.max())
print(arr.min())
print(arr.mean())


#before shorting
print("before shorting",arr)
#after shorting


arr.sort()
print("after shorting",arr)

arr=np.flip(arr)
#arr=arr[:: -1]

print(arr)