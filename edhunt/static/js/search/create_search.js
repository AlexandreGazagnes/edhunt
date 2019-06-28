function swapMobDisplay() {
    var co = document.getElementById("countryBlock");
    var re = document.getElementById("regionBlock");
    var de = document.getElementById("departementBlock");
    var to = document.getElementById("townBlock");
    var d = document.forms[0].mob.value;
    switch(d) {
        case "Pays":
            co.style.display = "block" ;
            swapCountryDisplay();
            re.style.display = "none" ;
            de.style.display = "none" ;
            to.style.display = "none" ;
            break;
        case "Région":
            co.style.display = "none" ;
            re.style.display = "block" ;
            swapRegionDisplay();
            de.style.display = "none" ;
            to.style.display = "none" ;
            break;
        case "Département":
            co.style.display = "none" ;
            re.style.display = "none" ;
            de.style.display = "block" ;
            swapDepartementDisplay();
            to.style.display = "none" ;
            break;
        case "Ville":
            co.style.display = "none" ;
            re.style.display = "none" ;
            de.style.display = "none" ;
            to.style.display = "block" ;
            swapTownDisplay();
            break;
        default :
            co.style.display = "none" ;
            re.style.display = "none" ;
            de.style.display = "none" ;
            to.style.display = "none" ;    }    }



function handleDisplay(field1, field2, field3, field4, field5,
                        var1, var2, var3, var4, var5){
    field1.style.display="block";
    field2.style.display="none";
    field3.style.display="none";
    field4.style.display="none";
    field5.style.display="none";

    if (var1) {
        field1.style.display="block";
        field2.style.display="block";
        field3.style.display="none";
        field4.style.display="none";
        field5.style.display="none";    }
    if (var1 && var2) {
        field1.style.display="block";
        field2.style.display="block";
        field3.style.display="block";
        field4.style.display="none";
        field5.style.display="none";    }
    if (var1 && var2 && var3) {
        field1.style.display="block";
        field2.style.display="block";
        field3.style.display="block";
        field4.style.display="block";
        field5.style.display="none";    }
    if (var1 && var2 && var3 && var4) {
        field1.style.display="block";
        field2.style.display="block";
        field3.style.display="block";
        field4.style.display="block";
        field5.style.display="block";    }      }


function swapCountryDisplay(){
    var field1 = document.getElementById("country1");
    var field2 = document.getElementById("country2");
    var field3 = document.getElementById("country3");
    var field4 = document.getElementById("country4");
    var field5 = document.getElementById("country5");
    var f = document.forms[0];
    var var1 = f.country_1.value;
    var var2 = f.country_2.value;
    var var3 = f.country_3.value;
    var var4 = f.country_4.value;
    var var5 = f.country_5.value;
    handleDisplay(field1, field2, field3, field4, field5,
                            var1, var2, var3, var4, var5);    }


function swapRegionDisplay(){
    var field1 = document.getElementById("region1");
    var field2 = document.getElementById("region2");
    var field3 = document.getElementById("region3");
    var field4 = document.getElementById("region4");
    var field5 = document.getElementById("region5");
    var f = document.forms[0];
    var var1 = f.region_1.value;
    var var2 = f.region_2.value;
    var var3 = f.region_3.value;
    var var4 = f.region_4.value;
    var var5 = f.region_5.value;
    handleDisplay(field1, field2, field3, field4, field5,
                        var1, var2, var3, var4, var5);    }


function swapDepartementDisplay(){
    var field1 = document.getElementById("departement1");
    var field2 = document.getElementById("departement2");
    var field3 = document.getElementById("departement3");
    var field4 = document.getElementById("departement4");
    var field5 = document.getElementById("departement5");
    var f = document.forms[0];
    var var1 = f.departement_1.value;
    var var2 = f.departement_2.value;
    var var3 = f.departement_3.value;
    var var4 = f.departement_4.value;
    var var5 = f.departement_5.value;
    handleDisplay(field1, field2, field3, field4, field5,
                  var1, var2, var3, var4, var5);    }


function swapTownDisplay(){
    var field1 = document.getElementById("town1");
    var field2 = document.getElementById("town2");
    var field3 = document.getElementById("town3");
    var field4 = document.getElementById("town4");
    var field5 = document.getElementById("town5");
    var f = document.forms[0];
    var var1 = f.town_1.value;
    var var2 = f.town_2.value;
    var var3 = f.town_3.value;
    var var4 = f.town_4.value;
    var var5 = f.town_5.value;
    handleDisplay(field1, field2, field3, field4, field5,
                   var1, var2, var3, var4, var5);    }
