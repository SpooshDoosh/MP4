from django.conf import settings
from django.http import HttpResponse
from checkout.webhook_handler import StripeWH_Handler
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get The Webhook Data And Verify It's Signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            wh_secret
        )
    except ValueError as e:
        # Invalid Payload
        return HttpResponse(status=400)
    except stripe.errorSignatureVerificationError as e:
        # Invalid Signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set Up A Webhook Handler
    handler = StripeWH_Handler(request)

    # Map Webhook events To Relevant Handler Functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get The Webhook Type From Stripe
    event_type = event['type']

    # If There Is A Handler For It, Get It From Event Map
    # Use Generic One By Default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call Event Handler With The Event
    response = event_handler(event)
    return response
