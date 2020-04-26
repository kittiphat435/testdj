from django.db import models

# Create your models here.
class MobileProduct(models.Model):
	mobile_name = models.CharField(max_length=100)
	mobile_detail = models.TextField(null=True)
	mobile_price = models.IntegerField(blank=True,null=True)
	mobile_photo = models.ImageField(upload_to="gallery",null=True,blank=True)

	def __str__(self):
		return self.mobile_name
		
class Ems(models.Model):
	ems_number = models.CharField(max_length=100)
	ems_name = models.CharField(max_length=100)
	ems_price = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return 'ชื่อ: {} No. {} '.format(self.ems_name,self.ems_number)
		
class Askqa(models.Model):
	name = models.CharField(max_length=100)
	topic_problem=[('price','ราคา'),('shipping','ขนส่ง'),('change','เปลี่ยนเครื่องใหม่')]

	topic = models.CharField(max_length=100,choices=topic_problem,default='price')

	detail = models.TextField(null=True)

	def __str__(self):
		return '{} - {}'.format(self.name,self.topic)