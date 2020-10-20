from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from pipeline.component_framework.library import ComponentLibrary
from django.urls import path
from .DEMO_DATA import *
from api.mongo import Template, Taskflow
from api.utils import Q2D_POST
from pymongo.collection import ObjectId
from pipeline.models import *
import time, json


# Create your views here.

class ComponentAPI(APIView):

    def get(self, request, component_code=None):
        if component_code:
            component = ComponentLibrary.components.get(component_code)
            name = component.name.split('-')
            return Response(
                dict(code=component.code, desc=component.desc, form=component.form, group_icon=component.group_icon,
                     group_name=name[0], name=name[1], output=component.outputs_format(),
                     resource_uri="/api/v3/component/%s/" % component.code))
        components = []
        _components = ComponentLibrary.components
        for _component in _components:
            component = _components[_component]
            name = component.name.split('-')
            components.append(
                dict(code=component.code, desc=component.desc, form=component.form, group_icon=component.group_icon,
                     group_name=name[0], name=name[1], output=component.outputs_format(),
                     resource_uri="/api/v3/component/%s/" % component.code)
            )

        return Response({"objects": components})


class BusinessAPI(APIView):

    def get(self, request):
        return Response(DEMO_BUSINESS)


class BusinessInfoAPI(APIView):
    def get(self, request, business_id=None):
        return Response(DEMO_BUSINESS_INFO)


class TemplateAPI(APIView):

    def get(self, request, template_id=None):
        if template_id:
            return Response(Template().get_one({"_id": ObjectId(template_id)}))

        templates = Template().get_all()
        data = []
        for template in templates:
            data.append({
                "category": "Other",
                "edit_time": "2018-04-23 17:30:48 +0800",
                "create_time": "2018-04-23 17:26:40 +0800",
                "name": template.get("name"),
                "bk_biz_id": "2",
                "creator": "admin",
                "bk_biz_name": "蓝鲸",
                "id": template.get('_id'),
                "editor": "admin"
            })
        return Response({"result": True, "objects": data, "meta": {"total_count": len(templates)}})

    def post(self, request, template_id=None):
        data = Q2D_POST(request)
        if template_id:
            Template().update({"_id": ObjectId(template_id)}, data)
            return Response({"result": True})
        Template(data).save()
        return Response({"result": True})


class VariableAPI(APIView):
    def get(self, request, code=None):
        if code:
            return Response(DEMO_VARIABLE_TYPE.get(code))
        return Response(DEMO_VARIABLE)


class SchemesAPI(APIView):
    def get(self, request):
        return Response(
            {"meta": {"limit": 1000, "next": None, "offset": 0, "previous": None, "total_count": 0}, "objects": []})


class TaskflowAPI(APIView):

    def get(self, request, taskflow_id=None):
        if taskflow_id:
            taskflow = Taskflow().get_one({"_id": ObjectId(taskflow_id)})
            taskflow['id'] = taskflow['_id']
            # pipeline_tree = json.loads(taskflow['pipeline_tree'])
            #
            taskflow['instance_id'] = taskflow['_id']
            taskflow['business'] = {"always_use_executor": True, "cc_company": "", "cc_id": 2, "cc_name": "蓝鲸",
                                    "cc_owner": "",
                                    "executor": "admin", "id": 1, "life_cycle": "2",
                                    "resource_uri": "/o/bk_sops/api/v3/business/2/", "time_zone": "Asia/Shanghai"}
            taskflow['resource_uri'] = "/api/v3/taskflow/%s/" % taskflow['id']
            return Response(taskflow)
        taskflows = Taskflow().get_all()
        data = {"meta": {"limit": 1000, "next": None, "offset": 0, "previous": None, "total_count": len(taskflows)},
                "objects": []}
        for taskflow in taskflows:
            taskflow['instance_id'] = taskflow['_id']
            taskflow['id'] = taskflow['_id']
            data['objects'].append(taskflow)
        return Response(data)

    def post(self, request, taskflow_id=None):
        data = Q2D_POST(request)
        data['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S")
        data['is_deleted'] = False
        data['is_finished'] = False
        data['is_started'] = False
        data['start_time'] = None


        taskflow_id = Taskflow(data).save()[0]

        taskflow = Taskflow().get_one({"_id": ObjectId(taskflow_id)})
        taskflow['id'] = taskflow_id
        taskflow['resource_uri'] = "/api/v3/taskflow/%s/" % taskflow['id']
        taskflow['instance_id'] = taskflow['_id']
        taskflow['business'] = {"always_use_executor": True, "cc_company": "", "cc_id": 2, "cc_name": "蓝鲸",
                                "cc_owner": "",
                                "executor": "admin", "id": 1, "life_cycle": "2",
                                "resource_uri": "/o/bk_sops/api/v3/business/2/", "time_zone": "Asia/Shanghai"}
        return Response(taskflow)


class CommonTemplateAPI(APIView):
    def get(self, request):
        return Response(
            {"meta": {"limit": 1000, "next": None, "offset": 0, "previous": None, "total_count": 0}, "objects": []})


urlpatterns = [
    path('component/', ComponentAPI.as_view()),
    path('component/<slug:component_code>/', ComponentAPI.as_view()),
    path('business/', BusinessAPI.as_view()),
    path('variable/', VariableAPI.as_view()),
    path('variable/<slug:code>/', VariableAPI.as_view()),
    path('get_business_basic_info/', BusinessInfoAPI.as_view()),
    path('template/', TemplateAPI.as_view()),
    path('scheme/', SchemesAPI.as_view()),
    path('taskflow/', TaskflowAPI.as_view()),
    path("common_template/",CommonTemplateAPI.as_view()),
    path('taskflow/<slug:taskflow_id>/', TaskflowAPI.as_view()),
    path('template/<slug:template_id>/', TemplateAPI.as_view()),
    path('get_business_basic_info/<int:business_id>/', BusinessInfoAPI.as_view()),
]
