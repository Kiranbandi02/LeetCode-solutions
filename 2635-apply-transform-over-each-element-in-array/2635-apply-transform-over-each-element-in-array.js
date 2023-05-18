/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    arr.forEach((ele,inx)=>{
                arr[inx]=fn(ele,inx);
                })
    return arr
};