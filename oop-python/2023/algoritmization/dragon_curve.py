import matplotlib.pyplot as plt

def generate_dragon_curve(ax, rules, iterations):
    for i in range(iterations):
        new_ax = ""
        for char in ax:
            new_ax += rules.get(char, char)
        ax = new_ax
    return ax

def dragon_curve_cords(sequence, length):
    direction = 0
    x, y = 0, 0
    points = [(x, y)]
    for letter in sequence:
        if letter == 'F':
            if direction == 0:
                x += length
            elif direction == 90:
                y += length
            elif direction == 180:
                x -= length
            elif direction == 270:
                y -= length
            points.append((x, y))
        elif letter == '+':
            direction = (direction + 90) % 360
        elif letter == '-':
            direction = (direction - 90) % 360
    return points

def main():
    ax = 'FX'
    rules = {'X': 'X+YF+', 'Y': '-FX-Y'}
    iterations = int(input("Enter the number of iterations: "))

    if iterations < 0:
        raise ValueError

    length = 2.5

    sequence = generate_dragon_curve(ax, rules, iterations)
    points = dragon_curve_cords(sequence, length)

    x_coords, y_coords = zip(*points)
    plt.figure(figsize=(10, 10))
    plt.plot(x_coords, y_coords, color="black")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
