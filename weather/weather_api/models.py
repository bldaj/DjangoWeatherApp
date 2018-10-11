from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, null=False, db_index=True)
    date = models.DateTimeField(null=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
