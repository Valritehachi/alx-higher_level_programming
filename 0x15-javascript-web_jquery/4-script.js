// Add an event listener to the document that will trigger
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('HEADER').toggleClass('red');
    $('HEADER').toggleClass('green');
  });
});
