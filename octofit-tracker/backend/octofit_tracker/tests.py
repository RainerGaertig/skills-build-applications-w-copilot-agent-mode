from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', members=['test@example.com'])
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test@example.com', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='test@example.com', points=100)
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user='test@example.com', workout='Chest Day', suggestion='Bench Press')
        self.assertEqual(workout.workout, 'Chest Day')
