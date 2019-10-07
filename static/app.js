$('document').ready(function() {
  // To Create FLIP action
  $(".card-grid").flip({
    trigger: 'manual'
  });
  $(".card-grid").click(function() {
    $(this).closest(".card-grid").flip('toggle');
  });
  // -----------------------------------

  $(".user-input").change(function(e) {

    const answer = e.currentTarget.parentElement.classList["0"].replace('-', ' ');
    const userInput = e.currentTarget.value.trim();
    if (answer === userInput) {
      $(e.currentTarget.parentNode.parentNode).addClass('correct');
      $(e.currentTarget.parentNode.parentNode).removeClass('wrong');
      $(e.currentTarget).prop("readonly", true);
    } else {
      $(e.currentTarget.parentNode.parentNode).addClass('wrong');
    }
  })
});