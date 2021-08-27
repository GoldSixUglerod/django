from django.db import models


class Leader(models.Model):
    leader_id = models.IntegerField(null=False)
    employee_id = models.IntegerField(null=False)
