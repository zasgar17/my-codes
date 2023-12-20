# def ters(list):
#     ilk_ind=0
#     son=len(list)-1
#     while ilk_ind<son:
#         temp=list[ilk_ind]
#         list[ilk_ind]=list[son]
#         list[son]=temp
#         ilk_ind+=1
#         son-=1
#     print(list)
    
# mes=[4, 7, 5, 9, 5, 3, 6]
# print(mes)
# tersi=ters(mes)
# print(tersi)

# def invertor(list_a):  
#     list_c=[]
#     for i in range (len(list_a)-1,-1,-1):
#         list_c.append(list_a[i])
#     return list_c
      

# list_a =input("Enter a list plss:\n")
# list_a = [int(num) for num in list_a.split(" ")]
# list_a=invertor(list_a)
# print(list_a)