# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import ListEntry
from django.test import Client


class IndexTestCase(TestCase):
    def setUp(self):
        ListEntry.objects.create(Description="task1", isDone=0)
        ListEntry.objects.create(Description="task2", isDone=0)
        ListEntry.objects.create(Description="task3", isDone=0)

    def test_get_initial_todoList(self):
        response = self.client.get(reverse('todo:todoList'))
        countListEntries = response.context[11].dicts[3].get('todo_list').count()
        self.assertEqual(countListEntries, 3)
class TestCase_GET_create(TestCase):
    def setUp(self):
        ListEntry.objects.create(Description="task1", isDone=0)
        ListEntry.objects.create(Description="task2", isDone=0)
        ListEntry.objects.create(Description="task3", isDone=0)

    def test_get_create_ListEntry(self):
        response = self.client.get(reverse('todo:create'))
        self.assertEqual(response.status_code, 200)
class TestCase_POST_create(TestCase):
    def setUp(self):
        ListEntry.objects.create(Description="task1", isDone=0)
        ListEntry.objects.create(Description="task2", isDone=0)
        ListEntry.objects.create(Description="task3", isDone=0)

    def test_post_create_ListEntry(self):
        self.client.post(reverse('todo:create'), data={"Description": "task4"})
        response = self.client.get(reverse('todo:todoList'))
        countListEntries = response.context[11].dicts[3].get('todo_list').count()
        self.assertEqual(countListEntries, 4)
class TestCase_GET_edit(TestCase):
    def setUp(self):
        ListEntry.objects.create(Description="task1", isDone=0)
        ListEntry.objects.create(Description="task2", isDone=0)
        ListEntry.objects.create(Description="task3", isDone=0)

    def test_get_edit_ListEntry(self):
        self.client.get(reverse('todo:edit', kwargs={"id": 1}))
        test = ListEntry.objects.get(pk=1)
        self.assertEqual(test.Description, "task1")
class TestCase_POST_edit(TestCase):
    def setUp(self):
        ListEntry.objects.create(Description="task1", isDone=0)
        ListEntry.objects.create(Description="task2", isDone=0)
        ListEntry.objects.create(Description="task3", isDone=0)

    def test_post_edit_ListEntry(self):
        self.client.post(reverse('todo:edit', kwargs={"id": 1}), data={"Description": "task_edited", "isDone": 1})
        test = ListEntry.objects.get(pk=1)
        self.assertEqual(test.Description, "task_edited")
class TestCase_GET_delete(TestCase):
    def setUp(self):
        ListEntry.objects.create(Description="task1", isDone=0)
        ListEntry.objects.create(Description="task2", isDone=0)
        ListEntry.objects.create(Description="task3", isDone=0)

    def test_get_delete_ListEntry(self):
        self.client.get(reverse('todo:delete', kwargs={"id": 1}))
        test = ListEntry.objects.get(pk=1)
        self.assertEqual(test.Description, "task1")
class TestCase_POST_delete(TestCase):
    def setUp(self):
        ListEntry.objects.create(Description="task1", isDone=0)
        ListEntry.objects.create(Description="task2", isDone=0)
        ListEntry.objects.create(Description="task3", isDone=0)

    def test_post_delete_ListEntry(self):
        response = self.client.get(reverse('todo:todoList'))
        countListEntriesInitial = response.context[11].dicts[3].get('todo_list').count() - 1
        self.client.post(reverse('todo:delete', kwargs={"id": 1}))
        response = self.client.get(reverse('todo:todoList'))
        countListEntries = response.context[11].dicts[3].get('todo_list').count()
        self.assertEqual(countListEntries, countListEntriesInitial)
