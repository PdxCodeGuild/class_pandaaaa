console.log("Hello Black Jack");

cardDeck = {
  "King ♣️": 10,
  "King ♠️": 10,
  "King ❤️": 10,
  "King ♦️": 10,
  "Queen ♣️": 10,
  "Queen ♠️": 10,
  "Queen ❤️": 10,
  "Queen ♦️": 10,
  "Jack ♣️": 10,
  "Jack ♠️": 10,
  "Jack ❤️": 10,
  "Jack ♦️": 10,
  "10 ♣️": 10,
  "10 ♠️": 10,
  "10 ❤️": 10,
  "10 ♦️": 10,
  "9 ♣️": 9,
  "9 ♠️": 9,
  "9 ❤️": 9,
  "9 ♦️": 9,
  "8 ♣️": 8,
  "8 ♠️": 8,
  "8 ❤️": 8,
  "8 ♦️": 8,
  "7 ♣️": 7,
  "7 ♠️": 7,
  "7 ❤️": 7,
  "7 ♦️": 7,
  "6 ♣️": 6,
  "6 ♠️": 6,
  "6 ❤️": 6,
  "6 ♦️": 6,
  "5 ♣️": 5,
  "5 ♠️": 5,
  "5 ❤️": 5,
  "5 ♦️": 5,
  "4 ♣️": 4,
  "4 ♠️": 4,
  "4 ❤️": 4,
  "4 ♦️": 4,
  "3 ♣️": 3,
  "3 ♠️": 3,
  "3 ❤️": 3,
  "3 ♦️": 3,
  "2 ♣️": 2,
  "2 ♠️": 2,
  "2 ❤️": 2,
  "2 ♦️": 2,
  "Ace ♣️": 1,
  "Ace ♠️": 1,
  "Ace ❤️": 1,
  "Ace ♦️": 1,
};

UIDeck = {
  "King ♣️": `<span class='card rank-k clubs'><span class='rank'>K</span><span class='suit'>&clubs;</span></span>`,
  "King ♠️": `<span class='card rank-k spades'><span class='rank'>K</span><span class='suit'>&spades;</span></span>`,
  "King ❤️": `<span class='card rank-k hearts'><span class='rank'>K</span><span class='suit'>&hearts;</span></span>`,
  "King ♦️": `<span class='card rank-k diams'><span class='rank'>K</span><span class='suit'>&diams;</span></span>`,
  "Queen ♣️": `<span class='card rank-q clubs'><span class='rank'>Q</span><span class='suit'>&clubs;</span></span>`,
  "Queen ♠️": 10,
  "Queen ❤️": 10,
  "Queen ♦️": 10,
  "Jack ♣️": `<span class='card rank-j clubs'><span class='rank'>J</span><span class='suit'>&clubs;</span></span>`,
  "Jack ♠️": 10,
  "Jack ❤️": 10,
  "Jack ♦️": 10,
  "10 ♣️": `<span class='card rank-10 clubs'><span class='rank'>10</span><span class='suit'>&clubs;</span></span>`,
  "10 ♠️": 10,
  "10 ❤️": 10,
  "10 ♦️": 10,
  "9 ♣️": `<span class='card rank-9 clubs'><span class='rank'>9</span><span class='suit'>&clubs;</span></span>`,
  "9 ♠️": 9,
  "9 ❤️": 9,
  "9 ♦️": 9,
  "8 ♣️": `<span class='card rank-8 clubs'><span class='rank'>8</span><span class='suit'>&clubs;</span></span>`,
  "8 ♠️": 8,
  "8 ❤️": 8,
  "8 ♦️": 8,
  "7 ♣️": `<span class='card rank-7 clubs'><span class='rank'>7</span><span class='suit'>&clubs;</span></span>`,
  "7 ♠️": 7,
  "7 ❤️": 7,
  "7 ♦️": 7,
  "6 ♣️": `<span class='card rank-6 clubs'><span class='rank'>6</span><span class='suit'>&clubs;</span></span>`,
  "6 ♠️": 6,
  "6 ❤️": 6,
  "6 ♦️": 6,
  "5 ♣️": `<span class='card rank-5 clubs'><span class='rank'>5</span><span class='suit'>&clubs;</span></span>`,
  "5 ♠️": 5,
  "5 ❤️": 5,
  "5 ♦️": 5,
  "4 ♣️": `<span class='card rank-4 clubs'><span class='rank'>4</span><span class='suit'>&clubs;</span></span>`,
  "4 ♠️": 4,
  "4 ❤️": 4,
  "4 ♦️": 4,
  "3 ♣️": `<span class='card rank-3 clubs'><span class='rank'>3</span><span class='suit'>&clubs;</span></span>`,
  "3 ♠️": 3,
  "3 ❤️": 3,
  "3 ♦️": 3,
  "2 ♣️": `<span class='card rank-2 clubs'><span class='rank'>2</span><span class='suit'>&clubs;</span></span>`,
  "2 ♠️": 2,
  "2 ❤️": 2,
  "2 ♦️": 2,
  "Ace ♣️": `<span class='card rank-a clubs'><span class='rank'>A</span><span class='suit'>&clubs;</span></span>`,
  "Ace ♠️": 1,
  "Ace ❤️": 1,
  "Ace ♦️": 1,
};

const populateDeck = () => {
  let deck = Array();
  for (card in cardDeck) {
    deck.push(card);
  }
  return deck;
};

const dealCard = (deck) => {
  const index = Math.floor(Math.random() * deck.length);
  const card = deck[index];
  deck.splice(index, 1);
  return card;
};

const deal = (deck) => {
  counter = 0;
  userHand = Array();
  dealerHand = Array();
  while (counter < 2) {
    userHand.push(dealCard(deck));
    dealerHand.push(dealCard(deck));
    counter++;
  }
  return [userHand, dealerHand];
};

const addHand = (hand) => {
  sum = 0;
  hand.forEach((card) => {
    sum += cardDeck[card];
  });
  return sum;
};

const countAces = (hand) => {
  let aces = 0;
  hand.forEach((card) => {
    if (card.charAt(0) == "A") {
      aces++;
    }
  });
  return aces;
};

const evaluateAces = (total, aces) => {
  if (!aces) return total;
  // No Aces means no change in the total
  if (total > 11) {
    // return the total because if your hand is 11 or more you wouldn't want an Ace to be worth 11
    return total;
  }
  //  only add 10 because an Ace is already counted as 1. If you had more then 1 Ace
  //  you would only want 1 Ace counted as 11 because any more and you would bust
  return total + 10;
};

// Dom Functions

// main Function
const playBlackJack = () => {
  let deck = populateDeck();
  let hands = deal(deck);
  let userHand = hands[0];
  let dealerHand = hands[1];
  let aces = countAces(userHand);
  let userTotal = addHand(userHand);
  let handWithAces = evaluateAces(userTotal, aces);
  let dealerTotal = addHand(dealerHand);
  let dealerAces = countAces(dealerHand);
  let dealerHandWithAces = evaluateAces(dealerTotal, dealerAces);

  console.log("handWithAces", handWithAces);
  console.log("dealerHandWithAces", dealerHandWithAces);
  console.log("deck", deck);
};

playBlackJack();
