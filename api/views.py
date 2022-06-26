from rest_framework.response import Response
from api.models import Profile
from api.serializers import ProfielSerializer
from rest_framework.views import APIView
from rest_framework import status


class ProfileView(APIView):
    def post(self, request, format = None):
        serializer = ProfielSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg' : 'Resume Uploaded Successfully',
                'status' : 'success', 
                'candidate' : serializer.data,
            }, status=status.HTTP_201_CREATED)


    def get(self, request, format = None):
        candidates = Profile.objects.all()
        serializer = ProfielSerializer(candidates, many = True)
        return Response({
            'status' : 'success', 'candidate' : serializer.data
        }, status= status.HTTP_200_OK)

    