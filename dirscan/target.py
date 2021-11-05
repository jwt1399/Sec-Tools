from django.shortcuts import HttpResponse


def get_target(request):
    try:
        file = open('reports/target.json', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="target.json"'
    except:
        response = HttpResponse("对不起，文件未生成")

    return response
