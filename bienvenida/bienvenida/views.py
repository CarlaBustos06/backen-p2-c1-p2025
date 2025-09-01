from django.http import HttpResponse


def inicio(request):
    nombre = "Carla Bustos"
    return HttpResponse(f"Bienvenidos a mi primera app Django, {nombre}!")

   
