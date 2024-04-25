str1 = "abcd"
str2 = "abcde"

for i in set(str2):
    if str1.count(i) != str2.count(i):
        print(i)