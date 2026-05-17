document.addEventListener("DOMContentLoaded", () => {
  const mainMenu = document.querySelector("#main-menu");
  const menuIcon = document.querySelector(".menu-nav-icon");
  const portfolioNav = document.querySelector(".portfolio-nav");
  const portfolioToggle = document.querySelector(".portfolio-toggle");
  const placeholder = document.querySelector("#portfolio-menu-placeholder");

  menuIcon?.addEventListener("click", (e) => {
    e.preventDefault();
    mainMenu?.classList.toggle("visible-menu");
  });

  portfolioToggle?.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();

    const isOpen = portfolioNav.classList.toggle("is-open");
    portfolioToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });

  document.addEventListener("click", (e) => {
    if (!portfolioNav?.contains(e.target)) {
      portfolioNav?.classList.remove("is-open");
      portfolioToggle?.setAttribute("aria-expanded", "false");
    }
  });

  if (placeholder) {
    const pathPrefix =
      window.location.pathname === "/" ||
      window.location.pathname.endsWith("/index.html")
        ? ""
        : "../";

    fetch(`${pathPrefix}portfolio-menu.html`, { cache: "no-cache" })
      .then((res) => res.text())
      .then((html) => {
        placeholder.innerHTML = html;
      });
  }
});

portfolioToggle?.addEventListener("click", (e) => {
  e.preventDefault();
  e.stopPropagation();

  const isOpen = portfolioNav.classList.toggle("is-open");

  portfolioToggle.setAttribute(
    "aria-expanded",
    isOpen ? "true" : "false"
  );

  portfolioToggle.classList.toggle("menu-open", isOpen);
});