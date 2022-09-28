class AbstractDictionary:
    GET_OK: int = 0  # успешно найдено значение по ключу
    GET_ERR: int = 1  # ошибка - данный ключ не найден
    PUT_OK: int = 0  # успешно добавлена пара ключ значение
    PUT_ERR: int = 1  # ошибка - не найден слот из-за коллизий
    DELETE_OK: int = 0  # успешно удалена пара ключ значение
    DELETE_ERR: int = 1  # ошибка - данный ключ не найден
    UPDATE_OK: int = 0  # успешно обновлено значение по ключу
    UPDATE_ERR: int = 1  # ошибка - данный ключ не найден

    # конструктор
    # постусловие: создан пустой словарь
    def __init__(self):
        raise NotImplementedError

    # команды
    # постусловие: в словарь добавлена новая пара ключ:значение
    def put(self, key, value):
        raise NotImplementedError

    # предусловие: в словаре есть ключ key
    # постусловие: в словаре удалена пара ключ:значение
    def delete(self, key):
        raise NotImplementedError

    # предусловие: в словаре есть ключ key
    # постусловие: в словаре обновлено value с ключом key
    def update(self, key, value):
        raise NotImplementedError

    # запросы
    def size(self):
        raise NotImplementedError

    def is_key(self):
        raise NotImplementedError

    # предусловие: в словаре есть ключ key
    def get(self, key):
        raise NotImplementedError

    # запросы статусов
    # успешно / ошибка коллизий
    def get_put_status(self):
        raise NotImplementedError

    # успешно / нет данного ключа
    def get_delete_status(self):
        raise NotImplementedError

    # успешно / данного ключа нет
    def get_update_status(self):
        raise NotImplementedError

    # успешно / данного ключа нет
    def get_get_status(self):
        raise NotImplementedError


class Dictionary:
    GET_OK: int = 0  # успешно найдено значение по ключу
    GET_ERR: int = 1  # ошибка - данный ключ не найден
    PUT_OK: int = 0  # успешно добавлена пара ключ значение
    PUT_ERR: int = 1  # ошибка - не найден слот из-за коллизий
    DELETE_OK: int = 0  # успешно удалена пара ключ значение
    DELETE_ERR: int = 1  # ошибка - данный ключ не найден
    UPDATE_OK: int = 0  # успешно обновлено значение по ключу
    UPDATE_ERR: int = 1  # ошибка - данный ключ не найден

    def __init__(self, size):
        self.capacity = size
        self.size = 0
        self.values = [None] * self.capacity
        self.keys = [] * self.capacity
        self.get_status = None
        self.update_status = None
        self.delete_status = None
        self.put_status = None

    def hash_value(self, value):
        return sum(bytearray(value, "utf-8")) % self.size

    def size(self):
        return self.size

    def put(self, key, value):
        if self.size == self.capacity:
            self.put_status = self.PUT_ERR
            return None
        index = self.find_slot(key)
        if index is None:
            self.put_status = self.PUT_ERR
        else:
            self.keys[index] = key
            self.values[index] = value
            self.size += 1
            self.put_status = self.PUT_OK

    def find_slot(self, value):
        index = self.hash_value(value)
        if self.keys[index] is None:
            return index
        step = 1
        new_index = (index + step) % self.capacity
        while new_index != index:
            if self.keys[new_index] is None:
                return new_index
            step = step * 2
            new_index = (new_index + step) % self.capacity

        return None

    def find_key(self, key):
        if self.size() < 1:
            return None
        index = self.hash_value(key)
        if self.keys[index] == key:
            return index
        step = 1
        new_index = (index + step) % self.capacity
        while new_index != index:
            if self.keys[new_index] == key:
                return new_index
            step = step * 2
            new_index = (new_index + step) % self.capacity
        else:
            return None

    def is_key(self, key):
        return self.find_key(key) is not None

    def get(self, key):
        index = self.find_key(key)
        if not self.is_key(key):
            self.get_status = self.GET_ERR
            return None
        self.get_status = self.GET_OK
        return self.values[index]

    def delete(self, key):
        if not self.is_key(key):
            self.delete_status = self.DELETE_ERR
            return None
        index = self.find_key(key)
        self.values[index] = None
        self.keys[index] = None
        self.delete_status = self.DELETE_OK

    def update(self, key, value):
        if not self.is_key(key):
            self.update_status = self.UPDATE_ERR
            return None
        index = self.find_key(key)
        self.values[index] = value
        self.update_status = self.UPDATE_OK

    def get_get_status(self):
        return self.get_status

    def get_update_status(self):
        return self.update_status

    def get_put_status(self):
        return self.put_status

    def get_delete_status(self):
        return self.delete_status
