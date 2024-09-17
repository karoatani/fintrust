"use strict";
const menuBar = document.getElementsByClassName("menu-bar")[0];
const navLinks = document.getElementById("nav-links");
const pageContent = document.getElementById("page-content");



menuBar.addEventListener("click", (event) => {
    navLinks.classList.add("flex");
    navLinks.classList.remove("hidden");
    pageContent.add("hidden");
})