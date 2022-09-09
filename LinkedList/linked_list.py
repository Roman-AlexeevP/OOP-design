class ATSLinkedList:

    REMOVE_OK: int = 0 # удаление прошло успешно
    REMOVE_ERR: int = 1 # список был пустой, удаление не отработано

    RIGHT_OK: int = 0  # курсор установлен в правый элемент
    RIGHT_ERR: int = 1  # правый элемент отсутствует/курсор остается на прежнем месте

# Конструктор
    # постусловие: создан пустой связный лист
    def __init__(self):
        raise NotImplementedError

# Команды:
    # постусловие: курсор установлен в первый элемент списка
    def head(self):
        raise NotImplementedError

    # постусловие: курсор установлен в последний элемент списка
    def tail(self):
        raise NotImplementedError

    # предусловие: курсор не установлен в последний элемент списка
    # постусловие: курсор установлен в правый от него элемент
    def right(self):
        raise NotImplementedError

    # постусловие: в список добавлен новый элемент, расположенный после элемента, помеченного курсором
    def put_right(self, value):
        raise NotImplementedError

    # постусловие: в список добавлен новый элемент, расположенный перед элементом, помеченного курсором
    def put_left(self, value):
        raise NotImplementedError

    # предусловие: список содержит хотя бы один элемент
    # постусловие: текущий узел удален, курсор смещен либо к правому соседу, если есть, либо к левому
    def remove(self):
        raise NotImplementedError

    # постусловие: список пустой, курсор установлен в head и указывает на пустое значение
    def clear(self):
        raise NotImplementedError

    # постусловие: добавлен новый элемент в конце списка
    def add_tail(self, value):
        raise NotImplementedError

    # постусловие: текущие значение изменено на value
    def replace(self, value):
        raise NotImplementedError

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

    def get_remove_status(self) -> bool:
        raise NotImplementedError

    def get_right_status(self) -> bool:
        raise NotImplementedError