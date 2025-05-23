def modify_content(content):
    # Example modification: convert to uppercase
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return

    modified_content = modify_content(content)

    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified content written to '{new_filename}' successfully.")
    except IOError:
        print(f"Error: Could not write to file '{new_filename}'.")

if __name__ == "__main__":
    main()
