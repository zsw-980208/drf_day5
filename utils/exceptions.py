from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status


def exception_handler(exc, context):
    # 详细错误信息的定义
    error = "%s %s %s" % (context['view'], context['request'].method, exc)
    print(error)
    response = drf_exception_handler(exc, context)
    if response is None:
        return Response(
            {"error_msg": "程序内部错误，请稍等一会儿~"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=None)
        # return Response({"error_msg": error})

    return response
