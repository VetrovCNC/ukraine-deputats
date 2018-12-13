from django.db import models



class Deputat(models.Model):

    vrd_link = models.URLField(null=True, blank=True)
    vrd_id = models.IntegerField(null=True, blank=True)
    vrd_photo = models.URLField(null=True, blank=True)
    surname = models.CharField(max_length=64, default="", null=True, blank=True)
    name = models.CharField(max_length=64, default="", null=True, blank=True)
    patronymic = models.CharField(max_length=64, default="", null=True, blank=True)
    selected_by = models.CharField(max_length=128, default="", null=True, blank=True)
    party = models.CharField(max_length=256, default="", null=True, blank=True)
    party_number = models.IntegerField(null=True, blank=True)
    fraction = models.CharField(max_length=256, default="", null=True, blank=True)
    position = models.CharField(max_length=512, default="", null=True, blank=True)
    region = models.CharField(max_length=256, default="", null=True, blank=True)
    gender = models.CharField(max_length=1, default="", null=True, blank=True)


    class Meta:
        verbose_name = "Deputat"
        verbose_name_plural = "Deputats"

    def __str__(self):
        return '{} {} {}'.format(self.surname, self.name, self.patronymic)

