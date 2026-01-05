// js/menu.js
document.addEventListener("DOMContentLoaded", async () => {
    const placeholder = document.getElementById("portfolio-menu-placeholder");
    if (!placeholder) return; // page doesn't have the menu
  
    // load menu HTML
    const res = await fetch("../portfolio-menu.html", { cache: "no-cache" });
    placeholder.innerHTML = await res.text();
  
    // dropdown toggle (works even after fetch)
    document.querySelectorAll(".drop-down > a").forEach((a) => {
      a.addEventListener("click", (e) => {
        e.preventDefault();
        const submenu = a.nextElementSibling; // the <ul>
        if (!submenu) return;
        submenu.classList.toggle("open");
      });
    });
  });