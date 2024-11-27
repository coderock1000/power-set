def find_substrings(string):
    substrings = []
    length = len(string)
    
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(string[i:j])
    
    return substrings

input_string = input("Enter a string: ")

all_substrings = find_substrings(input_string)

print("All substrings of the string are:")
print(all_substrings)
