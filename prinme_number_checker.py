
def prime_checker(num):
    is_prime=True
    for i in range(2,num):
        if num % i == 0:
            is_prime=False
    if is_prime:
            print(f"your num is {num} and its a prime number")
    else:
            print(f"your num is {num}  and its not a prime number")

num_take=int(input("enter a num"))
prime_checker(num=num_take)
