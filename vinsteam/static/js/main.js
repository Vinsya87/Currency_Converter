document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("#conversion-form");
  const resultDiv = document.querySelector("#result");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    fetch("/api/rates", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.result) {
          resultDiv.textContent = `Результат: ${data.result}`;
        } else if (data.error) {
          resultDiv.textContent = `Error: ${data.error}`;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});
