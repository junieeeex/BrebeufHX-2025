class Tag:
    def __init__(self, name):
        self.name = name
        self.count = 0


    def __str__(self):
        return f"{self.name}: {self.count}"
    
    def add_count(self):
        self.count += 1

    def remove_count(self):
        self.count -= 1

    def get_count(self):
        return self.count
    

    


    