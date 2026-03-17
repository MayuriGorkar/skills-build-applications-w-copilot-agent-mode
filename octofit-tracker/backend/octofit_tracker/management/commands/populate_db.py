from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team='dc', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Add users to teams
        marvel.members.add(users[0], users[1])
        dc.members.add(users[2], users[3])

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=date(2023, 1, 1))
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=date(2023, 1, 2))
        Activity.objects.create(user=users[2], type='swim', duration=60, date=date(2023, 1, 3))
        Activity.objects.create(user=users[3], type='yoga', duration=20, date=date(2023, 1, 4))

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        # Create Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
