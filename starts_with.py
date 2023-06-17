#Implement the starts_with() function taking two strings and returning true if the first argument starts with the second one.

def starts_with(string1, string2):
    i=0
    while len(string2)>i:
        if string1[i]!=string2[i]:
            return False      
        i+=1
    return True
  
print(starts_with("hello world", "hel"))
