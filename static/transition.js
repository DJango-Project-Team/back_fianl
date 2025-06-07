// transition.js

function navigateTo(url, boxSelector) {
  const box = document.querySelector(boxSelector);
  if (box) {
    box.classList.add("box-slide-out");
    setTimeout(() => {
      window.location.href = url;
    }, 150);
  } else {
    window.location.href = url;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const box =
    document.querySelector(".signup-box") ||
    document.querySelector(".login-box");
  if (box) {
    box.classList.add("box-slide-in");
  }

  const toLogin = document.getElementById("to-login");
  if (toLogin) {
    toLogin.addEventListener("click", () => {
      navigateTo("login.html", ".signup-box");
    });
  }

  const toSignup = document.getElementById("to-signup");
  if (toSignup) {
    toSignup.addEventListener("click", () => {
      navigateTo("signup.html", ".login-box");
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const fields = [
    { id: "name", placeholder: "이름" },
    { id: "email", placeholder: "이메일" },
    { id: "id", placeholder: "아이디" },
    { id: "password", placeholder: "비밀번호", isPassword: true }
  ];

  fields.forEach(field => {
    const input = document.getElementById(field.id);

    if (!input) return;

    input.addEventListener("focus", () => {
      if (input.value === field.placeholder) {
        input.value = "";
        if (field.isPassword) input.type = "password";
      }
    });

    input.addEventListener("blur", () => {
      if (input.value === "") {
        input.type = field.isPassword ? "text" : input.type;
        input.value = field.placeholder;
      }
    });
  });
});

