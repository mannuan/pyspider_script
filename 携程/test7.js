var map = function(arr, f) {
    if (Array.prototype.map) {
        return Array.prototype.map.call(arr, f);
    }
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        result.push(f(arr[i]));
    }
    return result;
};//返回数组
var nzydufghtskpmoeaqcjvlwxirb = function(r, n) {
    for (var t = [32, 43, 45, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], o = r.split(n.charAt(0)), p = [],
         u = function(r) {
            var o = map(r.split(""),
            function(r, o) {
                return String.fromCharCode(t[n.indexOf(r)])
            }).join("");
            return + o
         },
    e = function(r) {
        var n = p.pop(),
        t = p.pop();
        r === i ? p.push(t + n) : p.push(t - n)
    },
    i = n.charAt(1), a = n.charAt(2), f = 0; f < o.length; f++) if ("" !== o[f]) if (o[f] == i || o[f] == a) {
        var h = o[f];
        e(h)
    } else {
        var c = u(o[f], n);
        p.push( + c)
    }
    return p.pop()
};
