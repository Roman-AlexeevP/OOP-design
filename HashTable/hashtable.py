class ATSHashTable:

    PUT_OK: int = 0 # успешно добавлен новый элемент
    PUT_ERR: int = 1 # хеш-таблица переполнена

    DELETE_OK: int = 0 # успешно удален элемент
    DELETE_ERR: int = 1 # хеш-таблица пустая
    DELETE_NOT_FOUND: int = 2 # такого элемента в таблице нет

    FIND_OK: int = 0 # элемент есть в таблице
    FIND_EMPTY: int = 1 # таблица пуста
    FIND_NOT_FOUND: int = 2 # элемента нет в таблица

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

    # предусловие: таблица не пустая
    def find(self, value):
        raise NotImplementedError

    # запросы
    def size(self):
        raise NotImplementedError
    # запросы статусов

    # успешно/таблица пуста/не найден
    def get_find_status(self):
        raise NotImplementedError
    # успешно/ таблица пуста/ нет такого элемента
    def get_delete_status(self):
        raise NotImplementedError

    # успешно/таблица заполнена
    def get_put_status(self):
        raise NotImplementedError

class HashTable:
    PUT_OK: int = 0  # успешно добавлен новый элемент
    PUT_ERR: int = 1  # хеш-таблица переполнена

    DELETE_OK: int = 0  # успешно удален элемент
    DELETE_ERR: int = 1  # хеш-таблица пустая
    DELETE_NOT_FOUND: int = 2  # такого элемента в таблице нет

    FIND_OK: int = 0  # элемент есть в таблице
    FIND_EMPTY: int = 1  # таблица пуста
    FIND_NOT_FOUND: int = 2  # элемента нет в таблица

    def __init__(self, size):
        self.capacity = size
        self.size = 0
        self.values = [] * size
        self.find_status = None
        self.delete_status = None
        self.put_status = None


    def hash_value(self, value):
        return sum(bytearray(value, "utf-8")) % self.size

    def size(self):
        return self.size

    def get_find_status(self):
        return self.find_status

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
        if self.find_status == self.FIND_OK:
            self.values[index] = None
            self.delete_status = self.DELETE_OK
        else:
            self.delete_status = self.DELETE_NOT_FOUND

    def find(self, value):
        if self.size() < 1:
            self.find_status = self.FIND_EMPTY
            return None
        index = self.hash_value(value)
        if self.values[index] == value:
            self.find_status = self.FIND_OK
            return index
        step = 1
        new_index = (index + step) % self.capacity
        while new_index != index:
            if self.values[new_index] == value:
                self.find_status = self.FIND_OK
                return new_index
            step = step * 2
            new_index = (new_index + step) % self.capacity
        else:
            self.find_status = self.FIND_NOT_FOUND


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
