# 1
# mylist1=[20,40,32,6,78,90]
# mylist1[-1 -2 -3 -4 -5 -6 -7]
# print(mylist1)

# 2
# mylist1=[20,40,32,6,78,90]
# total=0
# for i in mylist1:
#     total=total+i
# print(total)

# 3
# mylist=[10 ,9 ,14]
# for i in range(len(mylist) -1 ):
#     if mylist [i] > mylist [i+1]:
#         temp=mylist [i]
#         mylist [i]=mylist [i+1]
#         mylist [i+1]=temp
        

# ikinci hell
# mylist=[10 ,9 ,14, 12,13,7,5,3,1]

# for j in range(len(mylist) ):
    
#     for i in range(  len(mylist) -1  ):    
#         if mylist [i] > mylist [i+1]:
#             temp=mylist [i]
#             mylist [i]=mylist [i+1]
#             mylist [i+1]=temp
 
# print(mylist)
# print(mylist)





# 4
# mylist1=[20,40,32,6, 6, 78, 40, 78, 90]
# for item in mylist1:
#     item_index = mylist1.index(item)
    
#     for i in range(item_index+1, len(mylist1) -1):
#         if item==mylist1[i]:
#             del mylist1[i]
# print(len(mylist1))


# 5/
# mylist=[2, 3, 4, 5, 6 ]
# Sum=sum(mylist)
# Count= len(mylist)
# print(Sum)
# print(Count)
# print(Sum/Count)
# if (Count//2==0):
#     print

# 5//
# nums=[1,2,3,5,4]

# sum = 0

# for num in nums:  
#     sum += num

# edediorta = sum / len(nums)  
# print(edediorta)
# for j in nums:
#    for i in range(len(nums)-1):
#       if nums[i]>nums[i+1]:
#          temp=nums[i]
#          nums[i]=nums[i+1]
#          nums[i+1]=temp
# print(nums)
# if len(nums)%2!=0:
#    median_index=len(nums)//2
#    print(nums[median_index])
   
# else :
#    median_index=len(nums)//2
#    res=(nums[median_index]+nums[median_index-1])/2
   
#    print(res)

# 5///
list_str=input("Listi daxil edin: ")
list_a=list_str.split(" ")
list_a=[int(item) for item in list_a]
print(list_a)
list_a