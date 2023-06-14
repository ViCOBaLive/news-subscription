from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .models import News,Subscription,Subcategory
from ussd.middlewares.smsMiddleware import SMSHandler

@receiver(post_save, sender=News)
def send_notification_to_subscribers(sender, instance, created, **kwargs):
    if created:
        # Get the subscribers of the news subcategory
        subscribers = Subscription.objects.filter(subcategory=instance.subcategory)

        # Send a notification to each subscriber
        news_Subbscribers = []
        for subscriber in subscribers:
            # Customize the message content and other details as needed
            news_Subbscribers.append(subscriber.user.phone_number)
            message = f"{instance.title}: {instance.content}"
            # Send the SMS using the AT gateway provider
            SMSHandler(get_response=None).sendMultipleSMS(news_Subbscribers,message=message)



