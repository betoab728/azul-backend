def nueva_orden_html(numero_orden: str) -> str:
    return f"""
    <h3>Nueva Orden de Servicio</h3>
    <p>Se ha registrado una nueva orden de servicio.</p>
    <p><strong>N° Orden:</strong> {numero_orden}</p>
    <p>Ingrese al sistema para revisar el detalle.</p>
    """

#nueva solicitud de cotizacion
def nueva_solicitud_cotizacion_html(numero_solicitud: str) -> str:
    return f"""
    <h3>Nueva Solicitud de Cotización</h3>
    <p>Se ha registrado una nueva solicitud de cotización.</p>
    <p><strong>N° Solicitud:</strong> {numero_solicitud}</p>
    <p>Ingrese al sistema para revisar el detalle.</p>
    """
#nueva cotizacion recibida
def nueva_cotizacion_html(numero_cotizacion: str) -> str:
    return f"""
    <h3>Nueva Cotización Recibida</h3>
    <p>Se ha recibido una nueva cotización.</p>
    <p><strong>N° Cotización:</strong> {numero_cotizacion}</p>
    <p>Ingrese al sistema para revisar el detalle.</p>
    """