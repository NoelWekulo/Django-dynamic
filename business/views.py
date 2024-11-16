from django.shortcuts import render, redirect
from .models import TeamMember, HeroSection, Service, Portfolio, ContactInfo, Inquiry
from .forms import InquiryForm

def index(request):
    # Fetch all required data for rendering the homepage
    team_members = TeamMember.objects.all()
    hero_section = HeroSection.objects.first()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    contact_info = ContactInfo.objects.first()

    # Initialize the contact form and handle submissions
    form_message = ''
    if request.method == 'POST':
        
        print(request.method)
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            form_message = 'Your message has been sent successfully.'
        else:
            form_message = 'There was an error. Please check the form and try again.'
    else:
        form = InquiryForm()

    context = {
        'team_members': team_members,
        'hero_section': hero_section,
        'services': services,
        'portfolios': portfolios,
        'contact_info': contact_info,
        'inquiries': Inquiry.objects.all(),
        'form': form,
        'form_message': form_message,
        'page_title': 'Home'
    }

    return render(request, 'index.html', context)

def portfolio_details(request):
    return render(request, 'portfolio_details.html')

def service_details(request):
    return render(request, 'service_details.html')



