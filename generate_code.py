# Create a string variable to store the generated code
generated_code = ""

# Iterate over the range and append code to the variable
for i in range(2**16):
    generated_code += "    if (number == "+str(i)+")\n"
    if i % 2 == 0:
        generated_code += "        print(\"even\"):\n"
    else:
        generated_code += "        print(\"odd\"):\n"

with open("output_script.py", "w") as file:
    file.write(generated_code)
