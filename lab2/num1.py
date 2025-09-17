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

def num_three():

    x1 = [10, 20, 30]
    y1 = [20, 40, 10]

    x2 = [10, 20, 30]
    y2 = [40, 10, 30]

    plt.plot(x1, y1, color='blue', linewidth=1, linestyle='dotted', label='line1-dotted')
    plt.plot(x2, y2, color='red', linewidth=5, linestyle=':', label='line2-dashed')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Plot with two or more lines with different styles')
    plt.legend()

    plt.xlim(10, 30)
    plt.ylim(10, 40)

    plt.xticks([10, 15, 20, 25, 30])

    plt.show()

def num_four():

    x = [1, 4, 5, 6, 7]
    y = [2, 6, 3, 6, 3]

    plt.plot(x, y, linestyle='dashdot', color='red', marker='o', markerfacecolor='blue', markersize=10) # пытался найти нормальный linestyle, но не нашел подходящий как в примере
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Display marker')

    plt.xlim(1, 8)
    plt.ylim(1, 8)

    plt.show()

def num_five():

    x1 = [3, 4, 6, 7, 9]
    y1 = [2, 6, 11, 20, 22]

    x2 = [2, 3, 5, 6, 8]
    y2 = [1, 5, 10, 17, 20]

    plt.scatter(x1, y1, color='red', s=50)
    plt.scatter(x2, y2, color='blue', marker='*', s=40)

    plt.xlim(0, 10)
    plt.ylim(0, 30)
    plt.show()

if __name__ == '__main__':
    pass

    # num_one()
    # num_two()
    # num_three()
    # num_four()
    num_five()
