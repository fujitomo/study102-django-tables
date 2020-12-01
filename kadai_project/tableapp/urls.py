from django.urls import path
from django.conf import settings
from .views import CharactorCreaterView, CharactorListView, CharactorUpdateView
from django.conf.urls.static import static


urlpatterns = [
    path('create/', CharactorCreaterView.as_view(), name='create'),
    path('list/', CharactorListView.as_view(), name='list'),
    path('update/<int:pk>', CharactorUpdateView.as_view(), name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
