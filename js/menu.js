document.addEventListener("DOMContentLoaded", async () => {
  const mainMenu = document.querySelector("#main-menu");
  const menuIcon = document.querySelector(".menu-nav-icon");
  const placeholder = document.getElementById("portfolio-menu-placeholder");

  // Load portfolio submenu
  if (placeholder) {
    const pathPrefix =
      window.location.pathname === "/" ||
      window.location.pathname.endsWith("/index.html")
        ? ""
        : "../";

    const res = await fetch(`${pathPrefix}portfolio-menu.html`, {
      cache: "no-cache",
    });

    placeholder.innerHTML = await res.text();
  }

  const dropdown = document.querySelector(".drop-down");
  const toggle = document.querySelector(".portfolio-toggle");

  // Hamburger menu
  if (menuIcon && mainMenu) {
    menuIcon.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();

      mainMenu.classList.toggle("visible-menu");

      if (dropdown && toggle) {
        dropdown.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Portfolio submenu
  if (toggle && dropdown) {
    toggle.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();

      const isOpen = dropdown.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }
});