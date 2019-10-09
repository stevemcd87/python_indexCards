$('document').ready(function() {
  // To Create FLIP action
  $(".card-grid").flip({
    trigger: 'manual'
  });
  $(".card-grid").click(function() {
    if ($(this).hasClass('test')) return false
    $(this).closest(".card-grid").flip('toggle');
  });
  // -----------------------------------

  $(".user-input").change(function() {
    let userInput = $(this)["0"].value,
      answer = $(this).siblings(".answer")[0].innerText.trim();
    if (answer === userInput) {
      $(this).closest(".card-grid")
        .addClass('correct')
        .removeClass('incorrect')
        .find('.incorrect-image').hide();
      $(this).closest(".card-grid").find('.correct-image').show();
      $(this).prop("readonly", true);
    } else {
      $(this).closest(".card-grid")
        .addClass('incorrect')
        .find('.incorrect-image').show();
    }
  })
});