count = 0
current_position = 50

with open('day1/input.txt', 'r') as f:
    for line in f:
        # ex. L10
        direction = 1 if line[0] == 'R' else -1
        magnitude = int(line[1:])
        movement = direction * magnitude

        raw = current_position + movement

        if raw <= 0:
            increment = abs((raw - 1) // 100)
            if current_position == 0:
                increment -= 1
            count += increment
        elif raw >= 100:
            increment = raw // 100
            count += increment

        current_position = (current_position + movement) % 100


print(f'The password is {count}')
