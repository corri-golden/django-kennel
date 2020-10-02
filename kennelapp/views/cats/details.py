import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from kennelapp.models import Cat, Kennel
# from libraryapp.models import model_factory
from ..connection import Connection


def create_cat(cursor, row):
    _row = sqlite3.Row(cursor, row)

    cat = Cat()
    cat.id = _row["cat_id"]
    cat.name = _row["name"]
    cat.specie = _row["specie"]
    cat.owner = _row["owner"]
    cat.admitted = _row["admitted"]

    caretaker = caretaker()
    caretaker.id = _row["caretaker_id"]
    caretaker.first_name = _row["first_name"]
    caretaker.last_name = _row["last_name"]

    kennel = kennel()
    kennel.id = _row["kennel_id"]
    kennel.title = _row["kennel_name"]

    cat.caretaker = caretaker
    cat.kennel = kennel

    return cat

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
            c.location_id,
            car.id caretaker_id,
            u.first_name,
            u.last_name,
            loc.id kennel_id,
            loc.title kennel_name
        FROM kennelapp_cat c
        JOIN kennelapp_caretaker car ON c.caretaker_id = car.id
        JOIN kennelapp_kennel loc ON c.location_id = loc.id
        JOIN auth_user u ON u.id = car.user_id
        WHERE c.id = ?
        """, (cat_id,))

        return db_cursor.fetchone()

@login_required
def cat_details(request, cat_id):
    if request.method == 'GET':
        cat = get_cat(cat_id)
        template = 'cats/details.html'
        context = {
            'cat': cat
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
    if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE kennelapp_cat
                SET name = ?,
                    specie = ?,
                    owner = ?,
                    admitted = ?,
                    location_id = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['specie'],
                    form_data['owner'], form_data['admitted'],
                    form_data["location"], cat_id,
                ))

            return redirect(reverse('kennelapp:cats'))
    
    
    
    if request.method == 'POST':
        form_data = request.POST

    # Check if this POST is for deleting a book
    #
    # Note: You can use parenthesis to break up complex
    #       `if` statements for higher readability
    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
    ):
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            DELETE FROM kennelapp_cat
            WHERE id = ?
            """, (cat_id,))

        return redirect(reverse('kennelapp:cats'))