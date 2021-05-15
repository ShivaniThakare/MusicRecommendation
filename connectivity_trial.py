# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
from datetime import timedelta
import random
import os
import sys
from music import Music
from the_user import Myuser
import numpy as np
import time


np.set_printoptions(threshold=sys.maxsize)
app = Flask(__name__)
app.secret_key = 'ussa2020'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'audio'

mysql = MySQL(app)
app.permanent_session_lifetime = timedelta(minutes=5)


s = []
tempS = []
final_song = []
cur_user = Myuser()

def firstsignup():
    for i in range(0, 10):
        s.append(random.randint(0, 499))

    cur = mysql.connection.cursor()
    for i in s:
        cur.execute('SELECT song FROM  songs WHERE song_id = %s', (i, ))
        account = cur.fetchone()
        tempS.append(account[0])
    mysql.connection.commit()
    cur.close()
    cur_user.setsong_list(tempS)

def loadlist(username):
    temp = []
    cur = mysql.connection.cursor()
    for i in range(0, 10):
        cur.execute('select songname from beforelogout where username = %s and songid = %s', (username, i + 1))
        templist = cur.fetchone()
        temp.append(templist[0])

    mysql.connection.commit()
    cur.close()
    cur_user.setsong_list(temp)

def getobj(tempS):
    theuser = cur_user.getuser_name
    a = np.zeros(shape=[500, 500], dtype=np.float32)  # Q matrix initialized to 0
    b = np.zeros(shape=[500, 500], dtype=np.float32)  # R matrix initialized to 0
    cur = mysql.connection.cursor()
    cur.execute('select rowno from matrixinput where username = %s', (theuser, ))  # to see if the user exits. if it does then the result is not null ie. if the rows are fetched.
    if cur.fetchone():  # see if the rows are fetched for a particular user
        for i in range(0, 500):
            for j in range(0, 500):
                cur.execute("select Qmatrix, Rmatrix from matrixinput where username = %s and rowno = %s and colno = %s", (theuser, i, j))
                tuple_ = cur.fetchone()
                a[i][j] = tuple_[0]  # creating the q matrix from the DB
                b[i][j] = tuple_[1]  # creating the r matrix from the DB
    s = []  # if the user does not exist then R-matrix and Q-matrix initialized to 0 are used for object creation.
    for i in range(0, 10):
        cur.execute("select Song_id from songs where song = %s", (tempS[i], ))  # tempS has 10 songs based on user type. if new user, then random songs. if existing user, then songs that were last reommended to him ie. from before logout table.
        # fetch the actual song id of the 10 songs in tempS from the songs table in DB
        t = cur.fetchone()
        s.append(t[0])

    mysql.connection.commit()
    cur.close()
    # creating an object of music class so as to bring the recommendation model to the updated position of the user.
    myobj = Music(s, a, b)  # song id of playlist, q matrix, r matrix
    return myobj

@app.route("/finalhome2")
def finalhome2():
    return render_template("finalhome2.html", final_song=final_song, S=tempS)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        details = request.form
        username = details['username']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user_info WHERE username = %s AND password = %s', (username, password))
        account = cur.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            # return 'success'
            cur_user.setmyuser_name(username)
            loadlist(username)
            tempS = cur_user.getsong_list()
            a = '/static/'
            b = '.mp3'
            for i in range(0, 10):
                final_song.append(a + tempS[i] + b)
            return render_template("finalhome2.html", final_song=final_song, S=tempS, username=username)
        mysql.connection.commit()
        cur.close()
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == "POST":
        details = request.form
        username = details['username']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user_info WHERE username = %s', (username,))
        account = cur.fetchone()
        if account:
            return redirect(url_for('login'))
        else:
            cur.execute("INSERT INTO user_info(username, password) VALUES (%s, %s)", (username, password))
            # msg = 'You have successfully registered!'
            firstsignup()
            cur_user.setmyuser_name(username)
            tempS = cur_user.getsong_list()
            print(tempS)
            a = '/static/'
            b = '.mp3'
            for i in range(0, 10):
                final_song.append(a + tempS[i] + b)

            return render_template("finalhome2.html", final_song=final_song, S=tempS, username=username)
        mysql.connection.commit()
        cur.close()
    return render_template('signup.html', error=error)

@app.route('/background_process', methods=["POST"])
def background_process():
    response = request.get_json()
    print(response)
    song_id = int(response['songnum'])
    songname = response['songname']
    length = int(response['len'])
    cur = mysql.connection.cursor()
    cur.execute("SELECT songlike FROM liked WHERE song_name = %s", (songname,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO liked(username, song_id, song_name, songlike, song_len) VALUES (%s, %s, %s, %s, %s)", (cur_user.getuser_name(), song_id, songname, length, 0))
        mysql.connection.commit()

    else:
        cur.execute("UPDATE liked SET songlike = %s WHERE song_name = %s and username = %s", (length, songname, cur_user.getuser_name()))
        mysql.connection.commit()

    cur.close()
    return jsonify(response)

@app.route('/trackTiming', methods=['GET', 'POST'])
def trackTiming():
    response_x = request.get_json()
    songname = response_x['trackTitle1']
    song_id = response_x['_currentTrack']
    temp_time = response_x['trackCurrentTime1']
    abc = 0
    abc = sum(x * int(t) for x, t in zip([60, 1], temp_time.split(":")))
    cur = mysql.connection.cursor()
    cur.execute("SELECT song_len FROM liked WHERE song_name = %s and username = %s", (songname, cur_user.getuser_name()))
    songlist = cur.fetchone()
    print(songlist)
    if songlist is None:
        print("inside If")
        cur.execute("INSERT INTO liked(username, song_id, song_name, songlike, song_len) VALUES (%s, %s, %s, %s, %s)", (cur_user.getuser_name(), song_id, songname, 1, abc))
        mysql.connection.commit()

    else:
        print("inside else")
        songlen = list(songlist)
        print(songlen)
        final_len = int(songlen[0]) + int(abc)
        cur.execute("UPDATE liked SET song_len = %s WHERE song_name = %s and username = %s", (final_len, songname, cur_user.getuser_name()))
        mysql.connection.commit()

    cur.close()
    return jsonify(response_x)


@app.route("/newrecommendation", methods=['GET', 'POST'])
def newrecommendation():
    # userinput matrix creation
    print("recommendation start")
    tempS = cur_user.getsong_list()
    rows, cols = (10, 4)
    userinput = [[0 for i in range(cols)] for j in range(rows)]
    i = 0
    cur = mysql.connection.cursor()
    for song in tempS:
        cur.execute("SELECT songlike, song_len FROM liked WHERE song_name = %s and username=%s", (song, cur_user.getuser_name()))
        temptuple = cur.fetchone()
        print(temptuple)
        if temptuple is None:
            userinput[i][1] = 0
            userinput[i][2] = 0
        else:
            userinput[i][1] = temptuple[0]
            userinput[i][2] = temptuple[1]
        cur.execute("SELECT song_id, genre FROM songs WHERE Song = %s", (song,))
        temptuple = cur.fetchone()
        userinput[i][0] = temptuple[0]
        userinput[i][3] = temptuple[1]
        i = i + 1

    mysql.connection.commit()
    cur.close()
    # calling newrecommendation
    print("user input liya")
    myMusic = getobj(tempS)
    print("obj create hua")
    t0 = time.time()
    myMusic.NewRecommendation(userinput)
    t1 = time.time() - t0
    print("Time elapsed for recommendation: ", t1)
    usercur = cur_user.getuser_name()
    print("recommendation hua")
    # songid search in db,  create final_song list which contain songname , send in finalhome2
    cummulative = []
    reward = 0.0
    t2 = time.time()
    cur = mysql.connection.cursor()
    a1 = time.time()
    cur.execute("select rowno from matrixinput where username = %s", (usercur, ))
    if cur.fetchone():
        for i in range(0, 500):
            cur.execute("delete from matrixinput where username=%s and rowno=%s ", (usercur, i))

    a2 = time.time() - a1
    print("Time for matrix del inner in DB:", a2)

    for i in range(0, 500):
        for j in range(0, 500):
            reward += myMusic.R[i][j]
            cur.execute("INSERT INTO matrixinput(username, rowno, colno, Qmatrix, Rmatrix) VALUES (%s, %s, %s, %s, %s)", (usercur, i, j, myMusic.Q[i][j], myMusic.R[i][j]))
    cummulative.append(reward)  
    print(cummulative)
    t3 = time.time() - t2
    print("Time for matrix insertion in DB:", t3)
    print("db me matrix gaya")
    playlist = []
    for i in range(0, 10):
        cur.execute('SELECT song FROM  songs WHERE song_id = %s', (myMusic.playlist[i][1], ))
        account = cur.fetchone()
        playlist.append(account[0])
    mysql.connection.commit()
    cur.close()
    cur_user.setsong_list(playlist)
    a = "/static/"
    b = ".mp3"
    final_song = []
    for i in range(0, 10):
        final_song.append(a + playlist[i] + b)
    return render_template("finalhome2.html", final_song=final_song, S=playlist, username=usercur)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    currrentuser = cur_user.getuser_name()
    tempS = cur_user.getsong_list()
    print(tempS)
    cur = mysql.connection.cursor()
    cur.execute('select songid from beforelogout where username = %s', (currrentuser, ))
    if cur.fetchone():
        print("inside if")
        for i in range(0, 10):
            cur.execute('update beforelogout set songname = %s where username=%s and songid=%s', (tempS[i], currrentuser, i + 1))
    else:
        for i in range(0, 10):
            cur.execute('insert into beforelogout(username, songid, songname) values (%s, %s, %s)', (currrentuser, i + 1, tempS[i]))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
