
class Singleton(object):

    def __init__(self, cls):
        print('cls --------> %s' % cls.__name__)
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls2(object):
    def __init__(self):
        pass


a = Cls2()
b = Cls2()
print(id(a) == id(b))
