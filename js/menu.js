document.addEventListener("DOMContentLoaded", async () => {
  const placeholder = document.getElementById("portfolio-menu-placeholder");
  if (!placeholder) return;

  const pathPrefix = window.location.pathname === "/" ? "" : "../";

  const res = await fetch(`${pathPrefix}portfolio-menu.html`, {
    cache: "no-cache",
  });

  placeholder.innerHTML = await res.text();

  const dropdown = placeholder.closest(".drop-down");
  const toggle = dropdown.querySelector(".portfolio-toggle");

  if (!toggle) return;

  toggle.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();

    const isOpen = dropdown.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });
});