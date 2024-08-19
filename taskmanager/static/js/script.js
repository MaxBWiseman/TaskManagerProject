document.addEventListener('DOMContentLoaded', function() {
    // side nav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    // modal initialization
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
    // datepicker initialization
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, options);
  });



  
// JavaScript to dynamically set the current year
document.getElementById('current-year').textContent = new Date().getFullYear();