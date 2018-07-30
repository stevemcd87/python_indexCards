$('document').ready(function(){
  // To Create FLIP action
  $(".card-grid").flip({
      trigger: 'manual'
  });
  $(".card-grid").hover(function () {
      $(this).closest(".card-grid").flip('toggle');
  });
  // -----------------------------------
});
