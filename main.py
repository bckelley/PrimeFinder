# Check if given number is prime

n = input("Enter a number: ")
num = int(n)

if num > 1:
    for i in range(2, int(num/2) + 1):
        if ( num % i ) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")