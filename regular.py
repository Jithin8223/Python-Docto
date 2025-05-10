# match

# import re                                                   
# pattern="Good"
# if re.match(pattern,"Good eve,how are you"):
#     print("yes")
# else:
#     print("sorry")

# import re
# pattern = r"123"  # Match the specific number '123'
# if re.search(pattern, "There are 123 apples"):
#     print("Yes, 123 is found")
# else:
#     print("Sorry, 123 not found")



# Search



# import re                                                   
# pattern="good"
# if re.search(pattern,"hi  eve,how are  you good"):
#     print("yes")
# else:
#     print("sorry")


# # #findall

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


# #to substitute / edit or change


# import re
# a='hi adarsh who are you'
# pattern='adarsh'
# c=re.sub(pattern,'jithin',a)
# print(c)


# import re
# text = "apple, orange;banana grape|melon"
# pattern = r'[,\s;|]+'
# split_text = re.split(pattern, text)
# print(split_text)

