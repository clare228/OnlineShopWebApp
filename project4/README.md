# OnlineShopWebAPP

Web Programming with Python and JavaScript (Django, SQL)

A family member of mine has been making macrame decorations and jewelleries. I have made an online shop website and have included a small number of items of hers in this website as a test.

# Short demonstration video
A short video that demonstrates functionality of website: https://www.youtube.com/watch?v=_o864JYeFUY&feature=youtu.be

# Progress
1st version completed

# Files
Python files:
1) models.py
- database of items, categories, photos etc
2) views.py
- index: renders home page
- home: renders home page
- collection: renders collection.html
- about: renders about.html
- category: renders category.html
- item: renders item.html
- contact: sets up contact form and renders contact.html
- search: renders search.html and filter items according to search
- success: renders success.html if contact is successful
3) forms.py
- contains class for contact form


Static files:
4) style.css - styling
5) script.js
- creating/changing dynamic elements for example the side navigation toggle and collapsible filters
- filter colours and prices of items


HTML files:
6) base.html - template that all other html files follow, contains logo, search icon and navigation bar
7) about.html - description of shop and page
8) category.html - display items by category
9) collection.html - display categories
10) contact.html - display contact form
11) home.html - display home screen
12) item.html - display details and photos of individual items
13) search.html - display search results
14) success.html - success message of contact form is submitted successfully


