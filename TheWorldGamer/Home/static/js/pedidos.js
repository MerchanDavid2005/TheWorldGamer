const todo = document.getElementById("Todo")

const formulario = document.getElementById("Formulario-pedido")

const nombre = document.querySelector(".Nombre-juego")

const archivo = document.querySelector(".archivo")

const foto = document.querySelector(".imagen")

const boton = document.querySelector(".enviar")

const textoMensaje = document.querySelector(".Validar")

const limite = document.querySelector("#Cuadro-Mensaje_pedido")

var validado = false

archivo.addEventListener("change", (e) => {

    if (e.target.files[0].type == "image/jpeg" || e.target.files[0].type == "image/jpg" || e.target.files[0].type == "image/png" || e.target.files[0].type == "image/jfjf"){

        const imagen = URL.createObjectURL(e.target.files[0])

        foto.setAttribute("src", imagen)

        validado = true

    }

    else{

        foto.setAttribute("src", `/static/img/pedidos/validacion.png`)

        textoMensaje.textContent = "No puedes subir una imagen que no cumpla con lo requisitos" 

        validado = false

    }

})

boton.addEventListener("mousedown", () => {

    if (validado == true){

        if (nombre.value != "") formulario.submit()

        else textoMensaje.textContent = "No puedes dejar en blanco el campo 'Nombre'" 
        
    }

    else textoMensaje.textContent = "Para poder hacer el pedido cumple con los requisitos pedidos" 

})

if (limite != undefined){

    todo.style.pointerEvents = "None"
    document.body.style.overflow = "hidden"

}
