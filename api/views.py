from django.http import HttpResponse


def vendedores(request):
    return HttpResponse("OK")


def sellers(request):
    return HttpResponse("OK")


def comissions(request):
    return HttpResponse("OK")


def check_commision(request):
    return HttpResponse("OK")
