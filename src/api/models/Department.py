from django.contrib.postgres.fields import ArrayField
from django.db import models

from ai_api.utils import KeywordsExtractor
from api.models import Task


class Department(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    list_targets = ArrayField(models.CharField(max_length=50), default=list)
    description = models.TextField(max_length=1000, blank=True, default="")

    def __str__(self):
        return str(self.name)

    def generate_targets(self):
        extractor = KeywordsExtractor()
        tasks = Task.objects.filter(employee__department=self.pk)
        key_words_for_tasks = {}
        for task in tasks:
            key_words = extractor.extract(task)
            for key_word in key_words:
                if key_word in key_words_for_tasks:
                    key_words_for_tasks[key_word] += 1
                else:
                    key_words_for_tasks[key_word] = 0
        self.list_targets = [k for k, v in sorted(key_words_for_tasks.items())][:5]

    def save(self, *args, **kwargs):
        self.generate_targets()
        super().save(*args, **kwargs)
