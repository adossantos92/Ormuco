from collections import OrderedDict


class LRUCache(object):
    def __init__(self, max_size=2024):
        self.max_size = max_size
        self.__cache = dict()
        self.__times = OrderedDict()
        self.iter = 0

    def __setitem__(self, key, value):
        self.__cache[key] = value
        self.__times[key] = self.iter
        self.iter += 1
        self.clean()

    def __getitem__(self, key):
        self.__times[key] = self.iter
        self.iter += 1
        return self.__cache[key]

    def __delete__(self, key):
        self.__cache.pop(key)
        self.__times.pop(key)

    def __contains__(self, key):
        return key in self.__cache

    def __len__(self):
        return len(self.__cache)

    def clear(self):
        self.__cache.clear()
        self.__times.clear()

    def clean(self):
        while len(self.__cache) > self.max_size:
            for key in self.__times:
                self.__delete__(key)
                break


