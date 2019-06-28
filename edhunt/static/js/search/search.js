// Search
function expandsearchOption() {
      var opt = document.getElementById("searchOption");
      var btn = document.getElementById("searchButton");
      if (opt.style.display == "none"){
          opt.style.display = "block";
          btn.style.display = "none";}
  }


function reducesearchOption() {
      var opt = document.getElementById("searchOption");
      var btn = document.getElementById("searchButton");
      if (opt.style.display == "block"){
          opt.style.display = "none";
          btn.style.display = "block";}
    }

// Status
function expandstatusOption() {
      var opt = document.getElementById("statusOption");
      var btn = document.getElementById("statusButton");
      if (opt.style.display == "none"){
          opt.style.display = "block";
          btn.style.display = "none";}
  }

function reducestatusOption() {
      var opt = document.getElementById("statusOption");
      var btn = document.getElementById("statusButton");
      if (opt.style.display == "block"){
          opt.style.display = "none";
          btn.style.display = "block";}
    }

// Job
function expandjobOption() {
      var opt = document.getElementById("jobOption");
      var btn = document.getElementById("jobButton");
      if (opt.style.display == "none"){
          opt.style.display = "block";
          btn.style.display = "none";}
  }

function reducejobOption() {
      var opt = document.getElementById("jobOption");
      var btn = document.getElementById("jobButton");
      if (opt.style.display == "block"){
          opt.style.display = "none";
          btn.style.display = "block";}
    }

// Languages
function expandlanguagesOption() {
      var opt = document.getElementById("languagesOption");
      var btn = document.getElementById("languagesButton");
      if (opt.style.display == "none"){
          opt.style.display = "block";
          btn.style.display = "none";}
  }

function reducelanguagesOption() {
      var opt = document.getElementById("languagesOption");
      var btn = document.getElementById("languagesButton");
      if (opt.style.display == "block"){
          opt.style.display = "none";
          btn.style.display = "block";}
    }


// reduce all /derouler all

function deroullerall1Option() {
      var derouller1 = document.getElementById("deroullerall1");
      var reduire1 = document.getElementById("reduireall1")
      var derouller2 = document.getElementById("deroullerall2");
      var reduire2 = document.getElementById("reduireall2")

      var optSearch = document.getElementById("searchOption");
      var btnSearch = document.getElementById("searchButton");
      var optStatus = document.getElementById("statusOption");
      var btnStatus = document.getElementById("statusButton");
      var optJob = document.getElementById("jobOption");
      var btnJob = document.getElementById("jobButton");
      var optLang = document.getElementById("languagesOption");
      var btnLang = document.getElementById("languagesButton");

      if (derouller1.style.display == "block"){
          derouller1.style.display = "none";
          reduire1.style.display = "block";
          derouller2.style.display = "none";
          reduire2.style.display = "block";
          optSearch.style.display = "block" ;
          btnSearch.style.display = "none" ;
          optStatus.style.display = "block" ;
          btnStatus.style.display = "none" ;
          optJob.style.display = "block" ;
          btnJob.style.display = "none" ;
          optLang.style.display = "block" ;
          btnLang.style.display = "none" ;
        }
    }



function reduireall1Option() {
      var derouller1 = document.getElementById("deroullerall1");
      var reduire1 = document.getElementById("reduireall1")
      var derouller2 = document.getElementById("deroullerall2");
      var reduire2 = document.getElementById("reduireall2")


      var optSearch = document.getElementById("searchOption");
      var btnSearch = document.getElementById("searchButton");
      var optStatus = document.getElementById("statusOption");
      var btnStatus = document.getElementById("statusButton");
      var optJob = document.getElementById("jobOption");
      var btnJob = document.getElementById("jobButton");
      var optLang = document.getElementById("languagesOption");
      var btnLang = document.getElementById("languagesButton");

      if (reduire1.style.display == "block"){
          derouller1.style.display = "block";
          reduire1.style.display = "none";
          derouller2.style.display = "block";
          reduire2.style.display = "none";
          optSearch.style.display = "none" ;
          btnSearch.style.display = "block" ;
          optStatus.style.display = "none" ;
          btnStatus.style.display = "block" ;
          optJob.style.display = "none" ;
          btnJob.style.display = "block" ;
          optLang.style.display = "none" ;
          btnLang.style.display = "block" ;
        }
    }


function deroullerall2Option() {
      var derouller1 = document.getElementById("deroullerall1");
      var reduire1 = document.getElementById("reduireall1")
      var derouller2 = document.getElementById("deroullerall2");
      var reduire2 = document.getElementById("reduireall2")

      var optSearch = document.getElementById("searchOption");
      var btnSearch = document.getElementById("searchButton");
      var optStatus = document.getElementById("statusOption");
      var btnStatus = document.getElementById("statusButton");
      var optJob = document.getElementById("jobOption");
      var btnJob = document.getElementById("jobButton");
      var optLang = document.getElementById("languagesOption");
      var btnLang = document.getElementById("languagesButton");

      if (derouller2.style.display == "block"){
          derouller1.style.display = "none";
          reduire1.style.display = "block";
          derouller2.style.display = "none";
          reduire2.style.display = "block";
          optSearch.style.display = "block" ;
          btnSearch.style.display = "none" ;
          optStatus.style.display = "block" ;
          btnStatus.style.display = "none" ;
          optJob.style.display = "block" ;
          btnJob.style.display = "none" ;
          optLang.style.display = "block" ;
          btnLang.style.display = "none" ;
        }
    }



function reduireall2Option() {
      var derouller1 = document.getElementById("deroullerall1");
      var reduire1 = document.getElementById("reduireall1")
      var derouller2 = document.getElementById("deroullerall2");
      var reduire2 = document.getElementById("reduireall2")


      var optSearch = document.getElementById("searchOption");
      var btnSearch = document.getElementById("searchButton");
      var optStatus = document.getElementById("statusOption");
      var btnStatus = document.getElementById("statusButton");
      var optJob = document.getElementById("jobOption");
      var btnJob = document.getElementById("jobButton");
      var optLang = document.getElementById("languagesOption");
      var btnLang = document.getElementById("languagesButton");

      if (reduire2.style.display == "block"){
          derouller1.style.display = "block";
          reduire1.style.display = "none";
          derouller2.style.display = "block";
          reduire2.style.display = "none";
          optSearch.style.display = "none" ;
          btnSearch.style.display = "block" ;
          optStatus.style.display = "none" ;
          btnStatus.style.display = "block" ;
          optJob.style.display = "none" ;
          btnJob.style.display = "block" ;
          optLang.style.display = "none" ;
          btnLang.style.display = "block" ;
        }
    }


