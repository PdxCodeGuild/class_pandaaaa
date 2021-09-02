console.log('WELCOME TO BLACK JACK ADVICE GIVER')

let card_values = {
    'Q': 10, //Q
    'K': 10, //K
    'J': 10, //J
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    '1': 1,
};
let usercards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'K', 'Q'];
let mypoints = 0;



//helper function for fill_hand, get random number 0-12
let deal = function() {
    return parseInt((Math.random() * 10) % 12);
}



//deal 3 random cards
let fill_hand = function() {
    let mycards = [];
    for (let i = 0; i < 3; ++i) {
        mycards.push(usercards[deal()]);
    }
    return mycards;
}



//calc points
let calc_points = function(mycards) {
    mypoints = 0;
    for (let i = 0; i < mycards.length; ++i) {
        mypoints += parseInt(card_values[mycards[i]]);
    }
    return mypoints;
}


//return true/false if there is/isn't an ace
let has_ace = function() {
    if (mycards.includes(1)) return true;
    return false;
}



//fix aces
let fix_aces = function() {
    if (mypoints <= 11 && has_ace()) {
        console.log("Ace Converted.\n");
        return 10;
    }
    return 0;
}



//display to console.
let display_hand = function() {
    console.log("\n\n");
    console.log("My hand:");
    console.log(mycards);
    console.log("\n\n");
    console.log("My points:");
    console.log(mypoints);
    console.log("\n\n");
}



let advice_calc = function(mypoints) {
    if (mypoints < 17) { // less than 17
        console.log("Hit!");
    } else if (mypoints < 21) { // greater or equal to 17
        console.log("Stay");
    } else if (mypoints == 21) { // exactly 21
        console.log("BlackJack");
    } else { //Over 21
        console.log("Already Busted.");
    }
}



mycards = fill_hand();
mypoints = calc_points(mycards);
mypoints += fix_aces();
display_hand();
advice_calc(mypoints);