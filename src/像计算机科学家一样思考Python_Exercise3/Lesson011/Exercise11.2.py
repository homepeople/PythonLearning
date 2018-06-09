#coding=utf-8
#Exercise11.2
import time
# known={0:0, 1:1}
# def fibonacci(n):#速度比6.1快很多
#     if n in known:
#         return known[n]
#     res = fibonacci(n-1)+fibonacci(n-2)
#     known[n]=res
#     return res
# 
# if __name__=='__main__':
#     start_time = time.time()
# #     h=histogram1('abccefsghijklmnopqrestuvwxyzxyzinowkdnownlnkdkalqpklakmfdkaiennqkjifdjancdishfekwfjiwjifdjskfjiewjifjweifndajfdahfjdkahfgkdahkghdkjafhkdahjfdhaskfjdasbciiioujaklbjkafldajifdabc9908zdfafdareiwnklqhifhdljahrjeyquiobfkbakfbdkashfjkdshakfhdasfksdhakfhjajjjjjjjfhhafdasfjdskjfalsjklfsdjajfldsajfkljqioruieowquroieuwiotyroityhroqhthkafhkghsdfafjsdlajflasdglsdhalghasdlakfghsdklaafhjsdklahfjlksdhflkasdhgklasdhgklasdhuiorweuyhoriqurioweurtiopwequtioweutoiweuytioqweurioqweuroiqweuroiqweurioweqhjiorqwejhiofhjqweohflqwerjkhfdjklhfgksdhajkgsdhkfasdhkfhsdajklfhjkdashfkjasdhfjkasdhbhjkfbndasjkfbnasdjkbvkasdbvkfbvkasdfbfjkhzxjkhkvhfkasdjhfhweupiorqweuyirtoewyriuewhfkhadjkfhdksajfhsdjklfhjdksahfkjsdaahfkdlashfkjasdhfkdasbfkasdbkfasdhfkasdhfksdahfklasdbfkbkxcvzbvcmxzbvmxcbnbvasdjbfsdjhkabfdshfsdhfkdsfjhdsfjsdfhsdkfhsdjfjsdlfjsdlajfdslkgjhdlqjhioreqwurioehklsdfahfklsdabnkfndaskvnkasdbksdhfasdjkfhasdkhfjkdashfkabkzxcvjlhvjkadflhfjkdashfksdlahfukdsahlfsdhajfkasdhfjksdalhfksdlahfkjasdhkfsdhafhdsahfdskafsdjkhafhdksahfksdahfkdlashfjsdahjfklsdahfjsdkahfjksdahfkjasdhjfksdahkjfhasdkfhkasdlhfjdksahfjkdashfjkdaslhqwehuiryehwqiuyorweyquiryewuiqyrueqwioryeqwuiryeuiqwhifhdasjkhfdjksahfqwehruioeqwyrweuqihfjkidasbhnfhqwerioryhqweuiryewiqhfiohfuidasyhruiqweohriqwehfiqwerohfui3eqyhruieqwyruiweyruiwehfuiqweohfqwiy347823572354235h3u2i4h3uh1o3huihfiadohfiowdhuifqwehiuofhasdkhfisdabfiadbfbahfbvbvbzxmvbczxbvmcxzvcxbzm,vbxcmnzbvm,zxcbnsdfjkahfjhsdahflqioeruyiqwuyewqtyqepwryuioy27894613868357648q35yuitgairfyseuiafysdiahfuisdahfksdhjkfhsdjkfhsdajkhfkasdkfhsdahfksdlahfjksdahjfkasdhjkfdashfjklasdhkfjasdhjkfhasdkjlfhasdjkfhasdkjlfhsdjkahfjkasdhfjkasdhfjkasdlhflasdjkhfkdjashfjkasdhfjkasdhjkfhasdjkhfkasdlhfkjsdahkfasdhjklfhasdjkhfkjasdhfkasdjhfjksdahfkjasdhfjkasdlhfdjksahfkjlasdhfjkasdhfklsdahfjkasdhuiewqryuiewqyruieqwyruiqweyruioqweyuirweyqiouryqwfgfgfggggggggggffffffffhgdfjkdfhgfdddddddfggggggggggggggggggggghhhhhhhhhhhhhhjjjjjjjjjjjjjjkkkkkkkkkkklzxxcxvcbxcvnbvcm,llfjkhgjdhggfawqwewqrewqtyrutyuiuyoiuipuiykffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqbbbbbbbbbbbbbnhhnhmhk,kloooppl;uytklly,8978735233141658798-0---=][p;nvcxzssdafa1135345346e5478r5679uyfkytuytry6809plilh/kmbnrt5323515332ythhggggggggggggggggggggggggggggggggggfffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggffffffffffffffdddddddddddddddddddddddddddddfgfklfjdslkfasdkljfioerjfiljfdsklnfdlanfldjaifljfklajfkdslsjfkldasjflsdkajfkldajfkldasjfdsklsklsklsklkkkkkkkkkkkkkkkkkkkkslajfdkaljkaljkjlfdsjfklasdjfklasdjflasdjfqweronfowenfoqlnfioweqnfioqwnfowjfiowjrowiejfiowejfoiwenfowenfweonfweionfiowenfiowejnfoiwenfid;lfndiokfnweoifnewoinfweionfweionfweionfoiwenfoiwenfiowejfkdlajkldjlk;sjkljkdfljalkfjdasiofjiowenfqweonfdasfjdkljklfdjasljfldkasajljfasdkl;jfl;djalfjdklsajklfjdsalk;jeiojiewjlkfjdasljfieojklfjkldaanlnknekrenionioniohfjwdiojaiojjjjjjjjjjjjjjjjjjekkeeeeeeeeeeeeewlekwlekwlklssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssdkllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadkdddddddddddcvcccccccccccccccccccccccccccccccccccccccccccbrontosaurusgsrtytkfgjhsdfgsdfghdfghfgjsfggdfgadfgjhsrgerrtgsdghsghegsdfsdvnfgsjsrthdgghdfsgvbsvfdgfagefagsdfassssssssssssssssssgfsfgvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaggggggggggggggggggggggggggggggggggggggggrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#     for i in range(100):
#         print(fibonacci(30))
# #     print(h)
#     elapsed_time = time.time() - start_time
#     print(elapsed_time, 'seconds')
    
def make_dict():
    fin=open('D:\编程\Python\Mobywords.txt')
    dic=dict()
    i=0
    for words in fin:
        words=words.strip()
        dic[words]=i
        i += 1
#     print(dic)   
    return dic     

def invert_dic(dic):
    inv_dic=dict()
    for key in dic:
        val=dic[key]
        inv_dic.setdefault(val,key) 
    return inv_dic

if __name__=='__main__':
    start_time = time.time()  
    print(invert_dic(make_dict()))
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'seconds') 