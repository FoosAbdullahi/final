from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProjectsSerializers
from .models import Projects


# Create your views here.
@api_view(['GET'])
def getAll(request):
    project=Projects.objects.all()
    serializers=ProjectsSerializers(project,many=True)
    return Response(serializers.data)
