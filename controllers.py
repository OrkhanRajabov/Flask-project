from flask import Flask , render_template, request, redirect,url_for
from app import app 

from models import Category, Product

@app.route('/')
@app.route('/shop.html')
def shop():
    categories = Category.query.all()
    products = Product.query.all()
    
    cat = request.args.get('category')
    if cat:
        cat_list = cat.split(',')
        cat_list = [int(i) for i in cat_list]
        products = []
        for i in cat_list:
            products += Product.query.filter_by(category_id=i).all()

      

    context = {
        'categories' : categories,
        'products' : products

    }
    return render_template('shop.html' , **context)

@app.route('/detail/<int:product_id>')
def detail(product_id):
    products = Product.query.get_or_404(product_id)
    categories = Category.query.all() 

    # cat = request.args.get('category')
    # if cat:
    #     cat_list = cat.split(',')
    #     cat_list = [int(i) for i in cat_list]
    #     products = []
    #     for i in cat_list:
    #         products += Product.query.filter_by(category_id=i).all()


    context = {
        'categories' : categories,
        'products' : products
        

    }
    return render_template('detail.html',**context)

