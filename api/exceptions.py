from django.http import JsonResponse


def custom_404(request, exception):
    return JsonResponse(
        {
            "status": 404,
            "message": "Not Found"
        },
        status=404,
        json_dumps_params={'separators': (',', ':')}
    )
