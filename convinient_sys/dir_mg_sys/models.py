from django.db import models



class dir_mst(models.Model):
    dirpath = models.CharField(primary_key=True,max_length=1000)
    dirvolume = models.IntegerField()
    dirmanager = models.CharField(max_length=50)
    dirphase = models.IntegerField()
    class Meta:
        ordering = ['dirpath']


class access_mst(models.Model):
    dirpath = models.ForeignKey(dir_mst,models.PROTECT)
    username = models.CharField(max_length=50)
    authority = models.CharField(choices=(('F','フルコントロール'),('W', '更新権'),('R', '検索権')),max_length=50)
