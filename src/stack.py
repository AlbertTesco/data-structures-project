class Node:
    """Класс для узла стека"""

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

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack = []
        self.top = None

    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.stack.append(Node(data, None))

        if len(self.stack) == 1:
            self.stack[0].next_node = None
        else:
            self.stack[-1].next_node = self.stack[-2]

        self.top = self.stack[-1]

    def pop(self):

        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data_from_first = self.stack.pop().data

        if len(self.stack) == 1:
            self.top = self.stack[0]
        elif len(self.stack) == 0:
            self.top = None

        return data_from_first
