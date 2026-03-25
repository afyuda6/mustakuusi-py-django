from django.urls import path, include
from django.http import HttpResponse

def robots_txt(request):
    content = "User-agent: *\nDisallow:"
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [
    path('', include('api.urls')),
    path('robots.txt', robots_txt),
]

handler404 = 'api.exceptions.custom_404'
