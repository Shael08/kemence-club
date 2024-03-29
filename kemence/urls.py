# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kemence.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('kemence_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
