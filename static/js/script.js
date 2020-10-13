function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(51.508742, -0.120850),
        zoom: 5,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}


// const inputUser = document.getElementsByName('form');

// console.log(inputUser.getAttribute("submit"));

// console.log(inputUser);

// function test() {
//     console.log(" TEST OK");
// }

// function test_query() {
//     const div = document.querySelector("div");
//     div.style.color = "pink"
// }

// test_query()
