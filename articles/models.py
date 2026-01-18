from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

