import sqlite3
from django.shortcuts import render, redirect, reverse
from kennelapp.models import Kennel
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required  
def kennel_list(request):
    if request.method == 'GET':
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

            all_kennels = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                kennel = Kennel()
                kennel.id = row['id']
                kennel.title = row['title']
                kennel.address = row['address']

                all_kennels.append(kennel)

        template = 'kennels/list.html'
        context = {
            'all_kennels': all_kennels
        }

        return render(request, template, context)


    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO kennelapp_kennel
            (
                title, address
            )
            VALUES (?, ?)
            """,
            (form_data['title'], form_data['address']))

        return redirect(reverse('kennelapp:kennels'))