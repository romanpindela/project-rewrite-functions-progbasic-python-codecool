import random 

def min(a, b):
    if a < b:
        c = a
    else: c = b
    return c


def max(value_list):
    c = value_list[0]
    for i in range(len(value_list)):
        if c <= value_list[i]:
            c = value_list[i]
    return (c)

def len(value_list):
    length = 0;
    c = 0;
    try:
        while True:
            c = value_list[length]
            length += 1

    except:
        return (length)

def multiply(a, b):
    c = a
    for i in range(1,b):
        c += a
    return c

def pow(a, b):
    c = a
    for i in range(1,b):
        c *= a
    return c

def divmod(a, b):
    reszta = a
    ile_razy = 0
    while reszta >= b:
        reszta -= b
        ile_razy += 1
    return(ile_razy, reszta)



def main():

    print("min (3,9) = ", min (3,9))
    print("max([3,1,9,91209,2324,-192,0]) = ", max([3,1,9,91209,2324,-192,0]))
    print("len([2,3,4,5,8,9]) = ", len([2,3,4,5,8,9]))   
    print("multiply(2,3) = ", multiply(2,3))
    print("pow(2,3) = ", pow(2,3))
    print("divmod(17,3) = ", divmod(17,3))


if __name__ == "__main__":
    main()
    
    
