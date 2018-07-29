$('document').ready(function(){

  $(".card-grid").flip({
      trigger: 'manual'
  });
  $(".card-grid").click(function () {
      $(this).closest(".card-grid").flip('toggle');
  });
  // $(".card-grid").click(function () {
  //     $(this).closest(".card-grid").flip(false);
  // });
  console.log('change');
});
