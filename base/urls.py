from django.urls import path, include
from .views import authView, home
from django.conf import settings
from django.conf.urls.static import static
from .views import inbox
from .views import send_message

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),   
    path('registrations/signup.html', authView,name='signup'),
    path('inbox/', inbox, name='inbox'),
    path('send-message/', send_message, name='send_message'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)