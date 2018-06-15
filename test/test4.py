class a(list):
    def add_field(self,field):
        self.append(field)
b = a()
b.add_field(123)
print(b)
