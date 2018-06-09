#coding=utf-8
#Exercise10.7
orglist=[1,2,3,3]
def has_duplicates(templist):
     global orglist
#      templist=list[:]#虽然赋值给临时列表，但是递归返回的也是临时列表，这样templist递归的时候就是list
     for i in templist:
         for j in templist[1:]:#切片赋值的话，源列表会改变
             if i==j:
#                  print(templist)
                 return True
         return has_duplicates(templist[1:])
    
print(has_duplicates(orglist))