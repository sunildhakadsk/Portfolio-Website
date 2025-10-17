from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# ===== Home Page =====
def home_view(request):
    return render(request, 'home.html')

# ===== Skills Page =====
def skills_view(request):
    return render(request, 'skills.html')

# ===== Projects Page =====
def projects_view(request):
    return render(request, 'projects.html')

# ===== Contact Page =====
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save message to the database
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
