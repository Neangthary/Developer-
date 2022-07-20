# # Python program to display all the prime numbers within an interval
# #

# from re import M
# from tkinter import W
# from unittest import result


# lower = 800
# upper = 850

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# #2. Write s sort function to sort the elements in list 
# my_list = [3,2,11,7,5]
# my_list.sort()
# print(my_list)

# #3. write a sorting function without using the list.sort function

# my_list = [4, 2, 3, -1, -2, 0, 1]

# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):

#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j], my_list[i]

# print(my_list)
# #or 
# #bubble sort smalles on the top
# intial_list = [12,13,34,5,1,2,3,6,7,90,67,102]
# new_list = []
# while intial_list:
#     minimun = intial_list[0]
#     for i in intial_list:
#         if minimun > i:
#             minimun = i
#     # new_list.insert(0, minimun)
#     new_list.append(minimun)
#     intial_list.remove(minimun)
#     print(new_list)
    
# #9Given an array arr[] of n elements, write a Python function to search a given element x in arr[].
# def search(arr, n, x):
#     for i in range(0, n):
#         if (arr[i]== x):
#             return i 
#     return -1
# # Driver Code
# arr = [2, 3, 4, 10, 40]
# x = 10
# n = len(arr)
# # Function call
# result = search(arr, n, x)
# if(result == -1):
#     print("Enter is not present in array")
# else: 
#     print("Enter is present at index", result)

    #Write a Python program to print a list in reverse
# list_num = [1, 2, 3, 4, 7]

# list_num.reverse()
# print(list_num)

# int = [54321]
# l =[]
# for i in int:
#     l.insert(0,i)
# print(l)

# num = 75432
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print("Reversed NUmber: " + str(reversed_num))


# write a Python to check whether an integer number is a Palindrome or not


# number = int (input("Type a integer number: "))
# temp = number
# reverse = 0
# while number!=0:
#     remainder = number % 10 
#     reverse = reverse *10 + remainder 
#     number = number//10
# print("Reverse integer number: ", reverse)
# if (temp == reverse):
#     print("True")
# else:
#     print("False")

number = int(input("enter number: "))

while number !=0:
    remainder =number %10
    if(remainder!=0 and remainder!=1):
        print("Number is not in bunary representation! ")
        break
    number = number//10
    if(number==0):
      print("Number is bunary representation !")



