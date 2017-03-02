from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    url(r'^$', 'todolist.views.home', name='home'),
    url(r'^contact/$', 'todolist.views.contact', name='contact'),
    url(r'^profile/$', 'todolist.views.profile', name='profile'),
    url(r'^about/$', 'todolist.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)