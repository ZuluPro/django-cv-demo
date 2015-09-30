from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<resume_id>\d*)/$', 'curriculum.revealjs.views.get_resume', name="reveal-js")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
