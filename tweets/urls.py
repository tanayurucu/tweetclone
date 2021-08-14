from django.urls import path

from .views import (
    home_view, 
    tweet_action_view,
    tweet_delete_view,
    tweet_detail_view, 
    tweet_list_view,
    tweet_create_view,
)
'''
CLIENT
Base ENDPOINT /api/tweets/
'''
urlpatterns = [
    path('', home_view),
    path('create-tweet', tweet_create_view),
    path('tweets', tweet_list_view),
    path('tweets/<int:tweet_id>', tweet_detail_view),
    path('api/tweets/', tweet_list_view),
    path('api/tweets/action/',tweet_action_view),
     path('api/tweets/create/',tweet_create_view),
        path('api/tweets/<int:tweet_id>/', tweet_detail_view),
    path('api/tweets/<int:tweet_id>/delete/', tweet_delete_view),
]