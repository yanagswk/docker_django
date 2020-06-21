
// function changeComment() {
//     var cmt = document.getElementById("comments");
//     if (cmt.style.display == "none") {
//         cmt.style.display = "block";
//     } else {
//         cmt.style.display = "none";
//     }
// }

$(function() {
    $('#comments').hide();
    $('#butom').click(function(){
    $('#comments').toggle('swing');
    });
    });
