(function () {
  const a = document.getElementById("email-pill");
  if (!a) return;

const gmail =
  "https://mail.google.com/mail/?view=cm&fs=1" +
  "&to=peikos.georgios@gmail.com" +
  "&su=%5BWebsite%20Contact%5D" +
"&body=Hello%2C%20and%20thank%20you%20for%20reaching%20out.%20Please%20keep%20the%20subject%20tag%20%5BWebsite%20Contact%5D%20so%20I%20can%20filter%20your%20message%20and%20reply%20faster.%20I%20am%20available%20during%20standard%20working%20hours%2C%20and%20I%20will%20get%20back%20to%20you%20as%20soon%20as%20possible.%20Many%20thanks%2C%20Georgios";

  a.addEventListener("click", function (e) {
    try {
      window.open(gmail, "_blank", "noopener,noreferrer");
      e.preventDefault();
    } catch (err) {
      // fallback to default href (mailto)
    }
  });
})();