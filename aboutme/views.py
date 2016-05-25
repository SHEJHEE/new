from django.shortcuts import render
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Content
from .models import TemplateImage
from .forms import ContentEditForm

# Create your views here.

def main(request):
#    username = request.user.id
#    ctx = {
#        'username' : username,
#    }
    return render(request, 'main.html')

def join(request):
    return render(request, 'join.html')

@login_required()
def edit(request):
    origin_content = Content.objects.get(user=request.user)
    if request.method == 'POST':
        form = ContentEditForm(request.POST, instance=origin_content)
        if form.is_valid():
            try :
                origin_content = Content.objects.get(user=request.user)
                origin_content = form.save(commit=False)
                origin_content.user = request.user
                origin_content.save()
                return redirect(result)

            except ObjectDoesNotExist:
                new_content = form.save(commit=False)
                new_content.user = request.user
                new_content.save()
                return redirect(result)


    elif request.method == 'GET':
        form = ContentEditForm(instance=origin_content)

    ctx = {
        'form' : form,
    }

    return render(request, 'edit.html', ctx)


def templates(request):
    if request.method == 'POST':
        origin_contents = Content.objects.get(user=request.user)
        origin_contents.template_image_id = request.POST.get("radio_num")
        origin_contents.save()
        return redirect(result)


    templates = TemplateImage.objects.all()
    ctx = {
        'templates': templates,
    }

    return render(request, 'templates.html', ctx)

def result(request):
    page = Content.objects.get(user=request.user)
    ctx = {
        'page' : page,
    }

    return render(request, 'result.html', ctx)



