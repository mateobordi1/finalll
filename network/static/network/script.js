document.addEventListener('DOMContentLoaded', function(){

    //boton follow and unfollow
    var followButtons = document.querySelectorAll('.follow');

    // Agrega un event listener a cada botón
    followButtons.forEach(button => {

        button.addEventListener('click', function(){

            var follow_following = this.getAttribute("data-state");
            console.log(id_user);

            fetch(`/user/${id_user}`,{
                method : "POST",
                headers: {
                    'Content-Type': 'application/json',
                  },
                body: JSON.stringify({
                    state : follow_following
                })
            })
            .then(response => response.json())
            .then(data => {
                this.innerHTML = data['content'];
                console.log(data['content'] );
                window.location.reload();
                
});
        });
    })

    const MgButtons = document.querySelectorAll('.mg_button');

    MgButtons.forEach(button =>{
        button.addEventListener('click', function(){


            const id_post = this.getAttribute('data-id_post');
            const csrftoken = getCookie('csrftoken');

            fetch(`/update_post/${id_post}`, {
                method : "PUT",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({ }),
            })
            .then(response => response.json())
            .then(data => {


                if (data.state != 0 ){
                    button.classList.add('liked')
                    button.classList.remove('mg_button')
                }
                else{
                    button.classList.remove('liked')
                    button.classList.add('mg_button')
                }


                // Actualizar la cantidad de mg en la interfaz
                const mgCountElement = document.querySelector(`#mg-count-${id_post}`);
                mgCountElement.textContent = data.mg_count;

                // Hacer otras acciones necesarias si es necesario
            })
            .catch(error => {
                console.error('Error:', error);
            });
            })

        })

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    })

    
