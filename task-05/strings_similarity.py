
def string_same(str1, str2):
  # Enter your code for string_same here
    if len(str1)!=len(str2):
        print("Invalid input")
    else:
        similar = []
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                similar.append(str1[i])
                print(str1[i])
        print(len(similar))

# Do not change any code from here onwards
string1 = input()
string2 = input()
string_same(string1, string2)
