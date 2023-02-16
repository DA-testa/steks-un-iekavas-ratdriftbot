# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
        if next in ")]}":
            if not opening_brackets_stack: 
                return i+1
            if not are_matching(opening_brackets_stack[-1].char,next): 
                return i+1
    if opening_brackets_stack: 
        return opening_brackets_stack[-1].position
    else: return "Success"


def main():
    artemix = input ("F or I")
    if "F" in artemix: 
        map =  input ("type file name")
        with open (map,"r", encoding= "latin1") as file:
            text = file.read ()
        y = find_mismatch(text)
        if y == "Success":
            print ("Success")
        else: 
            print (y)
    elif "I" in artemix:
        text = input()
        y = find_mismatch(text)
        if y == "Success":
            print ("Success")
        else: 
            print (y)
    else: print("Input error")



if __name__ == "__main__":
    main()
