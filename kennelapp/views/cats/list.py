import sqlite3
from django.shortcuts import render, redirect, reverse
from kennelapp.models import Cat
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required    
def cat_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.id,
                c.name,
                c.specie,
                c.owner,
                c.admitted,
                c.caretaker_id,
                c.location_id
            from kennelapp_cat c
            """)

            all_cats = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                cat = Cat()
                cat.id = row['id']
                cat.name = row['name']
                cat.specie = row['specie']
                cat.owner = row['owner']
                cat.admitted = row['admitted']
                cat.caretaker = row['caretaker_id']
                cat.location_id = row['location_id']

                all_cats.append(cat)

        template = 'cats/list.html'
        context = {
            'all_cats': all_cats
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO kennelapp_cat
            (
                name, specie, owner,
                admitted, location_id, caretaker_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['name'], form_data['specie'],
                form_data['owner'], form_data['admitted'],
                request.user.caretaker.id, form_data["location"]))

        return redirect(reverse('kennelapp:cats'))