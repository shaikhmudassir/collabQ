from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    STATUS_CHOICES = [
    (1, 'Open'),
    (2, 'Picked'),
    (3, 'Completed'),
    ]

    COMPLEXITY_CHOICES = [
    (1, 'Simple'),
    (2, 'Moderate'),
    (3, 'High'),
    (4, 'Advanced'),
    (5, 'Extreme'),
    ]
    
    title = models.CharField(max_length=30, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    complexity = models.IntegerField(choices=COMPLEXITY_CHOICES,null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status =  models.IntegerField(choices=STATUS_CHOICES, default=1, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)

class Assign(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)

