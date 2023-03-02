from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, FormView, ListView, DeleteView
from .models import Post
from . forms import PostFormRequest
from .models import PostOffer
from . forms import PostFormOffer



# CREATE THE VIEWS
# request -> response
# Works as a request handler, here we can pull data from our db, transform, send email, etc

class HomePageView(TemplateView):
    template_name = "home.html"

    # https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/TemplateView/
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_object_welcome'] = "Welcome to Cairdepool! "
        context['my_mission_object'] = "More then a friend's carpool"
        # context['posts'] = Post.objects.all().order_by('-id')   #ordering the posts so that last appears first
        return context


#this class is for user upload a new request
class AddPostViewRequest(FormView):
    template_name = "new_request_page.html"
    form_class = PostFormRequest
    success_url = "/"    # on success send back to homepage

    def dispatch(self, request, *args, **kwargs):  #displays success messages:
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            user_id=self.kwargs['pk'],
            text_destination=form.cleaned_data['text_destination'],
            text_origin=form.cleaned_data['text_origin'],
            text_date=form.cleaned_data['text_date'],
            text_time=form.cleaned_data['text_time']
            # image=form.cleaned_data['image 1']   //future implementation
        )
# https://docs.djangoproject.com/en/4.1/ref/contrib/messages/
# it's possible DISPLAY different messages for the user= DEBUG, INFO, SUCCESS, WARNING OR ERROR
        messages.add_message(self.request, messages.SUCCESS, "Yor request was successful!")
        return super().form_valid(form)


class AddPostViewOffer(FormView):
    template_name = "new_offers_page.html"
    form_class = PostFormOffer
    success_url = "/"    # on success  post offer send back to homepage

    def form_valid(self, form):
        new_offer = PostOffer.objects.create(
            user_id=self.kwargs['pk'],
            text_destination=form.cleaned_data['text_destination'],
            text_origin=form.cleaned_data['text_origin'],
            text_date=form.cleaned_data['text_date'],
            text_time=form.cleaned_data['text_time']
            # image=form.cleaned_data['image 1']   //future implementation
        )
        return super().form_valid(form)


class SeeRequests(ListView):
    model = Post
    template_name = 'my_requests.html'
    context_object_name = 'post_list'

    def get_queryset(self):  # returns list of published requests
        post_list = Post.objects.filter(user_id=self.kwargs["pk"])

        return post_list


class DeleteRequestPost(DeleteView):
    model = Post
    template_name = 'my_requests.html'

    def get(self, request, *args, **kwargs):
        model_list = Post.objects.filter(user_id=kwargs["pk"])
        model_list.delete()

        return redirect('carpool:requests', kwargs["pk"])


