import math

def probability_of_purchase(x, y):
    return 1 - math.exp(-y / x)

# Пример: среднее количество дней между покупками x = 10, спустя y = 5 дней
x = 4
y = 28
print(probability_of_purchase(x, y))