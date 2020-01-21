from django.utils.translation import get_language


def django_settings(request):

    return {
        "LANGUAGE": get_language(),
    }
