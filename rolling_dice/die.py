from random import randint

class Die:
    # tek bir zarı temsil eden bir sınıf
    
    def __init__(self, num_sides=6):
        # altı yüzlü bir zar olduğunu hayal edin
        self.num_sides = num_sides
        
        
    def roll(self):
        # 1 ile zar yüzü arasında bir sayı döndür
        return randint(1, self.num_sides)