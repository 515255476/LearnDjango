from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.ProjectsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='project-list'),
    path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destory'
    })),
    path('projects/names/', views.ProjectsViewSet.as_view({
        "get": "names"
    })),
    path('projects/<int:pk>/interfaces/', views.ProjectsViewSet.as_view({
        "get": "interfaces"
    }))
]
