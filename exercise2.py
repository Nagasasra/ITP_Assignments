def translate(text):
    list1 = list(text)
    output=''
    for text2 in list1:
        if text2=='a' or text2=='i' or text2=='u' or text2=='e' or text2=='o' or text2==' ':
            output = output + text2
        else:
            output = output + text2 + "o" + text2
    return output

text = input("Enter texts: ")
output=translate(text)
print("Output: "+output)


