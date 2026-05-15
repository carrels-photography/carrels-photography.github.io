document.addEventListener("DOMContentLoaded", async () => {
  const placeholder = document.getElementById("portfolio-menu-placeholder");
  if (!placeholder) return;

  const pathPrefix = window.location.pathname === "/" ? "" : "../";
  const res = await fetch(`${pathPrefix}portfolio-menu.html`, {
    cache: "no-cache",
  });

  placeholder.innerHTML = await res.text();

  const dropdown = placeholder.closest(".drop-down");
  const toggle = dropdown.querySelector(".portfolio-toggle, > a");

  if (!toggle) return;

  toggle.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();

    dropdown.classList.toggle("is-open");

    if (toggle.hasAttribute("aria-expanded")) {
      toggle.setAttribute(
        "aria-expanded",
        dropdown.classList.contains("is-open") ? "true" : "false"
      );
    }
  });
});