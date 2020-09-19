from django.shortcuts import render,redirect
from django.views.generic import View,DeleteView,CreateView,DetailView
from .models import Comment
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.

def cmnts(request):
    return render(request,"comments/comment_create.html")

def page2(request):
    return render(request,"comments/testing.html")

class CommentCreateView(View):
    def post(self, request) :
        url = request.POST.get('url')
        parentsno = request.POST.get('parentsno')
        comment = request.POST.get("comment")
        reply = request.POST.get("reply")

        if parentsno=="":
            comment = Comment(cmnt=comment, user=request.user,url=url)
            comment.save()
        else:
            parent = Comment.objects.get(sno=parentsno)
            comment = Comment(cmnt=reply,user=request.user,url=url,parent=parent)
            comment.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# class CommentDetailView(DetailView):
#     model = Comment
#     template_name = "comments/comment_create.html"
#     def get(self, request, url) :
#         comments = Comment.objects.filter(url=url).order_by('-date')
#         replies = Comment.objects.filter(url=url).exclude(parent=None)
#         context = {'comments': comments, 'replies': replies}
#         return render(request, self.template_name, context)


class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = "cmntdel"
    template_name = "comments/comment_delete.html"

    def get_queryset(self):
        qs = super(CommentDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


    def get_success_url(self):
        print("###############################################################",self.object.url)
        # response = HttpResponse("", status=302)
        # response['Location'] = "http://google.com"
        # return response
        # return HttpResponseRedirect(self.object.url)
        return reverse('mainpage')