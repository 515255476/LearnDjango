from django.db import models


# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=200, unique=True)
    leader = models.CharField(max_length=200)
    tester = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    app = models.CharField(max_length=200)

    class Meta:
        db_table = 'tb_project'
        verbose_name = '项目'
        verbose_name_plural = "项目"

    def __str__(self):
        return self.project_name


class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name='测试人员名称')
    sex = models.CharField(choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ), max_length=200)
    age = models.IntegerField(verbose_name='年龄')
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'tb_person'
        verbose_name = '测试人员'
        verbose_name_plural = "测试人员"

    def __str__(self):
        return self.name
