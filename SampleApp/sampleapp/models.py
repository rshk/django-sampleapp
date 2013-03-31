from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class MyObject(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('sample:detail', kwargs=dict(pk=self.pk))
