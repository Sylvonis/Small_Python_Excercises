"""
create a program that reads the files pares.txt and impares.txt and creates a single file pareseimpares.txt
with all lines from the other two files in order to preserve numerical order
"""

a = input("Write the name of the first archive to open and merge (without.txt)").strip()
b = input("Write the name of the second archive to open and merge (without.txt)").strip()


def numericOrderMerge(x, y):
    with open(f"{x}.txt", "r") as list1, open(f"{y}.txt", "r") as list2, open("merged.txt", "w") as mergedlist:
        i = list1.readlines()
        j = list2.readlines()
        pointer = 0
        counter = 0
        while pointer < (len(i) + len(j)):
            try:
                if i[pointer].strip() > j[pointer].strip():
                    mergedlist.write(j[pointer].strip() + "\n")
                    mergedlist.write(i[pointer].strip() + "\n")
                else:
                    mergedlist.write(i[pointer].strip() + "\n")
                    mergedlist.write(j[pointer].strip() + "\n")
                counter += 2
                pointer += 1
            except:
                print("end")
                break


numericOrderMerge(a, b)