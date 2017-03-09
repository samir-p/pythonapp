#!/usr/bin/env python

from flask import Flask
from flask import jsonify
import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='abcd1234',db='pocdata')

cur = conn.cursor()

cur.execute("Select * from ipeds limit 10")

listOut = []

for row in cur:
   listOut.append(row)



app = Flask(__name__)

@app.route("/universities",methods=['Get'])
def index():
    return jsonify({"unis": listOut})

if __name__ == "__main__":
    app.run(debug=True)



cur.close()
conn.close()


