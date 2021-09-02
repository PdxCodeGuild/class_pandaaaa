const homeScreen = document.getElementById('home');

const balanceButton = document.getElementById('balance');
const balanceScreen = document.getElementById('bal-display');
const balanceBackButton = document.getElementById('bal-back');

const withdrawButton = document.getElementById('withdraw');
const withdrawScreen = document.getElementById('wit-display');
const withdrawSubmitButton = document.getElementById('wit-submit');
const withdrawBackButton = document.getElementById('wit-back');

const depositButton = document.getElementById('deposit');
const depositScreen = document.getElementById('dep-display');
const depositSubmitButton = document.getElementById('dep-submit');
const depositBackButton = document.getElementById('dep-back');

const interestButton = document.getElementById('interest');
const interestScreen = document.getElementById('int-display');
const interestSubmitButton = document.getElementById('int-submit');
const interestBackButton = document.getElementById('int-back');



balanceButton.addEventListener('click', checkBalance);
withdrawButton.addEventListener('click', makeWithdraw);
depositButton.addEventListener('click', makeDeposit);
interestButton.addEventListener('click', addInterest);

let balance = 0.0;
let interest_rate = 0.1;
////////////////////
// BALANCE SCREEN //
////////////////////
function checkBalance() {
    homeScreen.classList.remove("current");
    homeScreen.classList.add("cleared");
    balanceScreen.classList.remove("cleared");
    balanceScreen.classList.add("current");
    balanceBackButton.addEventListener('click', balanceBack);
    document.getElementById('bal-message').innerHTML = "$" + balance + ".";
}

function balanceBack() {
    balanceScreen.classList.remove("current");
    balanceScreen.classList.add("cleared");
    homeScreen.classList.remove("cleared");
    homeScreen.classList.add("current");
}

/////////////////////
// Withdraw SCREEN //
/////////////////////
function makeWithdraw() {
    homeScreen.classList.remove("current");
    homeScreen.classList.add("cleared");
    withdrawScreen.classList.remove("cleared");
    withdrawScreen.classList.add("current");
    withdrawSubmitButton.addEventListener('click', withdrawSubmit);
    withdrawBackButton.addEventListener('click', withdrawBack);
}

function withdrawSubmit() {
    submit_value = document.getElementById('wit-input').value;
    if (submit_value) {
        document.getElementById('wit-message').innerHTML = "$" + submit_value + " withdrawn.";
        balance -= parseFloat(submit_value);
    }
}

function withdrawBack() {
    withdrawScreen.classList.remove("current");
    withdrawScreen.classList.add("cleared");
    homeScreen.classList.remove("cleared");
    homeScreen.classList.add("current");
    document.getElementById('wit-message').innerHTML = "";
    document.getElementById('wit-input').value = "";
}

////////////////////
// DEPOSIT SCREEN //
////////////////////
function makeDeposit() {
    homeScreen.classList.remove("current");
    homeScreen.classList.add("cleared");
    depositScreen.classList.remove("cleared");
    depositScreen.classList.add("current");
    depositSubmitButton.addEventListener('click', depositSubmit);
    depositBackButton.addEventListener('click', depositBack);
}

function depositSubmit() {
    submit_value = document.getElementById('dep-input').value;
    if (submit_value) {
        document.getElementById('dep-message').innerHTML = "$" + submit_value + " deposited.";
        balance += parseFloat(submit_value);
    }
    console.log(balance);
}

function depositBack() {
    depositScreen.classList.remove("current");
    depositScreen.classList.add("cleared");
    homeScreen.classList.remove("cleared");
    homeScreen.classList.add("current");
    document.getElementById('dep-message').innerHTML = "";
    document.getElementById('dep-input').value = ""
}

/////////////////////
// INTEREST SCREEN //
/////////////////////
function addInterest() {
    homeScreen.classList.remove("current");
    homeScreen.classList.add("cleared");
    interestScreen.classList.remove("cleared");
    interestScreen.classList.add("current");
    interestSubmitButton.addEventListener('click', interestSubmit);
    interestBackButton.addEventListener('click', interestBack);
}

function interestSubmit() {
    document.getElementById('int-message').innerHTML = "10% Interest added.";
    balance += parseFloat(balance * interest_rate);
}

function interestBack() {
    interestScreen.classList.remove("current");
    interestScreen.classList.add("cleared");
    homeScreen.classList.remove("cleared");
    homeScreen.classList.add("current");
    document.getElementById('int-message').innerHTML = "";
    document.getElementById('int-input').value = "";
}