from rest_framework import serializers
from api.models import Company

#crate serialziers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"