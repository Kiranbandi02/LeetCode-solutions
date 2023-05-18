/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let ne=[];
    arr.forEach((ele,inx)=>{
        if(fn(ele,inx)){
            ne.push(ele);
        }
    })
    return ne
};