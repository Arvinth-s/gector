# test_sentence="பொழுது சாய்ண்து வெகு நேரமாகிவிட்டது"
# for words in test_sentence.split(' '):
#     if("ாக" in words):
#         print(words)

# x = '''hello.
# I'm arvinth'''
# print(x.split(' '))
x = 'றோ'
tamil_inflation_list = ['ஂ', 'ௗ	', '்', 'ௌ', 'ோ', 'ொ', 'ை', 'ே', 'ெ', 'ூ', 'ு', 'ீ', 'ி', 'ா', 'ஂ']
for i in x:
    if(i in tamil_inflation_list):
        print('present')
