import math


def is_prime(n):
	if n == 2:
		return True
	if n < 2 or n%2 == 0:
		return False

	i=3
	while i**2 <= n:
		if n%i == 0:
			return False
		i += 2
	return True


def get_largest_prime_below(n):
	if n <= 2:
		return "(Error) n <= 2"

	n -= 1
	while not is_prime(n):
		n -= 1

	return n


def test_get_largest_prime_bellow():
    assert get_largest_prime_bellow(14) == "13"
    assert get_largest_prime_below(18) == "17"
    assert get_largest_prime_below(24) == "23"


def  get_temp(temp,s_from,s_to):
    temp = float(temp)

    if s_from not in ["C", "K", "F"]:
        print(f"(Error) wtf is {s_from}")
        return -1
    if s_to not in ["C", "K", "F"]:
        print(f"(Error) wtf is {s_to}")
        return -1

    #		F	>	C								K	>	C
    to_c = ((temp - 32) * 5 / 9) if s_from == "F" else (temp - 273.15)
    #		C	>	F								K	>	F
    to_f = ((temp * 9 / 5) + 32) if s_from == "C" else (temp - 273.15) * 9 / 5 + 32
    #		C	>	K								F	>	K
    to_k = (temp + 273.15) if s_from == "C" else (temp - 32) * 5 / 9 + 273.15

    if s_to == "C":
        return to_c
    if s_to == "F":
        return to_f
    return to_k

def test_get_temp():
    assert get_temp(26.85,C,K) == "300"
    assert get_temp(400,K,C) == "126.85"


def get_cmmmc(nums):
    lcm = 1
    for i in nums:
        lcm = lcm * i // math.gcd(lcm,i)
    return lcm


def run_get_cmmmc():
	n = int(input("n: "))

	nums = []

	for i in range(n):
		nums.append( int(input(f"nums[{i}]: ")) )

	print(f"cmmmc{nums} = {get_cmmmc(nums)}")


def menu():
	print("0. quit()")
	print("1. get_largest_prime_below(int n)")
	print("13.get_temp(int temp, string from, string to)" )
	print("14.get_cmmmc(list numbers)" )


def main():
    menu()

    choice = 1

    while choice:
        choice = int(input("choice: "))
        if choice == 1:
            n=int(input("get largest prime number below: "))
            print(get_largest_prime_below(n))
        if choice == 13:
            temp=float(input("write the tempreature you would like to convert "))
            init_unit=input()
            to_unit=input()
            print(get_temp(temp, init_unit, to_unit ))
        if choice == 14:
            print(run_get_cmmmc())


if __name__ == '__main__':
    main()
