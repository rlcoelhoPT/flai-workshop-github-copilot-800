from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model"""
    list_display = ('username', 'email', 'team', 'created_at')
    search_fields = ('username', 'email', 'team')
    list_filter = ('team',)
    ordering = ('username',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin configuration for Team model"""
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for Activity model"""
    list_display = ('user_email', 'activity_type', 'duration', 'calories_burned', 'date')
    search_fields = ('user_email', 'activity_type')
    list_filter = ('activity_type', 'date')
    ordering = ('-date',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin configuration for Leaderboard model"""
    list_display = ('rank', 'username', 'team', 'total_calories', 'total_activities', 'updated_at')
    search_fields = ('username', 'user_email', 'team')
    list_filter = ('team',)
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin configuration for Workout model"""
    list_display = ('name', 'category', 'difficulty', 'duration', 'calories_estimate')
    search_fields = ('name', 'category', 'difficulty')
    list_filter = ('category', 'difficulty')
    ordering = ('name',)
