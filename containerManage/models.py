from django.db import models

# python manage.py makemigrations
# python manage.py migrate
# 多表重新建立
# 后台管理布局
# 出版社下拉框，遍历数据库显示

# 一对多
class Host(models.Model):
    ip = models.CharField(max_length=32)
    name = models.CharField(max_length=32)


class Container(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    tag = models.CharField(max_length=32)
    host = models.ForeignKey('Host')

    def __str__(self):
        return self.name




# 多对多
class User(models.Model):
    name = models.CharField(max_length=32)
