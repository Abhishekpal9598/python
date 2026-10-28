 

# import calendar

# year = int(input("Enter year: "))

# print("\nCALENDAR FOR", year, "\n")
# # print(calendar.calendar(year))

# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Main program
# try:
#     N = int(input("Enter the value of N (N > 0): "))

#     if N <= 0:
#         print("Error: Input must be a positive integer greater than 0.")
#     else:
#         print("Fibonacci number F(", N, ") =", fibonacci(N))

# except ValueError:
#     print("Error: Please enter a valid integer.")







# # Function to convert binary to decimal
# def binary_to_decimal(binary):
#     try:
#         return int(binary, 2)
#     except ValueError:
#         return "Invalid Binary Number!"

# # Function to convert octal to hexadecimal
# def octal_to_hexadecimal(octal):
#     try:
#         decimal = int(octal, 8)      # Convert octal to decimal
#         return hex(decimal)[2:].upper()  # Convert decimal to hexadecimal
#     except ValueError:
#         return "Invalid Octal Number!"


# # Main Program
# print("Choose Conversion:")
# print("1. Binary to Decimal")
# print("2. Octal to Hexadecimal")

# choice = input("Enter your choice (1/2): ")

# if choice == '1':
#     b = input("Enter a binary number: ")
#     print("Decimal Value =", binary_to_decimal(b))

# elif choice == '2':
#     o = input("Enter an octal number: ")
#     print("Hexadecimal Value =", octal_to_hexadecimal(o))

# else:
#     print("Invalid Choice!")


# # Short version
# sentence = input("Enter a sentence: ")

# words = len(sentence.split())
# digits = sum(1 for char in sentence if char.isdigit())
# uppercase = sum(1 for char in sentence if char.isupper())
# lowercase = sum(1 for char in sentence if char.islower())

# print(f"Words: {words}")
# print(f"Digits: {digits}")
# print(f"Uppercase: {uppercase}")
# print(f"Lowercase: {lowercase}")

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
        
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
    
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# Test the sorting algorithms
# numbers = [64, 34, 25, 12, 22, 11, 90]

# print("Original list:", numbers)
# print("Insertion Sort:", insertion_sort(numbers.copy()))
# print("Merge Sort:", merge_sort(numbers.copy()))

# def roman_to_int(roman):
#     roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
#                   'C': 100, 'D': 500, 'M': 1000}
    
#     total = 0
#     prev_value = 0
    
#     for char in reversed(roman):
#         current_value = roman_dict[char]
        
#         if current_value < prev_value:
#             total -= current_value
#         else:
#             total += current_value
        
#         prev_value = current_value
    
#     return total

# # Test the function
# test_romans = ["III", "IV", "IX", "LVIII", "MCMXC"]
# for roman in test_romans:
#     print(f"{roman} = {roman_to_int(roman)}")


# # Without Regex:
# # 415-555-4242: True
# # 123-456-7890: True
# # 415-555-424: False
# # 415-555-424a: False

# # With Regex:
# # 415-555-4242: True
# # 123-456-7890: True
# # 415-555-424: False
# # 415-555-424a: False


# # Without Regular Expression
# def isphonenumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True

# # With Regular Expression
# import re

# def isphonenumber_regex(text):
#     pattern = r'\d{3}-\d{3}-\d{4}'
#     return bool(re.match(pattern, text))

# # Test both functions
# test_numbers = ["415-555-4242", "123-456-7890", "415-555-424", "415-555-424a"]

# print("Without Regex:")
# for num in test_numbers:
#     print(f"{num}: {isphonenumber(num)}")

# print("\nWith Regex:")
# # for num in test_numbers: 


# import zipfile
# import os

# folder_path = 'your_folder'      # Replace with your folder path
# zip_file_name = 'output.zip'     # Desired zip file name

# with zipfile.ZipFile(zip_file_name, 'w') as zipf:
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             arcname = os.path.relpath(file_path, folder_path)
#             zipf.write(file_path, arcname)

import zipfile
import os

def create_zip(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"ZIP file '{zip_name}' created successfully!")

# Usage
folder_path = "my_folder"  # Change to your folder path
zip_name = "my_folder.zip"
create_zip(folder_path, zip_name)



























































