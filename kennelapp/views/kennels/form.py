import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from kennelapp.models import Kennel
from kennelapp.models import Cat
# from kennelapp.views.cats.list import get_kennels
# from kennelapp.models import model_factory
from ..connection import Connection


# def get_kennels():
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         select
#             k.id,
#             k.title,
#             k.address
#         from kennelapp_kennel k
#         """)

#         return db_cursor.fetchall()

@login_required
def kennel_form(request):
    if request.method == 'GET':
        # kennels = get_kennels()
        template = 'kennels/form.html'
        # context = {
        #     'all_kennels': kennels
        # }

        return render(request, template)