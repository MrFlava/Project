from django.http import JsonResponse


def custom400(request, exception):
    return JsonResponse({
        'status_code': 400,
        'error': 'Bad Request. You sent a request that this server could not understand.'
    })


def custom401(request, exception):
    return JsonResponse({
        'status_code': 401,
        'error': 'Authorization Required.'
    })


def custom403(request, exception):
    return JsonResponse({
        'status_code': 403,
        'error': 'Forbidden.'
    })


def custom404(request, exception):
    return JsonResponse({
        'error': 'The resource was not found',
        'status_code': 404
    })


