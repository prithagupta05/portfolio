from django.shortcuts import render

def home(request):
    return render(request, 'myapp/index.html')  # ✅ This should match the file path
