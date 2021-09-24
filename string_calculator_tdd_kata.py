from typing import List

def string_sum(string: str) -> int:
    delimiter: str = ","
    
    if not string: return 0
    
    if string.startswith("//"):
        try: 
            delimiter = string.split("//")[1][0]
        except: Ellipsis

    check_negative: str = ",".join([str(number).strip() for number in string.replace("\n", delimiter).replace(",", delimiter).split(delimiter) if str(number).strip().startswith("-")])

    if check_negative: return f"Negatives not allowed. These are the negative number: {check_negative}"
    
    only_numbers: List = [int(number) for number in string.replace("\n", delimiter).replace("\\n", delimiter).replace(",", delimiter).split(delimiter) if str(number).strip().isnumeric()]
    
    return sum(only_numbers)

number = input("Enter Any Number String:")
print(string_sum(number))
