#!/usr/bin/python3

import statistics, scipy.stats, collections
import matplotlib.pyplot as plt

# Классы для Задания 1
class SimpleStatics:
    @staticmethod

    def mean(lst):
        print(f"Среднее арифметическое: {sum(lst)/len(lst)}")

    def median(lst):
        print(f"Медиана: {statistics.median(lst)}")

    def mode(lst):
        print(f"Мод: {statistics.mode(lst)}")

    def Range(lst):
        print(f"Выборочная дисперсия: {statistics.variance(lst)}")

    def standart_deviation(lst):
        print(f"Выборочное стандартное отклонение: {statistics.stdev(lst)}")

# Классы для Задния 2
class FrequencyDisribution:
    @staticmethod

    def calculate_frequencies(lst):
        print("Сколько раз элементы встречаются в списке:\n№\tВстречается")
        for _ in list(set(lst)): print(f"{_}:\t{lst.count(_)}")

    def display_frequency_table(lst):
        print(f"Список: {', '.join(str(_) for _ in lst)}")

    def get_most_frequent(lst):
        print(f"Чаще всего встречающийся элемент: {collections.Counter(lst).most_common(1)[0][0]}")

# Классы для Задания 3
class Correlation:
    @staticmethod

    def pearson_correlation(X, Y):
        corr, pval = scipy.stats.pearsonr(X, Y)
        print(f"Коэффициент корреляции Пирсона: {corr}\tЗначение p: {pval}")

    def spearman_correlation(X, Y):
        corr, pval = scipy.stats.spearmanr(X, Y)
        print(f"Коэффициент корреляции Спирмена: {corr}\tЗначение p: {pval}")

    def covariance(X, Y):
        corr, pval = scipy.stats.pearsonr(X, Y)
        print(f"Корреляция между списками: {pval}")

    def plot_scatter(X, Y):
        corr, pval = scipy.stats.pearsonr(X, Y)
        plt.scatter(X, Y, label = "Данные")
        plt.title(f"Диаграмма рассеяния\nКорреляция Пирсона = {corr:.2f}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.legend()
        plt.show()

def main():
    print("ЗАДАНИЕ 1:")
    a = (3, 5, 6, 7, 8, 5)
    print(f"Список: {a}")
    SimpleStatics.mean(a)
    SimpleStatics.median(a)
    SimpleStatics.mode(a)
    SimpleStatics.Range(a)
    SimpleStatics.standart_deviation(a)

    print("\nЗАДАНИЕ 2:")
    FrequencyDisribution.calculate_frequencies(a)
    FrequencyDisribution.display_frequency_table(a)
    FrequencyDisribution.get_most_frequent(a)

    print("\nЗАДАНИЕ 3:")
    b = (9, 4, 7, 2, 1, 8)
    Correlation.pearson_correlation(a, b)
    Correlation.spearman_correlation(a, b)
    Correlation.covariance(a, b)
    Correlation.plot_scatter(a, b)

if __name__ == "__main__": main()
