
#revstring = "abc123"

# revstring = "abc123"



# def go(abc):
    
#     r =  len(revstring)
#     revlist = []
#     for i in revstring:
#         r =  len(revstring)
#         revlist.append(i)

#         print(revlist)
#     return 


# abc = go(revstring)


def reversestring(somestring):
    if somestring is None: 
        return somestring
    if(len(somestring)) <= 1:
        return somestring
    return reversestring(somestring[1:]) + somestring[0]

somestring = "hello world"
print("reverse of string", somestring, " is ", reversestring(somestring))

print(somestring[::-1])