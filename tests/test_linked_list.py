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
