from django.db import models

# Create your models here.

class Post(models.Model):
    # 글의 제목
    title = models.CharField(max_length=50)
    # 글의 내용
    content = models.TextField()
    # 작성일
    dt_created = models.DateField(verbose_name="Date Created", auto_now_add=True)
    # 수정일
    dt_modified = models.DateField(verbose_name="Date Modified", auto_now=True)


    def __str__(self) -> str:
        return self.title