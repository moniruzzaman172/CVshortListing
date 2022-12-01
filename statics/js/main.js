$(document).ready(function(){
  $('button').click(function(){

     var question1 = document.quiz.ques1.value;
     var question2 =document.quiz.ques2.value;
     var question3 =document.quiz.ques3.value;
     var question4 = document.quiz.ques4.value;
     var question5 =document.quiz.ques5.value;
     var question6 =document.quiz.ques6.value;
     var question7 = document.quiz.ques7.value;
     var question8 =document.quiz.ques8.value;
     var question9 =document.quiz.ques9.value;
     var question10=document.quiz.ques10.value;

     var correct = 0;

     if (question1 == "1") {
       correct++;
     }
     if (question2 == "2") {
       correct++;
     }
     if (question3 == "2") {
       correct++;
     }
     if (question4 == "1") {
       correct++;
     }
     if (question5 == "2") {
       correct++;
     }
     if (question6 == "2") {
       correct++;
     }
     if (question7 == "1") {
       correct++;
     }
     if (question8 == "4") {
       correct++;
     }
     if (question9 == "3") {
       correct++;
     }
     if (question10 == "3") {
       correct++;
     }

     var messages =["Great","Good Job", "Excellent", "Wonderful","Good", "Not good", "Well","Bad", "Vary Bad", "Realy need to better"];



     var rang;
     if (correct <1) {
       rang=10;

     }
     if (correct>0 && correct <2) {
       rang=9;

     }
     if (correct>1 && correct <3) {
       rang=8;

     }
     if (correct>2 && correct <4) {
       rang=7;

     }
     if (correct>3 && correct <5) {
       rang=6;

     }
     if (correct>4 && correct <6) {
       rang=5;

     }
     if (correct>5 && correct <7) {
       rang=5;

     }
     if (correct>6 && correct <8) {
       rang=4;

     }
     if (correct>7 && correct <9) {
       rang=2;

     }
     if (correct>8 && correct <10) {
       rang=1;

     }
     if (correct>9 && correct <11) {
       rang=0;

     }
   /*var a = document.getElementById('message').innerHTML= messages[rang];*/
  var b =document.getElementById('curretNumber').innerHTML = correct ;
  document.getElementById('aftarSubmit').innerHTML= b;


  })
})
