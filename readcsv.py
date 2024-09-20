# Program to read csv file and return a list of list

fileName = "read.csv"

# function to read csv file and return list
def read_csv(file_name):
 fileHandle = open(file_name,"r")
 data = fileHandle.read()
 fileHandle.close()

 # your logic

 op = data
 return op # it should return list of list

recievedData = read_csv(fileName)

print(recievedData) 