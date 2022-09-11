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
    FIND_FALSE: int = 1 # элемент не найден
    FIND_ERR: int = 2  # список пустой

    REPLACE_OK: int = 0  # изменено значение текущего элемента
    REPLACE_ERR: int = 1  # список пустой

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
