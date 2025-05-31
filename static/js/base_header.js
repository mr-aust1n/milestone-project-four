document.addEventListener("DOMContentLoaded", function () {
  // Toggle notifications dropdown
  document.querySelector("#bellButton").addEventListener("click", function () {
    document.querySelector(".notification-bell").classList.toggle("active");
  });

  // Toggle mobile nav menu
  document.querySelector(".nav-toggle").addEventListener("click", function () {
    document.querySelector(".site-nav").classList.toggle("active");
  });
});
