
# from .views import DataDispatcher 

# router = DefaultRouter()
# router.register("", DataDispatcher, basename="event")
# urlpatterns = router.urls

from django.urls import path
from .views import DataDispatcher


urlpatterns = [
    path('', DataDispatcher.as_view(), name='download_books_api'),
]