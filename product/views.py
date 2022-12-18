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

def is_valid_queryparam(param):
    return param != '' and param is not None


def index(request):
    context = dict()
    context = {
        "categories": Category.objects.all()

    }
    return render(request, 'home/index.html', context)


def category_products(request, id):
    context = dict()
    # bir şelilde itema geçip oradan variyi price'a göre filtrelemeliyim
    # Product.objects.filter(product_category_id=id)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    size_option = request.GET.get('size-option')
    color_option = request.GET.get('color-option')
    search = request.GET.get('search')
    print(search,"---------------------")
    # categoriye göre filtereleme
    query_products = Item.objects.filter(product__product_category=id)
    if search != ''  and search is not None:
        query_products.filter(product__name__icontains = search,sku__icontains = search)
    if min_price != '' and min_price is not None and max_price != '' and max_price is not None:
        query_products = Item.objects.filter(
            price__range=(min_price, max_price))
    elif min_price != '' and min_price is not None:
        query_products = Item.objects.filter(
            price__gte=min_price)
    elif max_price != '' and max_price is not None:
        query_products = Item.objects.filter(
            price__lte=max_price)

    # size a göre filreleme


    if size_option != '' and max_price is not None:
        Configiraton.objects.filter()


    # query_product.filter(price__range=(min_price, max_price))

    context = {
        # "products": Product.objects.filter(product_category_id=id),
        "products": query_products,
        "categories": Category.objects.all(),
        'variations': Variation.objects.filter(product_category=id),
    }

    return render(request, 'home/products.html', context)


def product_detail(request, slug):
    context = dict()
    selectedProduct = Product.objects.get(slug=slug)
    context = {

        "product": selectedProduct,
        "categories": Category.objects.all(),
        'variations': Variation.objects.filter(product_category=selectedProduct.product_category.id),

    }

    return render(request, 'home/product_detail.html', context)


# yapılacaklar
# her bir ürünün kenine ait detay sayfası olacak
# ürünler habgi varyasyonlara göre filtelenebilceği getirilecek
# ürünleri vayastonlara göre filtreleyebimeliyiz.
