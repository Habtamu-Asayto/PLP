function miaw() {
  const form = document.getElementById("registerForm");
  const email = document.getElementById("email");
  const password = document.getElementById("password");
  const confirmPassword = document.getElementById("confirmPassword");

  const emailError = document.getElementById("emailError");
  const passwordError = document.getElementById("passwordError");
  const confirmError = document.getElementById("confirmError");

  const togglePassword = document.getElementById("togglePassword");
  const strengthBar = document.getElementById("strengthBar");

  // Show/hide password toggle
  togglePassword.addEventListener("click", () => {
    const type = password.type === "password" ? "text" : "password";
    password.type = type;
    togglePassword.textContent = type === "password" ? "Show" : "Hide";
  });

  // Password strength checker
  password.addEventListener("input", () => {
    const val = password.value;
    let strength = 0;

    if (val.match(/[a-z]/)) strength++;
    if (val.match(/[A-Z]/)) strength++;
    if (val.match(/[0-9]/)) strength++;
    if (val.match(/[^a-zA-Z0-9]/)) strength++;
    if (val.length >= 8) strength++;

    const colors = ["red", "orange", "yellow", "lightgreen", "green"];
    strengthBar.style.width = strength * 20 + "%";
    strengthBar.style.background = colors[strength - 1] || "transparent";
  });

  // Custom validation
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    let valid = true;

    // Email validation
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.value.match(emailPattern)) {
      emailError.textContent = "Enter a valid email address.";
      valid = false;
    } else {
      emailError.textContent = "";
    }

    // Password validation
    const passVal = password.value;
    const passPattern =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$/;
    if (!passVal.match(passPattern)) {
      passwordError.textContent =
        "Password must be 8+ chars, include upper, lower, number & symbol.";
      valid = false;
    } else {
      passwordError.textContent = "";
    }

    // Confirm password
    if (password.value !== confirmPassword.value) {
      confirmError.textContent = "Passwords do not match.";
      valid = false;
    } else {
      confirmError.textContent = "";
    }

    if (valid) {
      alert("Successful");
      form.reset();
      strengthBar.style.width = "0%";
    }
  });
}
