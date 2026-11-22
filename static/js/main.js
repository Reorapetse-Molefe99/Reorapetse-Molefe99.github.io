/* CV website interactions: loader, navbar, typing effect, scroll reveal,
   counters, tabs, portrait tilt and copy-to-clipboard. No external libraries. */
(function () {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const body = document.body;

  /* ---------- Loader ---------- */
  // Short branded intro: hide as soon as the page is ready (this script runs on
  // DOMContentLoaded), without waiting for fonts or images.
  setTimeout(() => body.classList.remove("is-loading"), reduceMotion ? 0 : 650);

  /* ---------- Navbar: solid on scroll, hide on scroll down ---------- */
  const nav = document.querySelector(".nav");
  let lastY = window.scrollY;
  function onScroll() {
    const y = window.scrollY;
    nav.classList.toggle("scrolled", y > 40);
    nav.classList.toggle("hidden", y > lastY && y > 500 && !body.classList.contains("menu-open"));
    lastY = y;
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile menu ---------- */
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.querySelector(".mobile-menu");
  function setMenu(open) {
    body.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    menu.setAttribute("aria-hidden", String(!open));
  }
  toggle.addEventListener("click", () => setMenu(!body.classList.contains("menu-open")));
  menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setMenu(false)));
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") setMenu(false); });

  /* ---------- Active nav link ---------- */
  const navLinks = Array.from(document.querySelectorAll(".nav-links a"));
  const sections = navLinks.map((a) => document.querySelector(a.getAttribute("href"))).filter(Boolean);
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      navLinks.forEach((a) => a.classList.toggle("active", a.getAttribute("href") === "#" + entry.target.id));
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  sections.forEach((s) => sectionObserver.observe(s));

  /* ---------- Typing effect ---------- */
  const typed = document.querySelector(".typed");
  if (typed && !reduceMotion) {
    const roles = JSON.parse(typed.dataset.roles || "[]");
    let r = 0, i = roles[0] ? roles[0].length : 0, deleting = true;
    const tick = () => {
      const word = roles[r];
      i += deleting ? -1 : 1;
      typed.textContent = word.slice(0, i);
      let delay = deleting ? 35 : 75;
      if (!deleting && i === word.length) { deleting = true; delay = 2200; }
      else if (deleting && i === 0) { deleting = false; r = (r + 1) % roles.length; delay = 350; }
      setTimeout(tick, delay);
    };
    if (roles.length > 1) setTimeout(tick, 2600);
  }

  /* ---------- Scroll reveal ---------- */
  const revealObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.classList.add("in"); obs.unobserve(entry.target); }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  document.querySelectorAll(".reveal").forEach((el) => revealObserver.observe(el));

  /* ---------- Count-up numbers ---------- */
  const counters = document.querySelectorAll(".count");
  function animateCount(el) {
    const target = parseFloat(el.dataset.value);
    const decimals = parseInt(el.dataset.decimals || "0", 10);
    const duration = 1600;
    const start = performance.now();
    const step = (now) => {
      const t = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - t, 4);
      el.textContent = (target * eased).toFixed(decimals);
      if (t < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }
  if (!reduceMotion) {
    counters.forEach((el) => { el.textContent = (0).toFixed(parseInt(el.dataset.decimals || "0", 10)); });
    const countObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) { animateCount(entry.target); obs.unobserve(entry.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach((el) => countObserver.observe(el));
  }

  /* ---------- Tabs (career roles + research summary) ---------- */
  function activate(tabs, panels, index) {
    tabs.forEach((t, j) => {
      t.classList.toggle("active", j === index);
      t.setAttribute("aria-selected", String(j === index));
      t.tabIndex = j === index ? 0 : -1;
    });
    panels.forEach((p, j) => {
      p.hidden = j !== index;
      p.classList.toggle("active", j === index);
    });
  }
  function setupTabs(tabs, panels) {
    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => {
        activate(tabs, panels, index);
        tab.scrollIntoView({ block: "nearest", inline: "nearest", behavior: reduceMotion ? "auto" : "smooth" });
      });
      tab.addEventListener("keydown", (e) => {
        const keys = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 };
        if (!(e.key in keys)) return;
        e.preventDefault();
        const next = (index + keys[e.key] + tabs.length) % tabs.length;
        activate(tabs, panels, next);
        tabs[next].focus();
      });
    });
  }
  setupTabs(Array.from(document.querySelectorAll(".career-tab")),
            Array.from(document.querySelectorAll(".career-panel")));
  const rTabs = Array.from(document.querySelectorAll(".tabs .tab"));
  setupTabs(rTabs, rTabs.map((t) => document.getElementById(t.dataset.tab)));

  /* ---------- Portrait tilt (desktop pointer only) ---------- */
  const tilt = document.querySelector(".tilt");
  if (tilt && !reduceMotion && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    const hero = document.querySelector(".hero");
    hero.addEventListener("mousemove", (e) => {
      const r = tilt.getBoundingClientRect();
      const x = (e.clientX - (r.left + r.width / 2)) / window.innerWidth;
      const y = (e.clientY - (r.top + r.height / 2)) / window.innerHeight;
      tilt.style.transform = `perspective(900px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg)`;
    });
    hero.addEventListener("mouseleave", () => { tilt.style.transform = ""; });
  }

  /* ---------- Copy email ---------- */
  document.querySelectorAll("[data-copy]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const label = btn.querySelector(".contact-v");
      const original = label.textContent;
      try {
        await navigator.clipboard.writeText(btn.dataset.copy);
        label.textContent = "Copied to clipboard ✓";
      } catch (err) {
        label.textContent = btn.dataset.copy;
      }
      setTimeout(() => { label.textContent = original; }, 2200);
    });
  });
})();
