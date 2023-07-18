class student: 
    def __init__(self, name, rollNumber):
        self.__name= name
        self.__rollNumber = rollNumber
        # getters and setter methods
    def setName(self, name):
        self.__name= name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
    
obj= student("vaishali", 13)

#print(obj.__name) # this will not access bcz of private instant

# Modifying the private properties using setter methods
obj.setName("Alice")
obj.setRollNumber(54321)

# Accessing the modified private properties again
print(obj.getName())  
print(obj.getRollNumber())