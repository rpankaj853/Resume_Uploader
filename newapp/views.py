from django.shortcuts import render, redirect

from .forms import newform

from .models import newmodel

# Create your views here.


def home(request):

	return render(request,'newapp/home.html')


def filelist(request):

	files = newmodel.objects.all()

	return render(request,'newapp/file_list.html',{

		'files':files
		})


def newview(request):

	if request.method == 'POST':


		
		form = newform(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('filelist')

	else:
		form = newform()


	return render(request,'newapp/fileuploader.html',{

		'form':form
		})




	
