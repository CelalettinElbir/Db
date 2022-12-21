from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator
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
    page_number = request.GET.get('page')
    # categoriye göre filtereleme
    query_products = Item.objects.filter(product__product_category=id)

    # Price'a göre filtreleleme
    if min_price != '' and min_price is not None and max_price != '' and max_price is not None:
        query_products = query_products.filter(
            price__range=(min_price, max_price))
    elif min_price != '' and min_price is not None:
        query_products = query_products.filter(
            price__gte=min_price)
    elif max_price != '' and max_price is not None:
        query_products = query_products.filter(
            price__lte=max_price)
    # seacrh' e göre filtreleme
    if search != '' and search is not None:
        query = query_products.filter(
            product__name__icontains=search)
        if query.count() == 0:
            query_products = query_products.filter(
                sku__exact=search)
        else:
            query_products = query

    # size a göre filreleme

    if size_option != "" and size_option is not None:
        query_products = query_products.filter(variations__value=size_option)
    # color'a a göre filreleme
    if color_option != "" and color_option is not None:
        query_products = query_products.filter(variations__value=color_option)


    paginator = Paginator(query_products, 10)

    product_per_page = paginator.get_page(page_number)
    context = {
        # "products": Product.objects.filter(product_category_id=id),
        "products": product_per_page,
        "categories": Category.objects.all(),
        'variations': Variation.objects.filter(product_category=id),
    }

    return render(request, 'home/products.html', context)


def product_detail(request, slug,id):
    context = dict()
    selectedProduct = Item.objects.get(id =id)
    context = {

        "product": selectedProduct,
        "categories": Category.objects.all(),
        # 'variations': Variation.objects.filter(product_category=selectedProduct.product_category.id),

    }

    return render(request, 'home/product_detail.html', context)

#yapılacaklar 
#ilk olarak itema slug ekledim 
#o sluga özel olarak detail sayfasına gitmesini sağla 
#sonra detail sayfasını düzenle
