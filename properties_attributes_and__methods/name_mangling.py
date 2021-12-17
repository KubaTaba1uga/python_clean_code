"""
    Name mangling is changing name of an attribute
       if it is prefixed with __ (double underscore)
       for _<class_name>__<attribute_name>

    Name mangling should be used to ensure that
       subclasses don't accidentially override the
       private methods or attributes of their 
       superclass.
    
       Example:
          class Foo:
            def __init__(self):
                self.__baz = 42

            def foo(self):
                print(self.__baz)


          class Bar(Foo):
            def __init__(self):
                super(Bar, self).__init__()
                self.__baz = 21
            
            def bar(self):
                print(self.__baz)
    
"""


class NameMangling:
    def __init__(self):
        self.__name = "Mickey Mouse"


example = NameMangling()

try:
    example.__name
except AttributeError:
    print("There is no __name attribute\n")

print("Attribute  _NameMangling__name:",
      example._NameMangling__name, "\n")
