from django.contrib import admin
from django.utils.html import format_html

# ======================= HomePage ===================================
from .models.home.beranda import CompanyValue, ValueDescription, WelcomeCard,TrustedBrand,Testimonial,FAQ

# [1] Card
class WelcomeCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image')  # Menampilkan kolom judul dan pratinjau gambar
    list_display_links = ('title',)  # Membuat judul menjadi link ke form edit
    search_fields = ('title', 'description')  # Menambahkan fitur pencarian
    readonly_fields = ('preview_image',)  # Menampilkan gambar sebagai field yang hanya bisa dibaca

admin.site.register(WelcomeCard)

# [2] Value
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'description')
    list_editable = ('description',)
    search_fields = ('abbreviation', 'description')

admin.site.register(CompanyValue, CompanyValueAdmin)

class ValueDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'title3', 'title4', 'subtitle')
    list_editable = ('subtitle',)

admin.site.register(ValueDescription, ValueDescriptionAdmin)

# [3] Brand
class TrustedBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview') 
    list_display_links = ('name',)  
    list_editable = ()  
    readonly_fields = ('logo_preview',)
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.logo.url)
        return "No Image"
    logo_preview.short_description = 'Logo Preview'

admin.site.register(TrustedBrand, TrustedBrandAdmin)

# [4] Testimoni
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 80px; height: auto;" />', obj.image.url)
        return "Tidak ada gambar"
    image_preview.short_description = "Pratinjau Gambar"

admin.site.register(Testimonial, TestimonialAdmin)

# [5] FAQ
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')

admin.site.register(FAQ, FAQAdmin)





# ========================== Tentang Kami ========================
from .models.home.about import About, Mission, Structur  # Ensure you import the new models

class MissionAdmin(admin.ModelAdmin):
    list_display = ['list']

class StructurAdmin(admin.ModelAdmin):
    list_display = ['list']

admin.site.register(Mission, MissionAdmin)
admin.site.register(Structur, StructurAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7')
    list_editable = ('subtitle',)
    search_fields = ('title', 'description', 'description2', 'description3', 'description4', 'description5', 'description6', 'description7')
    readonly_fields = ('logo_preview', 'diagram_preview',)

    def logo_preview(self, obj):
        return format_html('<img src="{}" style="width: 80px; height: auto;" />', obj.logo.url)

    def diagram_preview(self, obj):
        return format_html('<img src="{}" style="width: 80px; height: auto;" />', obj.diagram.url)

admin.site.register(About, AboutAdmin)
