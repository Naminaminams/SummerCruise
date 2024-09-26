document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('back-to-top-link');
    
    // Scroll to top script
    link.addEventListener('click', function(e) {
      e.preventDefault();
      window.scrollTo({top: 0, behavior: 'smooth'});
    });
  });