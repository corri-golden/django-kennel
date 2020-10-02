import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from kennelapp.models import Cat, Kennel
from ..connection import Connection


def get_kennel(kennel_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
         select
            k.id,
            k.title,
            k.address
            from kennelapp_kennel k
            WHERE k.id = ?
            """, (kennel_id,))

        return db_cursor.fetchone()

@login_required
def kennel_details(request, kennel_id):
    if request.method == 'GET':
        kennel = get_kennel(kennel_id)

        template = 'kennels/details.html'
        context = {
            'kennel': kennel
        }

        return render(request, template, context)