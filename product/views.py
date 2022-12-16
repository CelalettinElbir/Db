from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

# def productCategory(request,categoryId):
#     context = dict()
#     Product.objects.filter()

#     return render(request,f'product/{categoryId}/index.html',context)


# def all_product_categories(request):
#     return render(request, "genres.html", {'genres': productCategory.objects.all()})


def index(request):
    context = dict()
    context = {
        "categories": Category.objects.all()

    }
    return render(request, 'home/index.html', context)





def category_products(request, id, slug):
    context = dict()

    if (Category.objects.get(pk = id).slug != slug):
        return HttpResponse('<h1>Unknown Category</h1>')

    context = {
        "products": Product.objects.filter(product_category_id=id),
        "categories": Category.objects.all()
    }

    return render(request, 'home/products.html', context)



def product_detail(request,id):
    context = dict()

    context = {
        "product":Product.objects.get(pk = id),
        

    }



# yapılacaklar 
# her bir ürünün kenine ait detay sayfası olacak 
# ürünler habgi varyasyonlara göre filtelenebilceği getirilecek 
# ürünleri vayastonlara göre filtreleyebimeliyiz. 