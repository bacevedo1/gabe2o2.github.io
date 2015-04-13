$(document).ready(function(){
 $("#pie").click(function(){
    var item = $('#input').val();
    $('#boxes').append("<li class='box'>"+item+"</li>");
  
 });
 $("#empty").click(function(){
    var item = $('#input').val();
    $('#boxes').empty();
  
 });
});
