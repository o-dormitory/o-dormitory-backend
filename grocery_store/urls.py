from django.urls import path

from grocery_store.views import GroceryStoreDetailView, GroceryStoreView


urlpatterns = [
    path("stores/", GroceryStoreView.as_view()),
    path("stores/<uuid:uid>/", GroceryStoreDetailView.as_view()),
]
