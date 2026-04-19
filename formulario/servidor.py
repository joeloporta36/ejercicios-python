from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
app=Flask(__name__)
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    # datos del formulario
    nombre=request.form["nombre"]
    edad=request.form["edad"]
    correo=request.form["correo"]
    mensaje = request.form["mensaje"]
   # Mostrar en la termiinal
    print("Nombre:", nombre)
    print("Edad:",edad)
    print("Correo:", correo)
    print("Mensaje", mensaje)

    # Tus datos de Gmail
    tu_correo = "joeloporta36@gmail.com"
    tu_password = "hmuc idjv suaq fccg"

    #Crear mensaje
    mensaje= f"""
    Hola {nombre},

    Gracias por enviar el formulario.
    Estos son tus datos:

    Nombre: {nombre}
    Edad: {edad}
    Correo: {correo}

Mensaje:
{mensaje}


    """

    msg = MIMEText(mensaje, _charset="utf-8")
    msg["Subject"] = "Confirmación de formulario"
    msg["From"]= tu_correo
    msg["To"]= correo

    # Conectar con servidor SMTP
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(tu_correo, tu_password)

    # Enviar correo al usuario
    servidor.sendmail(tu_correo, correo, msg.as_string())

    #Enviar copia a ti
    servidor.sendmail(tu_correo, correo, msg.as_string())

    servidor.quit()

    return f"Datos recibidos correctamente, {nombre}"
if __name__ =="__main__":
    app.run(debug=True)