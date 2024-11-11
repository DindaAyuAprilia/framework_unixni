from django.shortcuts import render
from .models.home.beranda import CompanyValue, ValueDescription, WelcomeCard,TrustedBrand,Testimonial, FAQ
from .models.home.about import About, Mission, Structur

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

# Homepage
def homepage(request):
    
    # Welcome Card #
    welcome_cards = WelcomeCard.objects.all()
    
    # Nilai Perusahaan #
    company_values = CompanyValue.objects.all()
    company_profile = ValueDescription.objects.first()
    
    # Terpercaya
    trusted_brands = TrustedBrand.objects.all()
    grouped_brands = list(chunker(trusted_brands, 5))
    
    # Testimoni
    testimonials = Testimonial.objects.all()
    grouped_testimonials = list(chunker(testimonials, 3))
    
    # FAQ
    faqs = FAQ.objects.all()
    
    return render(request, 
                  'homepage.html', 
                  {'welcome_cards': welcome_cards,  
                  'company_values': company_values,
                  'company_profile': company_profile,
                  'trusted_brands': grouped_brands,
                  'grouped_testimonials': grouped_testimonials,
                  'faqs': faqs})
    

def about(request):
    structures = Structur.objects.all()
    mission = Mission.objects.all()
    about_details = About.objects.first()
    return render(request, 'about.html', 
                  {'about_details': about_details,
                   'mission': mission,
                   'structures': structures
                   })