from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0],item[0])for item in LEXERS])
STYLE_CHOICES = sorted((item,item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,default='',verbose_name='测试标题')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,default='python',max_length=100,verbose_name='语言')
    style = models.CharField(choices=STYLE_CHOICES,default='friendly',max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created',)
        verbose_name = 'rest学习'
        verbose_name_plural = verbose_name