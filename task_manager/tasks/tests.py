from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='user@example.com'
            )
        self.client.force_login(self.user)
        self.executor = User.objects.create_user(
            username='testexecutor',
            password='testpassword123',
            email='executor@example.com'
            )
        self.status = Status.objects.create(name='teststatus')
        self.label1 = Label.objects.create(name='testlabel1')
        self.label2 = Label.objects.create(name='testlabel2')

    def test_tasks_list_view(self):
        self.task1 = Task.objects.create(
            name='testtask1',
            description='testinfo1',
            status=self.status,
            author=self.user,
            executor=self.executor
            )
        self.task1.labels.add(self.label1, self.label2)
        self.task2 = Task.objects.create(
            name='testtask2',
            description='testinfo2',
            status=self.status,
            author=self.user,
            executor=self.executor
            )
        self.task2.labels.add(self.label1, self.label2)
        url = reverse('list_tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/list_tasks.html')

    def test_create_task(self):
        response = self.client.post(
            reverse("task_create"),
            {
                'name': 'testtask',
                'description': 'testinfo',
                'status': self.status.id,
                'author': self.user.id,
                'executor': self.executor.id,
                'label': self.label1.id
                },
            )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='testtask').exists())

    def test_update_task(self):
        self.task = Task.objects.create(
            name='testtask',
            description='testinfo',
            status=self.status,
            author=self.user,
            executor=self.executor
            )
        self.task.labels.add(self.label1, self.label2)
        response = self.client.post(
            reverse('task_update', args=[self.task.id]),
            {
                'name': 'updatedtask',
                'description': 'testinfo',
                'status': self.status.id,
                'author': self.user.id,
                'executor': self.executor.id,
                'label': [self.label1.id, self.label2.id]
                }
            )
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.name, 'updatedtask')

    def test_delete_task(self):
        self.task = Task.objects.create(
            name='testtask',
            description='testinfo',
            status=self.status,
            author=self.user,
            executor=self.executor
            )
        self.task.labels.add(self.label1, self.label2)
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(name='testtask').exists())


class TaskFilterTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='user@example.com'
            )
        self.client.force_login(self.user)
        self.executor = User.objects.create_user(
            username='testexecutor',
            password='testpassword123',
            email='executor@example.com'
            )
        self.status1 = Status.objects.create(name='teststatus1')
        self.status2 = Status.objects.create(name='teststatus2')
        self.label1 = Label.objects.create(name='testlabel1')
        self.label2 = Label.objects.create(name='testlabel2')
        self.task1 = Task.objects.create(
            name='testtask1',
            description='testinfo1',
            status=self.status1,
            author=self.user,
            executor=self.executor
            )
        self.task1.labels.add(self.label1)
        self.task2 = Task.objects.create(
            name='testtask2',
            description='testinfo2',
            status=self.status2,
            author=self.user,
            executor=self.executor
            )
        self.task2.labels.add(self.label2)

    def test_status_filter(self):
        data = {'status': self.status1.id}
        filter = TaskFilter(data=data, queryset=Task.objects.all()).qs
        self.assertEqual(filter.count(), 1)
        self.assertEqual(filter.first().name, 'testtask1')

    def test_executor_filter(self):
        data = {'executor': self.executor.id}
        filter = TaskFilter(data=data, queryset=Task.objects.all()).qs
        self.assertEqual(filter.count(), 2)
        self.assertIn(self.task1, filter)
        self.assertIn(self.task2, filter)

    def test_label_filter(self):
        data = {'label': self.label2.id}
        filter = TaskFilter(data=data, queryset=Task.objects.all()).qs
        self.assertEqual(filter.count(), 1)
        self.assertEqual(filter.first().name, 'testtask2')

    def test_my_tasks_filter(self):
        data = {'my_tasks': True}
        request = self.client.get('/tasks/', data)
        request.user = self.user
        filter = TaskFilter(
            data=data,
            queryset=Task.objects.all(),
            request=request
            ).qs
        self.assertEqual(filter.count(), 2)
        self.assertIn(self.task1, filter)
        self.assertIn(self.task2, filter)

    def test_no_filters(self):
        filter = TaskFilter(data={}, queryset=Task.objects.all()).qs
        self.assertEqual(filter.count(), 2)
