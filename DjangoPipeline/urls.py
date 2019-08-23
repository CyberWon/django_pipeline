"""DjangoPipeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http.response import JsonResponse
from pipeline.service import task_service
from pipeline.parser.pipeline_parser import PipelineParser
from pipeline.tests.pipeline_parser.data import NewData


def testTask(request):
    data = NewData().get_data()
    parser_obj = PipelineParser(data)
    pipeline = parser_obj.parser()
    act_result = task_service.run_pipeline(pipeline)
    print(act_result)
    return JsonResponse({},safe=False)


urlpatterns = [
    path('', testTask),
    path('admin/', admin.site.urls),
]
