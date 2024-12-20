from collision import *

print("Примеры isCorrectRect:")

print(isCorrectRect([(-3.4, 1),(9.2, 10)]))  
print(isCorrectRect([(-7, 9),(3, 6)]))      
   
print("Примеры isCollisionRect:")

print(isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)])) 
print(isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]))               
print(isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)])) #Пример вызывающий ошибку                
    
print("Примеры intersectionAreaRect:")

print(intersectionAreaRect([[(-3, 1), (9, 10)], [(-7, 0), (13, 12)]])) #Пример вызывающий ошибку
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])) #Пример вызывающий ошибку
   
print("Примеры intersectionAreaMultiRect:")

rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]

print(f"Общая площадь пересечения: {intersectionAreaMultiRect(rectangles)}")

#Пример вызывающий ошибку
incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]  
]

print(f"Общая площадь пересечения: {intersectionAreaMultiRect(incorrect_rectangles)}")
