const browseButton = document.getElementById("browse-btn");
const executeButton = document.getElementById("exec-btn");
const inputFile = document.getElementById("file-input");
const filePathInput = document.getElementById("file-path");
const entryArea = document.getElementById("entry-data-area");
const outArea = document.getElementById("out-area");

browseButton.addEventListener("click", function () {
    inputFile.click();
});


inputFile.addEventListener("change", function () {
    const selectedFile = inputFile.files[0];
    if (selectedFile) {
        // Establecer la ruta del archivo en el input
        filePathInput.value = selectedFile.name;

        // Leer y mostrar el contenido del archivo en el textarea
        const reader = new FileReader();
        reader.onload = function (e) {
            entryArea.value = e.target.result;
        };
        reader.readAsText(selectedFile);
    }
});

executeButton.addEventListener("click", function () {
    outArea.value = "Analizando..."
    var comando = entryArea.value;
    var urlApi = "http://18.215.167.146:3000/execute" + "?comando=" + encodeURIComponent(comando);

    $.ajax({
        url: urlApi,
        method: "GET",
        success: function (response) {
            outArea.value = response;
        },
        error: function (error) {
            console.log(error);
        }
    });
});