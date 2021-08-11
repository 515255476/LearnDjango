import json

from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins
from projects.models import Projects
from projects.serializer import ProjectSerializer, ProjectModelSerializer, ProjectNameSerializer, \
    InterfacesByProjectIdSerializer
from rest_framework import generics


#
#
# class IndexView(View):
#     def get(self, request, pk):
#         pr_name = "项目" + str(pk)
#         # Projects.objects.create(project_name=pr_name, leader="领导-1")
#         # print(Projects.objects.all())
#
#         ps=Projects.objects.filter(person__age=1)
#         ps.filter(project_name='姓名2')
#         pass
#
#     def post(self, request):
#         print(request)
#         return HttpResponse(" post请求，hello world")
#
#     def delete(self, request):
#         return HttpResponse(" delete请求，hello world")
class ProjectList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    ordering_fields = ["id"]

    def get(self, request, *args, **kwargs):
        # project_list = []
        # for project in project_qs:
        #     one_dict = {
        #         "name": project.project_name,
        #         "leader": project.leader,
        #         "tester": project.tester,
        #         "developer": project.developer,
        #     }
        #     project_list.append(one_dict)

        # project_qs = self.get_queryset()
        # project_qs = self.filter_queryset(project_qs)
        # page = self.paginate_queryset(project_qs)  # 分页输出
        # if page is not None:
        #     serializer = self.get_serializer(instance=project_qs, many=True)
        #     return self.get_paginated_response(serializer.data)
        # serializer = self.get_serializer(instance=project_qs, many=True)
        # return Response(serializer.data)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # json_data = request.body.decode('utf-8')
        # python_data = json.loads(json_data, encoding="utf-8")

        # one_dict = {
        #     "name": project.project_name,
        #     "leader": project.leader,
        #     "tester": project.tester,
        #     "developer": project.developer,
        # }

        #
        # serializer = ProjectSerializer(data=python_data)
        # try:
        #     serializer.is_valid(raise_exception=True)
        # except Exception as e:
        #     return JsonResponse(serializer.errors)
        # # project = Projects.objects.create(**serializer.validated_data)
        # project = serializer.save()
        # serializer = ProjectSerializer(instance=project)
        # return JsonResponse(serializer.data, status=201)
        return self.create(request, *args, **kwargs)


class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    # lookup_field = 'id'
    #
    # def get_object(self, pk):
    #     try:
    #         return Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         raise Http404

    def get(self, request, *args, **kwargs):
        # project = self.get_object(pk)
        # # one_dict = {
        # #     "name": project.project_name,
        # #     "leader": project.leader,
        # #     "tester": project.tester,
        # #     "developer": project.developer,
        # # }
        # serializer = self.get_serializer(instance=project)
        # return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # project = self.get_object(pk)
        # json_data = request.body.decode('utf-8')
        # python_data = json.loads(json_data, encoding='utf-8')
        # serializer = self.get_serializer(data=python_data, instance=project)
        #
        # # serializer = ProjectSerializer(data=python_data, instance=project)
        # # project.project_name = python_data["project_name"]
        # # project.leader = python_data["leader"]
        # # project.tester = python_data["tester"]
        # # project.developer = python_data["developer"]
        # # project.save()
        # # one_dict = {
        # #     "name": project.project_name,
        # #     "leader": project.leader,
        # #     "tester": project.tester,
        # #     "developer": project.developer,
        # # }
        # try:
        #     serializer.is_valid(raise_exception=True)
        # except Exception as e:
        #     return JsonResponse(serializer.errors)
        # serializer.save()
        # return JsonResponse(serializer.data)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # try:
        #     project = self.get_object()
        #     project.delete()
        # except Projects.DoesNotExist:
        #     raise Http404
        #
        # return JsonResponse(None, status=204)
        return self.destroy(request, *args, **kwargs)


from rest_framework import viewsets


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    ordering_fields = ["id"]

    @action(methods=['get'], detail=False)
    def names(self, request):
        queryset = self.get_queryset()
        serializer = ProjectNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def interface(self, request):
        instance = self.get_object()
        serializer = InterfacesByProjectIdSerializer(instance=instance)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
