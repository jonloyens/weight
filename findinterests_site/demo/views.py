from django.views.generic import TemplateView
from models import *
import facebook

from django.conf import settings

class DemoView(TemplateView):
    template_name = "index"

    def get_template_names(self):
    	return self.kwargs.get("template", self.template_name)+".html"

    def get_context_data(self, **kwargs):

    	user_session = facebook.get_user_from_cookie(
                			self.request.COOKIES, settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
        
        if user_session:
        	fb_user, created = FacebookUser.objects.get_or_create(uid=user_session["uid"], 
        		defaults={"access_token":user_session["access_token"]})

        	if not created:
        		fb_user.access_token = user_session["access_token"]
        		fb_user.save()


    	return {
            'settings' : settings,
            'params': kwargs,
            'fblogin' : user_session,
        }