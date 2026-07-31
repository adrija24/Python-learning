# Getter
class MyClass:
    def __init__(self, value):
        self._value = value
        
    @property
    def value(self):
        return self._value
    # setter
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
obj = MyClass(10)
print(obj.value)  # Accessing the value using the getter
obj.value = 20  # Setting the value using the setter
print(obj.value)  # Accessing the updated value using the getter
