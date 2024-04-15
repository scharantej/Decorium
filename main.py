
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product/<product_id>')
def product(product_id):
    return render_template('product.html', product_id=product_id)

if __name__ == '__main__':
    app.run(debug=True)
