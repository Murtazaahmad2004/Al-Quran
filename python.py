import mysql.connector
from flask import Flask, flash, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = '123789456'

# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'NHA@2004',
    'database': 'al_quran'
}

# Home Page
@app.route('/')
def home():
    return render_template('quran.html')

# Quran Page
@app.route('/quran.html')
def quran():
    return render_template('quran.html')

@app.route('/tajweed.html')
def tajwed():
    return render_template('tajweed.html')

@app.route('/qirat.html')
def qirat():
    return render_template('qirat.html')

@app.route('/hifz.html')
def hifz():
    return render_template('hifz.html')

@app.route('/nazra.html')
def nazra():
    return render_template('nazra.html')

@app.route('/tafseer.html')
def tafseer():
    return render_template('tafseer.html')

@app.route('/easypaisa.html')
def easypaisa():
    return render_template('easypaisa.html')

@app.route('/jazzcash.html')
def jazzcash():
    return render_template('jazzcash.html')

@app.route('/bank.html')
def banktransfer():
    return render_template('bank.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/learnmore.html')
def learnmore():
    return render_template('learnmore.html')

@app.route('/donate.html')
def donate():
    return render_template('donate.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/courses.html')
def course():
    return render_template('courses.html')

# Tajweed Page
@app.route('/tajweed', methods=['GET', 'POST'])
def tajweed():
    cursor = None
    conn = None
    success = None
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tajweed (
                    Name, 
                    Email, 
                    Phone
                ) VALUES (%s, %s, %s)      
            """,(
                name, email, phone
            ))
            conn.commit()
            success = "✅ Tajweed data submitted successfuly!"
        except Exception as e:
            error = f"❌ Failed to insert items: {e}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template('tajweed.html', success=success, error=error)

# Hifz Page
@app.route('/hifz', methods=['GET', 'POST'])
def hifzquran():
    cursor = None
    conn = None
    success = None
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO hifz (
                    Name, 
                    Email, 
                    Phone
                ) VALUES (%s, %s, %s)      
            """,(
                name, email, phone
            ))
            conn.commit()
            success = "✅ Hifz data submitted successfuly!"
        except Exception as e:
            error = f"❌ Failed to insert items: {e}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template('hifz.html', success=success, error=error)

# # Tafseer Page
@app.route('/tafseer', methods=['GET', 'POST'])
def tafseerquran():
    cursor = None
    conn = None
    success = None
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tafseer (
                    Name, 
                    Email, 
                    Phone
                ) VALUES (%s, %s, %s)      
            """,(
                name, email, phone
            ))
            conn.commit()
            success = "✅ Tafseer data submitted successfuly!"
        except Exception as e:
            error = f"❌ Failed to insert items: {e}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template('tafseer.html', success=success, error=error)

# # Nazra Page
@app.route('/nazra', methods=['GET', 'POST'])
def nazraquran():
    cursor = None
    conn = None
    success = None
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO nazra (
                    Name, 
                    Email, 
                    Phone
                ) VALUES (%s, %s, %s)      
            """,(
                name, email, phone
            ))
            conn.commit()
            success = "✅ Nazra data submitted successfuly!"
        except Exception as e:
            error = f"❌ Failed to insert items: {e}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template('nazra.html', success=success, error=error)

# # Qirat Page
@app.route('/qirat', methods=['GET', 'POST'])
def qiaratquran():
    cursor = None
    conn = None
    success = None
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO qiarat (
                    Name, 
                    Email, 
                    Phone
                ) VALUES (%s, %s, %s)      
            """,(
                name, email, phone
            ))
            conn.commit()
            success = "✅ Qiarat data submitted successfuly!"
        except Exception as e:
            error = f"❌ Failed to insert items: {e}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template('qirat.html', success=success, error=error)

if __name__ == '__main__':
    app.run(debug=True)