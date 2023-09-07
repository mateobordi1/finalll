document.addEventListener('DOMContentLoaded', function(){


    var botones_a_categoria = document.querySelectorAll('.botones_a_categoria');

    // Agrega un event listener a cada botón
    botones_a_categoria.forEach(button => {

        button.addEventListener('click', function(){

            var id_user = this.getAttribute("data-id_user");
            var agregar_quitar = this.innerHTML;
            if (agregar_quitar == "Agregar"){
                estado = true;
            }else{
                estado=false;
            }
            console.log(estado);
            console.log(agregar_quitar);
            const csrfToken = getCookie('csrftoken');

            fetch(`/a_q/${id_user}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json', 
                    'X-CSRFToken': csrfToken },
                body: JSON.stringify({
                    t_f: estado
                })
              })
              .then(response =>response.json())
              .then(result => {

                console.log(result["categoria_estado"])
                if (result["categoria_estado"] == true ){
                    this.innerHTML="Quitar"
                }else{
                    this.innerHTML="Agregar"
                }

              })


        });
    })

    var boton_convocar = document.querySelectorAll('.boton_convocar');

    boton_convocar.forEach(button => {
        button.addEventListener('click', function() {

            var id_categoria = this.getAttribute("data-id_categoria");
            var id_user = this.getAttribute("data-id_user");
            var convocar_desconvocar = this.innerHTML;

            if ( convocar_desconvocar == "Convocar"){
                estado = true;
            }else{
                estado=false;
            }
            console.log(estado);
            console.log(convocar_desconvocar);
            const csrfToken = getCookie('csrftoken');

            fetch(`/convocatoria/${id_categoria}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json', 
                    'X-CSRFToken': csrfToken },
                body: JSON.stringify({
                    c_d: estado ,
                    id_user: id_user 
                })
              })
              .then(response =>response.json())
              .then(result => {

                console.log(result["usuario_convocado"])
                if(result["usuario_convocado"] == true){
                    this.innerHTML="Desconvocar"
                }else{
                    this.innerHTML="Convocar"
                }
                location.reload();
              })
                
        })
    })


    function getCookie(name) {
        const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return cookieValue ? cookieValue.pop() : '';
      }
    })

    
