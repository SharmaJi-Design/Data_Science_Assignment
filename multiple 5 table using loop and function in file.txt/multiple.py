# Function to write multiplication table to file
def write_table(filename, number, lines):
    with open(filename, "w") as file:
        for i in range(1, lines + 1):
            space = " " * (i - 1) * 3  # spacing for formatting
            file.write(f"{space}{number}*{i}={number*i}\n")

# Call the function
write_table("data.txt", 5, 10)

# Read and print the content of the file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
