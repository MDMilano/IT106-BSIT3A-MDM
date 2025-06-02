import pymysql
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect

@app.route('/')
def home():
    return read_all_emp()

#View Read-All Page
@app.route('/read_all_emp')
def read_all_emp():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_emp_info")
        rows = cursor.fetchall()
        return render_template('reademps.html', rows=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#View Create New Employee Page
@app.route('/create_emp_view')
def create_emp_view():
    return render_template('addemps.html')

#POST METHOD to Save New Employee Record
@app.route('/create_emp', methods=['POST'])
def create_emp():
    conn = None
    cursor = None
    try:
        #GET EMPLOYEE INPUTS
        strMDMSID = request.form['EmployeeID']
        strMDMLName = request.form['LastName']
        strMDMFName = request.form['FirstName']
        strMDMMName = request.form['MiddleName']
        strMDMGender = request.form['gender']
        strMDMDateHired = request.form['DateHired']
        strMDMAge = request.form['Age']
        strMDMDepartment = request.form['Department']
        strMDMHomeAdd = request.form['Address']
        strMDMEmailAdd = request.form['EmailAdd']


        if request.method == 'POST':
            #SAVE RECORD TO DATABASE
            sql = "INSERT INTO tbl_emp_info \
                    (Employee_ID, Last_Name, First_Name, Middle_Name, Gender, \
                    Date_Hired,Age ,Department ,Home_Address, Email_Address) \
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (strMDMSID, strMDMLName, strMDMFName, strMDMMName, strMDMGender, strMDMDateHired,
                    strMDMAge, strMDMDepartment,strMDMHomeAdd, strMDMEmailAdd)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Record successfully saved in the database!')
            return redirect('/read_all_emp')
        else:
            return 'Error while adding employee'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#View Read-One Page
@app.route('/read_one_emp/<string:id>')
def read_one_emp(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_emp_info WHERE employee_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('viewemps.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#View Update Page
@app.route('/update_emp_view/<string:id>')
def update_emp_view(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_emp_info WHERE employee_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('editemps.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#POST Method to Save Changes in data
@app.route('/update_emp', methods=['POST'])
def update_emp():
    conn = None
    cursor = None
    try:
        # GET EMPLOYEE INPUTSs
        strMDMSID = request.form['EmployeeID']
        strMDMLName = request.form['LastName']
        strMDMFName = request.form['FirstName']
        strMDMMName = request.form['MiddleName']
        strMDMGender = request.form['gender']
        strMDMDateHired = request.form['DateHired']
        strMDMAge = request.form['Age']
        strMDMDepartment = request.form['Department']
        strMDMHomeAdd = request.form['Address']
        strMDMEmailAdd = request.form['EmailAdd']

        if request.method == 'POST':
            # SAVE RECORD TO DATABASE
            sql = "UPDATE tbl_emp_info SET \
                    Last_Name=%s, First_Name=%s, Middle_Name=%s, Gender=%s, \
                    Date_Hired=%s, Age=%s, Department=%s,Home_Address=%s, Email_Address=%s \
                    WHERE Employee_ID=%s"
            data = (strMDMLName, strMDMFName, strMDMMName, strMDMGender, strMDMDateHired,
                    strMDMAge, strMDMDepartment, strMDMHomeAdd, strMDMEmailAdd, strMDMSID)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Record successfully edited in the database!')
            return redirect('/read_all_emp')
        else:
            return 'Error while updating employee'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete_emp/<string:id>')
def delete_emp(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_emp_info WHERE employee_id=%s", (id,))
        conn.commit()
        flash('Record successfully deleted from the server!')
        return redirect('/read_all_emp')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)
