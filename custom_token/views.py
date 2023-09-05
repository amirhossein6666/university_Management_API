from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import AdminCustomToken, StudentCustomToken, ProfessorCustomToken
from .serializers import adminTokenSerializers, professorTokenSerializers , studentTokenSerializers
from rest_framework.response import Response
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def adminTokenList(request):
    adminTokens = AdminCustomToken.objects.all()
    serializedAdminTokens = adminTokenSerializers(adminTokens, many=True)
    return Response(serializedAdminTokens.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def professorTokenList(request):
    professorTokens = ProfessorCustomToken.objects.all()
    serializedProfessorTokens = professorTokenSerializers(professorTokens, many=True)
    return Response(serializedProfessorTokens.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def studentTokenList(request):
    studenstTokens = StudentCustomToken.objects.all()
    serializedStudentTokens = studentTokenSerializers(studenstTokens, many=True)
    return Response(serializedStudentTokens.data)