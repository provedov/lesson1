class Dessert:
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories
    def get_name(self):
        return self.name
    def set_name(self,a):
        self.name = a
    def get_calories(self):
        return self.calories
    def set_calories(self,a):
        self.calories = a
    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False
    def is_delicious(self):
        return True
