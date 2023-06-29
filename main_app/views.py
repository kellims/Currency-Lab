from django.shortcuts import render
from django.shortcuts import render
from django.views import View #
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Currency

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"   


class CurrencyItem:
    def __init__(self, name, image, country):
        self.name = name
        self.image = image
        self.country = country

# currencies = [
#     Currency("UAE Dirham", "https://www.foreigncurrencyandcoin.com/wp-content/uploads/2022/10/NEWUAE10.jpg", "United Arab Emirates" ),
#     Currency("Chinese Yuan", "https://img.industryweek.com/files/base/ebm/industryweek/image/2019/03/industryweek_6374_chinese_yuan_1.png?auto=format,compress&fit=fill&fill=blur&w=1200&h=630", "China" ),
#     Currency("South African Rand", "https://www.foreigncurrencyandcoin.com/wp-content/uploads/2018/12/products-17294.jpg", "South Africa" ),
#     Currency("Tanzanian Shilling", "https://www.foreigncurrencyandcoin.com/wp-content/uploads/2018/12/products-17428.jpg", "Tanzania" ),
#     Currency("New Zealand Dollar", "https://www.foreigncurrencyandcoin.com/wp-content/uploads/2018/12/products-16926.jpg", "New Zealand" ),
#     Currency("Australian Dollar", "https://www.aboutaustralia.com/wp-content/uploads/2014/10/Australia-5-Dollar-Bill.jpg", "Australia" ),
#     Currency("Chilean Peso", "https://www.foreigncurrencyandcoin.com/wp-content/uploads/2018/12/products-16032.jpg", "Chile" ),
#     Currency("British Pound", "https://uploads-ssl.webflow.com/62bb7145ca6e491c926489aa/62ec46e0c8eb83e4d0889819_the-british-pound.webp", "UK" ),
#     Currency("Euro", "https://en.numista.com/catalogue/photos/zone_euro/63b57a9bbfc8c0.69651644-original.jpg", "European Union" ),

# ]        

class CurrencyList(TemplateView):
    template_name = "currency_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["currencies"] = Currency.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["currencies"] = Currency.objects.all()
            context["header"] = "Currencies"
        return context


class CurrencyCreate(CreateView):
    model = Currency
    fields = ['name', 'image', 'country']
    template_name = "currency_create.html"
    success_url = "/currency/"