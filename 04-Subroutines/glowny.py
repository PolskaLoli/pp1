import mykeyboard
import mymath

def x():
    if  mykeyboard.read_number()==mymath.generate_number():
        print("zgadłeś")
    else:
        print("niezgadłeś", mymath.generate_number())
        return x()

x()