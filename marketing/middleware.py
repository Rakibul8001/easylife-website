from .models import MarketingMessage
from django.utils.deprecation import MiddlewareMixin

class DisplayMarketing(MiddlewareMixin):
    def process_request(self, request):
        try:
            request.session['marketing_message'] = MarketingMessage.objects.all()[0].message
        except:
            request.session['marketing_message'] = False
