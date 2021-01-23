file = open("C:\\Users\\mmishra30\\OneDrive - Georgia Institute of Technology\\Desktop\\Python_Scripts\\add_numbers.txt", "r")

line = file.read()

line.split(",")

print (line.split(","))

total = sum([int(num) for num in line.split(',')])

print(total)
