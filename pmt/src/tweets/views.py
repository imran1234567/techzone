from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

# Create your views here.


#Create
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweet/create/"
    #login_url = '/admin/'


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweet/"


#Retrive
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    #template_name = "tweets/detail_view.html"


    # def get_object(self):
    #     print (self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     print (pk)
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView,self).get_context_data(*args, **kwargs)
        print (context)
        return context

def tweet_detail_view(request,pk=None):
    #obj = Tweet.objects.get(pk=pk)
    obj = get_object_or_404(Tweet, pk=pk)
    print (obj)
    context = {
        "object":obj
    }
    return render(request, "tweets/detail_view.html", context)


# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print (queryset)
#     for obj in queryset:
#         print (obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)
