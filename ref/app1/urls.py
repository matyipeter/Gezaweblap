from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "app1"

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("services/", views.ServicesView.as_view(), name='services'),
    path("bemutatkozas/", views.Bemutakozas.as_view(), name="bemutatkozas"),
    path("referencia/", views.ReferenceView.as_view(), name="reference"),
    path("contact/", views.ContactView.as_view(), name="kapcsolat"),
    path("thanks/", views.Thanks.as_view(), name='thanks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
