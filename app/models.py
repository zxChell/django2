from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companys'


class Products(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return self.name


class Course2(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student2(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course2, through='Enrollment')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student2, on_delete=models.CASCADE)
    course = models.ForeignKey(Course2, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.IntegerField()
