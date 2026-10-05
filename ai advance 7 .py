student = {
    
    "name": "Ali",
   
    "age": 20,
    
    "course": "Python",
   
     "marks": 75

}


print("----- Part 1: Access Items -----")




print("Student Name:", student["name"])

print("Student Age:", student["age"])
print("Student Course:", student["course"])

print("Student Marks:", student["marks"])



# Using get() method

print("Course using get():", student.get("course"))





print("\n----- Part 2: Change Items -----")


student["age"] = 21

student["course"] = "Machine Learning"
student["marks"] = 85


print("Updated Dictionary:")

print(student)





print("\n----- Part 3: Add Items -----")



student["city"] = "Islamabad"

student["attendance"] = 90

student["grade"] = "A"



print("Dictionary after adding items:")

print(student)



print("\n----- Part 4: Remove Items -----")



# Remove grade using del

del student["grade"]



print("After removing grade:")

print(student)





# Remove attendance using del

del student["attendance"]




print("After removing attendance:")

print(student)





# Remove city using pop()

student.pop("city")




print("After removing city:")

print(student)






print("\n----- Part 5: Final Student Record -----")



print("Final Dictionary:")

print(student)



print("\nEach key and value separately:")



for key, value in student.items():
 
     print(key, ":", value)


