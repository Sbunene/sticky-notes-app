from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_has_title(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')


class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title='Test Note', 
            content='This is a test note.'
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        response = self.client.get(reverse(
            'note_detail', 
            args=[str(self.note.id)]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    def test_note_create_view_get(self):
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)

    def test_note_create_view_post(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Test Note',
            'content': 'This is a new test note.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Note.objects.filter(title='New Test Note').exists())

    def test_note_update_view_get(self):
        response = self.client.get(reverse(
            'note_update', 
            args=[str(self.note.id)]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_update_view_post(self):
        response = self.client.post(reverse(
            'note_update', 
            args=[str(self.note.id)]
        ), {
            'title': 'Updated Note',
            'content': 'This note has been updated.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_note_delete_view_get(self):
        response = self.client.get(reverse(
            'note_delete', 
            args=[str(self.note.id)]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_delete_view_post(self):
        response = self.client.post(reverse(
            'note_delete', 
            args=[str(self.note.id)]
        ))
        self.assertEqual(response.status_code, 302)  # Redirect after delete
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())