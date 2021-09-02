let cards = [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace'];
let hand = [];
let total = 0;


let deal = function() {
    return cards[Math.floor(Math.random()*cards.length)];
}

let add_cards = function(total,card) {
    if (card == 'jack' || card == 'queen' || card == 'king'){
        total = total + 10
    }
    else if (card == 'ace') {
        if (total <= 10){
            total = total + 11
        }
        else{
            total = total + 1
        }
    }
    else{
        total = total + card
    }
    return total
}

let advice = function(total){
    if (total < 17){
        alert("Recommend Hit!");
    }
    else if(total < 21){
        alert("Recommend Stay!");
    }
    else if (total == 21){
        alert("Blackjack!");
    }
    else{
        alert("Busted!");
    }
}

while (hand.length < 3) {
    hand.push(deal());
    total = add_cards(total,hand[hand.length-1]);   
}

alert(hand);
alert(total);
advice(total);