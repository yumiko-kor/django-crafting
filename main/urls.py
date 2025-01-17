from django.urls import path
from main.views import index, board, posting, post, remove

# img
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('board/', board, name='board'),
    path('board/<int:pk>', posting, name='posting'),
    path('board/post/', post, name='post'),
    path('board/<int:pk>/remove/', remove, name='remove'),
]

# img urls 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)