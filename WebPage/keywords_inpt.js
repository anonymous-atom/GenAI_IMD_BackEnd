// keywords_inpt.js

document.addEventListener("DOMContentLoaded", function () {
    const keywordInput = document.getElementById("keywords");
    const addKeywordButton = document.querySelector(".add-keyword");
    const addedKeywordsContainer = document.getElementById("added-keywords");

    addKeywordButton.addEventListener("click", function () {
        if (keywordInput.value.trim() !== "") {
            const keyword = keywordInput.value.trim();
            const keywordElement = document.createElement("div");
            keywordElement.classList.add("keyword");
            keywordElement.innerHTML = `
                ${keyword}
                <button class="remove-keyword-button" aria-label="Remove Keyword">[X]</button>
            `;

            keywordInput.value = "";
            keywordInput.placeholder = "Keyword";

            keywordElement.querySelector(".remove-keyword-button").addEventListener("click", function () {
                addedKeywordsContainer.removeChild(keywordElement);
            });

            addedKeywordsContainer.appendChild(keywordElement);
        }
    });

    keywordInput.addEventListener("keyup", function (event) {
        if (event.key === "Enter") {
            addKeywordButton.click();
        }
    });

});
