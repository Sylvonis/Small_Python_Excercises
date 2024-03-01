"""
    Create a program that receives a list of names of files and create a new big file
"""

archive_names = []

while True:
    name_input = input("input the archives you want to print. 0 to Quit/Print.\nInput Example: "
                       "'archive_name.txt'\n\n")
    if name_input == "0":
        break
    elif name_input[-4:] != ".txt":
        print("THIS IS NOT A VALID .TXT FILE\n")
        continue
    else:
        archive_names.append(name_input)

    if archive_names == "":
        print("No Archives were inputted.")
    else:
        print("Choosen Archives: ", end="")
        for name in archive_names:
            print(name, end=" | ")
        print("\n")

with open("fileCreateByInput.txt", "w") as newFile:
    for name in archive_names:
        try:
            with open(name, "r") as archive:
                newFile.write(f"WRITING '{name}'\n\n\n")
                for line in archive.readlines():
                    newFile.write(line)
                newFile.write("\n" * 4)
        except FileNotFoundError:
            print(f"FILE {name} WAS NOT FOUND")
            continue
print("end")







