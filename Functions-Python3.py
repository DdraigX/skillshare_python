
# coding: utf-8

# In[2]:

# Step 1: Define the function
def functionThatModifiesNumber(someNumber):
    print("Argument (input) passed in = ", someNumber)
    someNumber = someNumber * 10
    print("After modification, but inside function, value = ",someNumber)
    return


# In[3]:

# Step 2: Call the function
# Before the function calls
someNumber = 11
print("Value of the variable in calling code before function: ", someNumber)
functionThatModifiesNumber(someNumber)
print("Value of variable in calling code after function: ",someNumber)


# In[4]:

# Step 1: Define the function
def functionThatReAssignsNumber(someNumber):
    print("Argument (input) passed in = ", someNumber)
    someNumber = 3.14
    print("After re-assignment, value inside function = ", someNumber)
    return

# Step 2: Call the function
# Before function call
print("Value of variable in calling code before function is called:",someNumber)

# During function call
functionThatReAssignsNumber(someNumber)
# After function call
print("Value of variable in calling code after function is called", someNumber)


# Moral of the story: if a function reassigns a number (numeric argument)
#                     no result in the calling code (ie change not reflected)

# If a function modifies a numeric argument - no result in the calling code
# IN other words - numbers are not mutable by functions


# In[5]:

###################################################################
# A simple function that takes in a circle's radius, returns its area
###################################################################
# Step 1: Define the function 
def calculateAreaOfTheCircle(radius):
    # we are inside the function body now, as the indentation shows
    area = 3.14 * radius * radius
    # Now return the area ie send it back to the calling function
    return area

# step 2: call the function
radius = 5
area = calculateAreaOfTheCircle(radius)
print("Radius = ", radius, "Area = ",area)


# In[6]:

#######################################################################
# A similar function, but this prints the area to screen, rather than 
# returning it for outside usage
#######################################################################
# Step 1: Define the function
def printAreaOfCircle(radius):
    # indentation changes - we are inside the function now
    print("Given a circle with radius = ", radius," Area = ",(3.14*radius*radius))


# Indentation has changed - we are back outside the function
# the function above does not return anything - it does its thing, and 
# prints to screen inside the function itself
radius2 = 5
printAreaOfCircle(radius)


# In[7]:

###########################################################
# Ok, now a function that takes in a list of radii and returns
# a list of their areas
###########################################################

# step 1 define the function
def calculateAreaOfManyCirclesAllAtOnce(radiusList):
    # we are inside the function - indentation has changed
    # Define an empty list to hold the areas (we will return this)
    resultList = []    
    for oneRadius in radiusList:
        # indentation changes again - we are inside a for-loop now
        # 2 indents, 1 for the the function, 1 for the for-loop
        resultList.append(3.14*oneRadius*oneRadius)
    return resultList
# Indentation changes - we are back out of the function

# Step 2: Call the function
radiusList = [1,2,3,4]
areaList = calculateAreaOfManyCirclesAllAtOnce(radiusList)
print("for circles with radii =",radiusList, " areas are", areaList)


# In[8]:

#################################################################
# Now a function that takes in a list of circle radii, then returns
# 2, not 1, outputs
#    output 1: list of areas of those circles
#    output 2: list of circumferences of those circles
# How do we do this? Via a simple trick - return a diction with 2 keys
##################################################################

# Step 1: Define the function
def calculateAreaAndCircumference(radiusList):
    # we are inside the function - indentation changes
    areaResultList = []
    circumferenceResultList = []
    resultHash = {'Areas':areaResultList,'Circumferences': circumferenceResultList}
    # now walk through the list of radii and calculate the outputs
    for oneRadius in radiusList:
        # Indent changes again - we inside a for-loop inside the function
        areaResultList.append(3.14*oneRadius*oneRadius)
        circumferenceResultList.append(3.14*2*oneRadius)
    # done with the for-loop, return the result
    return resultHash

# step 2: call the function
radiusList = [1,2,3,4]
resultMap = calculateAreaAndCircumference(radiusList)
print("For circles with radii = ", radiusList, "\nAreas = ",resultMap['Areas'],"\n Circumferences = ",resultMap['Circumferences'])


# In[11]:

########################################################################
# A recursive function to reverse a string
#######################################################################

# Step 1: Define the function
def reverseStringRecursive(someString):
    # indentation changes - we are inside the function body
    
    # first, set up the base case
    # Base-case 1: if the string input is None, return as-is
    if someString is None:
        return someString
    # (we will have more to say on None in a bit)
    
    # Base-case 2: if the string is not None, ie it exists,
    # but its length is 0 or 1, then return as-is
    if(len(someString)) <= 1:
        return someString
    
    # btw, in case you are wondering why we needed separate
    # checks for the None and for the length <= 1, its because
    # a None string does not exist, so if we sought to test its
    # length using the len() function, an error would have occurred.
    # More on this when we get to conditionals in a bit.
    
    # Ok! Now for the magical recursive call. This line below is a call
    # to the function that we are already in (ie a call to itself) but
    # with a simpler string passed in.
    return reverseStringRecursive(someString[1:]) + someString[0]
# remember a few different things while parsing that last line 
# 1. a string is just a string of characters
# 2. in a list to get a sub-list of all elements starting from index 1,
# just use the syntax 'list[1:]'
# 3. How can we be sure that the list has an index 1? because we already
# handled the case where the list of length 0 or 1 in the base case.
# 4. the last bit of the line above, takes the first character and tacks
# it onto the end of the reversed substring

# That's it, we are ready to actually call the function now

# Step 2: Use the function, i.e. call it.

someString = "hello world"
print("the reverse of ",someString, " is",reverseStringRecursive(someString))

someString2 = "A"
print("the reverse of ",someString2, " is",reverseStringRecursive(someString2))

someString3 = None
print("the reverse of ",someString3, " is",reverseStringRecursive(someString3))


# In[14]:


# Btw, this example above was a good demonstration of basic
# recursion, but as a way to reverse a string, this is hopelessly
# overcomplicated: Python has amazing built-in features for operations 
# like this
print("the reverse of ", someString, " is ", someString[::-1])



# Never mind the magic of the [::-1] in the line above!
# For now, just remember that 
# 1. Recursion is very handy in a bunch of situations
# 2. Python has a bunch of magical but rather cryptic ways of getting stuff done


# In[ ]:



