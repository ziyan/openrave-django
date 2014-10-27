from __future__ import with_statement
from django.test import TestCase, Client
from django.contrib.auth.models import User
from user.models import Key
from robot.models import Robot
import os
import base64
import json

class RobotApiTestCase(TestCase):
    def setUp(self):
        # create a user
        self.username = 'mujin'
        self.password = 'verysecurepassword'
        self.user = User.objects.create_user(self.username, 'mujin@mujin.co.jp', self.password)

        # create a key
        self.key = Key(user=self.user)
        self.key.save()

        # create a robot for testing
        source = None
        with open(os.path.join(os.path.dirname(__file__), 'examples', 'man1.zae'), 'rb') as f:
            source = f.read()

        self.robot = Robot(user=self.user, source=source, content_type='application/zip')
        self.robot.save()

        # create a client
        self.client = Client(HTTP_AUTHORIZATION='Basic ' + base64.b64encode('%s:' % self.key.key))

    def test_auth(self):
        # try with key
        response = self.client.get('/api/robots')
        self.assertEqual(response.status_code, 200)

        # try anonymous
        client = Client()
        response = client.get('/api/robots')
        self.assertEqual(response.status_code, 401)

        # try with username password
        client = Client(HTTP_AUTHORIZATION='Basic ' + base64.b64encode('%s:%s' % (self.username, self.password)))
        response = client.get('/api/robots')
        self.assertEqual(response.status_code, 200)

        # try with incorrect username password
        client = Client(HTTP_AUTHORIZATION='Basic ' + base64.b64encode('%s:%s' % (self.username, self.password + '~')))
        response = client.get('/api/robots')
        self.assertEqual(response.status_code, 401)

        # try with incorrect key
        client = Client(HTTP_AUTHORIZATION='Basic ' + base64.b64encode('%s:' % self.key.key[32:] + self.key.key[:32]))
        response = client.get('/api/robots')
        self.assertEqual(response.status_code, 401)

    def test_list(self):
        response = self.client.get('/api/robots')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(len(data['robots']), 1)
        self.assertEqual(data['robots'][0]['id'], self.robot.id)
        self.assertEqual(data['robots'][0]['name'], self.robot.name)

    def test_get(self):
        response = self.client.get('/api/robots/%d' % self.robot.id)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data['robot']['id'], self.robot.id)
        self.assertEqual(data['robot']['name'], self.robot.name)

    def test_create(self):
        response = self.client.post('/api/robots', data=self.robot.source, content_type='application/zip')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertNotEqual(data['robot']['id'], self.robot.id)
        self.assertEqual(data['robot']['name'], self.robot.name)

        response = self.client.post('/api/robots', data=self.robot.source, content_type='application/xml')
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        response = self.client.delete('/api/robots/%d' % self.robot.id)
        self.assertEqual(response.status_code, 200)

        response = self.client.delete('/api/robots/%d' % self.robot.id)
        self.assertEqual(response.status_code, 404)

    def test_modify(self):
        response = self.client.put('/api/robots/%d' % self.robot.id, data=self.robot.source, content_type='application/zip')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data['robot']['id'], self.robot.id)
        self.assertEqual(data['robot']['name'], self.robot.name)

        self.assertEqual(len(Robot.objects.all()), 1)

        response = self.client.put('/api/robots/%d' % self.robot.id, data=self.robot.source, content_type='application/xml')
        self.assertEqual(response.status_code, 400)

