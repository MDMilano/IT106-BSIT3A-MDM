import pymysql
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect

#View Read-All Page
@app.route('/read_all_user')
def read_all_user():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user_info")
        rows = cursor.fetchall()
        return render_template('readusers.html', rows=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#View Create New User Page
@app.route('/create_user_view')
def create_user_view():
    return render_template('addusers.html')

#POST METHOD to Save New User Record
@app.route('/create_user', methods=['POST'])
def create_user():
    conn = None
    cursor = None
    try:
        #GET USER INPUTS
        strMDMID = request.form['UserID']
        strMDMLName = request.form['LastName']
        strMDMFName = request.form['FirstName']
        strMDMMName = request.form['MiddleName']
        strMDMHomeAdd = request.form['Address']
        strMDMEmailAdd = request.form['EmailAdd']
        strMDMMobNo = request.form['MobileNo']
        strMDMUType = request.form['usertype']
        strMDMStatus = request.form['status']
        strMDMPassword = 'default'

        if request.method == 'POST':
            #SAVE RECORD TO DATABASE
            sql = "INSERT INTO tbl_user_info \
                    (User_ID, Last_Name, First_Name, Middle_Name, Home_Address, \
                    Email_Address, Mobile_Number,User_Type,Status, Password) \
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (strMDMID, strMDMLName, strMDMFName, strMDMMName, strMDMHomeAdd, strMDMEmailAdd,
                    strMDMMobNo, strMDMUType,strMDMStatus, strMDMPassword)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Record successfully saved in the database!')
            return redirect('/read_all_user')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#View Read-One Page
@app.route('/read_one_user/<string:id>')
def read_one_user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user_info WHERE user_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('viewusers.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#View Update Page
@app.route('/update_user_view/<string:id>')
def update_user_view(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user_info WHERE user_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('editusers.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#POST Method to Save Changes in data
@app.route('/update_user', methods=['POST'])
def update_user():
    conn = None
    cursor = None
    try:
        # GET USER INPUTS
        strMDMID = request.form['UserID']
        strMDMLName = request.form['LastName']
        strMDMFName = request.form['FirstName']
        strMDMMName = request.form['MiddleName']
        strMDMHomeAdd = request.form['Address']
        strMDMEmailAdd = request.form['EmailAdd']
        strMDMMobNo = request.form['MobileNo']
        strMDMUType = request.form['usertype']
        strMDMStatus = request.form['status']

        if request.method == 'POST':
            # SAVE RECORD TO DATABASE
            sql = "UPDATE tbl_user_info SET \
                    Last_Name=%s, First_Name=%s, Middle_Name=%s, Home_Address=%s, \
                    Email_Address=%s, Mobile_Number=%s, User_Type=%s,Status=%s \
                    WHERE User_ID=%s"
            data = (strMDMLName, strMDMFName, strMDMMName, strMDMHomeAdd, strMDMEmailAdd,
                    strMDMMobNo, strMDMUType, strMDMStatus, strMDMID)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Record successfully edited in the database!')
            return redirect('/read_all_user')
        else:
            return 'Error while updating user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete_user/<string:id>')
def delete_user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_user_info WHERE user_id=%s", (id,))
        conn.commit()
        flash('Record successfully deleted from the server!')
        return redirect('/read_all_user')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)
