def calculate_sum(numbers):
    # TODO: Fix any potential bugs in this code
    total = 0
    for num in numbers:
        total += num
    print("The sum of the list is: " + str(total))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    calculate_sum(numbers)
