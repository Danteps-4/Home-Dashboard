const sidebar = document.querySelector(".sidebar");
const togleBtn = document.querySelector(".toggle-btn");

toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("active");
})