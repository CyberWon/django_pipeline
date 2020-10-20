from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path
from pipeline.service import task_service
from pipeline.parser.pipeline_parser import PipelineParser

from api.mongo import Template, Taskflow
from pipeline.engine.models import Status
from api.utils import Q2D_POST
from pymongo.collection import ObjectId
from pipeline.engine import api as pipeline_api
import json


class PreviewTaskTreeAPI(APIView):
    def post(self, request, business_id=None):
        data = Q2D_POST(request)
        template = Template().get_one({"_id": ObjectId(data.get("template_id"))})

        return Response({"result": True, "data": {"constants_not_referred": {},
                                                  "pipeline_tree": json.loads(template.get('pipeline_tree'))}})


class TaskStatusAPI(APIView):

    def get(self, request, taskflow_id=None):
        try:
            status = Status.objects.filter(id=request.GET.get('instance_id')).first()

            if status:
                return Response({"data": {"retry": 0, "finish_time": status.archived_time, "skip": 0,
                                          "start_time": status.started_time, "elapsed_time": 0,
                                          "state": status.state, "children": {}}, "result": True})
            else:
                return Response(
                    {"data": {"retry": 0, "finish_time": None, "skip": 0, "start_time": None, "elapsed_time": 0,
                              "state": "CREATED", "children": {}}, "result": True})
        except Exception as e:
            print(e)
            return Response({"data": {"retry": 0, "finish_time": None, "skip": 0, "start_time": None, "elapsed_time": 0,
                                      "state": "CREATED", "children": {}}, "result": True})


class TaskActionAPI(APIView):
    def get(self, request, action=None, business_id=None):
        return Response()

    def post(self, request, action=None, business_id=None):
        data = Q2D_POST(request)
        taskflow = Taskflow().get_one({"_id": ObjectId(data.get("instance_id"))})
        if action == "start":
            pipeline_data = json.loads(taskflow.get("pipeline_tree"))
            pipeline_data['id'] = taskflow.get('_id')
            pipeline_data['name'] = taskflow.get('name')
            if pipeline_data.get("data") is None:
                pipeline_data['data'] = {
                    "inputs": {},
                    "outputs": {}
                }
            parser_obj = PipelineParser(pipeline_data)
            pipeline = parser_obj.parser()
            act_result = task_service.run_pipeline(pipeline, instance_id=taskflow.get('_id'))

        return Response({"result": True})


class CreateMethodAPI(APIView):
    def get(self, request):
        return Response({"data": [{"name": "\u624b\u52a8", "value": "app"}, {"name": "API\u7f51\u5173", "value": "api"},
                                  {"name": "\u8f7b\u5e94\u7528", "value": "app_maker"},
                                  {"name": "\u5468\u671f\u4efb\u52a1", "value": "periodic"}], "result": True})


urlpatterns = [
    path('preview_task_tree/<slug:business_id>/', PreviewTaskTreeAPI.as_view()),
    path('status/', TaskStatusAPI.as_view()),
    path("get_task_create_method/", CreateMethodAPI.as_view()),
    path('status/<slug:taskflow_id>/', TaskStatusAPI.as_view()),
    path('action/<slug:action>/<slug:business_id>/', TaskActionAPI.as_view()),
]
