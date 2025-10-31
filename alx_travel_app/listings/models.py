from django.db import models


class Listing(models.Model):
    """A tiny sample model so the package is non-empty and importable."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
