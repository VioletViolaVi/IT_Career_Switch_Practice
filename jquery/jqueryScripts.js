// waits until DOM has been fully loaded
$("document").ready(function () {
  // $("#gallery a").hover(function () {
  //   let galleryHref = $(this).attr("href");
  //   let galleryAlt = $(this).attr("title");
  //   $("figure img").attr("src", galleryHref, "alt", galleryAlt);
  //   $("figcaption").text(galleryAlt);
  // });

  $("#gallery a").click(function () {
    let galleryHref = $(this).attr("href");
    let galleryAlt = $(this).attr("title");
    $("figure").css("display", "none");
    $("figure img").attr("src", galleryHref, "alt", galleryAlt);
    $("figcaption").text(galleryAlt);
    $("figure").fadeToggle(1000);
    return false;
  });

  $("form").validate();
});
