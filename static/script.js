document.addEventListener("DOMContentLoaded", function () {
    let yesButton = document.querySelector(".yes");
    let noButton = document.querySelector(".no");

    if (!yesButton || !noButton) {
        console.error("Buttons not found! Check if HTML structure is correct.");
        return;
    }

    noButton.addEventListener("click", function () {
        let currentSize = parseFloat(window.getComputedStyle(yesButton).fontSize);
        yesButton.style.fontSize = (currentSize + 10) + "px";
    });

    yesButton.addEventListener("click", function () {
        fetch("http://127.0.0.1:5000/submit", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ response: "Yes" })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to submit response");
            }
            return response.json();
        })
        .then(data => {
            console.log("Success:", data);
            document.body.innerHTML = "<h1>Yay! Happy Valentine's Day! ❤️</h1>";
        })
        .catch(error => console.error("Error:", error));
    });
});
