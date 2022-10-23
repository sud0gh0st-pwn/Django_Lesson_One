from django.http import HttpResponse


def index(request):
    return HttpResponse("If you see this text the view is working")