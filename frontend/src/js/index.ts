const menuBar  = document.getElementsByClassName("menu-bar")[0];
const navLinks = document.getElementById("navLinks");


console.log(navLinks)
menuBar.addEventListener("click", (event) => {
    // event.preventDefault()
    console.log(event);
    console.log(navLinks)
    // navLinks?.classList.remove("hidden");
    // navLinks?.classList.add("flex");
});