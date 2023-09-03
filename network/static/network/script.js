document.addEventListener('DOMContentLoaded', function(){

    //boton follow and unfollow
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
              .then(data => {
                window.location.reload();

              })


        });
    })



    function getCookie(name) {
        const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return cookieValue ? cookieValue.pop() : '';
      }
    })

    
