// script.js

function includeHTML(file, containerId) {
    fetch(file)
        .then(response => response.text())
        .then(data => {
            document.getElementById(containerId).innerHTML = data;
        })
        .catch(error => console.error(error));
}

document.addEventListener("DOMContentLoaded", function () {
    includeHTML("header.html", "header-container");
    includeHTML("main.html", "main-container");
    includeHTML("footer.html", "footer-container");
});
