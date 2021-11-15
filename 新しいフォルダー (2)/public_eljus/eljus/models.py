from accounts.models import CustomUser #11/12
from django.db import models

# Create your models here.
class ProblemManage(models.Model):
  #問題モデル

  username = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

  #使用言語   1112
  LANGUAGE_CHOICES = (
        ('java', 'java'),
        ('python', 'python'),
        ('html', 'html'),
        # (20, '20代'),
    )
  uselanguage = models.TextField(
        verbose_name="使用言語",
        choices=LANGUAGE_CHOICES)

  #使用構文    1112
  SYNTAX_CHOICES = (
        ('for', 'for'),
        # (20, '20代'),
    )
  usesyntax = models.TextField(
        verbose_name="使用構文",
        choices=SYNTAX_CHOICES)

  #その他選択     1115
  usesyntaxtext = models.CharField(verbose_name='その他の構文', max_length=10)


  problemstate = models.CharField(verbose_name='問題文', max_length=40)
  problemimage = models.ImageField(verbose_name='問題文画像', blank=True,null=True)


  #難易度　1115
  LEVEL_CHOICES = (
        ('初級', '初級'),
        ('中級', '中級'),
        ('上級', '上級'),
    )
  difficulty = models.TextField(
        verbose_name="難易度",
        choices=LEVEL_CHOICES)

  
  #ヒント
  tips = models.TextField(verbose_name='ヒント', blank=True, null=True)


  #答え
  #ans1 = 
  #photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)

  created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

  class Meta:
    verbose_name_plural = 'ProblemManage'#もとは'Diary'

  def __str__(self):
        return self.title

#   def clean(self):
#         cleaned_data = super().clean()
#         if #問題文 と 問題文画像 の組み合わせバリデーションルール:
#           raise models.ValidationError('どちらか必須')
#         return cleaned_data
