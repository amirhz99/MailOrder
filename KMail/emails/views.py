from django.shortcuts import render
from django.http import HttpResponse

from .models import StudentMail

from django.template import loader

def index(request):
    StudentMails = StudentMail.objects.order_by('Student_Id')
    template = loader.get_template("index.html")
    return HttpResponse(template.render({
        'title' : 'All StudentMails',
        'StudentMails' : StudentMail ,
    }, request))

# def send(request):
#     if request.method == 'POST':
#         # Validation data
#         form = SendArticleForm(request.POST)

#         if form.is_valid() :
#             Article.objects.create(
#                 title = form.cleaned_data['title'],
#                 body = form.cleaned_data['body'],
#                 published_at = form.cleaned_data['published_at']
#             )

#             return redirect('emails:emails')

#     else :
#        form = SendArticleForm()


    return render(request , 'emails/students.html' , { 'form' : form })
