from django.shortcuts import render
import logging
from .forms import UserForm, ManyFieldsForm, ImageForm
from .models import User
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data("name")
            email = form.cleaned_data("email")
            age = form.cleaned_data("age")
            logger.info(f"we got {name} {email} {age}")
            user = User(name = name, email=email, age=age)
            user.save()
            message = "User saved"
    else:
        form = UserForm()
        message = "fill the form"


    return render(request, "myapp4/user_form.html", {"form": form, "message":message})



def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
    # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp4/many_fields_form.html',{'form': form})



def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form':form})