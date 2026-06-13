"""
Service layer — pure business logic.

This layer has NO dependency on Django REST Framework, HTTP requests,
or responses. It could be reused in a CLI, a Celery task, or a
different web framework entirely. The controller (view) is just a
thin adapter that calls this layer.
"""

import logging
from .models import Account

logger = logging.getLogger(__name__)


class AccountNotFoundError(Exception):
    """Raised when the account does not exist."""
    pass


class AccountDeletionService:
    """Encapsulates the rules for deleting an account."""

    @staticmethod
    def delete_account(account_id: int) -> None:
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            raise AccountNotFoundError(f"Account ID {account_id} not found")

        # Perform the deletion (could later add soft-delete, audits, etc.)
        account.delete()

        # Required log pattern — matches: "Account ID {id} {action} {message}"
        logger.info(f"Account ID {account_id} deleted permanently")