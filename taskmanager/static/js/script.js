document.addEventListener('DOMContentLoaded', function() {
    // side nav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
  });



  
// JavaScript to dynamically set the current year
document.getElementById('current-year').textContent = new Date().getFullYear();