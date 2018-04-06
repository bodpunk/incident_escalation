$(document).ready(function() {
    $('.main-tree__element:not(.main-tree__first-element)').click(function() { // Ловим нажатие на любой элемент дерева, за исключением первого
      $(this).siblings().removeClass('selected'); // Снимаем класс выделения (и само выделение) с соседей нажатого элемента
      $(this).siblings().removeClass('line__visible'); //Снимаем класс раскрытия ветви (и саму ветвь) с соседей нажатого элемента
      $(this).addClass('selected'); // повесили класс выделения на нажатый элемент
      var identificator = $(this).attr('id'); // задаем переменную, которая равна идентификатору нажатого элемента
      var text = $(this).text(); //задаем переменную, которая равна тексту нажатого элемента
      $('.' + identificator + '__inner').addClass('line__visible'); // раскрываем ветвь нажатого элемента
      $('.main-tree__line:not(.line__visible) span').removeClass('selected'); // скрываем выделение элементов на скрытых ветках
      $('.textarea-block__text').text('В чём проблема?'); // Обнуляем содержимое textarea, сразу прописывая в него "В чём проблема?"
      $('.selected').each(function() { // для каждого элемента с классом .selected
        $('.textarea-block__text').append('&#13;&#10;&#8595;&#13;&#10;' + $(this).text()); // добавляем его содержимое в textarea в новую строку
      });
    });
    $('.textarea-block__button').click(function() { // Ловим нажатие по кнопке "Копировать"
      $('.textarea-block__text').select(); // Выделяем содержимое textarea
      document.execCommand("copy"); // Копируем содержимое textarea
      $('.textarea-block__button').focus(); // Снимаем выделение textarea, установив фокус на кнопку
    });
});
