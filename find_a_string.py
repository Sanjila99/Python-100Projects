import os

def search_text_infiles(text, path):
    found = False
    os.chdir(path)
    files_list = os.listdir(path)

    for filename in files_list:
        abs_path = os.path.abspath(filename)

        if os.path.isdir(abs_path):
            found = search_text_infiles(text, abs_path)
        elif os.path.isfile(abs_path):
            with open(abs_path, "r", encoding="utf-8", errors="ignore") as file:
                if text in file.read():
                    found = True
                    print(f"'{text}' found in:")
                    print(abs_path)
                    break

    return found

text_to_search = input("Enter the text: ")
directory_path = input("Enter the directory path: ")

if search_text_infiles(text_to_search, directory_path):
    print("Text found in at least one file.")
else:
    print("Text not found in any file.")



