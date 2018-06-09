#coding=utf-8
#Exercise6.1 and fibonacci
# import math
import time
# def factorial(n):
#      if not isinstance(n, int):
#          print('Factorial is only defined for integers')
#          return None
#      elif n<0:
#          print('Factorial is only defined for negative integers')
#          return None
#      elif n == 0:
#          return 1
#      else:
#          recurse =factorial(n-1)
#          result= n * recurse
#          return result
#
# z=factorial(5)
# print(z) 


# def hypotenuse(x,y):
#     dsquared=x**2+y**2
#     z=math.sqrt(dsquared)
#     return z
# print (hypotenuse(3, 4))

# def is_divisible(x,y):
#     if x%y==0:
#         return True
#     else:
#         return False
# print(is_divisible(3,2))

# known = {0: 0, 1: 1}
# def fibonacci(n):
#     if n in known:
#         return known[n]
#     res = fibonacci(n - 1) + fibonacci(n - 2)
#     known[n] = res
# #     print(n,res)#打印过程
#     return res


# def fibonacci(n):#冗余值太多，too many redundancies
#     if n==0 or n==1:
#         result=n
# #         print(n,result)
#         return result
#     else:
#         result= fibonacci(n-1)+fibonacci(n-2)
# #         print(n,result)#打印过程
#         return result
 
from time import time

# def fibonacci(max):
#     a, b = 0, 1
#     i=0
#     for i in range(max):
#         yield a
#         a, b = b, a+b
        
# def fibonacci(max): 
#    n, a, b = 0, 0, 1 
#    L = [] 
#    while n < max: 
#        L.append(b) 
#        a, b = b, a + b 
#        n = n + 1 
#    return L     
def fibonacci(num):#Fastest
     a,b =0,1
     i=0
#     for i in range(num):#for 和while 速度差不多, 但while 更灵活
     while i<=num:#(num) yield a ==(num-1) yield b
         yield a
         a, b = b, a+b 
         i+=1        

t = time()
for f in fibonacci(10000): # The generator constructs an iterator
        pass #print(f)#   
t = time() - t
print (t, f) 
  
# if __name__=='__main__':
#     start_time = time.time()
# #     h=histogram1('abccefsghijklmnopqrestuvwxyzxyzinowkdnownlnkdkalqpklakmfdkaiennqkjifdjancdishfekwfjiwjifdjskfjiewjifjweifndajfdahfjdkahfgkdahkghdkjafhkdahjfdhaskfjdasbciiioujaklbjkafldajifdabc9908zdfafdareiwnklqhifhdljahrjeyquiobfkbakfbdkashfjkdshakfhdasfksdhakfhjajjjjjjjfhhafdasfjdskjfalsjklfsdjajfldsajfkljqioruieowquroieuwiotyroityhroqhthkafhkghsdfafjsdlajflasdglsdhalghasdlakfghsdklaafhjsdklahfjlksdhflkasdhgklasdhgklasdhuiorweuyhoriqurioweurtiopwequtioweutoiweuytioqweurioqweuroiqweuroiqweurioweqhjiorqwejhiofhjqweohflqwerjkhfdjklhfgksdhajkgsdhkfasdhkfhsdajklfhjkdashfkjasdhfjkasdhbhjkfbndasjkfbnasdjkbvkasdbvkfbvkasdfbfjkhzxjkhkvhfkasdjhfhweupiorqweuyirtoewyriuewhfkhadjkfhdksajfhsdjklfhjdksahfkjsdaahfkdlashfkjasdhfkdasbfkasdbkfasdhfkasdhfksdahfklasdbfkbkxcvzbvcmxzbvmxcbnbvasdjbfsdjhkabfdshfsdhfkdsfjhdsfjsdfhsdkfhsdjfjsdlfjsdlajfdslkgjhdlqjhioreqwurioehklsdfahfklsdabnkfndaskvnkasdbksdhfasdjkfhasdkhfjkdashfkabkzxcvjlhvjkadflhfjkdashfksdlahfukdsahlfsdhajfkasdhfjksdalhfksdlahfkjasdhkfsdhafhdsahfdskafsdjkhafhdksahfksdahfkdlashfjsdahjfklsdahfjsdkahfjksdahfkjasdhjfksdahkjfhasdkfhkasdlhfjdksahfjkdashfjkdaslhqwehuiryehwqiuyorweyquiryewuiqyrueqwioryeqwuiryeuiqwhifhdasjkhfdjksahfqwehruioeqwyrweuqihfjkidasbhnfhqwerioryhqweuiryewiqhfiohfuidasyhruiqweohriqwehfiqwerohfui3eqyhruieqwyruiweyruiwehfuiqweohfqwiy347823572354235h3u2i4h3uh1o3huihfiadohfiowdhuifqwehiuofhasdkhfisdabfiadbfbahfbvbvbzxmvbczxbvmcxzvcxbzm,vbxcmnzbvm,zxcbnsdfjkahfjhsdahflqioeruyiqwuyewqtyqepwryuioy27894613868357648q35yuitgairfyseuiafysdiahfuisdahfksdhjkfhsdjkfhsdajkhfkasdkfhsdahfksdlahfjksdahjfkasdhjkfdashfjklasdhkfjasdhjkfhasdkjlfhasdjkfhasdkjlfhsdjkahfjkasdhfjkasdhfjkasdlhflasdjkhfkdjashfjkasdhfjkasdhjkfhasdjkhfkasdlhfkjsdahkfasdhjklfhasdjkhfkjasdhfkasdjhfjksdahfkjasdhfjkasdlhfdjksahfkjlasdhfjkasdhfklsdahfjkasdhuiewqryuiewqyruieqwyruiqweyruioqweyuirweyqiouryqwfgfgfggggggggggffffffffhgdfjkdfhgfdddddddfggggggggggggggggggggghhhhhhhhhhhhhhjjjjjjjjjjjjjjkkkkkkkkkkklzxxcxvcbxcvnbvcm,llfjkhgjdhggfawqwewqrewqtyrutyuiuyoiuipuiykffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqbbbbbbbbbbbbbnhhnhmhk,kloooppl;uytklly,8978735233141658798-0---=][p;nvcxzssdafa1135345346e5478r5679uyfkytuytry6809plilh/kmbnrt5323515332ythhggggggggggggggggggggggggggggggggggfffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggffffffffffffffdddddddddddddddddddddddddddddfgfklfjdslkfasdkljfioerjfiljfdsklnfdlanfldjaifljfklajfkdslsjfkldasjflsdkajfkldajfkldasjfdsklsklsklsklkkkkkkkkkkkkkkkkkkkkslajfdkaljkaljkjlfdsjfklasdjfklasdjflasdjfqweronfowenfoqlnfioweqnfioqwnfowjfiowjrowiejfiowejfoiwenfowenfweonfweionfiowenfiowejnfoiwenfid;lfndiokfnweoifnewoinfweionfweionfweionfoiwenfoiwenfiowejfkdlajkldjlk;sjkljkdfljalkfjdasiofjiowenfqweonfdasfjdkljklfdjasljfldkasajljfasdkl;jfl;djalfjdklsajklfjdsalk;jeiojiewjlkfjdasljfieojklfjkldaanlnknekrenionioniohfjwdiojaiojjjjjjjjjjjjjjjjjjekkeeeeeeeeeeeeewlekwlekwlklssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssdkllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadkdddddddddddcvcccccccccccccccccccccccccccccccccccccccccccbrontosaurusgsrtytkfgjhsdfgsdfghdfghfgjsfggdfgadfgjhsrgerrtgsdghsghegsdfsdvnfgsjsrthdgghdfsgvbsvfdgfagefagsdfassssssssssssssssssgfsfgvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaggggggggggggggggggggggggggggggggggggggggrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#     print(fibonacci(999))
# #     print(h)
#     elapsed_time = time.time() - start_time
#     print(elapsed_time, 'seconds')


  

