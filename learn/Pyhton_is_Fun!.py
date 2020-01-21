# Solution
# Create a Python function that turns a list of numbers into a string of all the digits together.

def big_num():
    list_of_num = input("Enter some numbers with a space after one another :- ")

    for space in list_of_num:

    str_num_list = [str(num) for num in list_of_num]
    print(int("".join(str_num_list)))

# Create a Python function that will replace any bad language with the word "beep"
