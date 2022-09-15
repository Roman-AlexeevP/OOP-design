import ctypes


class ATSDynArray:
    MIN_CAPACITY: int # минимальный размер буффера
    RESIZE_PERCENT: float # процент заполненности для уменьшения

    INSERT_OK: int # успешно
    INSERT_ERR: int # не найден заданны  индекс

    DELETE_OK: int # успешно
    DELETE_ERR: int # не найден заданный индекс

    # конструктор
    def __init__(self):
        raise NotImplementedError

    # команды:
    # постусловие: в конце массива добавлен элемент, если больше буфера - увеличен буфер
    def append(self, value):
        raise NotImplementedError

    # постусловие: в указанной позиции добавлен элемент и остальные элементы сдвинуты относительно него вправо,
    # если есть соседние элементы,
    # если превышен буфер - увеличен буфер
    def insert(self, index, value):
        raise NotImplementedError

    # постусловие: по указанной позиции удален элемент, элементы сдвинуты влево если есть соседние элементы
    # если буфер меньше определенного предела то уменьшается
    def delete(self, index):
        raise NotImplementedError

    # постусловие: массив скопирован в массив с новым буфером,
    # если новое кол-во больше буфера или меньше заданного процента
    def resize(self, new_count):
        raise NotImplementedError

    # запросы:
    def __getitem__(self, item):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def get_new_array(self, capacity):
        raise NotImplementedError

    def get_increased_capacity(self):
        raise NotImplementedError

    def get_decreased_capacity(self):
        raise NotImplementedError


    # получение статусов:

    # успешно / не найден индекс
    def get_insert_status(self):
        raise NotImplementedError

     # успешно / не найден индекс
    def get_delete_status(self):
        raise NotImplementedError


class DynArray:
    MIN_CAPACITY: int  = 16
    RESIZE_PERCENT: float  = 0.5



    INSERT_OK: int  = 0
    INSERT_ERR: int = 1

    DELETE_OK: int  = 0
    DELETE_ERR: int = 1

    def __init__(self):
        self.count = 0
        self.capacity = self.MIN_CAPACITY
        self.array = self.get_new_array(self.MIN_CAPACITY)
        self.insert_status = None
        self.delete_status = None

    def get_new_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.count

    def __getitem__(self, item):
        if item < 0 or item >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[item]

    def resize(self, new_count):
        new_capacity = 0
        if new_count > self.capacity:
            new_capacity = self.get_increased_capacity()
        if new_count < self.capacity * self.RESIZE_PERCENT:
            new_capacity = self.get_decreased_capacity()
        if new_capacity != 0:
            new_array = self.make_array(new_capacity)
            for i in range(self.count):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity
            self.count = new_count

    def append(self, value):
        new_count = self.count + 1
        self.resize(new_count)
        self.array[self.count] = value


    def insert(self, index, value):
        if index > self.count or index < self.count:
            self.insert_status = self.INSERT_ERR
            return None

        new_count = self.count + 1
        self.resize(new_count)
        if index == self.count:
            return self.append(value)
        self.append(0)
        for j in range(self.count, index, -1):
            self.array[j] = self.array[j - 1]
        self.array[index] = value
        self.insert_status = self.INSERT_OK

    def delete(self, index):
        if index > self.count or index < self.count:
            self.delete_status = self.DELETE_ERR
            return None
        new_count = self.count - 1
        self.resize(new_count)
        for j in range(index, self.count):
            self.array[j] = self.array[j+1]
    def get_insert_status(self):
        return self.insert_status

    def get_delete_status(self):
        return self.delete_status

    def get_increased_capacity(self):
        return (self.capacity * 3) / 2 + 1

    def get_decreased_capacity(self):
        new_capacity = int(self.capacity / 2)
        return new_capacity if new_capacity > self.MIN_CAPACITY else self.MIN_CAPACITY
