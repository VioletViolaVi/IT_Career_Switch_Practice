document.addEventListener("DOMContentLoaded", function () {
  function drawMe() {
    let canvas = document.getElementById("myCanvas");
    if (canvas.getContext) {
      let ctx = canvas.getContext("2d");
      ctx.fillStyle = "purple";
      ctx.font = "bold 5em Arial";
      ctx.fillText("City High", 10, 80);
      ctx.fillStyle = "rgba(231, 152, 95, 0.24)";
      ctx.fillRect(99, 88, 120, 70);
    }
  }
  drawMe();

  // document.write("This is a document.write thing");
  // document.write("<br>")
  // document.write("This is also <b><em>another</em></b> document.write thing");
  // document.write("<p>This is a paragraph element</p>");
  // document.write("<h2>This is a h2 element<h2>");
  // document.write(document.lastModified);
});
