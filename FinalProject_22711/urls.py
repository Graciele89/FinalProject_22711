from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView
from carpool import urls as carpool_urls
from django.conf.urls.static import static
from feedback import urls as feedback_urls

# Django will look top to bottom for url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('feedback/', include('feedback.urls')),
    path('', include(carpool_urls, namespace='carpool')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# The include() function allows referencing other URLconfs.
# Whenever Django encounters include(), it chops off whatever part of the URL matched up to
# that point and sends the remaining string to the included URLconf for further processing.
# The idea behind include() is to make it easy to plug-and-play URLs.
# Since polls are in their own URLconf (polls/urls.py),
# they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”,
# or any other path root, and the app will still work.
# from: https://docs.djangoproject.com/en/4.1/intro/tutorial01/