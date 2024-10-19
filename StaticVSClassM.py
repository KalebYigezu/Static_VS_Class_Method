
class MyClass:
    class_variable = 10

    @staticmethod
    def static_method(x, y):
        return x + y

    @classmethod
    def class_method(cls, x):
        return cls.class_variable * x

result1 = MyClass.static_method(2, 3)

result2 = MyClass.class_method(2)

print(result1, result2)


