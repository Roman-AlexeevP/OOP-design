class ATSBloomFilter:

    # постусловие: создан битовый массив размер filter_len
    def __init__(self, filter_len):
        raise NotImplementedError

    # постусловие: в фильтр занесено значение value
    def add(self, value):
        raise NotImplementedError

    # возвращает логическое значение: наличие в фильтре значения
    def get(self, value):
        raise NotImplementedError

class BloomFilter:

    FIRST_RANDOM_NUMBER = 17
    SECOND_RANDOM_NUMBER = 223

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitearray = 0

    def hash1(self, value):
        random_number = self.FIRST_RANDOM_NUMBER
        iter_value = 0
        for c in value:
            code = ord(c)
            iter_value = (iter_value * random_number + code) % self.filter_len
        return iter_value

    def hash2(self, value):
        random_number = self.SECOND_RANDOM_NUMBER
        iter_value = 0
        for c in value:
            code = ord(c)
            iter_value = (iter_value * random_number + code) % self.filter_len
        return iter_value

    def get_hashes(self, value):
        return (
            self.hash1(value),
            self.hash2(value)
        )

    def set_bit(self, index):
        mask = 1 << index
        self.bitearray |= mask
        return index

    def get_bit(self, index):
        mask = 1 << index
        return self.bitearray & mask

    def add(self, value):
        for index in self.get_hashes(value):
            self.set_bit(index)

    def get(self, value):
        bites = (self.get_bit(hashed) for hashed in self.get_hashes(value))
        return all(bites)