import sqlite3
from django.shortcuts import render
from kennelapp.models import Caretaker
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required  
def caretaker_list(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            car.id,
            car.location_id,
            car.user_id,
            u.first_name,
            u.last_name,
            u.email
        from kennelapp_caretaker car
        join auth_user u on car.user_id = u.id
        """)

        all_caretakers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            care = Caretaker()
            care.id = row["id"]
            care.location_id = row["location_id"]
            care.user_id = row["user_id"]
            care.first_name = row["first_name"]
            care.last_name = row["last_name"]
            care.email = row["email"]

            all_caretakers.append(care)

    template_name = 'caretakers/list.html'

    context = {
        'all_caretakers': all_caretakers
    }

    return render(request, template_name, context)