#creates a set from all the seperate text files of the required paints for all the warhammer armies i.e. removed any duplicates

all_paints = []
files = ["custodies.txt", "wolves.txt", "thousand.txt"]
for file in files:
    with open(file,'r') as c:
        for line in c:
            all_paints.append(line.strip())

print(sorted(set(all_paints)))
print(len(set(all_paints)))