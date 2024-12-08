def first_odd_flavor():
    N = int(input("Enter the number of candies (N): "))
    candies = [input("Enter the name:").strip() for _ in range(N)]
    flavor_count = {}
    for candy in candies:
        flavor_count[candy] = flavor_count.get(candy, 0) + 1
    for candy in candies:
        if flavor_count[candy] % 2 != 0:
            return candy
    return "All are even"
print(first_odd_flavor())
