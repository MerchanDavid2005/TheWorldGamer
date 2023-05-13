addEventListener("mousedown", (e) => {

    if (e.target.className == "boton_categoria"){

        const formHistorialCategorias = document.querySelector(".categoriasHistorial")
    
        let valor_categoria = document.querySelector(".campo_Categoria")
    
        valor_categoria.setAttribute("value", e.target.value)
    
        formHistorialCategorias.submit()

    }

    if (e.target.className == "boton_limite"){

        const formHistorialTiempos = document.querySelector(".tiempos")
    
        let valor_plazo = document.querySelector(".campo_limite")
    
        valor_plazo.setAttribute("value", e.target.value)
    
        formHistorialTiempos.submit()

    }

})