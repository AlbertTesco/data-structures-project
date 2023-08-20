class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        node.next_node = self.head
        self.head = node

        if self.tail is None:
            self.tail = self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
            self.tail.next_node = None

    def get_data_by_id(self, id: int) -> dict:
        """Возвращает данные (словарь) узла с указанным id"""

        for x in self.to_list():
            try:
                if x['id'] == id:
                    return x
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")

    def to_list(self) -> list:
        list_to_return = []
        node = self.head

        while node:
            list_to_return.append(node.data)
            node = node.next_node

        return list_to_return

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
