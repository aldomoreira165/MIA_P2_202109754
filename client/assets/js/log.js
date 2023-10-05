//ejecutar al cargar la pagina
window.onload = function () {
    $.ajax({
        url: "http://127.0.0.1:5000/getReportes",
        method: "GET",
        success: function (response) {
            const imagenes = response.imagenes;
            const listaReportes = document.getElementById('lista-reportes');

            // Recorrer las imágenes y agregarlas a la lista
            imagenes.forEach(function (imagen) {
                // Crear un elemento de lista
                const listItem = document.createElement('li');

                // Crear un enlace de descarga
                const downloadLink = document.createElement('a');
                downloadLink.href = 'data:image/png;base64,' + imagen.contenidoBase64; // Cambia 'image/png' según el tipo de imagen
                downloadLink.download = imagen.nombre;
                downloadLink.textContent = imagen.nombre;

                // Agregar el enlace de descarga al elemento de lista
                listItem.appendChild(downloadLink);

                // Agregar el elemento de lista a la lista de reportes
                listaReportes.appendChild(listItem);
            });

        },
        error: function (error) {
            console.log(error);
        }
    });
}