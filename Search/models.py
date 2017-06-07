from django.db import models

# Create your models here.
class BlinkMod(models.Model):
	name = models.TextField(unique=True,blank=False,null=True)
	url = models.TextField(unique=True,blank=False,null=True)

class FourMinMod(models.Model):
	name = models.TextField(unique=True,blank=False,null=True)
	url = models.TextField(unique=True,blank=False,null=True)

class ReadItForMeMod(models.Model):
	name = models.TextField(unique=True,blank=False,null=True)
	url = models.TextField(blank=False,null=True)

class BizSumMod(models.Model):
	name = models.TextField(unique=True,blank=False,null=True)
	url = models.TextField(blank=False,null=True)

class KirkusMod(models.Model):
	name = models.TextField(unique=True,blank=False,null=True)
	url = models.TextField(blank=False,null=True)

