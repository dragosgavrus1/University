import copy


class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = 2
        self.element_count = 0
        self.element_list = [None] * 2

    def compute_hash(self, key):
        if isinstance(key, int):
            return key % self.capacity

        total = 0
        for char in key:
            total += ord(char)
        return total % self.capacity

    def insert(self, key, value):
        if self.element_count and (self.capacity // self.element_count < 2):
            self.resize_and_rehash()

        index = self.compute_hash(key)
        node = self.element_list[index]

        if node is None:
            self.element_list[index] = HashNode(key, value)
            self.element_count += 1
            return

        while node.next is not None:
            node = node.next
        node.next = HashNode(key, value)
        self.element_count += 1

    def get(self, key):
        node = self.element_list[self.compute_hash(key)]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def resize_and_rehash(self):
        self.capacity *= 2

        old_bucket_list = copy.deepcopy(self.element_list)
        self.element_list = [None] * self.capacity
        self.element_count = 0
        for node in old_bucket_list:
            copy_node = copy.deepcopy(node)
            while copy_node is not None:
                self.insert(copy_node.key, copy_node.value)
                copy_node = copy_node.next
