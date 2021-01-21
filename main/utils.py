from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    handlers = {
        'Http404': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
        'ParseError': _handle_bad_request_error,
        'ValidationError': _handle_bad_request_error,
        'PermissionDenied': _handle_forbidden_error,
    }
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_bad_request_error(exc, content, response):
    response.data = {
        'error': 'Bad Request. You sent a request that this server could not understand.',
        'status': 400
    }
    return response


def _handle_generic_error(exc, content, response):
    response.data = {
        'error': 'Error 404. Not found.',
        'status': 404
    }
    return response


def _handle_authentication_error(exc, content, response):
    response.data = {
        'error': 'Authorization Required.',
        'status': 401
    }
    return response


def _handle_forbidden_error(exc, content, response):
    response.data = {
        'error': 'Forbidden.',
        'status': 403
    }
    return response
