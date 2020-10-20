(function(){
    $.atoms.ssh_ansible = [
        {
            tag_code: "test_input",
            type: "input",
            attrs: {
                name: gettext("参数1"),
                placeholder: gettext("请输入字符串"),
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "test_textarea",
            type: "textarea",
            attrs: {
                name: gettext("参数2"),
                placeholder: gettext("多个使用换行分隔"),
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "test_radio",
            type: "radio",
            attrs: {
                name: gettext("参数3"),
                items: [
                    {value: "1", name: gettext("选项1")},
                    {value: "2", name: gettext("选项2")},
                    {value: "3", name: gettext("选项3")}
                ],
                default: "1",
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        }
    ]
})();
