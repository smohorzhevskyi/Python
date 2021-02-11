"""
Соціальні мережі
В Instagram зареєстровано A учнів класу, у Faceboook - В учнів, С присутні в обох соцмережах,
а D учнів взагалі не користуються інтернетом та соціальними мережами.
Визначити скільки учнів у класі.

Формат вхідних даних
Вхідні дані складаються з одного рядка, в якому вказані чотири цілих числа - А, В, С, D.
За бажанням можете отримати значення з input("Enter numbers A,B,C,D:")

Формат результату
Виведіть одне число - кількість учнів у класі.

Приклад:
Enter numbers A,B,C,D: 1,3,1,2
Total students: 5
"""

A, B, C, D = [int(i) for i in input("Enter numbers A,B,C,D: ").split(",")]
print("Total students:", A + B - C + D)