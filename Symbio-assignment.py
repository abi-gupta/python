import pandas as pd

# Open text file and write all numbers to it
file = open("file.txt", "a")
for num in range(100):
    num += 1
    file.write("%i\n" % num)
file.close()

# Option 1
# Read and print half numbers from text file
with open("file.txt") as f:
    counter = 0
    for data in f:
        print(data)
        counter += 1
        if counter == 50:
            break

# Option 2
# Read and print n rows from text file using pandas library
data = pd.read_csv("file.txt", nrows=49)
print(data)
