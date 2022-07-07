from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.reverse import reverse

class BaseSerializer(serializers.ModelSerializer):
    pass
    # url = serializers.SerializerMethodField()

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if obj.__class__.__name__ == "employee":
    #         print(".......employee........")
    #         url = reverse('{}-detail'.format(obj.__class__.__name__.lower()), args=[obj.identifier], request=request) 
    #     else:
    #         url = reverse('{}-detail'.format(obj.__class__.__name__.lower()), args=[obj.pk], request=request) 
    #     return url
    