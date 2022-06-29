from rest_framework.exceptions import APIException


class ResumeNotFound(APIException):
    status_code = 404
    default_detail = "The requested resume does not exist"


class NotYourResume(APIException):
    status_code = 403
    default_detail = "You can't edit a resume that doesn't belong to you"

class ErrorLogin(APIException):
    status_code = 401
    default_detail = "authentication has failed"

class ErrorPassword(APIException):
    status_code = 401
    default_detail = "password has failed"