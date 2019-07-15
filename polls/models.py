import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('公開日')
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date >= now - datetime.timedelta(days=1) and self.pub_date <= now


class Choice(models.Model):
	#質問と選択肢の対応付け
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text