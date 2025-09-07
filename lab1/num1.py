from time import time
import numpy as np
import matplotlib.pyplot as plt


def foo(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]

# print(foo(a))

# 1. Данный код сортирует массив чисел методом пузырька (bubble sort)
# 2. O(n²) — квадратичная сложность : время выполнения алгоритма зависит от квадрата размера входных данных
# 3. Для построения графика воспользуемся библиотеками: time, numpy, matplotlib. Для отображения графика -> запустите файл


def measure_algorithm_time(n):
    array = np.random.randint(0,100,n)

    tic = time()
    foo(array) # ф-ция из задания
    toc = time()

    return toc - tic

def create_performance_chart():
    input_sizes = list(range(100, 2100, 200))
    times = []
    
    print("Измеряем время выполнения для разных размеров")
    
    for size in input_sizes:
        execution_time = measure_algorithm_time(size)
        times.append(execution_time)
        print(f"Размер: {size}, Время: {execution_time:.6f}s")
    
    plt.figure(figsize=(12, 8))
    plt.plot(input_sizes, times, marker='o', linewidth=2, markersize=8, color='blue')
    
    plt.title('Зависимость времени выполнения алгоритма от размера входных данных', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Размер входных данных (количество элементов)', fontsize=14)
    plt.ylabel('Время выполнения (секунды)', fontsize=14)
    
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    create_performance_chart()

