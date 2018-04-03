$(document).ready(function() {
    $('.main-tree__element').click(function() {
      $(this).siblings().removeClass('selected');
      $(this).siblings().removeClass('line__visible');
      $(this).addClass('selected');
      var identificator = $(this).attr('id');
      $('.' + identificator + '__inner').addClass('line__visible');
      $('.main-tree__line:not(.line__visible) span').removeClass('selected');
    });
});
