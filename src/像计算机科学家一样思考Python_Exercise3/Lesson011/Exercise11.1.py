#coding=utf-8
#Exercise11.1
import time
# def histogram1(s):
#     d = dict()
#     for c in s:
#          d[c]=d.get(c,0)+1
#     return d     
# def histogram2(s):#速度差不多
#     d = dict()
#     for c in s:         
#          if c not in d:
#             d[c]=1
#          else:
#             d[c]+=1
#     return d
# if __name__=='__main__':
#     start_time = time.time()
#     h=histogram1('abccefsghijklmnopqrestuvwxyzxyzinowkdnownlnkdkalqpklakmfdkaiennqkjifdjancdishfekwfjiwjifdjskfjiewjifjweifndajfdahfjdkahfgkdahkghdkjafhkdahjfdhaskfjdasbciiioujaklbjkafldajifdabc9908zdfafdareiwnklqhifhdljahrjeyquiobfkbakfbdkashfjkdshakfhdasfksdhakfhjajjjjjjjfhhafdasfjdskjfalsjklfsdjajfldsajfkljqioruieowquroieuwiotyroityhroqhthkafhkghsdfafjsdlajflasdglsdhalghasdlakfghsdklaafhjsdklahfjlksdhflkasdhgklasdhgklasdhuiorweuyhoriqurioweurtiopwequtioweutoiweuytioqweurioqweuroiqweuroiqweurioweqhjiorqwejhiofhjqweohflqwerjkhfdjklhfgksdhajkgsdhkfasdhkfhsdajklfhjkdashfkjasdhfjkasdhbhjkfbndasjkfbnasdjkbvkasdbvkfbvkasdfbfjkhzxjkhkvhfkasdjhfhweupiorqweuyirtoewyriuewhfkhadjkfhdksajfhsdjklfhjdksahfkjsdaahfkdlashfkjasdhfkdasbfkasdbkfasdhfkasdhfksdahfklasdbfkbkxcvzbvcmxzbvmxcbnbvasdjbfsdjhkabfdshfsdhfkdsfjhdsfjsdfhsdkfhsdjfjsdlfjsdlajfdslkgjhdlqjhioreqwurioehklsdfahfklsdabnkfndaskvnkasdbksdhfasdjkfhasdkhfjkdashfkabkzxcvjlhvjkadflhfjkdashfksdlahfukdsahlfsdhajfkasdhfjksdalhfksdlahfkjasdhkfsdhafhdsahfdskafsdjkhafhdksahfksdahfkdlashfjsdahjfklsdahfjsdkahfjksdahfkjasdhjfksdahkjfhasdkfhkasdlhfjdksahfjkdashfjkdaslhqwehuiryehwqiuyorweyquiryewuiqyrueqwioryeqwuiryeuiqwhifhdasjkhfdjksahfqwehruioeqwyrweuqihfjkidasbhnfhqwerioryhqweuiryewiqhfiohfuidasyhruiqweohriqwehfiqwerohfui3eqyhruieqwyruiweyruiwehfuiqweohfqwiy347823572354235h3u2i4h3uh1o3huihfiadohfiowdhuifqwehiuofhasdkhfisdabfiadbfbahfbvbvbzxmvbczxbvmcxzvcxbzm,vbxcmnzbvm,zxcbnsdfjkahfjhsdahflqioeruyiqwuyewqtyqepwryuioy27894613868357648q35yuitgairfyseuiafysdiahfuisdahfksdhjkfhsdjkfhsdajkhfkasdkfhsdahfksdlahfjksdahjfkasdhjkfdashfjklasdhkfjasdhjkfhasdkjlfhasdjkfhasdkjlfhsdjkahfjkasdhfjkasdhfjkasdlhflasdjkhfkdjashfjkasdhfjkasdhjkfhasdjkhfkasdlhfkjsdahkfasdhjklfhasdjkhfkjasdhfkasdjhfjksdahfkjasdhfjkasdlhfdjksahfkjlasdhfjkasdhfklsdahfjkasdhuiewqryuiewqyruieqwyruiqweyruioqweyuirweyqiouryqwfgfgfggggggggggffffffffhgdfjkdfhgfdddddddfggggggggggggggggggggghhhhhhhhhhhhhhjjjjjjjjjjjjjjkkkkkkkkkkklzxxcxvcbxcvnbvcm,llfjkhgjdhggfawqwewqrewqtyrutyuiuyoiuipuiykffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqbbbbbbbbbbbbbnhhnhmhk,kloooppl;uytklly,8978735233141658798-0---=][p;nvcxzssdafa1135345346e5478r5679uyfkytuytry6809plilh/kmbnrt5323515332ythhggggggggggggggggggggggggggggggggggfffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggffffffffffffffdddddddddddddddddddddddddddddfgfklfjdslkfasdkljfioerjfiljfdsklnfdlanfldjaifljfklajfkdslsjfkldasjflsdkajfkldajfkldasjfdsklsklsklsklkkkkkkkkkkkkkkkkkkkkslajfdkaljkaljkjlfdsjfklasdjfklasdjflasdjfqweronfowenfoqlnfioweqnfioqwnfowjfiowjrowiejfiowejfoiwenfowenfweonfweionfiowenfiowejnfoiwenfid;lfndiokfnweoifnewoinfweionfweionfweionfoiwenfoiwenfiowejfkdlajkldjlk;sjkljkdfljalkfjdasiofjiowenfqweonfdasfjdkljklfdjasljfldkasajljfasdkl;jfl;djalfjdklsajklfjdsalk;jeiojiewjlkfjdasljfieojklfjkldaanlnknekrenionioniohfjwdiojaiojjjjjjjjjjjjjjjjjjekkeeeeeeeeeeeeewlekwlekwlklssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssdkllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadkdddddddddddcvcccccccccccccccccccccccccccccccccccccccccccbrontosaurusgsrtytkfgjhsdfgsdfghdfghfgjsfggdfgadfgjhsrgerrtgsdghsghegsdfsdvnfgsjsrthdgghdfsgvbsvfdgfagefagsdfassssssssssssssssssgfsfgvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaggggggggggggggggggggggggggggggggggggggggrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#     print(h)
#     elapsed_time = time.time() - start_time
#     print(elapsed_time, 'seconds')

def make_dict():
    fin=open('D:\programming\Pythonlesson001\Mobywords.txt')
    dic=dict()
    i=0
    for words in fin:
        words=words.strip()
        dic[words]=i
        i += 1
#     print(dic)   
    return dic 
if __name__=='__main__':
    start_time=time.time()
    for word in ['aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob','aa', 'alien', 'allen', 'zymurgy','ffs','2fa','da2','yaomin','haha','joe','jason','steve','fred','jacob']:
        s=word
        if s in make_dict():
            print(s,'is in the dictionary')
        else:
            print(s,'is not in the dictionary')   
    elapsed_time = time.time() - start_time
    print(elapsed_time, 'seconds')