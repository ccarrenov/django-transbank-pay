function enviar(codigo, nombreFormulario) {
    console.log("codigo: " + codigo);
    console.log("codigo.length: " + codigo.length);

    if (codigo.length === 0){
        console.log("codigo vació ");
    }else{
        codigo = "-" + codigo;
    }
    console.log("codigo: " + codigo);
    //OBTENCIÓN DE DATOS DEL FORMULARIO POR ELEMENTOS Y SUS ID
    let nombres = document.getElementById("txt-nombres" + codigo).value;
    let apellidoPaterno = document.getElementById("txt-apellido-paterno" + codigo).value;
    let apellidoMaterno = document.getElementById("txt-apellido-materno" + codigo).value;
    let email = document.getElementById("txt-email" + codigo).value;
    let telefono = document.getElementById("txt-telefono" + codigo).value;
    let asunto = document.getElementById("txt-asunto" +codigo).value;

    // VALIDACIONES.
    let mensaje_error = isEmpty(nombres, "NOMBRES");
    mensaje_error = mensaje_error + isEmpty(apellidoPaterno, "APELLIDO PATERNO");
    mensaje_error = mensaje_error + isEmpty(apellidoMaterno, "APELLIDO MATERNO");
    mensaje_error = mensaje_error + isEmpty(email, "EMAIL");
    mensaje_error = mensaje_error + isEmpty(telefono, "TELÉFONO");
    mensaje_error = mensaje_error + isEmpty(asunto, "ASUNTO");

    let msgValidacion = document.getElementById("msg-validacion");
    let msgInformacion = document.getElementById("msg-informacion");
    if (mensaje_error == 0) {
        console.log("DATOS VALIDADOS CORRECTAMENTE.");
        msgValidacion.className = "alert alert-success alert-dismissible fade show";
        msgInformacion.innerHTML = "DATOS VALIDADOS CORRECTAMENTE.";
        document.getElementById(nombreFormulario).submit();
        clearForm(false);
    } else {
        console.log(mensaje_error);
        msgValidacion.className = "alert alert-danger alert-dismissible fade show";
        msgInformacion.innerHTML = mensaje_error.replaceAll("\n", "<br>");
        msgValidacion.hidden = false;
    }

}

function clearForm(msgvalidacionHidden) {
    console.log("INICIO CLEAR FORM");
    clear("txt-nombres");
    clear("txt-apellido-paterno");
    clear("txt-apellido-materno");
    clear("txt-email");
    clear("txt-telefono");
    clear("txt-asunto");
    let msgValidacion = document.getElementById("msg-validacion");
    msgValidacion.hidden = msgvalidacionHidden;
    console.log("INICIO CLEAR FORM");
}