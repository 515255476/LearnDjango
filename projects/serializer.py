from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Projects


def is_unique_project_name(name):
    if "项目" not in name:
        raise serializers.ValidationError("项目名称中必须包含项目")


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="ID", read_only=True)
    project_name = serializers.CharField(label="项目名称", max_length=200, help_text="项目名称", write_only=True,
                                         validators=[
                                             UniqueValidator(queryset=Projects.objects.all(), message="项目名不能重复"),
                                             is_unique_project_name])
    leader = serializers.CharField(label="ID", max_length=50, help_text="项目领导")
    tester = serializers.CharField(label="ID", max_length=50, help_text="测试人员")
    developer = serializers.CharField(label="ID", max_length=50, help_text="开发人员")
    app = serializers.CharField(label="ID", max_length=50, help_text="发布应用", allow_null=True, allow_blank=True)

    def validate_project_name(self, value):
        if not value.endswith("项目"):
            raise serializers.ValidationError("项目必须以”项目结尾")
        return value

    # 多字段联合校验
    def validate(self, attrs):
        if "wangyang" not in attrs["tester"] and "pinjie" not in attrs["leader"]:
            raise serializers.ValidationError("wangyang 必须为测试人员，品姐必须为项目负责人")
        return attrs

    def create(self, validate_data):
        project = Projects.objects.create(**validate_data)
        return project

    def update(self, instance, validated_data):
        instance.project_name = validated_data["project_name"]
        instance.leader = validated_data["leader"]
        instance.tester = validated_data["tester"]
        instance.developer = validated_data["developer"]
        instance.save()
        return instance


class ProjectModelSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(label="项目名称", max_length=200, help_text="项目名称",
                                         validators=[
                                             UniqueValidator(queryset=Projects.objects.all(), message="项目名不能重复"),
                                             is_unique_project_name])

    class Meta:
        model = Projects
        fields = "__all__"
        read_only_fields = ("id", "app")
        extra_kwargs = {
            "leader": {
                "write_only": True,
                "error_messages": {
                    "max_length": "最大长度不超过50字节"
                }
            }
        }


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'project_name')


class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
    interfaces_set=Int