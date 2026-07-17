#variable= it is used to store the values
# rules
#must start with letters(upper or lower or underscore)
#cannot start with number
#vaariablename contains letters,underscore,numbers
#cannot allow any special characters except underscore(_)

#syntax
# variable name=value
a=10
b=20
print(a)
print(b)
c="UDAY SAI"
print(c)
Color="black"
print(Color)
_number=4
print(_number)
#25color=("black") cannot start with number
#print(25color)
color25="black"
print(color25)
#color@=("black")  cannot allow special characters
#print(color@)

#cannot use keyword
#def=100
#class=python here def and class aare keywords

#type 1
#single value can be stored in single variable
code=100
print(code)
#type 2
#storing single value in multiple variables
a=b=c=200
print(b)
#type 3
#storing multiple values in multiple variables
a,b,c=1,2,3
print(b)
#type 4
#dont use same variable name  for value declaration
a=20
a=40
print(a)


#  datatypeS
#integer
#float
#string
#boolean
#list
#set
#tuple
#dict

#variablename=datatype(variable)
c=type("20")
print(c)
clas=type("python")
print(clas)
b=type("10")
print(b)
is_loggin=True
print(type(is_loggin))

nums=[1,2,3,4]
print(type(nums))
nums=["1","2","3"]
print(nums[1]) #it show index and its changable

nums=(1,2,3,4)
print(type(nums)) #tuple
colors=("red","black")
print(colors[0]) #showing index 0 is red

#set
nums={1,2,3,4}
print(type(nums)) #set
nums={1,2,3,3,1.5,6,2}
print(nums) #it removes duplicates

#dict: stores data in key:value format
student={"name":"UDAY SAI",
         "age":20,
         "marks":50}
print(type(student))

student={"name":"UDAY SAI",
         "age":20,
         "marks":50}
print(student["age"])