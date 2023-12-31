from app.modelo.usuarios_modelo import Usuario as usuario_modelo

from app.utils.db import db

from app import jsonify

def obtener_Usuarios():
    try:
        lista_Usuarios = [usuario.obtenerDatos for usuario in usuario_modelo.query.all()]
        return jsonify(status=True, msg=lista_Usuarios)
    except Exception as e:
        return jsonify(status= False, msg=str(e))

def obtener_usuario_by_id(usuarioID):
    try:
        # Traer el registro según el id dado
        usuario = usuario_modelo.query.filter_by(UserID=usuarioID).first()
        # si está vacio enviar mensaje
        if usuario is None:
            return jsonify(status=False, msg="No se encontraron usuarios.")
        
        return jsonify(status=True, msg=usuario.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def obtener_usuario_by_identificacion(identificacion):
    try:
        # Traer el registro según el id dado
        usuario = usuario_modelo.query.filter_by(Identificacion = identificacion).first()

        # si está vacio enviar mensaje
        if usuario is None:
            return jsonify(status=False, msg="Ningun usuario encontrado.")
        
        return jsonify(status=True, msg=usuario.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def agregar_usuario(usuario):
    try:
        db.session.add(usuario)
        db.session.commit()
        return jsonify(status=True, msg="usuario agregado correctamente.")
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def actualizar_usuario(usuario):
    try:
        old_usuario = usuario_modelo.query.filter_by(Identificacion=usuario.Identificacion).first()
        old_usuario.Identificacion = usuario.Identificacion
        old_usuario.Contraseña = usuario.Contraseña
        old_usuario.Rol = usuario.Rol
        db.session.commit()
        return jsonify(status=True, msg='Se ha actualizado el usuario.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def eliminar_usuario(identificacion):
    try:
        old_usuario = usuario_modelo.query.filter_by(Identificacion=identificacion).first()
        old_usuario.Estado = 'desactivado'
        db.session.commit()
        return jsonify(status=True, msg='Se ha eliminado el usuario.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def login_usuario(usuarioID, password):
    try:
        usuario = usuario_modelo.query.filter_by(Identificacion = usuarioID).first()

        if usuario is None:
            return jsonify(status=False, msg="Ningún usuario encontrado.")
        if usuario.Contraseña != password:
            print(usuario.Contraseña)
            return jsonify(status=False, msg="Contraseña Incorrecta.")
        
        return jsonify(status=True, msg=usuario.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))
