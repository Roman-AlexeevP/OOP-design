class ATSParentList:
    REMOVE_OK: int = 0  # удаление прошло успешно
    REMOVE_ERR: int = 1  # список был пустой, удаление не отработано

    RIGHT_OK: int = 0  # курсор установлен в правый элемент
    RIGHT_ERR: int = 1  # правый элемент отсутствует/курсор остается на прежнем месте

    HEAD_OK: int = 0  # курсор установлен в первый элемент списка
    HEAD_ERR: int = 1  # список пустой

    TAIL_OK: int = 0  # курсор установлен в последний элемент списка
    TAIL_ERR: int = 1  # список пустой

    PUT_RIGHT_OK: int = 0  # добавлен элемент справа от текущего
    PUT_RIGHT_ERR: int = 1  # список пустой

    PUT_LEFT_OK: int = 0  # добавлен элемент слева от текущего
    PUT_LEFT_ERR: int = 1  # список пустой

    FIND_OK: int = 0  # найден следующий элемент с заданным значением
    FIND_FALSE: int = 1  # элемент не найден
    FIND_ERR: int = 2  # список пустой

    REPLACE_OK: int = 0  # изменено значение текущего элемента
    REPLACE_ERR: int = 1  # список пустой

    GET_OK: int = 0  # Возвращен текущий элемент
    GET_ERR: int = 1  # список пустой

    # Конструктор
    # постусловие: создан пустой связный лист
    def __init__(self):
        raise NotImplementedError

    # Команды:
    # предусловие: список не пустой
    # постусловие: курсор установлен в первый элемент списка
    def head(self):
        raise NotImplementedError

    # предусловие: список не пустой
    # постусловие: курсор установлен в последний элемент списка
    def tail(self):
        raise NotImplementedError

    # предусловие: курсор не установлен в последний элемент списка
    # постусловие: курсор установлен в правый от него элемент
    def right(self):
        raise NotImplementedError

    # предусловие: список не пустой
    # постусловие: в список добавлен новый элемент, расположенный после элемента, помеченного курсором
    def put_right(self, value):
        raise NotImplementedError

    # предусловие: список не пустой
    # постусловие: в список добавлен новый элемент, расположенный перед элементом, помеченного курсором
    def put_left(self, value):
        raise NotImplementedError

    # предусловие: список не пустой
    # постусловие: текущий узел удален, курсор смещен либо к правому соседу, если есть, либо к левому
    def remove(self):
        raise NotImplementedError

    # постусловие: список пустой, курсор установлен в head и указывает на пустое значение
    def clear(self):
        raise NotImplementedError

    # постусловие: добавлен новый элемент в конце списка
    def add_tail(self, value):
        raise NotImplementedError

    # предусловие: список не пустой
    # постусловие: текущие значение изменено на value
    def replace(self, value):
        raise NotImplementedError

    # предусловие: список не пустой
    # постусловие: курсор установлен на следующий узел с заданным значением
    def find(self, value):
        raise NotImplementedError

    # постусловие: из списка удалены все узлы с заданным значением
    def remove_all(self, value):
        raise NotImplementedError

    # Запросы:

    def size(self):
        raise NotImplementedError

    def is_head(self):
        raise NotImplementedError

    def is_tail(self):
        raise NotImplementedError

    def is_value(self):
        raise NotImplementedError

    # предусловие: список не пустой
    def get(self):
        raise NotImplementedError

    # статусы команд:

    # успешно / список пустой
    def get_remove_status(self) -> bool:
        raise NotImplementedError

    # успешно / правее нет элемента
    def get_right_status(self) -> bool:
        raise NotImplementedError

    # успешно / список пустой
    def get_head_status(self) -> bool:
        raise NotImplementedError

    # успешно / список пустой
    def get_tail_status(self) -> bool:
        raise NotImplementedError

    # успешно / список пустой
    def get_put_right_status(self) -> bool:
        raise NotImplementedError

    # успешно / список пустой
    def get_put_left_status(self) -> bool:
        raise NotImplementedError

    # успешно / список пустой / не найден
    def get_find_status(self) -> bool:
        raise NotImplementedError

    # успешно / список пустой
    def get_replace_status(self) -> bool:
        raise NotImplementedError

    # успешно / список пустой
    def get_get_status(self) -> bool:
        raise NotImplementedError


class ATSLinkedList(ATSParentList):
    pass


class ATSTwoWayList(ATSParentList):
    LEFT_OK: int = 0  # курсор указывает на левый элемент от текущего
    LEFT_ERR: int = 1  # список пустой

    # команды:
    # предусловие: список пустой
    # постусловие: курсор установлен в левый от него элемент
    def left(self):
        raise NotImplementedError

    # запросы:
    # успешно / левее нет элемента
    def get_left_status(self) -> bool:
        raise NotImplementedError


class Node:
    def __init__(self, value, next_value=None, prev_value=None):
        self.value = value
        self.next_value = next_value
        self.prev_value = prev_value


class ParentList:
    REMOVE_OK: int = 0
    REMOVE_ERR: int = 1

    RIGHT_OK: int = 0
    RIGHT_ERR: int = 1

    HEAD_OK: int = 0
    HEAD_ERR: int = 1

    TAIL_OK: int = 0
    TAIL_ERR: int = 1

    PUT_RIGHT_OK: int = 0
    PUT_RIGHT_ERR: int = 1

    PUT_LEFT_OK: int = 0
    PUT_LEFT_ERR: int = 1

    FIND_OK: int = 0
    FIND_FALSE: int = 1
    FIND_ERR: int = 2

    REPLACE_OK: int = 0
    REPLACE_ERR: int = 1

    GET_OK: int = 0
    GET_ERR: int = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

        self.get_status = None
        self.replace_status = None
        self.find_status = None
        self.put_left_status = None
        self.put_right_status = None
        self.tail_status = None
        self.head_status = None
        self.right_status = None
        self.remove_status = None

    def size(self):
        node = self.head
        size = 0
        while node.next_value is not None:
            size += 1
            node = node.next_value
        return size

    def is_value(self):
        return self.head is None

    def is_head(self):
        return self.current is self.head

    def is_tail(self):
        return self.current is self.tail

    def head(self):
        if self.is_value():
            self.current = self.head
            self.head_status = self.HEAD_OK
        else:
            self.head_status = self.HEAD_ERR

    def tail(self):
        if self.is_value():
            self.current = self.tail
            self.tail_status = self.TAIL_OK
        else:
            self.tail_status = self.TAIL_ERR

    def right(self):
        if self.current.next_value is not None:
            self.current = self.current.next_value
            self.right_status = self.RIGHT_OK
        else:
            self.right_status = self.RIGHT_ERR

    def put_right(self, value):
        if self.is_value():
            new_node = Node(value=value, prev_value=self.current)
            if self.is_tail():
                self.tail = new_node

            else:
                self.current.next_value.prev_value = new_node
                new_node.next_value = self.current.next_value
            self.current.next_value = new_node
            self.put_right_status = self.PUT_RIGHT_OK

        else:
            self.put_right_status = self.PUT_RIGHT_ERR

    def put_left(self, value):
        if self.is_value():
            new_node = Node(value=value, next_value=self.current)
            if self.is_head():
                self.head = new_node
            else:
                self.current.prev_value.next_value = new_node
                new_node.prev_value = self.current.prev_value
            self.current.prev_value = new_node
            self.put_right_status = self.PUT_RIGHT_OK

        else:
            self.put_left_status = self.PUT_LEFT_ERR

    def remove(self):
        if self.is_value():
            if self.is_head():
                self.head = self.current.next_value

            if self.is_tail():
                self.tail = self.current.prev_value

            if self.current.next_value is not None:
                self.current.next_value.prev_value = self.current.prev_value
            if self.current.prev_value is not None:
                self.current.prev_value = self.current.next_value
            if self.current.next_value is not None:
                self.current = self.current.next_value
            else:
                self.current = self.current.prev_value

            self.remove_status = self.REMOVE_OK
        else:
            self.remove_status = self.REMOVE_ERR

    def clear(self):
        node = self.head
        while node is not None:
            temp = node.next
            node = None
            node = temp
        self.tail = self.head = None
        self.current = None

        self.get_status = None
        self.replace_status = None
        self.find_status = None
        self.put_left_status = None
        self.put_right_status = None
        self.tail_status = None
        self.head_status = None
        self.right_status = None
        self.remove_status = None

    def add_tail(self, value):
        new_node = Node(value=value)
        if not self.is_value():
            self.head = new_node
        else:
            self.tail.next_value = new_node
            new_node.prev_value = self.tail
        self.tail = new_node

    def replace(self, value):
        if self.is_value() and self.current is not None:
            self.current.value = value
            self.replace_status = self.REPLACE_OK
        else:
            self.replace_status = self.REPLACE_ERR

    def find(self, value):
        if self.is_value():
            node = self.current
            while node.next_value is not self.current:
                if node is self.tail:
                    node = self.head
                if node.value == value:
                    self.current = node
                    self.find_status = self.FIND_OK
                    break
            else:
                self.find_status = self.FIND_FALSE
        else:
            self.find_status = self.FIND_ERR

    def remove_all(self, value):
        self.find(value)
        while self.get_find_status() == self.FIND_OK:
            self.remove()

    # успешно / список пустой
    def get_remove_status(self) -> bool:
        return self.remove_status

    # успешно / правее нет элемента
    def get_right_status(self) -> bool:
        return self.right_status

    # успешно / список пустой
    def get_head_status(self) -> bool:
        return self.head_status

    # успешно / список пустой
    def get_tail_status(self) -> bool:
        return self.tail_status

    # успешно / список пустой
    def get_put_right_status(self) -> bool:
        return self.put_right_status

    # успешно / список пустой
    def get_put_left_status(self) -> bool:
        return self.put_left_status

    # успешно / список пустой / не найден
    def get_find_status(self) -> bool:
        return self.find_status

    # успешно / список пустой
    def get_replace_status(self) -> bool:
        return self.replace_status

    # успешно / список пустой
    def get_get_status(self) -> bool:
        return self.get_status


class LinkedList(ParentList):
    pass


class TwoWayList(ParentList):
    LEFT_OK: int = 0
    LEFT_ERR: int = 1

    def __init__(self):
        super().__init__()
        self.left_status = None

    def left(self):
        if self.current.prev_value is not None:
            self.current = self.current.prev_value
            self.left_status = self.LEFT_OK
        else:
            self.left_status = self.LEFT_ERR

    def clear(self):
        super().clear()
        self.left_status = None

    # успешно / список пустой
    def get_left_status(self) -> bool:
        return self.left_status
