document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var options = document.querySelectorAll('options');
    var instances = M.FormSelect.init(elems, options);
  });