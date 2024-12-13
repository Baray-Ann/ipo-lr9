from .isCorrectRect import isCorrectRect
from .isCollisionRect import isCollisionRect

def intersectionAreaRect(rect1, rect2):

    if isCorrectRect(rect1) == False or isCorrectRect(rect2) == False: 
        raise ValueError("Некорректный прямоугольник.")
    
    area = 0 
    
    if isCollisionRect(rect1, rect2): 
        lesser_x = max(rect1[0][0], rect2[0][0]) 
        lesser_y = max(rect1[0][1], rect2[0][1]) 
        larger_x = min(rect1[1][0], rect2[1][0]) 
        larger_y = min(rect1[1][1], rect2[1][1]) 
        
        area = (larger_x - lesser_x) * (larger_y - lesser_y) 
        
    return area