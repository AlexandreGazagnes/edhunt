function ouiFunct(item){
        $("#ouiButton"+item).mouseover(function(){
            $('#ouiKeyContent'+item).hide();
            $('#ouiValContent'+item).show();    });
        $("#ouiButton"+item).mouseout(function(){
            $('#ouiValContent'+item).hide();
            $('#ouiKeyContent'+item).show();    });   ;}


$(document).ready(function(){
    ouiFunct(1);    ouiFunct(2);    ouiFunct(3);
    ouiFunct(4);    ouiFunct(5);    ouiFunct(6);
    ouiFunct(7);    ouiFunct(8);    ouiFunct(9);
    ouiFunct(10);   ouiFunct(11);   ouiFunct(12);
    ouiFunct(13);   ouiFunct(14);   ouiFunct(15);    });



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
