from django.http import HttpResponse, JsonResponse


def ping(request):
    """
    Parameters
    ----------
    request : HttpRequest
        Description of param1 (request)

    Returns
    -------
    HttpResponse
        Description of return value
    """
    return HttpResponse("pong")


def create_user(request, user_data: dict):
    """
    Parameters
    ----------
    request : HttpRequest
        Description of param1 (request)
    user_data : dict
        Description of param2 (user_data) (may contain 'username', 'password' and 'email')

    Returns
    -------
    JsonResponse
        Returns User data in JSON format
    """
    return JsonResponse({"user": "user_data"})


def create_user2(request, user_data: dict):
    """
    Essa funcao realiza a acao ABCDEFG

    :param request: HttpRequest
    :param user_data: dict
    :return: JsonResponse
    """
    return JsonResponse({"user": "user_data"})
