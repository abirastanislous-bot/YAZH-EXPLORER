import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'yazh_explorer_secret_key_2026'

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS places (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            opening_hours TEXT,
            entrance_fee TEXT,
            distance REAL,
            travel_tips TEXT,
            historical_background TEXT,
            contact_details TEXT,
            latitude REAL,
            longitude REAL,
            image_folder TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/places')
def places():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM places")
    all_places = cursor.fetchall()
    conn.close()
    return render_template('places.html', places=all_places)

# --- NEW ROUTE FOR PLACE DETAILS ---
@app.route('/place/<int:place_id>')
def place_details(place_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM places WHERE id = ?", (place_id,))
    place = cursor.fetchone()
    conn.close()
    return render_template('place_details.html', place=place)

# --- MAP ROUTE ---
@app.route('/map')
def map_view():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM places")
    all_places = cursor.fetchall()
    conn.close()
    return render_template('map.html', places=all_places)

# --- ONE-DAY PLANNER ROUTE ---
@app.route('/planner')
def planner():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM places")
    all_places = cursor.fetchall()
    conn.close()
    return render_template('planner.html', places=all_places)

# --- ADMIN: DASHBOARD ---
@app.route('/admin')
def admin():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM places")
    all_places = cursor.fetchall()
    conn.close()
    return render_template('admin.html', places=all_places)


# --- ADMIN: ADD PLACE (GET = show form, POST = save) ---
@app.route('/admin/add', methods=['GET', 'POST'])
def admin_add():
    if request.method == 'POST':
        name = request.form['name'].strip()
        category = request.form['category'].strip()
        description = request.form['description'].strip()
        opening_hours = request.form.get('opening_hours', '').strip()
        entrance_fee = request.form.get('entrance_fee', '').strip()
        distance = request.form['distance']
        travel_tips = request.form.get('travel_tips', '').strip()
        historical_background = request.form.get('historical_background', '').strip()
        contact_details = request.form.get('contact_details', '').strip()
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        image_folder = request.form['image_folder'].strip()

        # Validation
        if not name or not category or not description:
            flash('Please fill all required fields!', 'error')
            return redirect(url_for('admin_add'))

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO places (name, category, description, opening_hours, entrance_fee, 
                                distance, travel_tips, historical_background, contact_details, 
                                latitude, longitude, image_folder)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, category, description, opening_hours, entrance_fee, distance,
              travel_tips, historical_background, contact_details, latitude, longitude, image_folder))
        conn.commit()
        conn.close()

        flash(f'✅ "{name}" was added successfully!', 'success')
        return redirect(url_for('admin'))

    return render_template('add_place.html')


# --- ADMIN: EDIT PLACE (GET = show form, POST = save) ---
@app.route('/admin/edit/<int:place_id>', methods=['GET', 'POST'])
def admin_edit(place_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name'].strip()
        category = request.form['category'].strip()
        description = request.form['description'].strip()
        opening_hours = request.form.get('opening_hours', '').strip()
        entrance_fee = request.form.get('entrance_fee', '').strip()
        distance = request.form['distance']
        travel_tips = request.form.get('travel_tips', '').strip()
        historical_background = request.form.get('historical_background', '').strip()
        contact_details = request.form.get('contact_details', '').strip()
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        image_folder = request.form['image_folder'].strip()

        cursor.execute('''
            UPDATE places SET name=?, category=?, description=?, opening_hours=?, entrance_fee=?, 
                              distance=?, travel_tips=?, historical_background=?, contact_details=?, 
                              latitude=?, longitude=?, image_folder=?
            WHERE id=?
        ''', (name, category, description, opening_hours, entrance_fee, distance,
              travel_tips, historical_background, contact_details, latitude, longitude,
              image_folder, place_id))
        conn.commit()
        conn.close()

        flash(f'✅ "{name}" was updated successfully!', 'success')
        return redirect(url_for('admin'))

    cursor.execute("SELECT * FROM places WHERE id = ?", (place_id,))
    place = cursor.fetchone()
    conn.close()

    if not place:
        flash('❌ Place not found!', 'error')
        return redirect(url_for('admin'))

    return render_template('edit_place.html', place=place)


# --- ADMIN: DELETE PLACE ---
@app.route('/admin/delete/<int:place_id>')
def admin_delete(place_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM places WHERE id = ?", (place_id,))
    row = cursor.fetchone()
    name = row[0] if row else "Place"

    cursor.execute("DELETE FROM places WHERE id = ?", (place_id,))
    conn.commit()
    conn.close()

    flash(f'🗑️ "{name}" was deleted.', 'success')
    return redirect(url_for('admin'))

# --- RUN THE APP ---
if __name__ == '__main__':
    app.run(debug=True)