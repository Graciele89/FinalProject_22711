from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    # https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/TemplateView/
    def get_context_data(self, **kwargs):
     context= super().get_context_data(**kwargs)
     context['my_object_whatsoever'] = "Hello: this is dynamic"
     return context
