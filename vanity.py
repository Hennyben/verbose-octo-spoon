def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    

def is_valid(s):
    T = False
    if len(s) < 2 and len(s) > 6:
        return False

    if not s.isalnum():
         return False
    
    for char in s:
        if char.isdigit() and char == "0" and T == False:
            return False
        if char.isdigit():
            T = True
        elif char.isalpha and T:
             return False

            
        
    
    if s[0].isalpha() and s[1].isalpha():
            return True
    else:
        return False

main()

