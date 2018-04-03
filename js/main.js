$(document).ready(function() {
    $('.main-tree__element:not(.main-tree__first-element)').click(function() {
      $(this).siblings().removeClass('selected');
      $(this).siblings().removeClass('line__visible');
      $(this).addClass('selected');
      var identificator = $(this).attr('id');
      var text = $(this).text();
      $('.' + identificator + '__inner').addClass('line__visible');
      $('.main-tree__line:not(.line__visible) span').removeClass('selected');
      $('.textarea').append('&#13;&#10;' + text);
    });
});
