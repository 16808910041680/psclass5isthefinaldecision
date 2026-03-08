
num1 = int(input("Enter your first number for ABSOLUTELY no reason: "))
num2 = int(input("Enter your second number for ABSOLUTELY no reason: "))
def palindrome(num1, num2):
    org_num1 = num1
    org_num2 = num2
    rev_num1 = 0
    rev_num2 = 0
    num1digit = 0
    num2digit = 0
    if len(str(num1)) < 2:
        num1digit = 1
    elif len(str(num2)) < 2:
        num2digit = 1
    else:
        return
    while num1 > 0:
        rev_num1 = (rev_num1 * 10) + (num1 % 10)
        num1 = num1 // 10
    while num2 > 0:
        rev_num2 = (rev_num2 * 10) + (num2 % 10)
        num2 = num2 // 10
    if org_num1 == rev_num1 and num1digit == 1:
        print(f"{org_num1} is a palindrome, but it's a 1 digit number so OF COURSE IT'S A PALINDROME")

    if org_num2 == rev_num2 and num2digit == 1:
        print(f"{org_num2} is a palindrome, but it's a 1 digit number so OF COURSE IT'S A PALINDROME")

    if org_num1 == rev_num1 and num1digit != 1:
        print(f"{org_num1} is a palindrome")

    if org_num2 == rev_num2 and num2digit != 1:
        print(f"{org_num2} is a palindrome")

palindrome(num1, num2)
is1prime = 0
is2prime = 0
def primecheck (num1, num2):
    global is1prime
    global is2prime
    if num1 > 1: 
        for i in range(2, num1): 
            if (num1 % i) == 0: 
                is1prime = 0
                break
        else: 
            is1prime = 1
    if num2 > 1:
        for i in range(2, num2): 
            if (num2 % i) == 0: 
                is2prime = 0
                break
        else: 
            is2prime = 1
primecheck(num1, num2)
def hcf(num1, num2, is1prime, is2prime):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            hcf = i
    if hcf == 1:
        if is1prime == 1 and is2prime == 1:
            print(f"{num1} and {num2} are both prime numbers, dude, did you expect an HCF to exist?")
        elif is1prime == 1 and is2prime == 0:
            print(f"{num1} is a prime number, but {num2} is not, so the HCF is 1")
        elif is1prime == 0 and is2prime == 1:
            print(f"{num2} is a prime number, but {num1} is not, so the HCF is 1")
        elif is1prime == 0 and is2prime == 0:
            print(f"Neither {num1} nor {num2} are prime numbers, which is a quite rare scenario, but possible. The HCF is still 1.")
    else: 
        print(f"The HCF of {num1} and {num2} is {hcf}")
    
hcf(num1, num2, is1prime, is2prime)

def lcm (num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break
        greater += 1
    if lcm == num1 * num2:
        if is1prime == 1 and is2prime == 1:
            print(f"{num1} and {num2} are both prime numbers, dude, did you expect an LCM to be anything OTHER THAN {num1} multiplied by {num2}? It's {lcm}.")
        if is1prime == 1 and is2prime == 0:
            print(f"{num1} is a prime number, but {num2} is not, so the LCM is {num1} multiplied by {num2}, or {lcm}")
        if is1prime == 0 and is2prime == 1:
            print(f"{num2} is a prime number, but {num1} is not, so the LCM is {num1} multiplied by {num2}, or {lcm}")
        if is1prime == 0 and is2prime == 0:
            print(f"Neither {num1} nor {num2} are prime numbers, which is a quite rare scenario, but possible. The LCM is {num1} multiplied by {num2}, or {lcm}")
    else:
        print(f"The LCM of {num1} and {num2} is {lcm}.")

lcm (num1, num2)