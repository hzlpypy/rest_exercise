from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^quick/',include('quickstart.urls')),
    url(r'',include('onestart_rest.urls')),
]
