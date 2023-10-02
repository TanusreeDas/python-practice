def read_my_file(filename):
    with open(filename, "r") as file:
        for content in file:
            print(content,end="")

def write_into_my_file(filename,content,write_mode):
    with open(filename,write_mode) as file:
        file.writelines(content)
        file.writelines(content)


if __name__ == "__main__":
    file_path = "../../docs/readfrom.txt"
    file_paths = "../../docs/readfrom2.txt"
    read_my_file(file_path)
    write_into_my_file(file_paths,"Another Line\n","a")#this will create a new file if does not exists and rewrite the file with porivided content
    read_my_file(file_paths)

