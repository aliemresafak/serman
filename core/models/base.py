from django.db import models

class CommonField(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)

    class Meta:
        abstract = True