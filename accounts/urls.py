from django.urls import path
from .views import delete_account_view

urlpatterns = [
    # DELETE /accounts/<id>
    path("<int:id>", delete_account_view, name="delete-account"),
]