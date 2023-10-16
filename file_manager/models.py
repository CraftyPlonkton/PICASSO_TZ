from django.db import models


class File(models.Model):
    file = models.FileField(null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-uploaded_at']
