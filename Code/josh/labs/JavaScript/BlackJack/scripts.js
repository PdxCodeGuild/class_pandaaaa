console.log("Hello Black Jack");
cardDeck = {
  kc: 10,
  ks: 10,
  kh: 10,
  kd: 10,
  qc: 10,
  qs: 10,
  qh: 10,
  qd: 10,
  jc: 10,
  js: 10,
  jh: 10,
  jd: 10,
  "10c": 10,
  "10s": 10,
  "10h": 10,
  "10d": 10,
  "9c": 9,
  "9s": 9,
  "9h": 9,
  "9d": 9,
  "8c": 8,
  "8s": 8,
  "8h": 8,
  "8d": 8,
  "7c": 7,
  "7s": 7,
  "7h": 7,
  "7d": 7,
  "6c": 6,
  "6s": 6,
  "6h": 6,
  "6d": 6,
  "5c": 5,
  "5s": 5,
  "5h": 5,
  "5d": 5,
  "4c": 4,
  "4s": 4,
  "4h": 4,
  "4d": 4,
  "3c": 3,
  "3s": 3,
  "3h": 3,
  "3d": 3,
  "2c": 2,
  "2s": 2,
  "2h": 2,
  "2d": 2,
  ac: 1,
  as: 1,
  ah: 1,
  ad: 1,
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

const makeHandString = (hand) => {
  handString = String();
  for (let i = 0; i < hand.length; i++) {
    const card = hand[i];
    if (i + 1 == hand.length) {
      handString += `and ${card}`;
    } else handString += `${card}${i + 2 == hand.length ? "" : ","} `;
  }
  return handString;
};

const countAces = (hand) => {
  let aces = 0;
  hand.forEach((card) => {
    if (card.charAt(0) == "a") {
      aces++;
    }
  });
  return aces;
};

const evaluateAces = (total, aces) => {
  if (!aces) return total;
  if (total > 11) {
    // return the total because if your hand is 11 or more you wouldn't want an ace to be worth 11
    return total;
  }
  let evaluated = aces * 10 + total;
  return evaluated;
};

const evaluateWinner = (dealerTotal, userTotal) => {
  if (dealerTotal > 21) {
    return `Dealer busted with ${dealerTotal} 🥳,  \n 🎊  You Win!!! 🎉`;
  } else if (dealerTotal == userTotal) {
    return `Push 😒, dealer has ${dealerTotal}`;
  } else if (userTotal == 21) {
    return `You got 21! \n 🎊  You Win!!! 🎉 \n dealer has ${dealerTotal}`;
  } else if (dealerTotal > userTotal) {
    return `Dealer has ${dealerTotal}, dealer wins 😞 `;
  } else return `Dealer has ${dealerTotal},\n 🎊  You Win!!! 🎉`;
};

const playBlackJack = () => {
  let deck = populateDeck();
  let hands = deal(deck);
  let userHand = hands[0];
  let dealerHand = hands[1];
  let aces = countAces(userHand);
  let userTotal = addHand(userHand);
  let handWithAces = evaluateAces(userTotal, aces);
  let userHandString = makeHandString(userHand);
  let dealerTotal = addHand(dealerHand);
  let dealerAces = countAces(dealerHand);
  let dealerHandWithAces = evaluateAces(dealerTotal, dealerAces);

  if (aces) {
    console.log("user has an Ace");
    if (aces == 2) {
      console.log("user has 2 Aces!!! better split that sh*t");
    }
  }

  let hitOrStay = prompt(
    `Your hand is ${userHandString} totaling ${userTotal} ${
      userTotal != handWithAces ? `or ${handWithAces}` : ""
    } \n the dealer is showing a ${dealerHand[1]}. \n Hit or Stay?`
  )
    .toLowerCase()
    .trim();
  while (true) {
    if (hitOrStay == "hit") {
      userHand.push(dealCard(deck));
      // userHand = ["as", "ks"];
      // aces = 1;
      userTotal = addHand(userHand);
      userTotalPlusAces = evaluateAces(userTotal, aces);
      userHandString = makeHandString(userHand);
      handWithAces = evaluateAces(userTotal, aces);
      if (userTotal > 21) {
        alert(`You Busted! 😞 , \n your hand: ${userHandString} \n Total: ${userTotal}`);
        break;
      }
      hitOrStay = prompt(
        `Your hand is ${userHandString} totaling ${userTotal} ${
          userTotal != handWithAces ? `or ${handWithAces}` : ""
        } \n the dealer is showing a ${dealerHand[1]}. \n Hit or Stay?`
      )
        .toLowerCase()
        .trim();
    } else if (hitOrStay != "stay") {
      userHandString = makeHandString(userHand);
      hitOrStay = prompt(
        `That's not a valid option \n Your hand is ${userHandString} totaling ${userTotal} \n the dealer is showing a ${dealerHand[1]}. \n Hit or Stay?`
      )
        .toLowerCase()
        .trim();
      // user either busted or got 21
    } else if (hitOrStay == "hit" && (userTotal >= 21 || handWithAces == 21)) {
      break;
      // user typed 'stay'
    } else {
      userTotal = addHand(userHand);
      handWithAces = evaluateAces(userTotal, aces);
      dealerTotal = addHand(dealerHand);
      dealerAces = countAces(dealerHand);
      dealerHandWithAces = evaluateAces(dealerTotal, dealerAces);
      console.log("dealer hand", dealerHandWithAces);
      // while loop draws for dealer until dealer hand satisfied the last || is if the dealer has a soft 17 (an Ace being counted as 11 and a hand adding up to 17)
      while (
        dealerHandWithAces < 17 ||
        (dealerHandWithAces == 17 && dealerHandWithAces != dealerTotal)
      ) {
        dealerHand.push(dealCard(deck));
        if (dealerHandWithAces == 17 && dealerHandWithAces != dealerTotal) {
          console.log(`Dealer has a soft 17, they hit ${dealerHand[-1]}`);
        }
        dealerTotal = addHand(dealerHand);
        dealerAces = countAces(dealerHand);
        dealerHandWithAces = evaluateAces(dealerTotal, dealerAces);
      }
      break;
    }
  }
  if (userTotal < 21) {
    alert(`You have ${makeHandString(userHand)} totaling: ${handWithAces} \n
    Dealer has: ${makeHandString(dealerHand)} \n
    ${evaluateWinner(dealerHandWithAces, handWithAces)}
    `);
  }

  console.log("userHand", userHand);
  console.log("deck", deck);
  console.log("userTotal", userTotal);
};

playBlackJack();
