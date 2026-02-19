from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League Champions'
        )
        
        # Create Marvel Users
        self.stdout.write('Creating Marvel users...')
        marvel_users = [
            {'username': 'Iron Man', 'email': 'tony.stark@marvel.com', 'password': 'stark123'},
            {'username': 'Captain America', 'email': 'steve.rogers@marvel.com', 'password': 'rogers123'},
            {'username': 'Thor', 'email': 'thor.odinson@marvel.com', 'password': 'thunder123'},
            {'username': 'Black Widow', 'email': 'natasha.romanoff@marvel.com', 'password': 'widow123'},
            {'username': 'Hulk', 'email': 'bruce.banner@marvel.com', 'password': 'smash123'},
            {'username': 'Spider-Man', 'email': 'peter.parker@marvel.com', 'password': 'spidey123'},
        ]
        
        for user_data in marvel_users:
            User.objects.create(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                team='Team Marvel'
            )
        
        # Create DC Users
        self.stdout.write('Creating DC users...')
        dc_users = [
            {'username': 'Superman', 'email': 'clark.kent@dc.com', 'password': 'krypton123'},
            {'username': 'Batman', 'email': 'bruce.wayne@dc.com', 'password': 'gotham123'},
            {'username': 'Wonder Woman', 'email': 'diana.prince@dc.com', 'password': 'amazon123'},
            {'username': 'The Flash', 'email': 'barry.allen@dc.com', 'password': 'speed123'},
            {'username': 'Aquaman', 'email': 'arthur.curry@dc.com', 'password': 'atlantis123'},
            {'username': 'Green Lantern', 'email': 'hal.jordan@dc.com', 'password': 'willpower123'},
        ]
        
        for user_data in dc_users:
            User.objects.create(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                team='Team DC'
            )
        
        # Get all users for activities
        all_users = list(User.objects.all())
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'CrossFit']
        
        for user in all_users:
            # Create 5-10 random activities for each user
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = duration * random.randint(5, 12)
                days_ago = random.randint(0, 30)
                activity_date = datetime.now().date() - timedelta(days=days_ago)
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=duration,
                    calories_burned=calories,
                    date=activity_date
                )
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard...')
        for user in all_users:
            user_activities = Activity.objects.filter(user_email=user.email)
            total_calories = sum(activity.calories_burned for activity in user_activities)
            total_activities = user_activities.count()
            
            Leaderboard.objects.create(
                user_email=user.email,
                username=user.username,
                team=user.team,
                total_calories=total_calories,
                total_activities=total_activities
            )
        
        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity military-style workout combining strength and endurance',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_estimate': 500,
                'category': 'Strength'
            },
            {
                'name': 'Speedster Sprint Circuit',
                'description': 'Fast-paced cardio workout to build speed and agility',
                'difficulty': 'Intermediate',
                'duration': 30,
                'calories_estimate': 350,
                'category': 'Cardio'
            },
            {
                'name': 'Amazonian Warrior Flow',
                'description': 'Combat-inspired yoga for flexibility and mental focus',
                'difficulty': 'Beginner',
                'duration': 45,
                'calories_estimate': 200,
                'category': 'Flexibility'
            },
            {
                'name': 'Hulk Power Lifting',
                'description': 'Heavy weightlifting program for maximum strength gains',
                'difficulty': 'Advanced',
                'duration': 90,
                'calories_estimate': 600,
                'category': 'Strength'
            },
            {
                'name': 'Web-Slinger Agility',
                'description': 'Bodyweight exercises focusing on agility and coordination',
                'difficulty': 'Intermediate',
                'duration': 40,
                'calories_estimate': 300,
                'category': 'Agility'
            },
            {
                'name': 'Atlantean Swim Session',
                'description': 'Full-body swimming workout for endurance',
                'difficulty': 'Intermediate',
                'duration': 60,
                'calories_estimate': 450,
                'category': 'Cardio'
            },
            {
                'name': 'Bat HIIT Training',
                'description': 'High-intensity interval training for peak performance',
                'difficulty': 'Advanced',
                'duration': 35,
                'calories_estimate': 400,
                'category': 'HIIT'
            },
            {
                'name': 'Kryptonian Core Blast',
                'description': 'Core-focused workout to build superhuman abs',
                'difficulty': 'Beginner',
                'duration': 25,
                'calories_estimate': 180,
                'category': 'Core'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams created: {Team.objects.count()}')
        self.stdout.write(f'Users created: {User.objects.count()}')
        self.stdout.write(f'Activities created: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('Database successfully populated with superhero test data!'))
