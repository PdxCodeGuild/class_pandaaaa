//Zach Watts
//Searching and Sorting Javascript Redo

//Part1 Linear Search

nums = [1, 6, 5, 4, 3, 2, 7, 8];
numbs = [1, 2, 3, 4, 6, 7, 8,9];
value = 5;

let linear_search = function () {
  inside = true;
  for (i in nums) {
    if (numbs[i] == value) {
      alert(`The value ${value} was found at index${i}`);
      return inside;
    }
  }
  inside = false;
  alert(`The value ${value} was NOT found in the list!`);
  return inside;
};

//Part 2 Binary Search
let binary_search = function () {
  let high = numbs.length - 1;
  let low = 0;
  let counter = 0;
  while (numbs[low] < numbs[high]) {
    let mid = Math.floor((low + high) / 2);
    console.log(mid == value)
    console.log(counter)
    if (numbs[mid] == value){
        alert(`The value is ${numbs[mid]}`)
        return mid
    }
    if (numbs[mid] < value) {
      low = mid;
    } 
    else if (numbs[mid] > value) {
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
  return alert("Unsuccessful");
};

//Part 3 Bubble Sort

let bubble_sort= function(){
    let n = nums.length
    let valid = 0
    let counter = 0
    while (valid == 0){
        let swapped = false
        for (let i=1; i<n-1; ++i)
            {
            let a = nums[i - 1] 
            let b = nums[i]
            if (a > b)
                {
                    let temp = nums[i-1]
                    nums[i-1] = nums[i]
                    nums[i] = temp
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
    alert(`The new sorted list is ${nums}`)
    return nums
    }

//linear_search()
// binary_search();
bubble_sort()