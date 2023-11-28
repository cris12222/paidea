// Obtén todos los elementos de encabezado del acordeón
const accordionHeaders = document.querySelectorAll(".accordion-header");

// Agrega un evento de clic a cada encabezado
accordionHeaders.forEach(header => {
    header.addEventListener("click", function() {
        // Encuentra el elemento de contenido asociado
        const content = this.nextElementSibling;

        // Cambia la visibilidad del contenido al hacer clic en el encabezado
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
});
