from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from account.api.serializers import UserSerializer , RegistrationSerializer,UserLoginSerializer,ChangePasswordSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth import  get_user_model
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



User = get_user_model()

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request,user)
        user_serializer = UserLoginSerializer(user)
        return Response(user_serializer.data,)



# class Register(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'footer.html'

#     def get(self, request, pk):
#         profile = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(profile)
#         return Response({'serializer': serializer, 'profile': profile})

#     def post(self, request, pk):
#         profile = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(profile, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'profile': profile})
#         serializer.save()
#         return redirect('index.html')



@api_view(['POST','GET'])
def registration_view(request):
    print("sfsfsfsfs")
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'footer.html'
    if request.method == 'GET':
        serializer = RegistrationSerializer()
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Succesfully registered'
            data['email'] = user.email
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['username'] = user.username
            data['bio'] = user.bio
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




class ChangePasswordView(APIView):
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)