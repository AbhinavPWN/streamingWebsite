from django.urls import re_path

from video.consumers import VideoConsumer

websocket_urlpatterns = [
    re_path(r'ws/video/(?P<video_id>\d+)/$', VideoConsumer.as_asgi()),
]