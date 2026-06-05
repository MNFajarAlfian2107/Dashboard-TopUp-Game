function openPopup(game) {
    document.getElementById("popup").style.display = "flex";
    document.getElementById("game").value = game;
    document.getElementById("game_name").innerText = game;
}

let selectedPrice = 0;

function showGame(game) {
    document.getElementById("popup").style.display = "flex";
    document.querySelectorAll(".nominal-section").forEach(el => {
        el.style.display = "none";
    });
    document.getElementById(game).style.display = "block";
    document.getElementById("game").value = game;
}

function closePopup() {
    document.getElementById("popup").style.display = "none";
}

function selectNominal(nama, harga, el) {
    document.getElementById("nominal").value = nama;
    document.getElementById("total").value = harga;
    document.getElementById("total_text").innerText =
        "Rp " + harga.toLocaleString("id-ID");
    document.querySelectorAll(".nominal-card").forEach(card => {
        card.classList.remove("active");
    });
    el.classList.add("active");
}

function selectPayment(el, method) {
    document.getElementById("payment").value = method;
    document.querySelectorAll(".payment-card").forEach(card => {
        card.classList.remove("active");
    });
    el.classList.add("active");
}