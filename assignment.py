# text = """Classes define blueprints, while objects are the instances of classes.

# Inheritance supports code reuse, allowing child classes to inherit behavior.

# Encapsulation ensures objects manage their internal states through methods.

# Python supports multiple inheritance, allowing a class to inherit from multiple classes.

# Abstraction simplifies complex systems by exposing only essential object properties."""

# with open("assignment.txt", "w") as file:
#     file.write(text)

#     print("'assignment.txt' created successfully")

try: 
    #Ask the user to insert the filename

    input_filename = input("Enter the name of the file to read: ")


    with open(input_filename, "r") as infile:
        content = infile.read()

    #modify the content(i.e., set to uppercase)

    modified_content = content.upper()

    #define the output file

    output_filename = "modified" + input_filename

    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)


    print(f"\n✅ Modified content has been written to '{output_filename}'.")


except FileNotFoundError:
       print(" The file does not exist.")
except IOError:
    print(" Could not read or write to the file.")
