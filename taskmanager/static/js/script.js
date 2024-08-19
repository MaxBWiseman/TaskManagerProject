document.addEventListener('DOMContentLoaded', function() {
    // side nav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });




  
// JavaScript to dynamically set the current year
document.getElementById('current-year').textContent = new Date().getFullYear();