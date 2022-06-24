from rest_framework import serializers
from post.models import Company, JobPost, JobPostSkillSet, JobType


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
        
        
class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'
        
    def validate(self, data):
        job_type = JobType.objects.get(id=data.get("job_type"))
        if not job_type:
            raise serializers.ValidationError(
                    detail={"error": "유효한 근무 형태가 아닙니다."},
                )
        return data
        
        
class JobPostSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSet
        fields = '__all__'
        
       
