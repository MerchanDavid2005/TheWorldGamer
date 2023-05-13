const todo = document.getElementById("juegos-todo")

const menu = document.querySelector(".juegos-todo-menu")

const juegos = document.querySelector(".juegos-todo-juegos")

addEventListener("mousedown", (e) => {

    objeto = e.target.className

    index = objeto.split("alquilar")

    i = index[1]

    if (e.target.className == `selector-alquilar${i}`){ 

        let selector = document.querySelector(`.selector-alquilar${i}`)

        let precio = document.querySelector(`.Precio${i}`)

        let valor = e.target.attributes[2].value

        let total = 0
    
        addEventListener("change", () => {
        
            if (selector.value == "value1"){ total = valor}
                
            else if (selector.value == "value2"){ total = (valor * 2) * 0.95}
                
            else if (selector.value == "value3"){ total = (valor * 3) * 0.93}
                
            else if (selector.value == "value4"){ total = (valor * 4) * 0.90}
                
            else if (selector.value == "value5"){ total = (valor * 5) * 0.85}
                
            else if (selector.value == "value6"){ total = (valor * 6) * 0.80}

            precio.innerHTML = total
                
        })

    } 
    
    if (e.target.className == `juegos-todo-juegos-game-boton_alquilar${i}`){

        // --------------------------------------- Crear contenedores ---------------------------------------

        let divConfirmacion = document.createElement("DIV")

        divConfirmacion.classList.add("Div-confirmacion")

        let textoConfirmacion = document.createElement("DIV")

        textoConfirmacion.classList.add("informacion-confirmacion")

        let valoresFormulario = document.createElement("DIV")

        valoresFormulario.classList.add("valores-formulario")

        let imagenConfirmacion = document.createElement("DIV")

        imagenConfirmacion.classList.add("imagen-confirmacion")

        let cerrar = document.createElement("BUTTON")

        cerrar.classList.add("Cerrar")

        // -------------------------------------------------- Tomar valores ------------------------------

        let nombreConfirmacion = document.querySelector(`.juegos-todo-juegos-game-Nombre${i}`)

        let seccionConfirmacion = document.querySelector(`.juegos-todo-juegos-game-Seccion${i}`)

        let precioConfirmacion = document.querySelector(`.Precio${i}`)

        let tiempoConfirmacion = document.querySelector(`.selector-alquilar${i}`)

        let formularioConfirmacion = document.querySelector(".formulario_confirmado")

        let imgConfirmacion = document.querySelector(`.juegos-todo-juegos-game-imagen_juego${i}`)

        // ----------------------------------------------------- Editar contenedores ------------------------

        if (tiempoConfirmacion.value == "value1"){ textoTiempo = "7 dias"}
        else if (tiempoConfirmacion.value == "value2"){ textoTiempo = "15 dias"}
        else if (tiempoConfirmacion.value == "value3"){ textoTiempo = "1 mes"}
        else if (tiempoConfirmacion.value == "value4"){ textoTiempo = "3 meses"}
        else if (tiempoConfirmacion.value == "value5"){ textoTiempo = "6 meses"}
        else if (tiempoConfirmacion.value == "value6"){ textoTiempo = "1 año"}

        formularioConfirmacion.setAttribute("action", `/alquilado/${i}`)

        textoConfirmacion.innerHTML = `
        
        <h1> ${nombreConfirmacion.innerHTML} </h1>

        <h2> ${seccionConfirmacion.innerHTML} </h2>`

        valoresFormulario.innerHTML = `
            
        <p> Por un precio de: <b> ${precioConfirmacion.innerHTML} </b> </p>

        <input type="hidden" name="precio_confirmar" value="${precioConfirmacion.innerHTML}">

        <p> Por un tiempo de: <b> ${textoTiempo} </b> </p>

        <input type="hidden" name="tiempo_confirmar" value="${textoTiempo}">

        <input class="confirmado" type="submit" value="Confirmar"> `

        imagenConfirmacion.innerHTML = imgConfirmacion.innerHTML

        cerrar.textContent = "X"

        // ---------------------------------------------------------- Unir contenedores ---------------------------------

        imagenConfirmacion.append(cerrar)

        formularioConfirmacion.append(valoresFormulario)
        
        textoConfirmacion.append(formularioConfirmacion)

        divConfirmacion.append(textoConfirmacion)

        divConfirmacion.append(imagenConfirmacion)

        todo.append(divConfirmacion)

        menu.style.pointerEvents = "none"

        menu.style.filter = "blur(15px)"

        juegos.style.pointerEvents = "none"

        juegos.style.filter = "blur(15px)"

        document.body.style.overflow = "hidden"

    }

    if(e.target.className == "Cerrar"){

        let divConfirmado = document.querySelector(".Div-confirmacion")

        let limpiarFormulario = document.querySelector(".valores-formulario")

        let salvarFormulario = document.querySelector(".formulario_confirmado")

        todo.append(salvarFormulario)

        limpiarFormulario.remove()

        divConfirmado.remove()

        menu.style.pointerEvents = "all"

        menu.style.filter = "blur(0)"

        juegos.style.pointerEvents = "all"

        juegos.style.filter = "blur(0)"

        document.body.style.overflow = "auto"

    }

    if (e.target.className == "boton_cambio"){

        const filtros = document.querySelector("#Filtros")

        let valor = document.querySelector(".Categoria")

        valor.setAttribute("value", e.target.value)

        filtros.submit()
        
    }

})

setTimeout(() => {

    let alquilado = document.querySelector(".alquilado") 

    if (alquilado != undefined){

        alquilado.style.color = "transparent"
        alquilado.style.transitionProperity = "color"
        alquilado.style.transitionDuration = "4.5s"
            
    }

}, 300)

setTimeout(() => {

    let alquilado = document.querySelector(".alquilado")
    alquilado.remove()

},4900)


