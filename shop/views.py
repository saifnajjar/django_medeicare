from django.shortcuts import render
from .models import Category, Product

def pharmacy(request):
    # استرجاع جميع الأقسام من قاعدة البيانات
    categories = Category.objects.all()

    # افتراض أننا في البداية لم نختر أي قسم، لذلك سنقوم بجلب جميع المنتجات
    products = Product.objects.all()

    # التحقق إذا ما كان هناك اختيار لقسم معين عبر العنوان (URL)، في هذه الحالة سنقوم بتحديث قائمة المنتجات
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'SHOP/SHOP.html', context)






def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product)
    categories = Category.objects.all()


    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            comments = Comment.objects.filter(product=product)  # تحديث قائمة التعليقات بعد إضافة تعليق جديد

    else:
        form = CommentForm()

    return render(request, 'SHOP/single_product.html', {'product': product,  'comments': comments, 'form': form, 'categories': categories, })




from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm

def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id=product_id)

    # في حالة الطلب الغير POST يعود لصفحة التفاصيل مع النموذج
    return redirect('product_detail', product_id=product_id)    

