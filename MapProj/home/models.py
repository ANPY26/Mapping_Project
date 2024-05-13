from django.db import models

class explorer(models.Model):
    version_id = models.IntegerField()
    mapping_desc = models.CharField(max_length=100)
    user_id = models.CharField(max_length = 20)
    date_id = models.DateField()

    def __str__(self) -> str:
        return self.user_id
