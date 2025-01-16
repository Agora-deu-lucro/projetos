from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail para Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'gabrielnery894@gmail.com'  # Seu e-mail do Gmail
app.config['MAIL_PASSWORD'] = 'dpzkybwbvmtdhrdj'  # Sua senha do Gmail ou senha de aplicativo
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        
        # Envia e-mail
        msg = Message('Novo Formulário Enviado',
                      sender='gabrielnery894@gmail.com',
                      recipients=['gabrielnery894@gmail.com'])  # Substitua pelo e-mail que deve receber a mensagem
        msg.body = f'Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}'
        
        try:
            mail.send(msg)
            return redirect(url_for('sucesso'))
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
            return "Ocorreu um erro ao enviar o e-mail. Verifique os logs para mais detalhes."
    
    return render_template('formulario.html')

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)
