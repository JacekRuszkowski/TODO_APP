// auto open modal
$(document).ready(function () {
      $("#staticBackdrop").modal('show');
  });

// show mobile menu
const menu = document.querySelector('.navigation-mobile-dropped')
const hamburger = document.querySelector('.hamburger-menu')
const menu_list = document.querySelector('.list-mobile')

function showMenu() {
    menu.classList.toggle('menu-height');
    menu_list.classList.toggle('list-mobile-display');
}

hamburger.addEventListener('click', showMenu)



