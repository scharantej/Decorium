## Flask Application Design for a Home Decor Website

### HTML Files
- **home.html:**
   - Represents the homepage of the website.
   - Displays the main content, such as featured products, categories, and links to other sections.
- **products.html:**
   - Lists all products available in the store.
   - Allows for filtering and sorting of products based on various criteria.
- **about.html:**
   - Provides information about the store, its mission, and contact details.

### Routes
- **@app.route('/')**:
   - Route for the homepage, which renders the **home.html** template.
- **@app.route('/products')**:
   - Route for the products page, which renders the **products.html** template.
- **@app.route('/about')**:
   - Route for the about page, which renders the **about.html** template.
- **@app.route('/product/<product_id>')**:
   - Route for individual product pages, which displays detailed information and allows for purchase.