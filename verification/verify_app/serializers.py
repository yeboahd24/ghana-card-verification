from rest_framework import serializers


class VerificationSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=20)
    id_card_image = serializers.ImageField()
