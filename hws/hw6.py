my_dict= {
   "list_1":[8,2,3,4],
   "list_2":[5,6,1,10],
 }


my_dict_2= {
   "list_1":[7,19,11],
   "list_4":[12,13,3],
 }

new_dict={
   
}

for key_1,value_1 in my_dict.items() :
      for key_2,value_2 in my_dict_2.items():
         if key_1!=key_2: 
            new_dict[key_1]=value_1
         else : 
            new_dict[key_1 + "_a"]
