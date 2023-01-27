class Dessert:
    def __init__(self,name = '',calories = 0):
        self.name = str(name)
        self.calories = int(calories)
    def get_name(self):
        return self.name
    def set_name(self,a):
        self.name = str(a)
    def get_calories(self):
        return self.calories
    def set_calories(self,a):
        self.calories = int(a)
    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False
    def is_delicious(self):
        return True
