// Add an event listener to the document that will trigger
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
  });
});
