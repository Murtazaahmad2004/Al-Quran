import MySQLdb
from flask import Flask, flash, render_template, request, jsonify
from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = '123789456'

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'al-quran'

db = MySQLdb.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    passwd=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

# Home Page
@app.route('/')
def home():
    return render_template('quran.html')

# Quran Page
@app.route('/quran.html')
def quran():
    return render_template('/quran.html')

# tajweed Page
@app.route('/tajweed.html')
def tajwed():
    return render_template('/tajweed.html')

# qiarat Page
@app.route('/qirat.html')
def qirat():
    return render_template('/qirat.html')

# hifz Page
@app.route('/hifz.html')
def hifz():
    return render_template('/hifz.html')

# nazra page
@app.route('/nazra.html')
def nazra():
    return render_template('/nazra.html')

# tafseer Page
@app.route('/tafseer.html')
def tafseer():
    return render_template('/tafseer.html')

# easypaisa Page
@app.route('/easypaisa.html')
def easypaisa():
    return render_template('/easypaisa.html')

# jazzcash Page
@app.route('/jazzcash.html')
def jazzcash():
    return render_template('/jazzcash.html')

# banktransfer Page
@app.route('/bank.html')
def banktransfer():
    return render_template('/bank.html')

# gallery Page
@app.route('/gallery.html')
def gallery():
    return render_template('/gallery.html')

# learners Page
@app.route('/learnmore.html')
def learnmore():
    return render_template('/learnmore.html')

# donate Page
@app.route('/donate.html')
def donate():
    return render_template('/donate.html')

# contact Page
@app.route('/contact.html')
def contact():
    return render_template('/contact.html')

# about Page
@app.route('/about.html')
def about():
    return render_template('/about.html')

# course Page
@app.route('/courses.html')
def course():
    return render_template('/courses.html')

# Tajweed Page
@app.route('/tajweed', methods=['GET', 'POST'])
def tajweed():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Print form data for debugging
        print("Received Data:", request.form)

        # Validate required fields
        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('/tajweed.html', error=error)

        cursor = db.cursor()
        try:
            # Insert into database
            sql = """
                INSERT INTO tajweed (Name, Email, Phone)
                VALUES (%s, %s, %s)
            """
            values = (name, email, phone)

            cursor.execute(sql, values)
            db.commit()
            
            return render_template('/tajweed.html', success=True)
        
        except MySQLdb.Error as e:
            error = f"Database error: {str(e)}"
            print(error)  # Log the error
            return render_template('/tajweed.html', error=error)

        finally:
            cursor.close()
    return render_template('tajweed.html')

# Hifz Page
@app.route('/hifz', methods=['GET', 'POST'])
def hifzquran():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Print form data for debugging
        print("Received Data:", request.form)

        # Validate required fields
        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('/hifz.html', error=error)

        cursor = db.cursor()
        try:
            # Insert into database
            sql = """
                INSERT INTO hifz (Name, Email, Phone)
                VALUES (%s, %s, %s)
            """
            values = (name, email, phone)

            cursor.execute(sql, values)
            db.commit()
            
            return render_template('/hifz.html', success=True)
        
        except MySQLdb.Error as e:
            error = f"Database error: {str(e)}"
            print(error)  # Log the error
            return render_template('/hifz.html', error=error)

        finally:
            cursor.close()
    return render_template('hifz.html')

# tafseer Page
@app.route('/tafseer', methods=['GET', 'POST'])
def tafseerquran():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Print form data for debugging
        print("Received Data:", request.form)

        # Validate required fields
        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('/tafseer.html', error=error)

        cursor = db.cursor()
        try:
            # Insert into database
            sql = """
                INSERT INTO tafseer (Name, Email, Phone)
                VALUES (%s, %s, %s)
            """
            values = (name, email, phone)

            cursor.execute(sql, values)
            db.commit()
            
            return render_template('/tafseer.html', success=True)
        
        except MySQLdb.Error as e:
            error = f"Database error: {str(e)}"
            print(error)  # Log the error
            return render_template('/tafseer.html', error=error)

        finally:
            cursor.close()
    return render_template('tafseer.html')

# nazra Page
@app.route('/nazra', methods=['GET', 'POST'])
def nazraquran():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Print form data for debugging
        print("Received Data:", request.form)

        # Validate required fields
        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('/nazra.html', error=error)

        cursor = db.cursor()
        try:
            # Insert into database
            sql = """
                INSERT INTO nazra (Name, Email, Phone)
                VALUES (%s, %s, %s)
            """
            values = (name, email, phone)

            cursor.execute(sql, values)
            db.commit()
            
            return render_template('/nazra.html', success=True)
        
        except MySQLdb.Error as e:
            error = f"Database error: {str(e)}"
            print(error)  # Log the error
            return render_template('/nazra.html', error=error)

        finally:
            cursor.close()
    return render_template('nazra.html')

# qiarat Page
@app.route('/qirat', methods=['GET', 'POST'])
def qiaratquran():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Print form data for debugging
        print("Received Data:", request.form)

        # Validate required fields
        if not all([name, email, phone]):
            error = "All fields are required!"
            return render_template('/qiarat.html', error=error)

        cursor = db.cursor()
        try:
            # Insert into database
            sql = """
                INSERT INTO qiarat (Name, Email, Phone)
                VALUES (%s, %s, %s)
            """
            values = (name, email, phone)

            cursor.execute(sql, values)
            db.commit()
            
            return render_template('/qirat.html', success=True)
        
        except MySQLdb.Error as e:
            error = f"Database error: {str(e)}"
            print(error)  # Log the error
            return render_template('/qirat.html', error=error)

        finally:
            cursor.close()
    return render_template('qirat.html')

if __name__ == '__main__':
    app.run(debug=True)