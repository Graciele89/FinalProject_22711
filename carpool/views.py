from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):
    template_name = "home.html"

    # https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/TemplateView/
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_object_welcome'] = "Welcome to Cairdepool!"
        context['my_mission_object'] = "More then a friend's carpool, friends of the planet"
        context['posts'] = Post.objects.all().order_by('-id')   #order the posts so last appears first
        return context

#this class is for user upload a new request
class AddPostView(FormView):
    template_name = "new_request_page.html"
    form_class = PostForm
    success_url = "/"    # on success send back to homepage

    def form_valid(self, form):
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            # image=form.cleaned_data['image 1']
        )
        return super().form_valid(form)

