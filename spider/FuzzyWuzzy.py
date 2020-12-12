from fuzzywuzzy import fuzz



# https://mp.weixin.qq.com/s/IrzoNCoT8E5LKut95Fdjcw
# 对字符串进行模糊匹配，然后返回相似度。


# ratio,  not very precise result. 
a = fuzz.ratio("aaabbb",  "aaabbb")
print(a)

b = fuzz.ratio("aaab", "aaabbb")
print(b)

c = fuzz.ratio("aabb", "aaabbb")
print(c)


# partial ratio,  better than "ratio"
print(fuzz.partial_ratio("aaabbb",  "aaabbb"))
print(fuzz.partial_ratio("aaab",  "aaabbb"))
print(fuzz.partial_ratio("aabb",  "aaabbb"))
print(fuzz.partial_ratio("aabbc",  "aaabbb"))


# token sort ratio,  wite space separated,  convert every letter to lower letter,  ignore all special character except whitespace.
print(fuzz.token_sort_ratio("I love you", "you love I"))
print(fuzz.token_sort_ratio("I love you", "you love me"))
print(fuzz.token_sort_ratio("I love you", "do you love I"))
print(fuzz.token_sort_ratio("I love you", "DO you LOVE me"))


# token set ratio
print(fuzz.token_set_ratio("I love you", "you love I I I I"))
print(fuzz.token_set_ratio("I love you", "you you love me me"))
print(fuzz.token_set_ratio("I love you", "do you love I I I I "))
print(fuzz.token_set_ratio("I love you", "DO DO DO you LOVE me me me "))

from fuzzywuzzy import process
choices = ["河南省", "郑州市", "湖北省", "武汉市"]
print(process.extract("郑州", choices, limit=2))
print(process.extractOne("郑州", choices))
print(process.extractOne("北京", choices))
print(process.extractOne("哥本哈根", choices))
print(process.extractOne("山东省", choices))
print(process.extractOne("qingdao", choices))
      
