"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """Тесты для класса linked_list."""

    def test_insert_beginning(self):
        """Тест для метода insert_beginning."""
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        self.assertEqual(linked_list.head.data, {'id': 1})

    def test_insert_end(self):
        """Тест для метода insert_end."""
        linked_list = LinkedList()
        linked_list.insert_at_end({'id': 1})
        self.assertEqual(linked_list.tail.data, {'id': 1})

    def test_str(self):
        """Тест для метода __str__."""
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1})
        self.assertEqual(str(linked_list), " {'id': 1} -> None")

    def test_to_list_and_get_data_by_id(self):
        linked_list = LinkedList()

        linked_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        linked_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
        linked_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
        linked_list.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = linked_list.to_list()
        assert len(lst) == 4
        user_data = linked_list.get_data_by_id(3)
        assert user_data == {'id': 3, 'username': 'mosh_s'}
