//Zach Watts
//Searching and Sorting Javascript Redo

//Part1 Linear Search

nums = [1, 6, 5, 4, 3, 2, 7, 8];
numbs = [1, 2, 3, 4, 6, 7, 8,9];
//value = 5;

let linear_search = function () {
  let value_linear = document.getElementById('value_linear').value
  inside = true;
  for (i in nums) {
    if (numbs[i] == value_linear) {
      alert(`The value ${value_linear} was found at index${i}`);
      return inside;
    }
  }
  inside = false;
  alert(`The value ${value_linear} was NOT found in the list!`);
  return inside;
};

//Part 2 Binary Search
let binary_search = function () {
  let value_binary = document.getElementById('value_binary').value
  let high = numbs.length - 1;
  let low = 0;
  let counter = 0;
  while (numbs[low] < numbs[high]) {
    let mid = Math.floor((low + high) / 2);
    console.log(mid == value_binary)
    console.log(counter)
    if (numbs[mid] == value_binary){
        alert(`The value is at index: ${mid}`)
        return mid
    }
    if (numbs[mid] < value_binary) {
      low = mid;
    } 
    else if (numbs[mid] > value_binary) {
      high = mid;
    } 
    else {
      return numbs[mid];
    }
    console.log(low, mid, high);
    counter = counter + 1;
    if (counter >= 16) {
      break;
    }
  }
  return alert(`${value_binary} was not in the list!`);
};

//Part 3 Bubble Sort

let bubble_sort= function(){
    let bubble1 = document.getElementById('bubble1').value
    let bubble2 = document.getElementById('bubble2').value
    let bubble3 = document.getElementById('bubble3').value
    let bubble4 = document.getElementById('bubble4').value
    let bubble5 = document.getElementById('bubble5').value
    let bubble6 = document.getElementById('bubble6').value
    let bubble7 = document.getElementById('bubble7').value
    let bubble8 = document.getElementById('bubble8').value
    let bubble9 = document.getElementById('bubble9').value
    let num_list = []
    num_list.push(bubble1, bubble2, bubble3, bubble3, bubble4, bubble5, bubble6, bubble7, bubble8, bubble9)
    let n = num_list.length
    let valid = 0
    let counter = 0
    while (valid == 0){
        let swapped = false
        for (let i=1; i<n-1; ++i)
            {
            let a = num_list[i - 1] 
            let b = num_list[i]
            if (a > b)
                {
                    let temp = num_list[i-1]
                    num_list[i-1] = num_list[i]
                    num_list[i] = temp
                swapped = true
                }
            else{continue}
        if (swapped == false)
            {
            valid = 1
            }
            }
        counter += 1
        if (counter >= 20){break}}
    alert(`The new sorted list is ${num_list}`)
    return num_list
    }

let btn1 = document.getElementById("linear_submit")
btn1.addEventListener('click', linear_search)

let btn2 = document.getElementById("binary_submit")
btn2.addEventListener('click', binary_search)

let btn3 = document.getElementById("bubble_sort")
btn3.addEventListener('click', bubble_sort)

// let value_linear = document.getElementById('value').value
// let btn = document.getElementById("submit")
// btn.addEventListener('click', user_feedback)



//linear_search()
// binary_search();
//bubble_sort()