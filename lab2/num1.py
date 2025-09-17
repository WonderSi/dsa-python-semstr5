import matplotlib.pyplot as plt

def num_one():
    x = range(0, 50)
    y = [i * 3 for i in x]

    plt.plot(x, y, color='blue')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Draw a line.')
    plt.show()


if __name__ == '__main__':
    pass

    # num_one()
