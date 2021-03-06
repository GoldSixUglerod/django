from django.contrib.postgres.fields import ArrayField
from django.db import models

from ai_api.utils import KeywordsExtractor
from ..models.Task import Task

class Department(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    list_targets = ArrayField(models.CharField(max_length=50), default=list)
    description = models.TextField(max_length=1000, blank=True, default="")

    def __str__(self):
        return str(self.name)

    def generate_targets(self):
        extractor = KeywordsExtractor()  # Создается экстрактор
        tasks = Task.objects.filter(employee__department=self.pk)  # Создается список всех задач департамента
        # Словарь вида {ключевое слово: количество задач, в которых используется это ключевое слово}
        key_words_for_tasks = {}

        for task in tasks:
            key_words, confidences = extractor.extract(task.description)  # Извлечение ключевых слов для конкретной задачи из писка задач
            for key_word in key_words:
                # Добавление ключевого слова в словарь для подсчёта их количества
                if key_word in key_words_for_tasks:
                    key_words_for_tasks[key_word] += 1
                else:
                    key_words_for_tasks[key_word] = 0

        # Сортировка ключевых слов по частоте использования и выделение до 5 самых используемых ключевых слов
        self.list_targets = [k for k, v in sorted(key_words_for_tasks.items())][:5]

    def save(self, *args, **kwargs):
        self.generate_targets()
        super().save(*args, **kwargs)
