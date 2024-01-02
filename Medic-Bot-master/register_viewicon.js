
function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var togglePassword = document.querySelector(".toggle-password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.style.backgroundImage = "url(eye-password.png)"; /* Replace with your closed eye icon */
    } else {
        passwordInput.type = "password";
        togglePassword.style.backgroundImage = "url(eye.png)"; /* Replace with your open eye icon */
    }
}
function PasswordVisibility() {
    var passwordInput = document.getElementById("confirm_password");
    var togglePassword = document.querySelector(".toggle-password");
    if (passwordInput.type === "confirm_password") {
        passwordInput.type = "text";
        togglePassword.style.backgroundImage = "url(eye-password.png)"; /* Replace with your closed eye icon */
    } else {
        passwordInput.type = "confrim_password";
        togglePassword.style.backgroundImage = "url(eye.png)"; /* Replace with your open eye icon */
    }
}

