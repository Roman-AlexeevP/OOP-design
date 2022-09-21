class ATSParentQueue:
    POP_HEAD_OK: int = 0  # успешно
    POP_HEAD_ERR: int = 1  # очередь пустая

    GET_HEAD_OK: int = 0  # успешно
    GET_HEAD_ERR: int = 1  # очередь пустая

    # конструктор
    # постусловие: создана пустая очередь
    def __init__(self):
        raise NotImplementedError

    # команды:
    # постусловие: добавлен новый элемент в конец очереди
    def add_tail(self, value):
        raise NotImplementedError

    # предусловие: очередь не пустая
    # постусловие: первый элемент очереди удален
    def pop_head(self):
        raise NotImplementedError

    # запросы:

    def size(self):
        raise NotImplementedError

    # предусловие: очередь не пустая
    def get_head(self):
        raise NotImplementedError

    # запросы статусов:

    # успешно/очередь пустая
    def get_get_head_status(self):
        raise NotImplementedError

    # успешно/очередь пустая
    def get_pop_head_status(self):
        raise NotImplementedError


class ATSQueue(ATSParentQueue):
    pass


class ATSDeque(ATSParentQueue):
    POP_TAIL_OK: int = 0  # успешно
    POP_TAIL_ERR: int = 1  # очередь пустая

    GET_TAIL_OK: int = 0  # успешно
    GET_TAIL_ERR: int = 1  # очередь пустая

    # конструктор
    # постусловие: создана пустая очередь
    def __init__(self):
        raise NotImplementedError

    # команды:
    # постусловие: добавлен новый элемент в начало очереди
    def add_head(self, value):
        raise NotImplementedError

    # предусловие: очередь не пустая
    # постусловие: последний элемент очереди удален
    def pop_tail(self):
        raise NotImplementedError

    # запросы:
    # предусловие: очередь не пустая
    def get_tail(self):
        raise NotImplementedError

    # успешно/очередь пустая
    def get_get_tail_status(self):
        raise NotImplementedError

    # успешно/очередь пустая
    def get_pop_tail_status(self):
        raise NotImplementedError


class ParentQueue:
    POP_HEAD_OK: int = 0  # успешно
    POP_HEAD_ERR: int = 1  # очередь пустая

    GET_HEAD_OK: int = 0  # успешно
    GET_HEAD_ERR: int = 1  # очередь пустая

    def __init__(self):
        self.values = []
        self.get_head_status = None
        self.pop_head_status = None

    def size(self):
        return len(self.values)

    def pop_head(self):
        if self.size() > 0:
            self.values.pop(0)
            self.pop_head_status = self.POP_OK
        else:
            self.pop_head_status = self.POP_ERR

    def add_tail(self, value):
        self.values.append(value)

    def get_head(self):
        if self.size() > 0:
            self.get_head_status = self.GET_OK
            return self.values[0]
        else:
            self.get_head_status = self.GET_OK
            return 0

    def get_get_head_status(self):
        return self.get_head_status

    def get_pop_head_status(self):
        return self.pop_head_status


class Queue(ParentQueue):
    pass


class Deque(ParentQueue):
    POP_TAIL_OK: int = 0  # успешно
    POP_TAIL_ERR: int = 1  # очередь пустая

    GET_TAIL_OK: int = 0  # успешно
    GET_TAIL_ERR: int = 1  # очередь пустая

    def __init__(self):
        super().__init__()
        self.pop_tail_status = None
        self.get_tail_status = None

    def pop_tail(self):
        if self.size() > 0:
            self.values.pop()
            self.pop_tail_status = self.POP_TAIL_OK
        else:
            self.pop_tail_status = self.POP_TAIL_ERR

    def add_head(self, value):
        self.values.insert(0, value)

    def get_tail(self):
        if self.size() > 0:
            self.get_tail_status = self.GET_TAIL_OK
            return self.values[-1]
        else:
            self.get_tail_status = self.GET_TAIL_OK
            return 0

    def get_get_tail_status(self):
        return self.get_tail_status

    def get_pop_tail_status(self):
        return self.pop_tail_status
