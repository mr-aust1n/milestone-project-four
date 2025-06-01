// Home Search
document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("itemSearch");
  const items = document.querySelectorAll("#itemList li");

  input.addEventListener("keyup", function () {
    const query = this.value.toLowerCase();
    items.forEach(function (li) {
      const title = li.querySelector(".item-title").textContent.toLowerCase();
      li.style.display = title.includes(query) ? "" : "none";
    });
  });
});
