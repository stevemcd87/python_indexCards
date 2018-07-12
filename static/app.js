$('document').ready(function(){
  $('.card').click(function(e){
    for (var i = 0; i < e.currentTarget.children.length; i++) {
      if (e.currentTarget.children[i].className) {
        e.currentTarget.children[i].className = "";
      } else {
        e.currentTarget.children[i].className = "hidden";
      }
    }
  })
});
