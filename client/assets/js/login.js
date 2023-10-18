const btnLogin = document.getElementById('btn-login');
const inputUser = document.getElementById('input-user');
const inputPassword = document.getElementById('input-password');

btnLogin.addEventListener('click', function () {
    var username = inputUser.value;
    var password = inputPassword.value;

    var urlApi =    "http://18.215.167.146:3000/login" + 
                    "?username=" + encodeURIComponent(username) + 
                    "&password=" + encodeURIComponent(password);

    $.ajax({
        url: urlApi,
        method: "GET",
        success: function (response) {
            var estado = JSON.parse(response)
            if (estado == true) {
                Swal.fire({
                    icon: 'success',
                    title: 'Login exitoso',
                    text: 'Creedenciales correctas',
                })
                //esperar 2 segundos
                setTimeout(function () {
                    //redireccionar
                    window.location.href = "./log.html"
                }, 2000);
            }else {
                Swal.fire({
                    icon: 'error',
                    title: 'Login fallido',
                    text: 'Creedenciales incorrectas',
                })
            }   
        },
        error: function (error) {
            console.log(error);
        }
    });
});