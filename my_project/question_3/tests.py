# Create your tests here.
from django.test import TestCase
from django.db import transaction
from .models import MyModel

class SignalTransactionTest(TestCase):
    def test_signal_in_transaction(self):
        with transaction.atomic():
            instance = MyModel.objects.create(name="Test")
            self.assertEqual(instance.name, "Updated by Signal")

            # Now rollback the transaction
            transaction.set_rollback(True)
            # Check if the instance name reverts back
            instance.refresh_from_db()
            self.assertEqual(instance.name, "Test")

