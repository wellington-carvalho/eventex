from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Wellington Carvalho', cpf='12345678901',
                    email='wellington.carvalho@armazemparaiba.com.br', phone='86-99405-1162')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'wellington.carvalho@armazemparaiba.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Wellington Carvalho',
            '12345678901',
            'wellington.carvalho@armazemparaiba.com.br',
            '86-99405-1162'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

