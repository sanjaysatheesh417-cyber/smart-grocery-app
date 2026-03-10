// -------------------- TOTAL CALCULATION --------------------

function calculateTotal() {

let rows = document.querySelectorAll("table tr");
let total = 0;

rows.forEach((row, i) => {

if (i === 0) return; // skip header row

let checkbox = row.querySelector(".select");
let price = row.querySelector(".price");
let qty = row.querySelector(".qty");

if (!checkbox || !price || !qty) return;

if (checkbox.checked) {

let itemPrice = parseFloat(price.innerText);
let quantity = parseInt(qty.value) || 0;

total += itemPrice * quantity;

}

});

document.getElementById("total").innerText = total;


// -------------------- BUDGET CHECK --------------------

let budget = document.getElementById("budget");

if (budget) {

let budgetValue = parseFloat(budget.value);

if (budgetValue) {

if (total > budgetValue) {

document.getElementById("budgetStatus").innerText = "Budget exceeded";
document.getElementById("budgetStatus").style.color = "red";

} else {

document.getElementById("budgetStatus").innerText = "Within budget";
document.getElementById("budgetStatus").style.color = "green";

}

}

}

}


// -------------------- TRANSLATION FUNCTION --------------------

async function translateWord() {

let text = document.getElementById("translateText").value.trim().toLowerCase();

if (!text) {
alert("Please enter a word");
return;
}

try {

let res = await fetch("/translate", {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify({ text: text })
});

let data = await res.json();

document.getElementById("translationResult").innerText = data.translation;

} catch (error) {

console.error("Translation error:", error);
document.getElementById("translationResult").innerText = "Error translating";

}

}


// -------------------- EVENT LISTENERS --------------------

document.addEventListener("DOMContentLoaded", () => {

let calcBtn = document.getElementById("calculateBtn");
if (calcBtn) {
calcBtn.addEventListener("click", calculateTotal);
}

let translateBtn = document.getElementById("translateBtn");
if (translateBtn) {
translateBtn.addEventListener("click", translateWord);
}

});


// -------------------- SERVICE WORKER --------------------

if ("serviceWorker" in navigator) {

navigator.serviceWorker.register("/static/sw.js")
.then(() => console.log("Service Worker Registered"))
.catch(err => console.log("Service Worker Failed:", err));

}