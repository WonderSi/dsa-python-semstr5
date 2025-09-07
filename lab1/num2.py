from time import time
import numpy as np
import matplotlib.pyplot as plt

array_number = np.random.randint(0, 99, 20)

# ф-ции поразумевают, что list не будет <= 1
def func_one(list):
    min_element = max_element = list[0]

    for num in list:
        if num < min_element:
            min_element = num
        elif num > max_element:
            max_element = num

    return min_element, max_element


def func_two(list): 
    list_copy = list.copy()
    for i in range(len(list_copy), 0, -1):
        for j in range(1, i):
            if list_copy[j-1] > list_copy[j]:
                list_copy[j-1], list_copy[j] = list_copy[j], list_copy[j-1]
    return list_copy[0], list_copy[len(list_copy)-1]

def measure_algorithm_time(func, n):
    array = np.random.randint(0,100,n)

    tic = time()
    func(array) 
    toc = time()

    return toc - tic

def create_performance_chart():
    input_sizes = list(range(100, 10000, 500))
    times_func_one = []
    times_func_two = []
    
    print("Измеряем время выполнения для разных размеров")
    
    for size in input_sizes:
        time_one = measure_algorithm_time(func_one, size)
        time_two = measure_algorithm_time(func_two, size)

        times_func_one.append(time_one)
        times_func_two.append(time_two)

        print(f"Размер: {size}, func_one: {time_one:.6f}s, func_two: {time_two:.6f}s")
    
    plt.figure(figsize=(12, 8))

    plt.plot(input_sizes, times_func_one, marker='o', linewidth=2, markersize=8, color='blue')
    plt.plot(input_sizes, times_func_two, marker='s', linewidth=2, markersize=8, color='red')
    
    plt.title('Сравнение времени выполнения алгоритма', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Размер входных данных (количество элементов)', fontsize=14)
    plt.ylabel('Время выполнения (секунды)', fontsize=14)
    
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    create_performance_chart()

# первая ф-ция имеет асимптотическую сложность O(n), т.к. функция линейна и проходится лишь один раз по массиву.
# Вторая ф-ция имеет асимптотическую сложность O(n^2), Т.к. в методе сортировку пузырки мы используем массив данных дважды
