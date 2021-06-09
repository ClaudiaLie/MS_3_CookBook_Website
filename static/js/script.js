   
$(".dropdown-trigger").dropdown();

$('#textarea1').val('');
  M.textareaAutoResize($('#textarea1'));

$(document).ready(function(){
  $('.collapsible').collapsible();
  $('.tooltipped').tooltip();
  $('.sidenav').sidenav();
  $('select').formSelect();
});

// Add Ingredients Tag

$('.chips').chips();
  $('.chips-autocomplete').chips({
    autocompleteOptions: {
      data: {
        'Pasta': null,
        'Salt': null,
        'Pepper': null,
        'Eggs': null,
        'Guanciale': null,
        'Pecorino': null
      },
      limit: Infinity,
      minLength: 2
    }
  });