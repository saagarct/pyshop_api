from rest_framework import serializers
from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

    # def validate_content(self, value):
    #   if len(value)>1000:
    #       raise serializers.ValidationError("This is way too long")

    def validate(self, data):
        content = data.get("content", None)
        if content == "" or content == None:
            raise serializers.ValidationError("No content provided")
        return data
