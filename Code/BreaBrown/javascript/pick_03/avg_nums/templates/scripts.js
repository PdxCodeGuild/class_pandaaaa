// version 1

let num_list = [5, 0, 8, 3, 4, 1, 6];

function avg_nums(x) {
    let s = 0;
    console.log(x);
    for (i in x) {
        s += x[i];
        console.log(i);
    };
    console.log(s);
    answer = s / x.length;
    return answer;
    };
console.log(avg_nums(num_list));



// version 2

function list_popuation() {
    let l = [];
    while (true) {
        let ui = prompt('Enter a number to add to the list or "done" to exit: ');
        console.log(ui)
        if (ui == 'done') {
            break;
        };
        ui = Number(ui)
        if (isNaN(ui)) {
            console.log('Error, please enter a number!');
            continue;
        }
        else {
            l.push(parseInt(ui));
            console.log(l)
        }
    }
    return l
    }

function run() {
    let l = list_popuation();
    console.log(l)
        let output = avg_nums(l);
        console.log(`The average of the numbers you entered is: ${output}`);
};
run()