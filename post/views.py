from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q
from post.serializers import JobPostSerializer


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = int( request.data.get("job_type", None) )
        company_name = request.data.get("company_name", None)

        return Response(status=status.HTTP_200_OK)


class JobPostView(APIView):
    
    def get(self, request):
        skills = request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)
        
        JobPostSkillSet.objects.filter(Q(name=skills[0]) | Q(name=skills[1]))
        return Response(status=status.HTTP_200_OK)    
    def post(self, request):
        job_post_serializer = JobPostSerializer(data=request.data)
        if job_post_serializer.is_valid():
            job_post_serializer.save
            return Response(job_post_serializer.data, status=status.HTTP_200_OK)
