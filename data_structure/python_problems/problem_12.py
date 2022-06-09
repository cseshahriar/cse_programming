# inputs
n = int(input("Please enter a number "))
data = list(map(int, input("Enter numbers ").strip().split()))[:n] 
number_to_check = int(input('Please number to check '))

def check_number_in_array(number):
    """ checking given number in array """
    if number in data:
        print("The number found in the array")
    else:
        print("The number did't found in the array")


check_number_in_array(number_to_check)