from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
