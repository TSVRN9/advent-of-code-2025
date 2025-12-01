count = 0
current_position = 50

with open('day1/input.txt', 'r') as f:
    for line in f:
        # ex. L10
        direction = 1 if line[0] == 'R' else -1
        magnitude = int(line[1:])
        movement = direction * magnitude

        current_position = (current_position + movement) % 100

        if current_position == 0:
            count += 1

print(f'The password is {count}')
