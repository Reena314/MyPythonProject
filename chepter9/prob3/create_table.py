# wap to generate multiplication table  2 to 20 and write  it to diffrent files and write it to a foldar.

def generate_table(n):
    table = ""  # store multiplication table as text. We’ll use this variable to build the table text line by line.
    
    # Generate the table
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    # Write the table to a file inside 'tables' folder
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 2 to 20
for i in range(2, 21):
    generate_table(i)

print("✅ Multiplication tables generated successfully in the 'tables' folder!")