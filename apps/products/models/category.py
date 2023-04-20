from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products_category'

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
