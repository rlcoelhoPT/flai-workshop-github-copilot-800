from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserAPITestCase(APITestCase):
    """Tests for the User API endpoints"""

    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpass123',
            team='Team Marvel',
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'team': 'Team DC',
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        response = self.client.get(f'/api/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')


class TeamAPITestCase(APITestCase):
    """Tests for the Team API endpoints"""

    def setUp(self):
        self.team = Team.objects.create(
            name='Team Marvel',
            description="Earth's Mightiest Heroes",
        )

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        data = {
            'name': 'Team DC',
            'description': 'Justice League Champions',
        }
        response = self.client.post('/api/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_team(self):
        response = self.client.get(f'/api/teams/{self.team.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team Marvel')


class ActivityAPITestCase(APITestCase):
    """Tests for the Activity API endpoints"""

    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='tony.stark@marvel.com',
            activity_type='Running',
            duration=30,
            calories_burned=300,
            date=date.today(),
        )

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity(self):
        data = {
            'user_email': 'peter.parker@marvel.com',
            'activity_type': 'Cycling',
            'duration': 45,
            'calories_burned': 400,
            'date': str(date.today()),
        }
        response = self.client.post('/api/activities/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITestCase(APITestCase):
    """Tests for the Leaderboard API endpoints"""

    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='tony.stark@marvel.com',
            username='Iron Man',
            team='Team Marvel',
            total_calories=1500,
            total_activities=5,
            rank=1,
        )

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_leaderboard_entry(self):
        response = self.client.get(f'/api/leaderboard/{self.entry.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'Iron Man')


class WorkoutAPITestCase(APITestCase):
    """Tests for the Workout API endpoints"""

    def setUp(self):
        self.workout = Workout.objects.create(
            name='Morning Run',
            description='30-minute moderate-pace run',
            difficulty='Medium',
            duration=30,
            calories_estimate=300,
            category='Cardio',
        )

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_workout(self):
        data = {
            'name': 'Evening Yoga',
            'description': '45-minute relaxing yoga session',
            'difficulty': 'Easy',
            'duration': 45,
            'calories_estimate': 200,
            'category': 'Flexibility',
        }
        response = self.client.post('/api/workouts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_workout(self):
        response = self.client.get(f'/api/workouts/{self.workout.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Morning Run')


class APIRootTestCase(APITestCase):
    """Tests for the API root endpoint"""

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
