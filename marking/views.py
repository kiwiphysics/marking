from django.shortcuts import render

# Create your views here.
def mark_menu(request):
	return render(request, 'test.html', {})