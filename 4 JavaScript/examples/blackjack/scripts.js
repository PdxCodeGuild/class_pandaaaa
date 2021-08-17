let card_values = {
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 9, 
    '8': 8, 
    '7': 7,
    '6': 6,
    '5': 5, 
    '4': 4, 
    '3': 3,
    '2': 2,
    '1': 1
};
let usercards = ['2','3','4','5','6','7','8','9','J','Q','K','A'];
let hand = [];

let deal = function(){
    return usercards[Math.floor(Math.random()*usercards.length)]
};

let check_aces = function(cards){
    let total = 0;
    let cardsFiltered = [];
    if (cards.includes('A')){
        console.log('ace found')
        for (let i=0; i<cards.length; i++){
            if (cards[i] != 'A'){
                cardsFiltered.push(cards[i])
            }
        }
        // possible other option for removing elements
        // hand.filter((element) => element !== 'A')
        if (cardsFiltered.length == 0){
            total = 13
            alert('your total is 13: one ace is 11, two aces are 1')
        }
        else {
            for(card in cardsFiltered){
                total = total + card_values[cardsFiltered[card]]
                console.log('above switch ' + cardsFiltered)
            }            
            if(total < 10 && cardsFiltered.length == 2){
                    alert('your ace should be 11')
                    total = total + 11
            }
                else if(total < 10 && cardsFiltered.length == 1){
                    alert('one ace is 11, the other is 1')
                    total = total + 12
            }
                else if(total == 10 && cardsFiltered.length == 1){
                    alert('your aces should be 1')
                    total = total + 2
            }
                else if(total == 10 && cardsFiltered.length == 2){
                    alert('your ace should be 11')
                    total = total + 11;
            }
                else if(total > 10 && cardsFiltered.length == 2){
                    alert('your ace should be 1')
                    total = total + 1;
            }
                else if(total > 10 && cardsFiltered.length == 1){
                    alert('both aces are 1')
                    total = total + 2
            }
            }     
    }
    else {
        console.log('no aces')
        cardsFiltered = cards
        for(card in cardsFiltered){
            total = total + card_values[cardsFiltered[card]]
        }
        };

    return total
    }

let giveAdvice = function(total){
    if(total< 17){
        alert(`Your total is ${total}. You should hit!`)
    }
    else if(total < 21){
        alert(`Your total is ${total}. You should hit!`)
    }
    else if(total == 21){
        alert(`BLACKJACK!`)
    }
    else {
        alert(`busted :(`)
    }
}
while (hand.length < 3){
    // card = prompt("Whats your cards?")
    hand.push(deal())
    console.log(hand)
}

alert(`you've been dealt: ${hand}`)
// console.log(check_aces(hand))
giveAdvice(check_aces(hand))
