from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from projects import views

router = routers.SimpleRouter()
router.register(r'projects', views.ProjectsViewSet)

urlpatterns = [
    # path('projects/', views.ProjectsViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }), name='project-list'),
    # path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destory'
    # })),
    # path('projects/names/', views.ProjectsViewSet.as_view({
    #     "get": "names"
    # })),
    # path('projects/<int:pk>/interfaces/', views.ProjectsViewSet.as_view({
    #     "get": "interfaces"
    # })),
    path('', include(router.urls)),
    path('docs/',include_docs_urls(title="测试平台接口文档"))

]
