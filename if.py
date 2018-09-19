a = 10
b = 5
if a > b :
	print("a is greater")
else :
        print("b is greater")
        
print ("Enter your name :")
name = input()
if name == 'dinesh' :
        print ("Hi"+" "+name)
elif name == "" :
        print ("please enter your name")
else :
        print ("invalid name")

print ("Enter your alias name")
name=input()
print ("Enter your age")
age=input()
print ("Hi "+name+" you're "+age+" years old" )
if int(age)<18:
    print ("you're not eligible for voting")
    diff=int(age)-18
    print ("you can vote after "+str(diff)+" years")
else:
    print ("you're eligible for voting")
