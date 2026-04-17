#string operations

a = "jayapriya"

#    012345678

print(a[0])#j
print(a[4])#p
print(a[-1])#a
print(a[-3])#i
#print(a[start index,stop index-1])
print(a[4:8])#priya
#print(a[start index:stop index-1:step])
print(a[::2])#alternate
print(a[::-1])#reverse


b = "Bavani Kandhan"
print(b[9:6:-1])#nak
print(b[-5:-9:-1])

b = "     Manideep Thalluru        "
print(b.strip())
print(b.lstrip())
print(b.rstrip())

a = ["usha", "manideep", "abirami"]
print(a)
print(type(a))

b = ["usha", "manideep", "abirami"]
print(b)
print(type(b))

a[0] = "Baradwaj"
print(a)
#b(0) = "Baradwaj"

c = {1,1.1,"i"}
print(c)


d = {1:"ravi",2:"raj"}
print(d)
print(d[1])



d = {"veg":{"tamato":5,"carrot":10,"fruit":{"grapes":6,"apple":8}}}
print(d)
print(d["veg"])
 




