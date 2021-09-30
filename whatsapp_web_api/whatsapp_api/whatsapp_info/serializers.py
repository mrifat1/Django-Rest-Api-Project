from rest_framework import serializers
from .models import WhatsappInfo

class info_serializers(serializers.ModelSerializer):
    class Meta:
        model = WhatsappInfo
        fields = '__all__'