import matplotlib.pyplot as plt


def num_one():
    x = range(0, 50)
    y = [i * 3 for i in x]

    plt.plot(x, y, color='blue')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Draw a line.')

    plt.show()


def num_two():
    x1 = [10, 20, 30]
    y1 = [20, 40, 10]

    x2 = [10, 20, 30]
    y2 = [40, 10, 30]

    plt.plot(x1, y1, color='blue', linewidth=3, label='line1-width-3')
    plt.plot(x2, y2, color='red', linewidth=5, label='line2-width-5')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title(
        'Two or more lines with different widths and colors with suitable legends')
    plt.legend()

    plt.xlim(10, 30)
    plt.ylim(10, 40)

    plt.xticks([10, 15, 20, 25, 30]) # кастыль, но зато как в примере
    
    plt.show()


if __name__ == '__main__':
    pass

    # num_one()
    num_two()
