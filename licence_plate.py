# Type in your ideas for possible licence plates and check whether they are allowed or not

# must start with > 2 letters
# maximum of 6 char, min of 2 char
# numbers must come at the end, first number != 0
# no . " " or !

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    x = 0
    while x < len(s):
        if s[x].isalpha() == False:
            if s[x] == "0":
                return False
            else:
                break
        x += 1

    for x in range(len(s)):
        if s[x].isdigit():
            if x < len(s) - 1 and s[x + 1].isalpha():
                return False
    for char in s:
        if char in [".", " ", "!", "?"]:
            return False

    return True
main()
