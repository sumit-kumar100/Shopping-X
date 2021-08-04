$(document).ready(function(){
    $('.small-images img').click(function(){
        var image = $(this).attr('src');
        $('.big-image img').attr('src',image);
    });
});

function Product_Details() {
    var x = document.getElementById("specification");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}


