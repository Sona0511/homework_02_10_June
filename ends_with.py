#Implement the ends_with() function taking two strings and returning true if the first argument ends with the second one.

def ends_with(string1, string2):
    i=-1
    while len(string2)<i:
        if string2[i]!=string1[i]:
            return False      
        i+=1
    return True

print(ends_with("hello world", "rld"))
