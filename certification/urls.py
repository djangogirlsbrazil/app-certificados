from django.conf.urls import include, url
from django.contrib import admin

from attendees_certification import urls as attendees_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'certification.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^attendees/', include(attendees_urls)),
]
