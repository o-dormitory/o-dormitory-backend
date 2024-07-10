import uuid
from django.http import HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from grocery_store.models import GroceryStore
from grocery_store.serializers import GroceryStoreSerializer
from grocery_store.services.store_services import GroceryStoreService
from utils.serializers import ErrorResponseSerializer


@extend_schema(tags=["Grocery Stores"])
class GroceryStoreView(APIView):

    @extend_schema(responses=GroceryStoreSerializer)
    def get(self, request: HttpRequest) -> Response:
        """Method for getting all grocery stores without products"""
        serializer = GroceryStoreService.get_all_stores()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=GroceryStoreSerializer,
        responses={
            201: GroceryStoreSerializer,
            400: None,
            # TODO: 400: CustomErrorResponseSerializer
        },
    )
    def post(self, request: HttpRequest) -> Response:
        """Method for creating new grocery store"""
        serializer = GroceryStoreService.create_store(**request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Grocery Stores"])
class GroceryStoreDetailView(APIView):

    @extend_schema(
        responses={
            200: GroceryStoreSerializer,
            404: ErrorResponseSerializer
        }
    )
    def get(self, request: HttpRequest, uid: uuid.UUID) -> Response:
        """Method for getting specific grocery store by its uid"""
        try:
            serializer = GroceryStoreService.get_store_by_uid(uid)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except GroceryStore.DoesNotExist:
            error = f"store with uid '{uid}' does not exists"
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        request=GroceryStoreSerializer,
        responses={
            200: GroceryStoreSerializer,
            404: ErrorResponseSerializer
        }
    )
    def patch(self, request: HttpRequest, uid: uuid.UUID) -> Response:
        """Method for updating specific grocery store by its uid"""
        try:
            serializer = GroceryStoreService.update_store_by_uid(
                uid=uid,
                **request.data,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        except GroceryStore.DoesNotExist:
            error = f"store with uid '{uid}' does not exists"
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(responses={204: None, 404: ErrorResponseSerializer})
    def delete(self, request: HttpRequest, uid: uuid.UUID) -> Response:
        """Method for deleting specific grocery store by its uid"""
        try:
            GroceryStoreService.delete_store_by_uid(uid=uid)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GroceryStore.DoesNotExist:
            error = f"store with uid '{uid}' does not exists"
            return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)
