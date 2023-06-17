#Implement the find_last_not_of() function taking a string and a character sequence as its arguments. 
#The function returns the last character equal to none of the characters in the given character sequence.
def find_last_not_of(string, chars):
    for char in reversed(string):
          if char not in chars:
              return char
    return "false"   
    
#Example
string = "abc def ghi"
chars = "def ghi" 

print(find_last_not_of(string, chars))  
