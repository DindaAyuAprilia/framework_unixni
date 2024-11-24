from django.shortcuts import render, get_object_or_404, redirect
from .models.home.beranda import CompanyValue, ValueDescription, WelcomeCard,TrustedBrand,Testimonial, FAQ
from .models.home.about import About, Mission, Structur
from  .models.home.tim import Tim, Value, Pencapaian, Target
from .models.home.galeri import GaleriUtama, Galeri
from .models.home.kontak import Kontak, Kerja, Alamat
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models.home.blog import BlogUtama, BlogPost, RelatedPost, Comment
from django.contrib.auth.decorators import login_required

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
    
def tim(request):
    
    tim_details = Tim.objects.first()
    value = Value.objects.all()
    pencapaian = Pencapaian.objects.all()
    target = Target.objects.all()
    return render(request, 'tim.html', 
                  {'tim_details': tim_details,
                   'value': value,
                   'pencapaian': pencapaian,
                   'target': target,
                   })
    
def galeri(request):
    # Ambil data GaleriUtama pertama (judul dan deskripsi utama galeri)
    galeri_utama = GaleriUtama.objects.first()

    # Ambil semua galeri dan item terkait
    galeri_list = Galeri.objects.prefetch_related('items').all()

    # Group items menjadi batch per galeri
    galeri_data = []
    for galeri in galeri_list:
        if galeri.items.exists():  # Pastikan galeri memiliki item
            grouped_items = list(chunker(galeri.items.all(), 2))  # Kelompokkan item per 3
            galeri_data.append({
                'galeri': galeri,
                'items': grouped_items,
            })

    return render(request, 'galeri.html', {
        'galeri_utama': galeri_utama,
        'galeri_data': galeri_data,
        'galeri_list': galeri_list,
    })
    
def kontak(request):
    kontak_info = Kontak.objects.first()
    working_hours = Kerja.objects.all()
    address_info = Alamat.objects.all()
    if request.method == 'POST':
        from_email = request.POST.get('from')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email
        send_mail(
            subject,
            message,
            from_email,
            [settings.EMAIL_HOST_USER],  # Recipient list
            fail_silently=False,
        )
        messages.success(request, 'Email sudah berhasil di kirim')
    return render(request, 'kontak.html', {
        'kontak_info': kontak_info,
        'working_hours': working_hours,
        'address_info': address_info
    })

def blog_list(request):
    posts = BlogPost.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(title__icontains=search_query)

    context = {
        'posts': posts,
        'blog_main': BlogUtama.objects.first()
    }
    return render(request, 'blog.html', context)

@login_required
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    related_posts = post.related_posts.all()
    if request.method == 'POST' and 'comment' in request.POST:
        comment_content = request.POST.get('comment')
        if comment_content:
            Comment.objects.create(post=post, user=request.user, content=comment_content)
            messages.success(request, "Your comment has been posted.")
            return redirect('blog_detail', pk=post.pk)

    context = {
        'post': post,
        'comments': comments,
        'related_posts': related_posts
    }
    return render(request, 'blog_detail.html', context)

@login_required
def blog_like(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        messages.info(request, "You disliked the post.")
    else:
        post.likes.add(request.user)
        messages.success(request, "You liked the post.")
    return redirect('blog_detail', pk=pk)


def daftar(request):
    
    return render(request, 'daftar.html')

def masuk(request):
    
    return render(request, 'masuk.html')