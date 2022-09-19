class ATSQueue:

    POP_OK: int = 0 # успешно
    POP_ERR: int = 1 # очередь пустая

    GET_OK: int = 0 # успешно
    GET_ERR: int = 1 # очередь пустая
    # конструктор
    # постусловие: создана пустая очередь
    def __init__(self):
        raise NotImplementedError

    # команды:
    # постусловие: добавлен новый элемент в конец очереди
    def push(self, value):
        raise NotImplementedError

    # предусловие: очередь не пустая
    # постусловие: первый элемент очереди удален
    def pop(self):
        raise NotImplementedError

    # запросы:

    def size(self):
        raise NotImplementedError

    # предусловие: очередь не пустая
    def get(self):
        raise NotImplementedError

    # запросы статусов:

    # успешно/очередь пустая
    def get_get_status(self):
        raise NotImplementedError

    # успешно/очередь пустая
    def get_pop_status(self):
        raise NotImplementedError


class Queue:
    POP_OK: int = 0  # успешно
    POP_ERR: int = 1  # очередь пустая

    GET_OK: int = 0  # успешно
    GET_ERR: int = 1  # очередь пустая

    def __init__(self):
        self.values = []
        self.get_status = None
        self.pop_status = None

    def size(self):
        return len(self.values)

    def pop(self):
        if self.size() > 0:
            self.values.pop(0)
            self.pop_status = self.POP_OK
        else:
            self.pop_status = self.POP_ERR

    def push(self, value):
        self.values.append(value)

    def get(self):
        if self.size() > 0:
            self.get_status = self.GET_OK
            return self.values[0]
        else:
            self.get_status = self.GET_OK
            return 0

    def get_get_status(self):
        return self.get_status

    def get_pop_status(self):
        return self.pop_status