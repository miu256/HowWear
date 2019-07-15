import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):
	
	def test_future_question(self):
		""" 
		公開日が明日となっている質問に対して、
		was_published_recently関数がFalseを返すかどうかのテスト
		"""
		time = timezone.now() + datetime.timedelta(days=1)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_old_question(self):
		""" 
		公開日が一日より前となっている質問に対して、
		was_published_recently関数がFalseを返すかどうかのテスト
		"""
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_correct_question(self):
		""" 
		公開日が現在から一日以内となっている質問に対して、
		was_published_recently関数がTrueを返すかどうかのテスト
		"""
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)
		
    
    
def create_question(question_text, days):
    """ 質問の作成を行う """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
    

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """ 質問が無い場合のテスト """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "質問がありません。")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """ 現在より前の質問を表示するテスト """
        create_question(question_text="Past question.", days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """ 未来の質問に対して404を返すテスト """
        future_question = create_question(question_text='Future question.', days=10)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """ 昔の質問の詳細を表示するテスト """
        past_question = create_question(question_text='Past Question.', days=-10)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

