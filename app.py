from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample list of products
products = [
    {'id': 1, 'name': 'Apple', 'price': 1.00, 'description': 'A juicy apple.', 'image': 'apple.jpg'},
    {'id': 2, 'name': 'Banana', 'price': 0.50, 'description': 'A ripe banana.', 'image': 'banana.jpg'},
    # Add more products as needed
]

# Sample shopping cart (list of products)
shopping_cart = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Registration logic
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/products')
def product_listing():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Find the product with the given ID
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_details.html', product=product)
    else:
        return 'Product not found', 404

@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart_page():
    if request.method == 'POST':
        # Add product to shopping cart
        product_id = request.form.get('product_id')
        product = next((p for p in products if p['id'] == int(product_id)), None)
        if product:
            shopping_cart.append(product)
            return 'Product added to cart successfully!'
        else:
            return 'Product not found', 404
    else:
        return render_template('cart.html', cart=shopping_cart)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Process checkout form data
        # Implement your checkout logic here
        return 'Checkout Successful!'
    else:
        return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
