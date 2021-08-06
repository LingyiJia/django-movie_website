import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [{'title': 'Monster House', 'url': 'http://127.0.0.1:8000/rango/about/', 'views': 3}, {'title': 'ELI', 'url': 'http://127.0.0.1:8000/rango/about1/', 'views': 4}]
    django_pages = [{'title': 'READY OR NOT', 'url': 'http://127.0.0.1:8000/rango/about2/', 'views': 6}, {'title': 'Spiral', 'url': 'http://127.0.0.1:8000/rango/about3/', 'views': 7}]
    other_pages = [{'title': 'THE CONJURING', 'url': 'http://127.0.0.1:8000/rango/about4/', 'views': 9}, {'title': 'Corpse Bride', 'url': 'http://127.0.0.1:8000/rango/about5/', 'views': 10}]
    cats = {'PGlevel 13': {'pages': python_pages, 'views': 128, 'likes': 64}, 'PGlevel 15': {'pages': django_pages, 'views': 64, 'likes': 32}, 'PGlevel 17': {'pages': other_pages, 'views': 32, 'likes': 16}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            p = add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title, views=views)[0]
    p.url = url
    # p.views = views
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    # c.views = views
    # c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()