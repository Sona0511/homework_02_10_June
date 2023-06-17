#Implement the rotate_by() function taking an integer array and a number as its arguments. 
#The function returns the array rotated by the specified number of positions (given by the second argument).
def rotate_by(array, number):
    rotated = array[number:] + array[:number]
    return rotated

# Example
array = [8, 1, 6, 5, 2]
print(rotate_by(array, 3))  
