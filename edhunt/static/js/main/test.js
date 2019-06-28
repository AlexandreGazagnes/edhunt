function updateMySize() {

    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    document.getElementById('mySize').innerHTML = width;
}
