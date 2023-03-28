from pathlib import Path

print(f"Current Working Directory : {Path.cwd()}")

filepath=Path("./FinTech-Bootcamp-Week-2/datastruct/input.txt")

with open(filepath, 'r') as file:
    text = file.read()
    print(text)

output_path = Path("./FinTech-Bootcamp-Week-2/datastruct/output.txt") 

with open(output_path, "w") as file:
    file.write("This is in the output file")
    file.write(text)