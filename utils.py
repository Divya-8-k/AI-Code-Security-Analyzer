def calculate_total(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total += number
        elif number < 0:
            total -= number

    return total
