#!/usr/bin/env python
# coding: utf-8

# In[28]:


# write python function get the unique number of elements from the user given list 

mylist = ['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']

def get_unique_elements(list):
    unique = [x for i, x in enumerate(mylist) if i == mylist.index(x)]
    return unique

get_unique_elements(mylist)


# In[86]:


# write a python function get the maximum number in passed list

def max_check(x):
    max_val = x[0] 
    for check in x: 
        if check > max_val: 
            max_val = check 
    return max_val

print(f'{max_check([2,4,5,7,98])}')


# In[88]:


# write a python function to get the minimum number in passed list

def min_check(x):
    min_val = x[0] 
    for check in x: 
        if check < min_val: 
            min_val = check 
    return min_val

print(f'{min_check([2,4,5,7,98])}')


# In[1]:


# write a program to reverse the list elemnets

list_ = [40,0,1,29,3]
rev_list = list_[::-1]
print(f'reversed list: {rev_list}')


# In[7]:


# write a progarm to sort the list in assending order
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(f'assending_order_list: {new_list}')


# In[8]:


# write a program to sort the list in desending order
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x > minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(f'decending_order_list: {new_list}')


# In[11]:


# write a python function to sort a list of tuples by the second Item 
  
def Sort_Tuple(tup):  
      
    # getting length of list of tuples 
    lst = len(tup)  
    for i in range(0, lst):  
          
        for j in range(0, lst-i-1):  
            if (tup[j][1] > tup[j + 1][1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp  
    return tup  
  
# Driver Code  
tup =[('for', 24), ('is', 10), ('to', 28),  
      ('goal', 1), ('portal', 20), ('a', 15)]  
        
Sort_Tuple(tup) 


# In[12]:


# write a program to insert elemnet in the list after every nth element

letters = ['a','b','c','d','e','f','g','h','i','j']
i = 3
while i < len(letters):
    letters.insert(i, 'x')
    i += 4

letters


# In[22]:


# write a program to find sum of elements in list
total = 0
print(f'sum: {sum([total + x for x in [1, 2, 3, 4, 5]])}')


# In[23]:


# write a  program to get th ematched elemnets from two list 
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
[i for i, j in zip(a, b) if i == j]


# In[24]:


# write a  program to get the matched elements from two list 
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
[i for i, j in zip(a, b) if i != j]


# In[31]:


# write a python program to create dictionary from the lists 

L1 = ['a','b','c','d']
L2 = [1,2,3,4]
d = dict(zip(L1,L2))
print(f'dictionary:{d}')


# In[45]:


# write a program to convert given dictonary to list of list key value pairs 

d = {'Food':'Fish&Chips','2012':'Olympics','Capital':'London'}
list_key_value = [ [k,v] for k, v in d.items() ]
print(f'lsit_key_value:{list_key_value}')


# In[53]:


# write program to Compare two dictionaries and check how many (key, value) pairs are equal
x = {"a":2,"b":2,"c":3,"d":4}
y = {"b":2,"c":3, "d":4}
shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
length = len(shared_items)
print(f'count:{length}')


# In[63]:


# write a python function get the random number from the given range and square the number
import random 

min_value = 10
max_value = 20

def square(x):
    return x*x

def get_square_of_random_number(min_value,max_value):
    return square(random.randint(min_value,max_value))

get_square_of_random_number(min_value,max_value)


# In[67]:


# write a python function to identify the total counts of chars, digits,and symbols for given input string 

def findDigitsCharsSymbols(inputString):
    charCount = 0
    digitCount = 0
    symbolCount = 0
    for char in inputString:
        if char.islower() or char.isupper():
              charCount+=1
        elif char.isnumeric():
              digitCount+=1
        else:
            symbolCount+=1
      
    print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
      
inputString = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols \n")

findDigitsCharsSymbols(inputString)


# In[71]:


#  write a python function to find all occurrences of user given substring in user provided input string ignoring the case

def count_word_occurrences(inputstring,substring):
    inputstring = inputstring
    tempString = inputString.lower()
    count = tempString.count(substring.lower())
    return print(f'Given substring count is :{count}')  
      
inputString = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"
count_word_occurrences(inputString,substring)


# In[74]:


# write a program that prints the sum and average of the digits that appear in the string, ignoring all other characters
import re

inputStr = "English = 78 Science = 83 Math = 68 History = 65"
markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
totalMarks = 0
for mark in markList:
    totalMarks+=mark

percentage = totalMarks/len(markList)  
print(f'Total Marks is:{totalMarks},Percentage is:{percentage}')


# In[75]:


# write a python funaction to create a new string by appending second string in the middle of first string

def appendMiddle(s1, s2):
    middleIndex = int(len(s1) /2)
    print("Original Strings are", s1, s2)
    middleThree = s1[:middleIndex:]+ s2 +s1[middleIndex:]
    print("After appending new string in middle", middleThree)

appendMiddle("bananna", "monkey")


# In[81]:


# write a program to find the last position of a given substring in a given string
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(f"Original String is: {str1}")

index = str1.rfind("Emma")
print(f"Last occurrence of Emma starts at {index}")


# In[82]:


# write a program to remove the empty list from the given list 
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print(str_list)

# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)


# In[85]:


# write a program from given string replace each punctuation with #

from string import punctuation

str1 = '/*Jon is @developer & musician!!'
print(f"The original string is :{str1}")

# Replace punctuations with #
replace_char = '#'

for char in punctuation:
    str1 = str1.replace(char, replace_char)

print(f"The strings after replacement : {str1}")


# In[90]:


# write a program to convert all the sentances present in the list to upper 

mylis = ['this is test', 'another test']
print(f'{[item.upper() for item in mylis]}')


# In[96]:


# write a progarm to adds every 3rd number in a list
from functools import reduce
input_list = [x for x in range(10)]
reduce((lambda x, y: x + y), [val for idx, val in enumerate(input_list) if (idx+1)%3==0])


# In[97]:


# write a program to strips every vowel from a string provided 

vowels = ('a', 'e', 'i', 'o', 'u')
input_string = "awesome"
' '.join([x for x in input_string.lower() if x not in vowels])

