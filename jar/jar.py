class Jar:
    def __init__(self,capacity = 12):
        if capacity < 0:
            raise ValueError
        self._size = 0
        self._capacity = capacity
    def __str__(self):
        return "🍪"*self._size

    def deposit(self,n):
        if n > self._capacity or self._size + n > self._capacity:
            raise ValueError("deposit Error")
        self._size += n
    def withdraw(self,n):
        if n > self._size:
            raise ValueError("withdraw Error")
        self._size -= n
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,value):
        self.value = value
        if self.value < 0 :
            raise ValueError
        else:
            self.value = self._capacity
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,value):
        self._size = value
