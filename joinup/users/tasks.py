from celery import shared_task


@shared_task
def send_email_async(email):
    # Here would go the logic to send the email
    print(f"Sending email to {email}")


@shared_task
def send_sms_async(phone):
    # Here would go the logic to send the sms
    print(f"Sending SMS to {phone}")
