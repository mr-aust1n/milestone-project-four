document.addEventListener("DOMContentLoaded", function () {
  const bell = document.getElementById("bellButton");
  const dropdown = document.getElementById("notificationDropdown");

  if (bell && dropdown) {
    bell.addEventListener("click", function (e) {
      e.stopPropagation();
      dropdown.style.display =
        dropdown.style.display === "block" ? "none" : "block";
    });

    document.addEventListener("click", function () {
      dropdown.style.display = "none";
    });
  }
});
