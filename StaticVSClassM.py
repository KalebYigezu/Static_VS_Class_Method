

class MyClass:
    class_variable = 10

    @staticmethod
    def static_method():
        return MyClass.class_variable

    @classmethod
    def class_method(cls):
        cls.class_variable = 100
        return cls.class_variable


class_result = MyClass.class_method()

static_result = MyClass.static_method()


print("class_result  = ", class_result)
print("static_result = ", static_result)


