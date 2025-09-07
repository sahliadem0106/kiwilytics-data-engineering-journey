animals=["bird","cat","lion",1,2,3]
print(animals)
#append(new_elem_value) is a method to add a new element in the list but in the end of it 
animals.append("hamster")
print(animals)
#insert(pos,new_elem_value)  is a command to add a new value in a specific position
animals.insert(4,"turtle")
print(animals)
#remove(wanted_to _del_element) is a method to delete a specific element in the list 
animals.remove("turtle")
print(animals)
# while studing else if elif i we used this to cheack if an elemnt is in a list
if "bird" in animals:
    print("chedou")
if "lion" not in animals:
    print ("i love poland bro")
