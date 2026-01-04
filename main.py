from flask import Flask, render_template, request
import os, subprocess, connect

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/connect", methods=["POST"])
def repeaterConf():
    iface = os.popen('sudo ls /run/wpa_supplicant/', 'r')
    iface = iface.read()
    iface = iface.split('\n')

    ssid = request.form.get("essid")
    password = request.form.get("pass")

    scheme = connect.SchemeWPA(
        iface[1],
        ssid,
        {"ssid": ssid, "psk": password}
    )
    scheme.save()

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
