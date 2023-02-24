from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList,FormField, RadioField,IntegerField 
from wtforms.fields import EmailField
from wtforms import validators

def mi_validacion(form, field):
    if len(field.data) ==0:
        raise validators.ValidationError("El campo no tiene datos")

class UserForm(Form):
    matricula=StringField('Matricula',
    [validators.DataRequired('El campo es requeriddo'),
    validators.length(min=5, max=10, message='Ingresa min 5 max 10')])
    nombre=StringField('Nombre', [validators.DataRequired(message='El campo nombre es requerido')])
    apaterno=StringField('Apaterno',[mi_validacion])
    amanterno=StringField('Amaterno')
    email=StringField('Correo')

class BoxForm(Form):
    numCant = IntegerField('Ingresa el número de cajas a realizar')
    num = FieldList(StringField('Ingresa el número'))

class TraductorForm(Form):
    txtEspanol=StringField('Ingresa la palabra en Español',
    [validators.DataRequired('El campo es requeriddo'),
    validators.length(min=1, max=20, message='Ingresa min 1 max 20')])

    txtIngles=StringField('Ingresa la palabra en Ingles',
    [validators.DataRequired('El campo es requeriddo'),
    validators.length(min=1, max=20, message='Ingresa min 1 max 20')])

    txtPalabra=StringField('Ingresa la palabra a Traducir',
    [validators.DataRequired('El campo es requeriddo'),
    validators.length(min=1, max=20, message='Ingresa min 1 max 20')])


class LoginForm(Form):
    username=StringField('Usuario',
    [validators.DataRequired(message='El campo Matricula es requerido'),
    validators.length(min=5,max=10,message='Ingesa un min 5 max 10')])
    password=StringField('Contraseña',[validators.DataRequired(message='El campo Contraseña es requerido'),
    validators.length(min=5,max=10,message='Ingesa un min 5 max 10')])