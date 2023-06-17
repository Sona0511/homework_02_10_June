#Implement the convert_to_int() function taking a string argument and returning its integer representation. 
#Throw an exception if the conversion is not possible.
def convert_to_int(string):
    try:
        integer=int(string)
        return integer
    except ValueError:
        raise Exception("not possible")


#example
string="14"
print(convert_to_int(string))
