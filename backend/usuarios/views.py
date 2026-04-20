from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.values().get(id=id)
        return JsonResponse(usuario, safe=False)
    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'Usuario nao encontrado'}, status=404)