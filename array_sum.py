def _sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum
arr=[]
arr=[10,20,30,40]
n=len(arr)
ans=_sum(arr)
print("Sum of array is=",ans)