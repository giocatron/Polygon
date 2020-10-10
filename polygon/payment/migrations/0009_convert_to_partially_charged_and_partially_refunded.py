# Generated by Django 2.1.4 on 2019-02-15 08:46

from django.db import migrations

from polygon.payment import ChargeStatus, TransactionKind

CHARGED = "charged"


def is_fully_charged(payment):
    if payment.total - payment.captured_amount > 0:
        return False
    return True


def convert_charged_to_paritally_charged_and_partially_refunded(apps, schema_editor):
    PaymentModel = apps.get_model("payment", "Payment")
    for payment in PaymentModel.objects.all():
        if payment.charge_status == CHARGED:
            if is_fully_charged(payment):
                payment.charge_status = ChargeStatus.FULLY_CHARGED
            elif (
                payment.transactions.filter(
                    kind=TransactionKind.REFUND, is_success=True
                ).first()
                is not None
            ):
                payment.charge_status = ChargeStatus.PARTIALLY_REFUNDED
            else:
                payment.charge_status = ChargeStatus.PARTIALLY_CHARGED
            payment.save()


def convert_paritally_charged_and_partially_refunded_to_charged(apps, schema_editor):
    PaymentModel = apps.get_model("payment", "Payment")
    for payment in PaymentModel.objects.all():
        if payment.charge_status in (
            ChargeStatus.PARTIALLY_CHARGED,
            ChargeStatus.FULLY_CHARGED,
            ChargeStatus.PARTIALLY_REFUNDED,
        ):
            payment.charge_status = CHARGED
            payment.save()


class Migration(migrations.Migration):

    dependencies = [("payment", "0008_merge_20190214_0447")]

    operations = [
        migrations.RunPython(
            convert_charged_to_paritally_charged_and_partially_refunded,
            convert_paritally_charged_and_partially_refunded_to_charged,
        )
    ]
