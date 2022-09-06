class ATSBoundedStack:
    PUSH_NIL: int = 0  # push() не вызывался
    PUSH_OK: int = 1  # в стек добавлен элемент
    PUSH_ERR: int = 2  # в стеке кол-во элементов равно заданному размеру

    POP_NIL: int = 0  # push() не вызывалась
    POP_OK: int = 1  # последняя pop() отработала успешно
    POP_ERR: int = 2  # стек пустой

    PEEK_NIL: int = 0  # push() не вызывалась
    PEEK_OK: int = 1  # последняя peek() вернула верное значение
    PEEK_ERR: int = 2  # стек пустой

    # постусловие: создан новый пусток стек с размером size
    def __init__(self, size: int = 32):
        raise NotImplementedError

    # предусловие: кол-во элементов меньше заданного размера size
    # постусловие: в стек добавляется новый элемент
    def push(self, value):
        raise NotImplementedError

    # предусловие: стек не пустой
    # постусловие: из стека удален последний элемент
    def pop(self):
        raise NotImplementedError

    # предусловие: стек не пустой
    def peek(self):
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError

    # постусловие: в стеке нет элементов
    def clear(self):
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    # Возвращает значение PEEK_*
    def get_peek_status(self) -> int:
        raise NotImplementedError

    # Возвращает значение POP_*
    def get_pop_status(self) -> int:
        raise NotImplementedError

    # Возвращает значение PUSH_*
    def get_push_status(self) -> int:
        raise NotImplementedError


class BoundedStack:
    PUSH_NIL: int = 0  # push() не вызывался
    PUSH_OK: int = 1  # в стек добавлен элемент
    PUSH_ERR: int = 2  # в стеке кол-во элементов равно заданному размеру

    POP_NIL: int = 0  # push() не вызывалась
    POP_OK: int = 1  # последняя pop() отработала успешно
    POP_ERR: int = 2  # стек пустой

    PEEK_NIL: int = 0  # push() не вызывалась
    PEEK_OK: int = 1  # последняя peek() вернула верное значение
    PEEK_ERR: int = 2  # стек пустой

    def __init__(self, max_size: int = 32):
        self.peek_status = None
        self.pop_status = None
        self.stack = None
        self.push_status = None
        self.max_size = max_size
        self.clear()

    def clear(self):
        self.stack = []
        self.push_status = self.PUSH_NIL
        self.pop_status = self.POP_NIL
        self.peek_status = self.PEEK_NIL

    def peek(self):
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = self.PEEK_OK
        else:
            result = 0
            self.peek_status = self.PEEK_ERR

        return result

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() > 0:
            self.stack.remove(-1)
            self.pop_status = self.POP_OK
        else:
            self.pop_status = self.POP_ERR

    def is_full(self) -> bool:
        return self.size() > (self.max_size - 1)

    def push(self, value):
        if self.is_full():
            self.push_status = self.PUSH_ERR
        else:
            self.stack.append(value)
            self.push_status = self.PUSH_OK

    def get_peek_status(self) -> int:
        return self.peek_status

    def get_pop_status(self) -> int:
        return self.pop_status

    def get_push_status(self) -> int:
        return self.push_status
