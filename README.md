# scripteddddd
Java script practice
var price = 15.00;
var money = 20.00;
var cost = 30.00
if ( money >= price) {
    console.log ("Buy the hammer");
} else{
    console.log ("Dont buy the hammer");
}
if ( cost >= money) {
    console.log ("Leave the shop and run away");
} else{
    console.log ("Buy like May Weather")

}
var colt = "Not busy";
var weather = "Nice";
if ( colt === "Not busy") {
    if ( weather === "Nice") {
        console.log("Go to the Park");
    } else
}
 

 var x = 1;
 console.log(x + "mississipi");

 var x = 1;
 while (x <= 100) {
     console.log(x + "mississipi");
     x = x + 1;
 }
 for (var i=0; i < 6; i = i + 1) {
     console.log(i)
 }
 function isprime(integer) {
     for(var x = 2; x < integer; x++) {
         if(integer % x === 0 ) {
             console.log(integer + " is divisible by " + x) ;
             return false;
         }
     }
     return true;
 }


 function findaverage(x, y) {
     var answer = (x + y) / 2;
     return answer;
 }


 function findme(x, y, z) {
     var answer = (x * 10) + (y / 4) - z;
     return answer;
 }
 function saygreeting() {
     var greeting = "Hello"
     console.log(greeting);
 }

 saygreeting();

 var Name = prompt("What is your name?");
 var Message = "Hello!" + Name;
 document.write(Message);



 var Vistor = prompt('What is Your name ?')
 var message = "Hello " + Visitor + " You are welcome to this lesson ";
 message = message + "We love your prssence " + "And it's kinda different"
 document.write(message);



 var visitor = prompt("Please input only one name here");
 var mass = "Your name have " + message.length + " letters";
 document.write(mass);



 


 var verb = prompt("Type out a verb");
 var noun = prompt("Type out a noun");
 var adjective = prompt("Type out an adjective");
 var mess = "There once was a " + adjective + " programmer who wanted to use java script to change the " + noun;



 var secondsperminute = 60;
 var minuteperhour = 60;
 var hoursperday = 24;
 var daysperweek = 7;
 var weekperyear = 52;
 var seconndsperday = secondsperminute * minuteperhour * hoursperday;
 document.write("There are " + seconndsperday + " in a day ");
 var secondsalive = seconndsperday * 365;
 var age = prompt("What is your age?");
 var x = age * secondsalive;
 document.write("CONGRATS!!!!!!    You have been alive for " + x + " seconds")


 Var dieRoll = Math.floor (Math.random() * 6 ) + 1;
 alert(" You rolled a" + dieRoll)



var correct = 0;
var question1 = prompt("Which programming language is a gem ?");
if (question1.toUpperCase() === "RUBY"){
    correct += 1;
}
var question2 = prompt("Which programming language is a snake?");
if (question2.toUpperCase() === "PYTHON"){
    correct +=1;
}
var question3 = prompt("Which language is used for designing the webpage ?");
if (question3.toUpperCase() === "CSS"){
    correct += 1;
}
var question4 = prompt("Which language serves as the structure of a webpage?");
if (question4.toUpperCase() === "HTML"){
    correct += 1;
}
var question5 = prompt("What is the programming language of the web?");
if (question5.toUpperCase() === "JAVASCRIPT"){
    correct += 1;
}
if (correct > 2){
    alert("You got " + correct + " correct out of 5")
}
else{
    alert("You can do better next time")
}
if (correct === 5){
    document.write("You won gold for your performance")
}
else if(correct >= 3){
    document.write("You won silver for your performance")
}
else if(correct >= 1){
    document.write("You won bronze for your performance")
}
else{
    document.write("You can do better bro")
}

//FUNCTION 
function alertRandom(){
    Math.floor(Math.random() * 6) + 1;
}
alert(alertRandom());



function RandomNumber(Upper, Lower){
    var random = Math.random() * (Upper - Lower) + Lower;
    return random
}
