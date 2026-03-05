from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for collection/index ops
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample data
        users = [
            {"name": "Tony Stark", "email": "tony@marvel.com", "team": "Marvel"},
            {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "Marvel"},
            {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "DC"},
            {"name": "Clark Kent", "email": "clark@dc.com", "team": "DC"},
        ]
        teams = [
            {"name": "Marvel", "members": ["tony@marvel.com", "steve@marvel.com"]},
            {"name": "DC", "members": ["bruce@dc.com", "clark@dc.com"]},
        ]
        activities = [
            {"user": "tony@marvel.com", "activity": "Running", "duration": 30},
            {"user": "steve@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "bruce@dc.com", "activity": "Swimming", "duration": 60},
            {"user": "clark@dc.com", "activity": "Flying", "duration": 120},
        ]
        leaderboard = [
            {"user": "tony@marvel.com", "points": 100},
            {"user": "steve@marvel.com", "points": 90},
            {"user": "bruce@dc.com", "points": 110},
            {"user": "clark@dc.com", "points": 120},
        ]
        workouts = [
            {"user": "tony@marvel.com", "workout": "Chest Day", "suggestion": "Bench Press"},
            {"user": "steve@marvel.com", "workout": "Leg Day", "suggestion": "Squats"},
            {"user": "bruce@dc.com", "workout": "Cardio", "suggestion": "Treadmill"},
            {"user": "clark@dc.com", "workout": "Full Body", "suggestion": "Deadlift"},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
