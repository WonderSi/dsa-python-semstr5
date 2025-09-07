from time import time
import matplotlib.pyplot as plt

# Главное отличие проверок в том, что в множестве она работает через хэш, а в листе проверка идет последовательно. Именно поэтому список проверяется дольше, чем множество

# O(n) - создание множества
# O(1) - вычисление: поиск середины
# O(1000) - константа
# O(1) - поиск в множестве
# отбросив все константы мы получаем асимптотическую сложность: O(n)

def test_in_set(n):
    s = set(range(n))
    target = n // 2 
    for _ in range(1000): # работает слишком быстро, поэтому зададим выполнение поиска 1000 раз
        target in s
    return

# O(n) - создание списка
# O(1) - вычисление
# O(1000) - константа
# O(n) - поиск в списке

def test_in_list(n):
    lst = list(range(n))
    target = n // 2
    for _ in range(1000): 
        target in lst
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
        time_one = measure_algorithm_time(test_in_set, size)
        time_two = measure_algorithm_time(test_in_list, size)

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
