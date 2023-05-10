from django.http import HttpResponse


class StripeWH_Handler:
    def __innit__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
