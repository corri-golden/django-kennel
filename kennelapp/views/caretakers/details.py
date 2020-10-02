import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from kennelapp.models import Caretaker, Cat
# from libraryapp.models import model_factory
from ..connection import Connection


def get_caretaker(caretaker_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            car.id,
            car.location_id,
            car.user_id,
            u.first_name,
            u.last_name,
            u.email
        FROM kennelapp_caretaker car
        JOIN auth_user u ON car.user_id= u.id
        WHERE car.id = ?
        """, (caretaker_id,))

        return db_cursor.fetchone()

@login_required
def caretaker_details(request, caretaker_id):
    if request.method == 'GET':
        caretaker = get_caretaker(caretaker_id)

        template = 'caretakers/detail.html'
        context = {
            'caretaker': caretaker
        }

        return render(request, template, context)