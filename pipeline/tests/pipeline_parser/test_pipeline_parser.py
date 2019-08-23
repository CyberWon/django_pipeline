
from pipeline.parser.pipeline_parser import PipelineParser
from pipeline.core.pipeline import Pipeline
from pipeline.tests.pipeline_parser.data import (
    PIPELINE_DATA,
    PIPELINE_WITH_SUB_PROCESS,
    CONDITIONAL_PARALLEL,
)
from pipeline.component_framework.component import Component
from pipeline.core.flow.activity import Service
from pipeline.service import task_service


class TestService(Service):
    def execute(self, data, parent_data):
        print(data, parent_data)
        return True

    def outputs_format(self):
        return []


class TestComponent(Component):
    name = 'test'
    code = 'test'
    bound_service = TestService
    form = 'test.js'


if __name__ == "__main__":
    parser_obj = PipelineParser(PIPELINE_DATA)
    pipeline = parser_obj.parser()
    act_result = task_service.run_pipeline(pipeline)
    print(pipeline)
