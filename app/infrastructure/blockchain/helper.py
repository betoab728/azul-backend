import hashlib

def generar_hash_historial(id_orden, id_estado, fecha, observaciones):
    data = f"{id_orden}-{id_estado}-{fecha}-{observaciones}"
    return hashlib.sha256(data.encode()).hexdigest()