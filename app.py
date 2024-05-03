from flask import Flask, render_template, json
import json
app = Flask(__name__)
#-------amthuc--------------------------------------------------------------------------------------------#

@app.route('/ẩm_thực_ct')

def ẩm_thực_ct():
 with open("amthuc.json", encoding="utf-8") as f:
     data = json.load(f)
 return render_template("ẩm_thực_ct.html", data=data)
@app.route('/amthuc1')

def amthuc1():
     
     return render_template('amthuc1.html')

@app.route('/amthuc2')

def amthuc2():
     
     return render_template('amthuc2.html')

@app.route('/amthuc3')

def amthuc3():
     
     return render_template('amthuc3.html')

@app.route('/amthuc4')

def amthuc4():
     
     return render_template('amthuc4.html')

@app.route('/amthuc5')

def amthuc5():
     
     return render_template('amthuc5.html')

@app.route('/amthuc6')

def amthuc6():
     
     return render_template('amthuc6.html')

@app.route('/amthuc7')

def amthuc7():
     
     return render_template('amthuc7.html')

@app.route('/amthuc8')

def amthuc8():
     
     return render_template('amthuc8.html')

#-------amthuc---------------------------------------------------------------------------------#

#-------web_ct---------------------------------------------------------------------------------#
@app.route('/web_ct')

def web_ct():
 with open("load.json", encoding="utf-8") as f:
     data = json.load(f)
 return render_template('web_ct.html', data=data)
     
#-------web_ct---------------------------------------------------------------------------------#

#-------login---------------------------------------------------------------------------------#
@app.route('/login')

def login():
     
     return render_template('login.html')
#-------login---------------------------------------------------------------------------------#

#-------thangcanh--------------------------------------------------------------------------------------------#
@app.route('/thắng_cảnh_ct')

def thắng_cảnh_ct():
 with open("thangcanh.json", encoding="utf-8") as f:
     data = json.load(f)
 return render_template("thắng_cảnh_ct.html", data=data)
@app.route('/thangcanh1')

def thangcanh1 ():
     
     return render_template('thangcanh1.html')
@app.route('/thangcanh2')

def thangcanh2 ():
     
     return render_template('thangcanh2.html')
@app.route('/thangcanh3')

def thangcanh3 ():
     
     return render_template('thangcanh3.html')
@app.route('/thangcanh4')

def thangcanh4 ():
     
     return render_template('thangcanh4.html')
@app.route('/thangcanh5')

def thangcanh5 ():
     
     return render_template('thangcanh5.html')
@app.route('/thangcanh6')

def thangcanh6 ():
     
     return render_template('thangcanh6.html')
@app.route('/thangcanh7')

def thangcanh7 ():
     
     return render_template('thangcanh7.html')
@app.route('/thangcanh8')

def thangcanh8 ():
     
     return render_template('thangcanh8.html')
#-------thangcanh--------------------------------------------------------------------------------------------#

#-------vanhoa--------------------------------------------------------------------------------------------#
@app.route('/văn_hóa_ct')

def văn_hóa_ct():
 with open("vanhoa.json", encoding="utf-8") as f:
     data = json.load(f)
 return render_template("văn_hóa_ct.html", data=data)

@app.route('/vanhoa1')

def vanhoa1 ():
     
     return render_template('vanhoa1.html')
@app.route('/vanhoa2')

def vanhoa2 ():
     
     return render_template('vanhoa2.html')
@app.route('/vanhoa3')

def vanhoa3 ():
     
     return render_template('vanhoa3.html')
@app.route('/vanhoa4')

def vanhoa4 ():
     
     return render_template('vanhoa4.html')
@app.route('/vanhoa5')

def vanhoa5 ():
     
     return render_template('vanhoa5.html')
@app.route('/vanhoa6')

def vanhoa6 ():
     
     return render_template('vanhoa6.html')
@app.route('/vanhoa7')

def vanhoa7 ():
     
     return render_template('vanhoa7.html')
@app.route('/vanhoa8')

def vanhoa8 ():
     
     return render_template('8.html')
#-------vanhoa--------------------------------------------------------------------------------------------#

#-------vuichoi--------------------------------------------------------------------------------------------#
@app.route('/vui_chơi_ct')

def vui_chơi_ct():
 with open("vuichoi.json", encoding="utf-8") as f:
     data = json.load(f)
 return render_template("vui_chơi_ct.html", data=data)

@app.route('/vuichoi1')

def vuichoi1 ():
     
     return render_template('vuichoi1.html')
@app.route('/vuichoi2')

def vuichoi2 ():
     
     return render_template('vuichoi2.html')
@app.route('/vuichoi3')

def vuichoi3 ():
     
     return render_template('vuichoi3.html')
@app.route('/vuichoi4')

def vuichoi4 ():
     
     return render_template('vuichoi4.html')
@app.route('/vuichoi5')

def vuichoi5 ():
     
     return render_template('vuichoi5.html')
@app.route('/vuichoi6')

def vuichoi6 ():
     
     return render_template('vuichoi6.html')
@app.route('/vuichoi7')

def vuichoi7 ():
     
     return render_template('vuichoi7.html')
@app.route('/vuichoi8')

def vuichoi8 ():
     
     return render_template('vuichoi8.html')
#-------vuichoi--------------------------------------------------------------------------------------------#

#-------luutru--------------------------------------------------------------------------------------------#
@app.route('/Lưu_trú_ct')

def Lưu_trú_ct():
  with open("luutru.json", encoding="utf-8") as f:
    data = json.load(f)
  return render_template("Lưu_trú_ct.html", data=data)

@app.route('/luutru1')

def luutru1 ():
     
     return render_template('luutru1.html')
@app.route('/luutru2')

def luutru2 ():
     
     return render_template('luutru2.html')
@app.route('/luutru3')

def luutru3 ():
     
     return render_template('luutru3.html')
@app.route('/luutru4')

def luutru4 ():
     
     return render_template('luutru4.html')
@app.route('/luutru5')

def luutru5 ():
     
     return render_template('luutru5.html')
@app.route('/luutru6')

def luutru6 ():
     
     return render_template('luutru6.html')
@app.route('/luutru7')

def luutru7 ():
     
     return render_template('luutru7.html')
@app.route('/luutru8')

def luutru8 ():
     
     return render_template('luutru8.html')
#-------luutru--------------------------------------------------------------------------------------------#

#-------muasam--------------------------------------------------------------------------------------------#
@app.route('/mua_sắm_ct')

def mua_sắm_ct():
 with open("muasam.json", encoding="utf-8") as f:
     data = json.load(f)
 return render_template("mua_sắm_ct.html", data=data)
@app.route('/muasam1')

def muasam1 ():
     
     return render_template('muasam1.html')
@app.route('/muasam2')

def muasam2 ():
     
     return render_template('muasam2.html')
@app.route('/muasam3')

def muasam3 ():
     
     return render_template('muasam3.html')
@app.route('/muasam4')

def muasam4 ():
     
     return render_template('muasam4.html')
@app.route('/muasam5')

def muasam5 ():
     
     return render_template('muasam5.html')
@app.route('/muasam6')

def muasam6 ():
     
     return render_template('6.html')
@app.route('/muasam7')

def muasam7 ():
     
     return render_template('muasam7.html')
@app.route('/muasam8')

def muasam8 ():
     
     return render_template('muasam8.html')
#-------muasam --------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)