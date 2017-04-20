from django.db import models
import sys;

reload(sys)
sys.setdefaultencoding("utf8")

# Create your models here.
class Business(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField()
	createdate = models.DateTimeField()
	status = models.SmallIntegerField(default=1)
	deadline = models.DateTimeField()
	owner = models.CharField(max_length=20)

	def __unicode__(self):
		return self.title