from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None

        prds = Product.get_all_product()
        cate = Category.get_all_categories()
        catted = request.GET.get('category')
        if catted:
            products = Product.get_all_product_by_category_id(catted)
        else:
            products = Product.get_all_product()
        data = {'products': products, 'categories': cate}
        # print(products)
        return render(request, 'index.html', data)

# Create your views here.


# return render(request, 'orders/orders.html')
# return HttpResponse('<H1>index page</H1>')
