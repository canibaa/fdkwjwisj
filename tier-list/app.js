const participants = [
  { id: "demo-1", name: "Ученик 1", photo: "" },
  { id: "demo-2", name: "Ученик 2", photo: "" },
  { id: "demo-3", name: "Ученик 3", photo: "" },
  { id: "demo-4", name: "Ученик 4", photo: "" },
  { id: "demo-5", name: "Ученик 5", photo: "" },
  { id: "demo-6", name: "Ученик 6", photo: "" }
];

const tiers = ["S","A","B","C","D"];
const pool = document.querySelector("#pool");
const tierItems = [...document.querySelectorAll(".tier-items")];
const tierView = document.querySelector("#tierView");
const cardView = document.querySelector("#cardView");
const singleCard = document.querySelector("#singleCard");
const progressText = document.querySelector("#progressText");
const resultsDialog = document.querySelector("#resultsDialog");

function makeCard(person) {
  const el = document.createElement("article");
  el.className = "card";
  el.draggable = true;
  el.dataset.id = person.id;
  const photo = person.photo || "data:image/svg+xml," + encodeURIComponent(
    '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="500"><rect width="100%" height="100%" fill="#303641"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="#aeb7c7" font-size="28">PHOTO</text></svg>'
  );
  el.innerHTML = '<img alt=""><div class="card-name"></div>';
  el.querySelector("img").src = photo;
  el.querySelector(".card-name").textContent = person.name;
  el.addEventListener("dragstart", e => e.dataTransfer.setData("text/plain", person.id));
  return el;
}

function render() {
  pool.innerHTML = "";
  tierItems.forEach(x => x.innerHTML = "");
  participants.forEach(person => pool.appendChild(makeCard(person)));
}
render();

document.addEventListener("dragover", e => {
  if (e.target.closest(".tier-items,.pool")) e.preventDefault();
});
document.addEventListener("drop", e => {
  const target = e.target.closest(".tier-items,.pool");
  if (!target) return;
  e.preventDefault();
  const id = e.dataTransfer.getData("text/plain");
  const card = document.querySelector('.card[data-id="' + CSS.escape(id) + '"]');
  if (card) target.appendChild(card);
});

document.querySelectorAll(".mode").forEach(btn => btn.addEventListener("click", () => {
  document.querySelectorAll(".mode").forEach(x => x.classList.remove("active"));
  btn.classList.add("active");
  const mode = btn.dataset.mode;
  tierView.classList.toggle("hidden", mode !== "tier");
  document.querySelector(".pool-section").classList.toggle("hidden", mode !== "tier");
  document.querySelector("#submitBtn").classList.toggle("hidden", mode !== "tier");
  cardView.classList.toggle("hidden", mode !== "cards");
  if (mode === "cards") startCardMode();
}));

let cardIndex = 0;
const cardVotes = {};
function startCardMode() {
  cardIndex = 0;
  Object.keys(cardVotes).forEach(k => delete cardVotes[k]);
  showNextCard();
}
function showNextCard() {
  if (cardIndex >= participants.length) {
    singleCard.innerHTML = '<div class="notice"><strong>Готово.</strong><p>Все участники оценены. Здесь позже будет отправка результатов.</p></div>';
    progressText.textContent = participants.length + " / " + participants.length;
    return;
  }
  const person = participants[cardIndex];
  const wrap = document.createElement("div");
  wrap.className = "single-card-wrap";
  wrap.appendChild(makeCard(person));
  singleCard.replaceChildren(wrap);
  progressText.textContent = (cardIndex + 1) + " / " + participants.length;
}
document.querySelectorAll(".tier-buttons button").forEach(btn => btn.addEventListener("click", () => {
  if (cardIndex >= participants.length) return;
  cardVotes[participants[cardIndex].id] = btn.dataset.tier;
  cardIndex++;
  showNextCard();
}));

document.querySelector("#submitBtn").addEventListener("click", () => {
  const placed = document.querySelectorAll(".tier-items .card").length;
  if (placed !== participants.length) {
    alert("Сначала распределите всех участников по тирам.");
    return;
  }
  alert("Демо-режим: подключение Supabase и отправка голосов будет добавлено следующим этапом.");
});

document.querySelector("#resultsBtn").addEventListener("click", () => resultsDialog.showModal());
document.querySelector("#closeResults").addEventListener("click", () => resultsDialog.close());