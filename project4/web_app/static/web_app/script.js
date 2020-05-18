document.addEventListener('DOMContentLoaded', () => {
    
    if (document.querySelector('#open_nav')){
        document.querySelector('#open_nav').onclick = () => {
            document.getElementById("mySidenav").style.width = "250px";
        }
    }

    if (document.querySelector('#close_nav')){
        document.querySelector('#close_nav').onclick = () => {
            document.getElementById("mySidenav").style.width = "0";
        }
    }

});