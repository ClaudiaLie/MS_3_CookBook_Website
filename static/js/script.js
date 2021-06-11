   
$(".dropdown-trigger").dropdown();

$('#textarea1').val('');
  M.textareaAutoResize($('#textarea1'));

$(document).ready(function(){
  $('.collapsible').collapsible();
  $('.tooltipped').tooltip();
  $('.sidenav').sidenav();
  $('select').formSelect();
});