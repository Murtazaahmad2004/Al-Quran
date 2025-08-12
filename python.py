import mysql.connector
from flask import Flask, flash, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = '123789456'

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'al_quran'

# Database Connection
db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

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
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        print("Received Data:", request.form)

        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('tajweed.html', error=error)

        cursor = db.cursor()
        try:
            sql = "INSERT INTO tajweed (Name, Email, Phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            cursor.execute(sql, values)
            db.commit()
            return render_template('tajweed.html', success=True)
        except mysql.connector.Error as e:
            error = f"Database error: {str(e)}"
            print(error)
            return render_template('tajweed.html', error=error)
        finally:
            cursor.close()
    return render_template('tajweed.html')

# Hifz Page
@app.route('/hifz', methods=['GET', 'POST'])
def hifzquran():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        print("Received Data:", request.form)

        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('hifz.html', error=error)

        cursor = db.cursor()
        try:
            sql = "INSERT INTO hifz (Name, Email, Phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            cursor.execute(sql, values)
            db.commit()
            return render_template('hifz.html', success=True)
        except mysql.connector.Error as e:
            error = f"Database error: {str(e)}"
            print(error)
            return render_template('hifz.html', error=error)
        finally:
            cursor.close()
    return render_template('hifz.html')

# Tafseer Page
@app.route('/tafseer', methods=['GET', 'POST'])
def tafseerquran():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        print("Received Data:", request.form)

        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('tafseer.html', error=error)

        cursor = db.cursor()
        try:
            sql = "INSERT INTO tafseer (Name, Email, Phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            cursor.execute(sql, values)
            db.commit()
            return render_template('tafseer.html', success=True)
        except mysql.connector.Error as e:
            error = f"Database error: {str(e)}"
            print(error)
            return render_template('tafseer.html', error=error)
        finally:
            cursor.close()
    return render_template('tafseer.html')

# Nazra Page
@app.route('/nazra', methods=['GET', 'POST'])
def nazraquran():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        print("Received Data:", request.form)

        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('nazra.html', error=error)

        cursor = db.cursor()
        try:
            sql = "INSERT INTO nazra (Name, Email, Phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            cursor.execute(sql, values)
            db.commit()
            return render_template('nazra.html', success=True)
        except mysql.connector.Error as e:
            error = f"Database error: {str(e)}"
            print(error)
            return render_template('nazra.html', error=error)
        finally:
            cursor.close()
    return render_template('nazra.html')

# Qirat Page
@app.route('/qirat', methods=['GET', 'POST'])
def qiaratquran():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        print("Received Data:", request.form)

        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('qirat.html', error=error)

        cursor = db.cursor()
        try:
            sql = "INSERT INTO qiarat (Name, Email, Phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            cursor.execute(sql, values)
            db.commit()
            return render_template('qirat.html', success=True)
        except mysql.connector.Error as e:
            error = f"Database error: {str(e)}"
            print(error)
            return render_template('qirat.html', error=error)
        finally:
            cursor.close()
    return render_template('qirat.html')

if __name__ == '__main__':
    app.run(debug=True)