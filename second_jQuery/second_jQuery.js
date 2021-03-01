$("document").ready(function () {
  /****************************************************************************************************/

  function sayingHello() {
    $("#firstHeading").dblclick(function () {
      $(this).html("Goodbye World!");
    });
  }
  sayingHello();

  /****************************************************************************************************/

  function changeParaColours() {
    $("#paraColoursBtn").click(function () {
      $("#secondSection p").toggle();
    });
  }
  changeParaColours();

  function alertBtn() {
    $("#alertBtn").click(function () {
      alert($("#secondSection p:first").html());
    });
  }
  alertBtn();

  /****************************************************************************************************/

  function getAnchorValue() {
    let anchorValue = $("#anchorLink").attr("href");
    console.log(anchorValue);
  }
  getAnchorValue();

  /****************************************************************************************************/

  function changeHeadingTwo() {
    $("#fourthSection h2").click(function () {
      $(this).text("This text got changed when you clicked on the button.");
    });
  }
  changeHeadingTwo();

  /****************************************************************************************************/

  function changePara() {
    $("#fifthSection p").click(function () {
      $(this).html("<p>This is a para tag from jQuery.</p>");
    });
  }
  changePara();

  function inputId() {
    $("#inputIdBtn").click(function () {
      $("#inputId").val("told you it'll change");
    });
  }
  inputId();

  /****************************************************************************************************/

  function appendList() {
    $("#appendBtn").click(function () {
      $("ol").append(
        '<li class="addedClass">this was <b><em>appended</em></b></li>'
      );
    });
  }
  appendList();

  function prependList() {
    $("#prependBtn").click(function () {
      $("ol").prepend(
        '<li class="addedClass">this was <b><em>prepended</em></b></li>'
      );
    });
  }
  prependList();

  function removeList() {
    $("#removeBtn").click(function () {
      $(".addedClass").remove();
    });
  }
  removeList();

  /****************************************************************************************************/

  function appendingTextInGrownBox() {
    $(this).append(
      "<p style='text-align:center'>The box grew longer and showed this text AFTER using the CALLBACK function!</p>"
    );
  }

  function appendingTextInShrunkBox() {
    $(this).append(
      "<p style='text-align:center'>The box shrunk shorter and showed this text AFTER using the CALLBACK function!</p>"
    );
  }

  function growingBox() {
    $("#grow").click(function () {
      $("#growingAndShrinkingBox").animate(
        {
          width: "40em",
        },
        3000,
        "linear",
        appendingTextInGrownBox
      );
      $("div p").remove();
    });
  }
  growingBox();

  function shrinkingBox() {
    $("#shrink").click(function () {
      $("#growingAndShrinkingBox").animate(
        {
          width: "6em",
          height: "9em",
        },
        900,
        "swing",
        appendingTextInShrunkBox
      );
      $("div p").remove();
    });
  }
  shrinkingBox();

  /****************************************************************************************************/
  
  function accordionPractice() {
    $("#accordion").accordion();
  }  
  accordionPractice();
  
  /****************************************************************************************************/
});
