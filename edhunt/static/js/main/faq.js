function ouiFunct(item){
        $(".ouiButton"+item).mouseover(function(){
            $('.ouiKeyContent'+item).hide();
            $('.ouiValContent'+item).show();
            console.log("mouse over");  });
        $(".ouiButton"+item).mouseout(function(){
            $('.ouiValContent'+item).hide();
            $('.ouiKeyContent'+item).show();   });
        $("#ouiButton"+item).mouseover(function(){
            $('#ouiKeyContent'+item).hide();
            $('#ouiValContent'+item).show();
            console.log("mouse over");  });
        $("#ouiButton"+item).mouseout(function(){
            $('#ouiValContent'+item).hide();
            $('#ouiKeyContent'+item).show();   });   ;}

function ouiFunctManager(){
    ouiFunct(0);    ouiFunct(1);    ouiFunct(2);    ouiFunct(3);
    ouiFunct(4);    ouiFunct(5);    ouiFunct(6);
    ouiFunct(7);    ouiFunct(8);    ouiFunct(9);
    ouiFunct(10);   ouiFunct(11);   ouiFunct(12);
    ouiFunct(13);   ouiFunct(14);   ouiFunct(15);    }


function manageHeader() {
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

    if (width > 992){
        console.log("desktop version")
        $(".ehOuiHeaderMobile").css("display", "none") ;
        $(".ehOuiHeaderLaptop").css("display", "block");         }
    else {
        console.log("mobile version")
        $(".ehOuiHeaderLaptop").css("display", "none");
        $(".ehOuiHeaderMobile").css("display", "block");       }    }




// main
$(function(){
    manageHeader();
    ouiFunctManager();
    $(window).resize(function() {
        manageHeader();
        ouiFunctManager();   }); });






// $(document).ready(function(){
//     $(".ouiButton2").click(function(){
//         $('.ouiRow3').slideDown();
//         $('.ouiButton2').slideUp();   });

//      $(".ouiButton3up").click(function(){
//         $('.ouiRow3').slideUp();
//         $('.ouiButton2').slideDown();   });

//     $(".ouiButton3down").click(function(){
//         $('.ouiRow4').slideDown();
//         $('.ouiButton3up').slideUp();
//         $('.ouiButton3down').slideUp();    });

//     $(".ouiButton4").click(function(){
//         $('.ouiRow4').slideUp();
//         $('.ouiButton3up').slideDown();
//         $('.ouiButton3down').slideDown();    });    });
