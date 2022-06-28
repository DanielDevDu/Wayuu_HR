from rest_framework.exceptions import APIException


class ResumeNotFound(APIException):
    status_code = 404
    default_detail = "The requested resume does not exist"


class NotYourResume(APIException):
    status_code = 403
    default_detail = "You can't edit a resume that doesn't belong to you"