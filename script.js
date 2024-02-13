function handleSubmit(event) {
  event.preventDefault();

  var linkInput = document.getElementById("link").value.trim();

  if (linkInput === "") {
    alert("Please enter the link");
  } else {
    console.log("Link submitted:", linkInput);
  }
}

document
  .getElementById("form-control")
  .addEventListener("submit", handleSubmit);
