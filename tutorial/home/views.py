

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author
from .serializers import Authorserializer
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
# Create your views here.

@api_view(['POST'])
def home(request):
    serializer=Authorserializer(data=request.data)
    if( serializer.is_valid()):
        serializer.save()
        return  Response({
            'status':'400',
            'Message' :' The following data was added successfully!!',
            'data' : serializer.data
        })
    else:
        return Response({
            'status':'400',
            'Message' :' Data add was unsuccessful',
            'data' : serializer.data
        })
    


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class HandleView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,author):
        if request.method=='GET':
            pp=Author.objects.filter(author=author)
            serializer=Authorserializer(pp,many=True)
            return  Response({
                'status':'400',
                'Message' :' The following data was getted from database',
                'data'  : serializer.data
            })
