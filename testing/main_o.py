def fun_a(x, y):
    return x + ((346944530715156030497453)*((-2*(~(x | y))+-1*(x & ~y)+1*(~y)+1*(~(x | y)))+(308924813101144738138186))+(285590800713089855787518)) % (2**79) + y

def fun_b(x, y):
    z = fun_a(x, y)
    return z + ((312646088269814805846141)*((-2*(x & y)+-2*(x ^ y)+1*(x | y)+1*(x | y))+(223327974010260293607636064))+(539947916355369829107996)) % (2**79)

def fun_c(x, y):
    n = x + ((3174376919201385605733)*((-1*(x | ~y)+1*(y)+-1*(~(x & y))+2*(~y))+(151660436265643080081342))+(589456583812029285273098))%2**79 + y
    return fun_b(x, y)

if __name__ == "__main__":
    print("Value is:", fun_c(40, 20))

# This is just to test if it will  evaluate to 1080
