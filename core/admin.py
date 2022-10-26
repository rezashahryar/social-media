from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id_user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']


@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ['username', 'post_id']


@admin.register(FollowersCount)
class FollowersCount(admin.ModelAdmin):
    list_display = ['follower']
