
# coding: utf-8

# In[2]:

someString = "This is a random string"


# In[3]:

# since strings are lists of characters, lets use the len() function to 
# print the length of this string

print("the length of " + someString + " is " + str(len(someString)))


# In[4]:

# similarly we can use the [] and : operators (indexing operators) to print
# substrings - by accessing the subparts of the string 

print(someString[:5])


# In[4]:

print(someString[6:])


# In[5]:

print(someString[9:14])


# In[6]:

# the count function returns how often a substring appears in a string 
print(someString.count("random"))


# In[7]:

# the index function will return the first index where a given substring appears
# remember that strings - being lists are indexed from zero

print(someString.index("random"))


# In[8]:

# in addition to being lists, strings have other nifty functions too - 
# for instance, to convert case, use lower() and upper() respectively
print(someString.lower())


# In[9]:

print(someString.upper())


# In[10]:

# to split a string into words or sub-strings separated by some character, use 
# the split() function
print(someString.split(' '))


# In[12]:

# there are easy ways to check if strings end with or start with
# specific character sequences
print(someString.startswith("Some"))
print(someString.endswith("string"))


# In[ ]:

# one last trick - the indexing operator [] can take in negative numbers 
# too. They are interpreted as being 'from the end of the string'


# In[13]:

someString[-3:]


# In[14]:

someString[-7:-3]


# In[ ]:



