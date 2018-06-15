var arr = [32769,26495,32473,23567,19977,20080,20102,21253,65292,32,21364,27809,26377,32473,20320,38065,20080,25151]

var fun2 = function(a,b){if(typeof a.map==="function"){return a.map(b)}var c=[],d=0;for(i=0;i<a.length;i++){c[d++]=b(a[i],i,a)}return c};

arr = fun2(arr,
    function(a) {
        return String.fromCharCode(a);
    }
    ).join('');

console.log(arr);