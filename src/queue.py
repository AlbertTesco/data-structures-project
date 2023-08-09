class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = []
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.queue.append(Node(data, None))

        if len(self.queue) == 1:
            self.tail = self.queue[-1]
            self.head = self.queue[-1]
        else:
            self.tail = self.queue[-1]
            self.head = self.queue[0]

            self.head.next_node = self.queue[1]

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if len(self.queue) == 0:
            return None

        self.head = self.queue[0].next_node

        return self.queue.pop(0).data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        list_ = []

        for node in self.queue:
            list_.append(node.data)

        return "\n".join(list_)
