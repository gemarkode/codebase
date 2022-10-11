function selectionSort(arr) { 
    for(let n = 0; n < arr.length; n++) {
        let min = n;

        for(let j = n+1; j < arr.length; j++){
            if(arr[j] < arr[min]) {
                min=j; 
            }
        }

        if (min !== n) {
            let current = arr[n]; 
            arr[n] = arr[min];
            arr[min] = current;      
        }
    }

    return arr;
}

let sortedArray = selectionSort([5,13,4,7,8]);
console.log(sortedArray);
