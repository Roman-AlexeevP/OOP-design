class ATSHashTable:

    PUT_OK: int = 0 # успешно добавлен новый элемент
    PUT_ERR: int = 1 # хеш-таблица переполнена

    DELETE_OK: int = 0 # успешно удален элемент
    DELETE_NOT_FOUND: int = 1 # такого элемента в таблице нет

    # конструктор
    # постусловие: создана пустая хэщ-таблица размера size
    def __init__(self, size):
        raise NotImplementedError


    # команды
    # предусловие: таблица не заполнена полностью
    # постусловие: в таблицу добавлен элемент value
    def put(self, value):
        raise NotImplementedError

    # предусловие: таблица не пустая
    # постусловие: из таблицы удален элемент value
    def delete(self, value):
        raise NotImplementedError

    # запросы
    def get(self, value) -> bool:
        raise NotImplementedError

    def size(self):
        raise NotImplementedError
    # запросы статусов

    # успешно/ нет такого элемента
    def get_delete_status(self):
        raise NotImplementedError

    # успешно/таблица заполнена
    def get_put_status(self):
        raise NotImplementedError

class ATSPowerSet(ATSHashTable):

    # предусловие: в множестве нет такого же элемента
    # постусловие: если элемента нет во множестве, то он в него записан
    def put(self, value):
        raise NotImplementedError

    # запросы:
    def intersection(self, set2) -> ATSPowerSet:
        raise NotImplementedError

    def union(self, set2) -> ATSPowerSet:
        raise NotImplementedError

    def difference(self, set2) -> ATSPowerSet:
        raise NotImplementedError

    def issubset(self, set2) -> bool:
        raise NotImplementedError


class HashTable:
    PUT_OK: int = 0  # успешно добавлен новый элемент
    PUT_ERR: int = 1  # хеш-таблица переполнена

    DELETE_OK: int = 0  # успешно удален элемент
    DELETE_NOT_FOUND: int = 1  # такого элемента в таблице нет

    def __init__(self, size):
        self.capacity = size
        self.size = 0
        self.values = [] * size
        self.delete_status = None
        self.put_status = None


    def hash_value(self, value):
        return sum(bytearray(value, "utf-8")) % self.size

    def size(self):
        return self.size

    def get_delete_status(self):
        return self.delete_status

    def get_put_status(self):
        return self.put_status

    def put(self, value):
        if self.size == self.capacity:
            self.put_status = self.PUT_ERR
            return None
        index = self.find_slot(value)
        if index is None:
            self.put_status = self.PUT_ERR
        else:
            self.values[index] = value
            self.size += 1
            self.put_status = self.PUT_OK

    def delete(self, value):
        if self.size() < 1:
            self.delete_status = self.DELETE_ERR
            return None
        index = self.find(value)
        if index is not None:
            self.values[index] = None
            self.delete_status = self.DELETE_OK
        else:
            self.delete_status = self.DELETE_NOT_FOUND

    def get(self, value):
        return self.find(value) is not None


    def find(self, value):
        if self.size() < 1:
            return None
        index = self.hash_value(value)
        if self.values[index] == value:
            return index
        step = 1
        new_index = (index + step) % self.capacity
        while new_index != index:
            if self.values[new_index] == value:
                return new_index
            step = step * 2
            new_index = (new_index + step) % self.capacity
        else:
            return None

    def find_slot(self, value):
        index = self.hash_value(value)
        if self.slots[index] is None:
            return index
        step = 1
        new_index = (index + step) % self.capacity
        while new_index != index:
            if self.values[new_index] is None:
                return new_index
            step = step * 2
            new_index = (new_index + step) % self.capacity

        return None


class PowerSet(HashTable):

    def put(self, value):
        if self.get(value):
            self.put_status = self.PUT_ERR
        else:
            super().put(value)

    def issubset(self, set2):
        result = True
        for value in set2.items:
            if not self.get(value):
                result = False
                break
        return result

    def intersection(self, set2):
        result = PowerSet()
        if set2 is None:
            return result
        for value in self.items:
            if set2.get(value):
                result.put(value)
        return result

    def union(self, set2):
        result = PowerSet()
        for value in self.items:
            result.put(value)
        for value in set2.items:
            result.put(value)
        return result

    def difference(self, set2):
        result = PowerSet()
        if set2 is None:
            return result
        for value in self.items:
            if not set2.get(value):
                result.put(value)
        return result
