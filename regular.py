# match

# import re                                                   
# pattern="good"
# if re.match(pattern,"good eve,how are you "):
#     print("yes")
# else:
#     print("sorry")

# Search

# import re                                                   
# pattern="good"
# if re.search(pattern,"hi good eve,how are you"):
#     print("yes")
# else:
#     print("sorry")


# #findall

# import re                                                   
# pattern="you"
# b=re.findall(pattern,"hello how are you ,where are you from,'how old are you")
# print(b)
# c=len(b)
# print(c)

# import re                                                   
# pattern = "are"
# matches = re.findall(pattern, "hello how are you ,where are you from,'how old are you")
# output = {pattern: len(matches)}
# print(output)


#to substitute / edit or change


# import re
# str="hey prabhu dilras who are you"
# pattern="prabhu"
# b=re.sub(pattern,"hari ram",str)
# print(b)




# import re
# a='hi adarsh who are you'
# pattern='who'
# c=re.sub(pattern,'how',a)
# print(c)

import re
text = "apple, orange;banana grape|melon"
pattern = r'[,\s;|]+'
split_text = re.split(pattern, text)
print(split_text)

