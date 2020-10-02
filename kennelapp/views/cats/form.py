import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from kennelapp.models import Cat
from kennelapp.models import Kennel
# from kennelapp.models import model_factory
from ..connection import Connection


def get_cat(cat_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.specie,
            c.owner,
            c.admitted,
            c.caretaker_id,
            c.location_id
            from kennelapp_cat c
            where c.id = ?
        """, (cat_id,))

        return db_cursor.fetchone()

def get_kennels():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            k.id,
            k.title,
            k.address
        from kennelapp_kennel k
        """)

        return db_cursor.fetchall()

@login_required
def cat_form(request):
    if request.method == 'GET':
        kennels = get_kennels()
        template = 'cats/form.html'
        context = {
            'all_kennels': kennels
        }

        return render(request, template, context)

@login_required
def cat_edit_form(request, cat_id):

    if request.method == 'GET':
        cat = get_cat(cat_id)
        kennels = get_kennels()

        template = 'cats/form.html'
        context = {
            'cat': cat,
            'all_kennels': kennels
        }

        return render(request, template, context)