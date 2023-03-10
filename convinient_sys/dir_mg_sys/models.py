from django.db import models


class group_mst(models.Model):
    group_id= models.CharField(primary_key=True,max_length=100)
    group_name = models.CharField(max_length=100,null=True)

class user_mst(models.Model):
    user_id = models.CharField(primary_key=True,max_length=100)
    user_name = models.CharField(max_length=100,null=True)

class group_organaization(models.Model):
    group_mst= models.ForeignKey(group_mst,to_field='group_id',on_delete=models.CASCADE)
    user_mst= models.ForeignKey(user_mst,to_field='user_id',on_delete=models.CASCADE)

class dir_mst(models.Model):
    dirpath = models.CharField(primary_key=True,max_length=1000)
    dirvolume = models.IntegerField()
    dirmanager = models.ForeignKey(user_mst,on_delete=models.PROTECT)
    dirphase = models.IntegerField()
    class Meta:
        ordering = ['dirpath']

class access_mst_user(models.Model):
    dirpath = models.ForeignKey(dir_mst,models.PROTECT)
    user_mst = models.ForeignKey(user_mst,models.PROTECT)
    authority = models.CharField(choices=(('F','フルコントロール'),('W', '更新権'),('R', '検索権')),max_length=50)

class access_mst_group(models.Model):
    dirpath = models.ForeignKey(dir_mst,models.PROTECT)
    group_mst = models.ForeignKey(group_mst,models.PROTECT)
    authority = models.CharField(choices=(('F','フルコントロール'),('W', '更新権'),('R', '検索権')),max_length=50)