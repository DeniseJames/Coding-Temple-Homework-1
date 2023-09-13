'''
Question 1
Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the
code has been defined as below. def hello_name(user_name):

'''
# function to print usernamr
def hello_name(user_name):
   # Print the entered username
    print(f"Hello {user_name}")
    
    
# call the hello_name function    
hello_name("Viola")   

# Prompt the user for a username
client_name = input("Please enter your username: ")
hello_name(client_name)

'''
Question 2
Write a python function, first_odds that prints
the odd numbers from 1-100 and returns nothing def first_odds():

'''
def first_odds():
    i = 1
    # loop from 1 to 100
    while(i < 101):
        # If there is a remainder divided by 2, print the odd numver
         if (i%2)==1:
            print(i)
         i+=1    
            
first_odds()       

''''
Question 3
Please write a Python function, max_num_in_list to return the max number of a given list.
The first line of the code has been defined as below. def max_num_in_list(a_list):
'''    
    
def max_num_in_list(a_list):
    # a check for empty a_list
    if not a_list:
        return None
    # start with first number
    max_num = a_list[0]
    # use for loop to compare max_num to integers in a_list start with second element
    for i in a_list[1:]:
        if i > max_num:
            max_num = i
    print(f"The maximum number is:  {max_num}")        
    return max_num

# call max_num_in_list 
max_num_in_list([1,2,-10,5, -2])
        
'''
Question 4
Write a function to return if the given year is a leap year.
A leap year is divisible by 4, but not divisible by 100 unless
it is also divisible by 400. The return should be boolean 
Type (true/false). def is_leap_year(a_year):
'''

def is_leap_year(a_year):
    if a_year%4==0 and a_year%100!=0 or  a_year%4==0 and a_year%100==0 and a_year%400==0:
        
            return True
    return False    
        
print(f" Is 2000 a leap year?  {is_leap_year(2000)}")
print(f" Is 2001 a leap year?  {is_leap_year(2001)}")

'''
Question 5
Write a function to check to see if all numbers in the list are consecutive numbers.
For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
'''

def is_consecutive(a_list):
    # Iterate through the full list
    a = a_list[0]
    for num in a_list[1:]:
        if num-1 !=a:
            return False
        else:
            a = num
    return True

print(f"Is the list consecutive? {is_consecutive([1,2,4,5])}")    
print(f"Is the list consecutive? {is_consecutive([2,3,4,5,6,7])}")    
        