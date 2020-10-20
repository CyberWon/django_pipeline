DEMO_BUSINESS = {"meta": {"limit": 1000, "next": None, "offset": 0, "previous": None, "total_count": 1}, "objects": [
    {"always_use_executor": False, "cc_company": "", "cc_id": 2, "cc_name": "蓝鲸", "cc_owner": "", "executor": "",
     "id": 1, "life_cycle": "2", "resource_uri": "/o/bk_sops/api/v3/business/2/", "time_zone": "Asia/Shanghai"}]}

DEMO_COMPONENTS = {'job_fast_push_file': {"code": "job_fast_push_file", "desc": "",
                                          "form": "http://127.0.0.1:8000/static/components/atoms/job/job_fast_push_file.js",
                                          "group_icon": "http://127.0.0.1:8000/static/components/icons/job.png",
                                          "group_name": "作业平台(JOB)", "name": "快速分发文件",
                                          "output": [{"key": "job_inst_id", "name": "JOB任务ID", "type": "int"},
                                                     {"key": "job_inst_url", "name": "JOB任务链接", "type": "str"},
                                                     {"key": "_result", "name": "执行结果", "type": "bool"}],
                                          "resource_uri": "/o/bk_sops/api/v3/component/job_fast_push_file/"},
                   'bk_http_request': {"code": "bk_http_request",
                                       "desc": "提示: 1.请求URL需要在当前网络下可以访问，否则会超时失败 2.响应状态码在200-300(不包括300)之间，并且相应内容是 JSON 格式才会执行成功提示: 1.请求URL需要在当前网络下可以访问，否则会超时失败 2.响应状态码在200-300(不包括300)之间，并且相应内容是 JSON 格式才会执行成功",
                                       "form": "http://127.0.0.1:8000/static/components/atoms/bk/http.js",
                                       "group_icon": "", "group_name": "蓝鲸服务(BK)",
                                       "name": "HTTP 请求", "output": [
                           {"key": "data", "name": "响应内容", "type": "str"},
                           {"key": "status_code", "name": "状态码", "type": "int"}]}}

DEMO_BUSINESS_INFO = {
    "flow_type_list": [{"name": "\u9ed8\u8ba4\u4efb\u52a1\u6d41\u7a0b", "value": "common"},
                       {"name": "\u804c\u80fd\u5316\u4efb\u52a1\u6d41\u7a0b",
                        "value": "common_func"}],
    "notify_group": [{"text": "\u8fd0\u7ef4\u4eba\u5458", "value": "Maintainers"},
                     {"text": "\u4ea7\u54c1\u4eba\u5458", "value": "ProductPm"},
                     {"text": "\u5f00\u53d1\u4eba\u5458", "value": "Developer"},
                     {"text": "\u6d4b\u8bd5\u4eba\u5458", "value": "Tester"}],
    "task_categories": [{"name": "\u8fd0\u7ef4\u5de5\u5177", "value": "OpsTools"},
                        {"name": "\u76d1\u63a7\u544a\u8b66", "value": "MonitorAlarm"},
                        {"name": "\u914d\u7f6e\u7ba1\u7406", "value": "ConfManage"},
                        {"name": "\u5f00\u53d1\u5de5\u5177", "value": "DevTools"},
                        {"name": "\u4f01\u4e1aIT", "value": "EnterpriseIT"},
                        {"name": "\u529e\u516c\u5e94\u7528", "value": "OfficeApp"},
                        {"name": "\u5176\u5b83", "value": "Other"}],
    "notify_type_list": [{"name": "\u5fae\u4fe1", "value": "weixin"},
                         {"name": "\u77ed\u4fe1", "value": "sms"},
                         {"name": "\u90ae\u4ef6", "value": "email"},
                         {"name": "\u8bed\u97f3", "value": "voice"}]}

DEMO_VARIABLE = {"meta": {"limit": 1000, "next": None, "offset": 0, "previous": None, "total_count": 8}, "objects": [
    {"code": "input", "form": "/static/variables/input.js", "meta_tag": None, "name": "输入框",
     "resource_uri": "/api/v3/variable/input/", "tag": "input.input", "type": "general"},
    {"code": "textarea", "form": "/static/variables/textarea.js", "meta_tag": None, "name": "文本框",
     "resource_uri": "/api/v3/variable/textarea/", "tag": "textarea.textarea", "type": "general"},
    {"code": "datetime", "form": "/static/variables/datetime.js", "meta_tag": None, "name": "日期时间",
     "resource_uri": "/api/v3/variable/datetime/", "tag": "datetime.datetime", "type": "general"},
    {"code": "int", "form": "/static/variables/int.js", "meta_tag": None, "name": "整数",
     "resource_uri": "/api/v3/variable/int/", "tag": "int.int", "type": "general"},
    {"code": "password", "form": "/static/variables/password.js", "meta_tag": None, "name": "密码",
     "resource_uri": "/api/v3/variable/password/", "tag": "password.password", "type": "general"},
    {"code": "select", "form": "/static/variables/select.js", "meta_tag": "select.select_meta", "name": "下拉框",
     "resource_uri": "/api/v3/variable/select/", "tag": "select.select", "type": "meta"},
    {"code": "ip", "form": "/static/variables/sites/open/var_ip_picker.js", "meta_tag": None, "name": "IP选择器(简单版)",
     "resource_uri": "/api/v3/variable/ip/", "tag": "var_ip_picker.ip_picker", "type": "general"},
    {"code": "ip_selector", "form": "/static/variables/sites/open/var_cmdb_ip_selector.js", "meta_tag": None,
     "name": "IP选择器", "resource_uri": "/api/v3/variable/ip_selector/", "tag": "var_cmdb_ip_selector.ip_selector",
     "type": "general"}]}

DEMO_VARIABLE_TYPE = {"input": {"code": "input", "form": "/static/variables/input.js", "meta_tag": None, "name": "输入框",
                                "resource_uri": "/api/v3/variable/input/", "tag": "input.input", "type": "general"},
                      "textarea": {"code": "textarea", "form": "/static/variables/textarea.js", "meta_tag": None,
                                   "name": "文本框",
                                   "resource_uri": "/api/v3/variable/textarea/", "tag": "textarea.textarea",
                                   "type": "general"},
                      "datetime": {"code": "datetime", "form": "/static/variables/datetime.js", "meta_tag": None,
                                   "name": "日期时间",
                                   "resource_uri": "/api/v3/variable/datetime/", "tag": "datetime.datetime",
                                   "type": "general"},
                      "int": {"code": "int", "form": "/static/variables/int.js", "meta_tag": None, "name": "整数",
                              "resource_uri": "/api/v3/variable/int/", "tag": "int.int", "type": "general"},
                      "password": {"code": "password", "form": "/static/variables/password.js", "meta_tag": None,
                                   "name": "密码",
                                   "resource_uri": "/api/v3/variable/password/", "tag": "password.password",
                                   "type": "general"},
                      "select": {"code": "select", "form": "/static/variables/select.js",
                                 "meta_tag": "select.select_meta", "name": "下拉框",
                                 "resource_uri": "/api/v3/variable/select/", "tag": "select.select", "type": "meta"},
                      "ip_selector": {"code": "ip_selector",
                                      "form": "/static/variables/sites/open/var_cmdb_ip_selector.js", "meta_tag": None,
                                      "name": "IP选择器", "resource_uri": "/api/v3/variable/ip_selector/",
                                      "tag": "var_cmdb_ip_selector.ip_selector",
                                      "type": "general"},
                      "ip": {"code": "ip", "form": "/static/variables/sites/open/var_ip_picker.js", "meta_tag": None,
                             "name": "IP选择器(简单版)",
                             "resource_uri": "/api/v3/variable/ip/", "tag": "var_ip_picker.ip_picker",
                             "type": "general"}}