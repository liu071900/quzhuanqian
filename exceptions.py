from tornado.web import HTTPError


# http error code

class ResultCode:
    """
        http 状态为200的状态码，这里代表 错误分类，具体错误还可以在程序中细分
        如 {"code":'3.1',"message":"手机号格式不正确"}，代表 注册类错误，具体原因是手机号格式不正确
        错误分类后面的小数，代表为 具体的业务逻辑的 第几步出现错误
    """
    # 成功
    SUCCESS = "0"
    # 普通错误
    ERROR = "1"
    # 注册类错误
    SIG_IN_ERROR = "2"
    # 登陆类错误
    LOGIN_ERROR = "3"

    @staticmethod
    def join_code(pre_code: str, detail_code: str = None) ->str:
        if detail_code:
            return pre_code + "." + detail_code
        else:
            return pre_code

