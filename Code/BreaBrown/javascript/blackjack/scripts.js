console.group('hello from scriptsjs')

let card_values = {
    'K': 10,
    'Q': 10,
    'J': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'A': 1
}


let usercards = [2,3,4,5,6,7,8,9,10,'J','Q', 'K', 'A']
let hand = [];

let deal = function(){
    return usercards(Math.floor.random()*usercards.length)]
};

let check_aces = function(cards){
    total = 0
    counter = 0
    if (cards.includes('A')){
        
    }
}

while(usercards.length < 3){
    // card = prompt("Whats your cards?")
    hand.push{deal()}
    console.log(hand)
}

alert(`you've been dealt: ${hand}`)