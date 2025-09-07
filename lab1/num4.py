from time import time
import numpy as np
import matplotlib.pyplot as plt

# код удаляет половину элементов, чтобы показать разность в сложности. 
# Тем самым видно, что второй способ асимптотически сложней, чем первый
#  
# O(n) - создание словаря
# O(n/2) - удаление(отбросим константу 1/2)
# O(1) - удаление элемента по ключу
# Получаем O(n) + O(n/2) * O(1) = O(n)
def del_dict(n):
    d = {i: i for i in range(n)}
    for i in range(n//2):
        del d[i]
    return

# В этой ф-ции удаление просиходит енмго иначе. Здесь при удаленнии все остальные элементы смещаются влево и поэтому
# O(n) - создание словаря
# O(n/2) - удаление(отбросим константу 1/2)
# O(n-i) - удаление по индексу
# Получаем 
# T(n) = Σ(n-i) для i от 0 до (n/2-1)
# *T(n) = n + (n-1) + (n-2) + ... + (n - n/2 + 1)*
# T(n) = Σ(n-i) = Σn - Σi - розобьем сумму

# Σn = n × (n/2) = n²/2
# Σi = (n/2) × (n/2-1) / 2 
# Σi = (n/2) × (n/2) / 2 
# Σi = n(n-2) / 8

# T(n) = n²/2 - n(n-2)/8
# T(n) = n²/2 - n²/8 + 2n/8
# T(n) = n²/2 - n²/8 + n/4
# T(n) = 3n²/8 + n/4
# При больших значениях доминирует 3n²/8
# Поэтому T(n) = O(n²)


def del_list(n):
    lst = list(range(n)) 
    for i in range(n//2):
        del lst[i]
    return

def measure_algorithm_time(func, n):
    tic = time()
    func(n) 
    toc = time()

    return toc - tic

def create_performance_chart():
    input_sizes = list(range(100, 10000, 500))
    times_func_one = []
    times_func_two = []
    
    print("Измеряем время выполнения для разных размеров")
    
    for size in input_sizes:
        time_one = measure_algorithm_time(del_dict, size)
        time_two = measure_algorithm_time(del_list, size)

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
