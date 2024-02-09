from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import VerificationSerializer
from .utils import extract_text_from_image
from django.conf import settings


class VerifyUserAPIView(APIView):
    @extend_schema(
        request=VerificationSerializer, responses={200: VerificationSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data["user_id"]
            id_card_image = serializer.validated_data["id_card_image"]

            # Process the image and extract text using OCR
            extracted_text = extract_text_from_image(id_card_image)
            print(extracted_text)

            # Implement verification logic based on the extracted text and user_id
            if any(text in extracted_text for text in user_id):
                print("ID Found")
                return Response(
                    {"user_id": user_id, "status": "verified"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"user_id": user_id, "status": "not verified"},
                    status=status.HTTP_200_OK,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
