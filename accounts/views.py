"""
Controller layer — handles HTTP concerns only.

Responsibilities:
- Parse the request
- Call the service layer
- Translate service results/exceptions into HTTP responses

No business logic lives here.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services import AccountDeletionService, AccountNotFoundError


@api_view(["DELETE"])
def delete_account_view(request, id: int):
    try:
        AccountDeletionService.delete_account(account_id=id)
    except AccountNotFoundError:
        # Return 404 if the account doesn't exist
        return Response(
            {"detail": "Account not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    # 200 OK with a simple confirmation body
    return Response(
        {"detail": f"Account {id} deleted successfully"},
        status=status.HTTP_200_OK,
    )