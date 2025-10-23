from django.db import models

class Note(models.Model):
    """
    A simple sticky note model.
    Fields:
      - title: short text
      - content: big text area
      - created_at: timestamp created automatically
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This string helps admin and shell show a readable name
        return self.title
