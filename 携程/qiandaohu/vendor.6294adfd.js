console.log("vendor");
!function(t) {
    console.log("vendor-t");
    function e(r) {
        console.log("vendor-t-e");
        if (n[r]) return n[r].exports;
        var i = n[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        return t[r].call(i.exports, i, i.exports, e), i.l = !0, i.exports;
    }
    var n = {};
    e.m = t, e.c = n, e.d = function(t, n, r) {
        console.log("vendor-t-e.d");
        e.o(t, n) || Object.defineProperty(t, n, {
            configurable: !1,
            enumerable: !0,
            get: r
        });
    }, e.n = function(t) {
        console.log("vendor-e.n");
        var n = t && t.__esModule ? function() {
            return t.default;
        } : function() {
            return t;
        };
        return e.d(n, "a", n), n;
    }, e.o = function(t, e) {
        console.log("vendor-t-e.o");
        return Object.prototype.hasOwnProperty.call(t, e);
    }, e.p = "", e(e.s = 0);
}({
    0: function(t, e, n) {
        console.log("vendor-0");
        n("GnDS"), n("h2Jj"), t.exports = n("CbkN");
    },
    CbkN: function(t, e, n) {
        console.log("vendor-CbkN");
        function r(t, e) {
            console.log("vendor-CbkN-r");
            var n = document.createElement("script");
            n.src = t, n.onload = function() {
                e();
            }, n.onerror = function() {
                e(new Error("Failed to load script " + t));
            }, document.head.appendChild(n);
        }
        function i(t) {
            console.log("vendor-CbkN-i");
            r("//webresource.c-ctrip.com/resaresonline/hotel/h5web/polyfills.707f6a7b.js", t);
        }
        window.execOndemand = function(t) {
            console.log("vendor-CbkN-execOndemand");
            return t();
        };
        var o = [], a = {
            enqueue: function(t) {
                o.push(t);
            },
            flush: function() {
                for (;o.length; ) window.execOndemand(o.shift());
            }
        }, s = !(window.Promise && Object.defineProperty && Object.keys && Function.prototype.bind);
        !function(t) {
            if (t) {
                var e = window.execOndemand;
                window.execOndemand = function(t) {
                    return a.enqueue(t);
                }, i(function(t) {
                    t && console.error("runtime: browser needs patching, but fail to load polyfills, page will probably not work!"),
                    window.execOndemand = e, a.flush();
                });
            }
        }(s);
    },
    GnDS: function(t, e) {
        var n = function() {
            function t(t) {
                return null == t ? String(t) : W[J.call(t)] || "object";
            }
            function e(e) {
                return "function" == t(e);
            }
            function n(t) {
                return null != t && t == t.window;
            }
            function r(t) {
                return null != t && t.nodeType == t.DOCUMENT_NODE;
            }
            function i(e) {
                return "object" == t(e);
            }
            function o(t) {
                return i(t) && !n(t) && Object.getPrototypeOf(t) == Object.prototype;
            }
            function a(t) {
                var e = !!t && "length" in t && t.length, r = S.type(t);
                return "function" != r && !n(t) && ("array" == r || 0 === e || "number" == typeof e && e > 0 && e - 1 in t);
            }
            function s(t) {
                return N.call(t, function(t) {
                    return null != t;
                });
            }
            function c(t) {
                return t.length > 0 ? S.fn.concat.apply([], t) : t;
            }
            function u(t) {
                return t.replace(/::/g, "/").replace(/([A-Z]+)([A-Z][a-z])/g, "$1_$2").replace(/([a-z\d])([A-Z])/g, "$1_$2").replace(/_/g, "-").toLowerCase();
            }
            function l(t) {
                return t in A ? A[t] : A[t] = new RegExp("(^|\\s)" + t + "(\\s|$)");
            }
            function f(t, e) {
                return "number" != typeof e || D[u(t)] ? e : e + "px";
            }
            function h(t) {
                var e, n;
                return k[t] || (e = _.createElement(t), _.body.appendChild(e), n = getComputedStyle(e, "").getPropertyValue("display"),
                e.parentNode.removeChild(e), "none" == n && (n = "block"), k[t] = n), k[t];
            }
            function p(t) {
                return "children" in t ? P.call(t.children) : S.map(t.childNodes, function(t) {
                    if (1 == t.nodeType) return t;
                });
            }
            function d(t, e, n) {
                for (E in e) n && (o(e[E]) || Y(e[E])) ? (o(e[E]) && !o(t[E]) && (t[E] = {}), Y(e[E]) && !Y(t[E]) && (t[E] = []),
                d(t[E], e[E], n)) : e[E] !== x && (t[E] = e[E]);
            }
            function m(t, e) {
                return null == e ? S(t) : S(t).filter(e);
            }
            function v(t, n, r, i) {
                return e(n) ? n.call(t, r, i) : n;
            }
            function g(t, e, n) {
                null == n ? t.removeAttribute(e) : t.setAttribute(e, n);
            }
            function y(t, e) {
                var n = t.className || "", r = n && n.baseVal !== x;
                if (e === x) return r ? n.baseVal : n;
                r ? n.baseVal = e : t.className = e;
            }
            function b(t) {
                try {
                    return t ? "true" == t || "false" != t && ("null" == t ? null : +t + "" == t ? +t : /^[\[\{]/.test(t) ? S.parseJSON(t) : t) : t;
                } catch (e) {
                    return t;
                }
            }
            function w(t, e) {
                e(t);
                for (var n = 0, r = t.childNodes.length; n < r; n++) w(t.childNodes[n], e);
            }
            var x, E, S, j, T, O, C = [], P = C.slice, N = C.filter, _ = window.document, k = {}, A = {}, D = {
                "column-count": 1,
                columns: 1,
                "font-weight": 1,
                "line-height": 1,
                opacity: 1,
                "z-index": 1,
                zoom: 1
            }, M = /^\s*<(\w+|!)[^>]*>/, L = /^<(\w+)\s*\/?>(?:<\/\1>|)$/, $ = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/gi, R = /^(?:body|html)$/i, F = /([A-Z])/g, Z = [ "val", "css", "html", "text", "data", "width", "height", "offset" ], z = [ "after", "prepend", "before", "append" ], q = _.createElement("table"), V = _.createElement("tr"), B = {
                tr: _.createElement("tbody"),
                tbody: q,
                thead: q,
                tfoot: q,
                td: V,
                th: V,
                "*": _.createElement("div")
            }, I = /complete|loaded|interactive/, H = /^[\w-]*$/, W = {}, J = W.toString, U = {}, X = _.createElement("div"), G = {
                tabindex: "tabIndex",
                readonly: "readOnly",
                "for": "htmlFor",
                "class": "className",
                maxlength: "maxLength",
                cellspacing: "cellSpacing",
                cellpadding: "cellPadding",
                rowspan: "rowSpan",
                colspan: "colSpan",
                usemap: "useMap",
                frameborder: "frameBorder",
                contenteditable: "contentEditable"
            }, Y = Array.isArray || function(t) {
                return t instanceof Array;
            };
            return U.matches = function(t, e) {
                if (!e || !t || 1 !== t.nodeType) return !1;
                var n = t.matches || t.webkitMatchesSelector || t.mozMatchesSelector || t.oMatchesSelector || t.matchesSelector;
                if (n) return n.call(t, e);
                var r, i = t.parentNode, o = !i;
                return o && (i = X).appendChild(t), r = ~U.qsa(i, e).indexOf(t), o && X.removeChild(t),
                r;
            }, T = function(t) {
                return t.replace(/-+(.)?/g, function(t, e) {
                    return e ? e.toUpperCase() : "";
                });
            }, O = function(t) {
                return N.call(t, function(e, n) {
                    return t.indexOf(e) == n;
                });
            }, U.fragment = function(t, e, n) {
                var r, i, a;
                return L.test(t) && (r = S(_.createElement(RegExp.$1))), r || (t.replace && (t = t.replace($, "<$1></$2>")),
                e === x && (e = M.test(t) && RegExp.$1), e in B || (e = "*"), a = B[e], a.innerHTML = "" + t,
                r = S.each(P.call(a.childNodes), function() {
                    a.removeChild(this);
                })), o(n) && (i = S(r), S.each(n, function(t, e) {
                    Z.indexOf(t) > -1 ? i[t](e) : i.attr(t, e);
                })), r;
            }, U.Z = function(t, e) {
                return t = t || [], t.__proto__ = S.fn, t.selector = e || "", t;
            }, U.isZ = function(t) {
                return t instanceof U.Z;
            }, U.init = function(t, n) {
                var r;
                if (!t) return U.Z();
                if ("string" == typeof t) if (t = t.trim(), "<" == t[0] && M.test(t)) r = U.fragment(t, RegExp.$1, n),
                t = null; else {
                    if (n !== x) return S(n).find(t);
                    r = U.qsa(_, t);
                } else {
                    if (e(t)) return S(_).ready(t);
                    if (U.isZ(t)) return t;
                    if (Y(t)) r = s(t); else if (i(t)) r = [ t ], t = null; else if (M.test(t)) r = U.fragment(t.trim(), RegExp.$1, n),
                    t = null; else {
                        if (n !== x) return S(n).find(t);
                        r = U.qsa(_, t);
                    }
                }
                return U.Z(r, t);
            }, S = function(t, e) {
                return U.init(t, e);
            }, S.extend = function(t) {
                var e, n = P.call(arguments, 1);
                return "boolean" == typeof t && (e = t, t = n.shift()), n.forEach(function(n) {
                    d(t, n, e);
                }), t;
            }, U.qsa = function(t, e) {
                var n, i = "#" == e[0], o = !i && "." == e[0], a = i || o ? e.slice(1) : e, s = H.test(a);
                return r(t) && s && i ? (n = t.getElementById(a)) ? [ n ] : [] : 1 !== t.nodeType && 9 !== t.nodeType ? [] : P.call(s && !i ? o ? t.getElementsByClassName(a) : t.getElementsByTagName(e) : t.querySelectorAll(e));
            }, S.contains = _.documentElement.contains ? function(t, e) {
                return t !== e && t.contains(e);
            } : function(t, e) {
                for (;e && (e = e.parentNode); ) if (e === t) return !0;
                return !1;
            }, S.type = t, S.isFunction = e, S.isWindow = n, S.isArray = Y, S.isPlainObject = o,
            S.isEmptyObject = function(t) {
                var e;
                for (e in t) return !1;
                return !0;
            }, S.inArray = function(t, e, n) {
                return C.indexOf.call(e, t, n);
            }, S.camelCase = T, S.trim = function(t) {
                return null == t ? "" : String.prototype.trim.call(t);
            }, S.uuid = 0, S.support = {}, S.expr = {}, S.map = function(t, e) {
                var n, r, i, o = [];
                if (a(t)) for (r = 0; r < t.length; r++) null != (n = e(t[r], r)) && o.push(n); else for (i in t) null != (n = e(t[i], i)) && o.push(n);
                return c(o);
            }, S.each = function(t, e) {
                var n, r;
                if (a(t)) {
                    for (n = 0; n < t.length; n++) if (!1 === e.call(t[n], n, t[n])) return t;
                } else for (r in t) if (!1 === e.call(t[r], r, t[r])) return t;
                return t;
            }, S.grep = function(t, e) {
                return N.call(t, e);
            }, window.JSON && (S.parseJSON = JSON.parse), S.each("Boolean Number String Function Array Date RegExp Object Error".split(" "), function(t, e) {
                W["[object " + e + "]"] = e.toLowerCase();
            }), S.fn = {
                forEach: C.forEach,
                reduce: C.reduce,
                push: C.push,
                sort: C.sort,
                indexOf: C.indexOf,
                concat: C.concat,
                map: function(t) {
                    return S(S.map(this, function(e, n) {
                        return t.call(e, n, e);
                    }));
                },
                slice: function() {
                    return S(P.apply(this, arguments));
                },
                ready: function(t) {
                    return I.test(_.readyState) && _.body ? t(S) : _.addEventListener("DOMContentLoaded", function() {
                        t(S);
                    }, !1), this;
                },
                get: function(t) {
                    return t === x ? P.call(this) : this[t >= 0 ? t : t + this.length];
                },
                toArray: function() {
                    return this.get();
                },
                size: function() {
                    return this.length;
                },
                remove: function() {
                    return this.each(function() {
                        null != this.parentNode && this.parentNode.removeChild(this);
                    });
                },
                each: function(t) {
                    return C.every.call(this, function(e, n) {
                        return !1 !== t.call(e, n, e);
                    }), this;
                },
                filter: function(t) {
                    return e(t) ? this.not(this.not(t)) : S(N.call(this, function(e) {
                        return U.matches(e, t);
                    }));
                },
                add: function(t, e) {
                    return S(O(this.concat(S(t, e))));
                },
                is: function(t) {
                    return this.length > 0 && U.matches(this[0], t);
                },
                not: function(t) {
                    var n = [];
                    if (e(t) && t.call !== x) this.each(function(e) {
                        t.call(this, e) || n.push(this);
                    }); else {
                        var r = "string" == typeof t ? this.filter(t) : a(t) && e(t.item) ? P.call(t) : S(t);
                        this.forEach(function(t) {
                            r.indexOf(t) < 0 && n.push(t);
                        });
                    }
                    return S(n);
                },
                has: function(t) {
                    return this.filter(function() {
                        return i(t) ? S.contains(this, t) : S(this).find(t).size();
                    });
                },
                eq: function(t) {
                    return -1 === t ? this.slice(t) : this.slice(t, +t + 1);
                },
                first: function() {
                    var t = this[0];
                    return t && !i(t) ? t : S(t);
                },
                last: function() {
                    var t = this[this.length - 1];
                    return t && !i(t) ? t : S(t);
                },
                find: function(t) {
                    var e = this;
                    return t ? "object" == typeof t ? S(t).filter(function() {
                        var t = this;
                        return C.some.call(e, function(e) {
                            return S.contains(e, t);
                        });
                    }) : 1 == this.length ? S(U.qsa(this[0], t)) : this.map(function() {
                        return U.qsa(this, t);
                    }) : S();
                },
                closest: function(t, e) {
                    var n = [], i = "object" == typeof t && S(t);
                    return this.each(function(o, a) {
                        for (;a && !(i ? i.indexOf(a) >= 0 : U.matches(a, t)); ) a = a !== e && !r(a) && a.parentNode;
                        a && n.indexOf(a) < 0 && n.push(a);
                    }), S(n);
                },
                parents: function(t) {
                    for (var e = [], n = this; n.length > 0; ) n = S.map(n, function(t) {
                        if ((t = t.parentNode) && !r(t) && e.indexOf(t) < 0) return e.push(t), t;
                    });
                    return m(e, t);
                },
                parent: function(t) {
                    return m(O(this.pluck("parentNode")), t);
                },
                children: function(t) {
                    return m(this.map(function() {
                        return p(this);
                    }), t);
                },
                contents: function() {
                    return this.map(function() {
                        return P.call(this.childNodes);
                    });
                },
                siblings: function(t) {
                    return m(this.map(function(t, e) {
                        return N.call(p(e.parentNode), function(t) {
                            return t !== e;
                        });
                    }), t);
                },
                empty: function() {
                    return this.each(function() {
                        this.innerHTML = "";
                    });
                },
                pluck: function(t) {
                    return S.map(this, function(e) {
                        return e[t];
                    });
                },
                show: function() {
                    return this.each(function() {
                        "none" == this.style.display && (this.style.display = ""), "none" == getComputedStyle(this, "").getPropertyValue("display") && (this.style.display = h(this.nodeName));
                    });
                },
                replaceWith: function(t) {
                    return this.before(t).remove();
                },
                wrap: function(t) {
                    var n = e(t);
                    if (this[0] && !n) var r = S(t).get(0), i = r.parentNode || this.length > 1;
                    return this.each(function(e) {
                        S(this).wrapAll(n ? t.call(this, e) : i ? r.cloneNode(!0) : r);
                    });
                },
                wrapAll: function(t) {
                    if (this[0]) {
                        S(this[0]).before(t = S(t));
                        for (var e; (e = t.children()).length; ) t = e.first();
                        S(t).append(this);
                    }
                    return this;
                },
                wrapInner: function(t) {
                    var n = e(t);
                    return this.each(function(e) {
                        var r = S(this), i = r.contents(), o = n ? t.call(this, e) : t;
                        i.length ? i.wrapAll(o) : r.append(o);
                    });
                },
                unwrap: function() {
                    return this.parent().each(function() {
                        S(this).replaceWith(S(this).children());
                    }), this;
                },
                clone: function() {
                    return this.map(function() {
                        return this.cloneNode(!0);
                    });
                },
                hide: function() {
                    return this.css("display", "none");
                },
                toggle: function(t) {
                    return this.each(function() {
                        var e = S(this);
                        (t === x ? "none" == e.css("display") : t) ? e.show() : e.hide();
                    });
                },
                prev: function(t) {
                    return S(this.pluck("previousElementSibling")).filter(t || "*");
                },
                next: function(t) {
                    return S(this.pluck("nextElementSibling")).filter(t || "*");
                },
                html: function(t) {
                    return 0 in arguments ? this.each(function(e) {
                        var n = this.innerHTML;
                        S(this).empty().append(v(this, t, e, n));
                    }) : 0 in this ? this[0].innerHTML : null;
                },
                text: function(t) {
                    return 0 in arguments ? this.each(function(e) {
                        var n = v(this, t, e, this.textContent);
                        this.textContent = null == n ? "" : "" + n;
                    }) : 0 in this ? this.pluck("textContent").join("") : null;
                },
                attr: function(t, e) {
                    var n;
                    return "string" != typeof t || 1 in arguments ? this.each(function(n) {
                        if (1 === this.nodeType) if (i(t)) for (E in t) g(this, E, t[E]); else g(this, t, v(this, e, n, this.getAttribute(t)));
                    }) : this.length && 1 === this[0].nodeType ? !(n = this[0].getAttribute(t)) && t in this[0] ? this[0][t] : n : x;
                },
                removeAttr: function(t) {
                    return this.each(function() {
                        1 === this.nodeType && t.split(" ").forEach(function(t) {
                            g(this, t);
                        }, this);
                    });
                },
                prop: function(t, e) {
                    return t = G[t] || t, 1 in arguments ? this.each(function(n) {
                        this[t] = v(this, e, n, this[t]);
                    }) : this[0] && this[0][t];
                },
                data: function(t, e) {
                    var n = "data-" + t.replace(F, "-$1").toLowerCase(), r = 1 in arguments ? this.attr(n, e) : this.attr(n);
                    return null !== r ? b(r) : x;
                },
                val: function(t) {
                    return 0 in arguments ? (null == t && (t = ""), this.each(function(e) {
                        this.value = v(this, t, e, this.value);
                    })) : this[0] && (this[0].multiple ? S(this[0]).find("option").filter(function() {
                        return this.selected;
                    }).pluck("value") : this[0].value);
                },
                offset: function(t) {
                    if (t) return this.each(function(e) {
                        var n = S(this), r = v(this, t, e, n.offset()), i = n.offsetParent().offset(), o = {
                            top: r.top - i.top,
                            left: r.left - i.left
                        };
                        "static" == n.css("position") && (o.position = "relative"), n.css(o);
                    });
                    if (!this.length) return null;
                    if (_.documentElement !== this[0] && !S.contains(_.documentElement, this[0])) return {
                        top: 0,
                        left: 0
                    };
                    var e = this[0].getBoundingClientRect();
                    return {
                        left: e.left + window.pageXOffset,
                        top: e.top + window.pageYOffset,
                        width: Math.round(e.width),
                        height: Math.round(e.height)
                    };
                },
                css: function(e, n) {
                    if (arguments.length < 2) {
                        var r = this[0];
                        if ("string" == typeof e) {
                            if (!r) return;
                            return r.style[T(e)] || getComputedStyle(r, "").getPropertyValue(e);
                        }
                        if (Y(e)) {
                            if (!r) return;
                            var i = {}, o = getComputedStyle(r, "");
                            return S.each(e, function(t, e) {
                                i[e] = r.style[T(e)] || o.getPropertyValue(e);
                            }), i;
                        }
                    }
                    var a = "";
                    if ("string" == t(e)) n || 0 === n ? a = u(e) + ":" + f(e, n) : this.each(function() {
                        this.style.removeProperty(u(e));
                    }); else for (E in e) e[E] || 0 === e[E] ? a += u(E) + ":" + f(E, e[E]) + ";" : this.each(function() {
                        this.style.removeProperty(u(E));
                    });
                    return this.each(function() {
                        this.style.cssText += ";" + a;
                    });
                },
                index: function(t) {
                    return t ? this.indexOf(S(t)[0]) : this.parent().children().indexOf(this[0]);
                },
                hasClass: function(t) {
                    return !!t && C.some.call(this, function(t) {
                        return this.test(y(t));
                    }, l(t));
                },
                addClass: function(t) {
                    return t ? this.each(function(e) {
                        if ("className" in this) {
                            j = [];
                            var n = y(this);
                            v(this, t, e, n).split(/\s+/g).forEach(function(t) {
                                S(this).hasClass(t) || j.push(t);
                            }, this), j.length && y(this, n + (n ? " " : "") + j.join(" "));
                        }
                    }) : this;
                },
                removeClass: function(t) {
                    return this.each(function(e) {
                        if ("className" in this) {
                            if (t === x) return y(this, "");
                            j = y(this), v(this, t, e, j).split(/\s+/g).forEach(function(t) {
                                j = j.replace(l(t), " ");
                            }), y(this, j.trim());
                        }
                    });
                },
                toggleClass: function(t, e) {
                    return t ? this.each(function(n) {
                        var r = S(this);
                        v(this, t, n, y(this)).split(/\s+/g).forEach(function(t) {
                            (e === x ? !r.hasClass(t) : e) ? r.addClass(t) : r.removeClass(t);
                        });
                    }) : this;
                },
                scrollTop: function(t) {
                    if (this.length) {
                        var e = "scrollTop" in this[0];
                        return t === x ? e ? this[0].scrollTop : this[0].pageYOffset : this.each(e ? function() {
                            this.scrollTop = t;
                        } : function() {
                            this.scrollTo(this.scrollX, t);
                        });
                    }
                },
                scrollLeft: function(t) {
                    if (this.length) {
                        var e = "scrollLeft" in this[0];
                        return t === x ? e ? this[0].scrollLeft : this[0].pageXOffset : this.each(e ? function() {
                            this.scrollLeft = t;
                        } : function() {
                            this.scrollTo(t, this.scrollY);
                        });
                    }
                },
                position: function() {
                    if (this.length) {
                        var t = this[0], e = this.offsetParent(), n = this.offset(), r = R.test(e[0].nodeName) ? {
                            top: 0,
                            left: 0
                        } : e.offset();
                        return n.top -= parseFloat(S(t).css("margin-top")) || 0, n.left -= parseFloat(S(t).css("margin-left")) || 0,
                        r.top += parseFloat(S(e[0]).css("border-top-width")) || 0, r.left += parseFloat(S(e[0]).css("border-left-width")) || 0,
                        {
                            top: n.top - r.top,
                            left: n.left - r.left
                        };
                    }
                },
                offsetParent: function() {
                    return this.map(function() {
                        for (var t = this.offsetParent || _.body; t && !R.test(t.nodeName) && "static" == S(t).css("position"); ) t = t.offsetParent;
                        return t;
                    });
                }
            }, S.fn.detach = S.fn.remove, [ "width", "height" ].forEach(function(t) {
                var e = t.replace(/./, function(t) {
                    return t[0].toUpperCase();
                });
                S.fn[t] = function(i) {
                    var o, a = this[0];
                    return i === x ? n(a) ? a["inner" + e] : r(a) ? a.documentElement["scroll" + e] : (o = this.offset()) && o[t] : this.each(function(e) {
                        a = S(this), a.css(t, v(this, i, e, a[t]()));
                    });
                };
            }), z.forEach(function(e, n) {
                var r = n % 2;
                S.fn[e] = function() {
                    var e, i, o = S.map(arguments, function(n) {
                        var r = [];
                        return e = t(n), "array" == e ? (n.forEach(function(t) {
                            return t.nodeType !== x ? r.push(t) : S.zepto.isZ(t) ? r = r.concat(t.get()) : void (r = r.concat(U.fragment(t)));
                        }), r) : "object" == e || null == n ? n : U.fragment(n);
                    }), a = this.length > 1;
                    return o.length < 1 ? this : this.each(function(t, e) {
                        i = r ? e : e.parentNode, e = 0 == n ? e.nextSibling : 1 == n ? e.firstChild : 2 == n ? e : null;
                        var s = S.contains(_.documentElement, i);
                        o.forEach(function(t) {
                            if (a) t = t.cloneNode(!0); else if (!i) return S(t).remove();
                            i.insertBefore(t, e), s && w(t, function(t) {
                                if (!(null == t.nodeName || "SCRIPT" !== t.nodeName.toUpperCase() || t.type && "text/javascript" !== t.type || t.src)) {
                                    var e = t.ownerDocument ? t.ownerDocument.defaultView : window;
                                    e.eval.call(e, t.innerHTML);
                                }
                            });
                        });
                    });
                }, S.fn[r ? e + "To" : "insert" + (n ? "Before" : "After")] = function(t) {
                    return S(t)[e](this), this;
                };
            }), U.Z.prototype = S.fn, U.uniq = O, U.deserializeValue = b, S.zepto = U, S;
        }();
        window.Zepto = n, void 0 === window.$ && (window.$ = n), function(t) {
            function e(t) {
                return t._zid || (t._zid = h++);
            }
            function n(t, n, o, a) {
                if (n = r(n), n.ns) var s = i(n.ns);
                return (v[e(t)] || []).filter(function(t) {
                    return t && (!n.e || t.e == n.e) && (!n.ns || s.test(t.ns)) && (!o || e(t.fn) === e(o)) && (!a || t.sel == a);
                });
            }
            function r(t) {
                var e = ("" + t).split(".");
                return {
                    e: e[0],
                    ns: e.slice(1).sort().join(" ")
                };
            }
            function i(t) {
                return new RegExp("(?:^| )" + t.replace(" ", " .* ?") + "(?: |$)");
            }
            function o(t, e) {
                return t.del && !y && t.e in b || !!e;
            }
            function a(t) {
                return w[t] || y && b[t] || t;
            }
            function s(n, i, s, c, l, h, p) {
                var d = e(n), m = v[d] || (v[d] = []);
                i.split(/\s/).forEach(function(e) {
                    if ("ready" == e) return t(document).ready(s);
                    var i = r(e);
                    i.fn = s, i.sel = l, i.e in w && (s = function(e) {
                        var n = e.relatedTarget;
                        if (!n || n !== this && !t.contains(this, n)) return i.fn.apply(this, arguments);
                    }), i.del = h;
                    var d = h || s;
                    i.proxy = function(t) {
                        if (t = u(t), !t.isImmediatePropagationStopped()) {
                            t.data = c;
                            var e = d.apply(n, t._args == f ? [ t ] : [ t ].concat(t._args));
                            return !1 === e && (t.preventDefault(), t.stopPropagation()), e;
                        }
                    }, i.i = m.length, m.push(i), "addEventListener" in n && n.addEventListener(a(i.e), i.proxy, o(i, p));
                });
            }
            function c(t, r, i, s, c) {
                var u = e(t);
                (r || "").split(/\s/).forEach(function(e) {
                    n(t, e, i, s).forEach(function(e) {
                        delete v[u][e.i], "removeEventListener" in t && t.removeEventListener(a(e.e), e.proxy, o(e, c));
                    });
                });
            }
            function u(e, n) {
                return !n && e.isDefaultPrevented || (n || (n = e), t.each(j, function(t, r) {
                    var i = n[t];
                    e[t] = function() {
                        return this[r] = x, i && i.apply(n, arguments);
                    }, e[r] = E;
                }), e.timeStamp || (e.timeStamp = Date.now()), (n.defaultPrevented !== f ? n.defaultPrevented : "returnValue" in n ? !1 === n.returnValue : n.getPreventDefault && n.getPreventDefault()) && (e.isDefaultPrevented = x)),
                e;
            }
            function l(t) {
                var e, n = {
                    originalEvent: t
                };
                for (e in t) S.test(e) || t[e] === f || (n[e] = t[e]);
                return u(n, t);
            }
            var f, h = 1, p = Array.prototype.slice, d = t.isFunction, m = function(t) {
                return "string" == typeof t;
            }, v = {}, g = {}, y = "onfocusin" in window, b = {
                focus: "focusin",
                blur: "focusout"
            }, w = {
                mouseenter: "mouseover",
                mouseleave: "mouseout"
            };
            g.click = g.mousedown = g.mouseup = g.mousemove = "MouseEvents", t.event = {
                add: s,
                remove: c
            }, t.proxy = function(n, r) {
                var i = 2 in arguments && p.call(arguments, 2);
                if (d(n)) {
                    var o = function() {
                        return n.apply(r, i ? i.concat(p.call(arguments)) : arguments);
                    };
                    return o._zid = e(n), o;
                }
                if (m(r)) return i ? (i.unshift(n[r], n), t.proxy.apply(null, i)) : t.proxy(n[r], n);
                throw new TypeError("expected function");
            }, t.fn.bind = function(t, e, n) {
                return this.on(t, e, n);
            }, t.fn.unbind = function(t, e) {
                return this.off(t, e);
            }, t.fn.one = function(t, e, n, r) {
                return this.on(t, e, n, r, 1);
            };
            var x = function() {
                return !0;
            }, E = function() {
                return !1;
            }, S = /^([A-Z]|returnValue$|layer[XY]$|webkitMovement[XY]$)/, j = {
                preventDefault: "isDefaultPrevented",
                stopImmediatePropagation: "isImmediatePropagationStopped",
                stopPropagation: "isPropagationStopped"
            };
            t.fn.delegate = function(t, e, n) {
                return this.on(e, t, n);
            }, t.fn.undelegate = function(t, e, n) {
                return this.off(e, t, n);
            }, t.fn.live = function(e, n) {
                return t(document.body).delegate(this.selector, e, n), this;
            }, t.fn.die = function(e, n) {
                return t(document.body).undelegate(this.selector, e, n), this;
            }, t.fn.on = function(e, n, r, i, o) {
                var a, u, h = this;
                return e && !m(e) ? (t.each(e, function(t, e) {
                    h.on(t, n, r, e, o);
                }), h) : (m(n) || d(i) || !1 === i || (i = r, r = n, n = f), i !== f && !1 !== r || (i = r,
                r = f), !1 === i && (i = E), h.each(function(f, h) {
                    o && (a = function(t) {
                        return c(h, t.type, i), i.apply(this, arguments);
                    }), n && (u = function(e) {
                        var r, o = t(e.target).closest(n, h).get(0);
                        if (o && o !== h) return r = t.extend(l(e), {
                            currentTarget: o,
                            liveFired: h
                        }), (a || i).apply(o, [ r ].concat(p.call(arguments, 1)));
                    }), s(h, e, i, r, n, u || a);
                }));
            }, t.fn.off = function(e, n, r) {
                var i = this;
                return e && !m(e) ? (t.each(e, function(t, e) {
                    i.off(t, n, e);
                }), i) : (m(n) || d(r) || !1 === r || (r = n, n = f), !1 === r && (r = E), i.each(function() {
                    c(this, e, r, n);
                }));
            }, t.fn.trigger = function(e, n) {
                return e = m(e) || t.isPlainObject(e) ? t.Event(e) : u(e), e._args = n, this.each(function() {
                    e.type in b && "function" == typeof this[e.type] ? this[e.type]() : "dispatchEvent" in this ? this.dispatchEvent(e) : t(this).triggerHandler(e, n);
                });
            }, t.fn.triggerHandler = function(e, r) {
                var i, o;
                return this.each(function(a, s) {
                    i = l(m(e) ? t.Event(e) : e), i._args = r, i.target = s, t.each(n(s, e.type || e), function(t, e) {
                        if (o = e.proxy(i), i.isImmediatePropagationStopped()) return !1;
                    });
                }), o;
            }, "focusin focusout focus blur load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select keydown keypress keyup error".split(" ").forEach(function(e) {
                t.fn[e] = function(t) {
                    return 0 in arguments ? this.bind(e, t) : this.trigger(e);
                };
            }), t.Event = function(t, e) {
                m(t) || (e = t, t = e.type);
                var n = document.createEvent(g[t] || "Events"), r = !0;
                if (e) for (var i in e) "bubbles" == i ? r = !!e[i] : n[i] = e[i];
                return n.initEvent(t, r, !0), u(n);
            };
        }(n), function(t) {
            function e(e, n, r) {
                var i = t.Event(n);
                return t(e).trigger(i, r), !i.isDefaultPrevented();
            }
            function n(t, n, r, i) {
                if (t.global) return e(n || y, r, i);
            }
            function r(e) {
                e.global && 0 == t.active++ && n(e, null, "ajaxStart");
            }
            function i(e) {
                e.global && !--t.active && n(e, null, "ajaxStop");
            }
            function o(t, e) {
                var r = e.context;
                if (!1 === e.beforeSend.call(r, t, e) || !1 === n(e, r, "ajaxBeforeSend", [ t, e ])) return !1;
                n(e, r, "ajaxSend", [ t, e ]);
            }
            function a(t, e, r, i) {
                var o = r.context;
                r.success.call(o, t, "success", e), i && i.resolveWith(o, [ t, "success", e ]),
                n(r, o, "ajaxSuccess", [ e, r, t ]), c("success", e, r);
            }
            function s(t, e, r, i, o) {
                var a = i.context;
                i.error.call(a, r, e, t), o && o.rejectWith(a, [ r, e, t ]), n(i, a, "ajaxError", [ r, i, t || e ]),
                c(e, r, i);
            }
            function c(t, e, r) {
                var o = r.context;
                r.complete.call(o, e, t), n(r, o, "ajaxComplete", [ e, r ]), i(r);
            }
            function u() {}
            function l(t) {
                return t && (t = t.split(";", 2)[0]), t && (t == S ? "html" : t == E ? "json" : w.test(t) ? "script" : x.test(t) && "xml") || "text";
            }
            function f(t, e) {
                return "" == e ? t : (t + "&" + e).replace(/[&?]{1,2}/, "?");
            }
            function h(e) {
                e.processData && e.data && "string" != t.type(e.data) && (e.data = t.param(e.data, e.traditional)),
                !e.data || e.type && "GET" != e.type.toUpperCase() && "jsonp" != e.dataType || (e.url = f(e.url, e.data),
                e.data = void 0);
            }
            function p(e, n, r, i) {
                return t.isFunction(n) && (i = r, r = n, n = void 0), t.isFunction(r) || (i = r,
                r = void 0), {
                    url: e,
                    data: n,
                    success: r,
                    dataType: i
                };
            }
            function d(e, n, r, i) {
                var o, a = t.isArray(n), s = t.isPlainObject(n);
                t.each(n, function(n, c) {
                    o = t.type(c), i && (n = r ? i : i + "[" + (s || "object" == o || "array" == o ? n : "") + "]"),
                    !i && a ? e.add(c.name, c.value) : "array" == o || !r && "object" == o ? d(e, c, r, n) : e.add(n, c);
                });
            }
            var m, v, g = +new Date(), y = window.document, b = /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, w = /^(?:text|application)\/javascript/i, x = /^(?:text|application)\/xml/i, E = "application/json", S = "text/html", j = /^\s*$/, T = y.createElement("a");
            T.href = window.location.href, t.active = 0, t.ajaxJSONP = function(e, n) {
                if (!("type" in e)) return t.ajax(e);
                var r, i, c = e.jsonpCallback, u = (t.isFunction(c) ? c() : c) || "Zepto" + g++, l = y.createElement("script"), f = window[u], h = function(e) {
                    t(l).triggerHandler("error", e || "abort");
                }, p = {
                    abort: h
                };
                return n && n.promise(p), t(l).on("load error", function(o, c) {
                    clearTimeout(i), t(l).off().remove(), "error" != o.type && r ? a(r[0], p, e, n) : s(null, c || "error", p, e, n),
                    window[u] = f, r && t.isFunction(f) && f(r[0]), f = r = void 0;
                }), !1 === o(p, e) ? (h("abort"), p) : (window[u] = function() {
                    r = arguments;
                }, l.src = e.url.replace(/\?(.+)=\?/, "?$1=" + u), y.head.appendChild(l), e.timeout > 0 && (i = setTimeout(function() {
                    h("timeout");
                }, e.timeout)), p);
            }, t.ajaxSettings = {
                type: "GET",
                beforeSend: u,
                success: u,
                error: u,
                complete: u,
                context: null,
                global: !0,
                xhr: function() {
                    return new window.XMLHttpRequest();
                },
                accepts: {
                    script: "text/javascript, application/javascript, application/x-javascript",
                    json: E,
                    xml: "application/xml, text/xml",
                    html: S,
                    text: "text/plain"
                },
                crossDomain: !1,
                timeout: 0,
                processData: !0,
                cache: !0
            }, t.ajax = function(e) {
                var n, i, c = t.extend({}, e || {}), p = t.Deferred && t.Deferred();
                for (m in t.ajaxSettings) void 0 === c[m] && (c[m] = t.ajaxSettings[m]);
                r(c), c.crossDomain || (n = y.createElement("a"), n.href = c.url, n.href = n.href,
                c.crossDomain = T.protocol + "//" + T.host != n.protocol + "//" + n.host), c.url || (c.url = window.location.toString()),
                (i = c.url.indexOf("#")) > -1 && (c.url = c.url.slice(0, i)), h(c);
                var d = c.dataType, g = /\?.+=\?/.test(c.url);
                if (g && (d = "jsonp"), !1 !== c.cache && (e && !0 === e.cache || "script" != d && "jsonp" != d) || (c.url = f(c.url, "_=" + Date.now())),
                "jsonp" == d) return g || (c.url = f(c.url, c.jsonp ? c.jsonp + "=?" : !1 === c.jsonp ? "" : "callback=?")),
                t.ajaxJSONP(c, p);
                var b, w = c.accepts[d], x = {}, E = function(t, e) {
                    x[t.toLowerCase()] = [ t, e ];
                }, S = /^([\w-]+:)\/\//.test(c.url) ? RegExp.$1 : window.location.protocol, O = c.xhr(), C = O.setRequestHeader;
                if (p && p.promise(O), c.crossDomain || E("X-Requested-With", "XMLHttpRequest"),
                E("Accept", w || "*/*"), (w = c.mimeType || w) && (w.indexOf(",") > -1 && (w = w.split(",", 2)[0]),
                O.overrideMimeType && O.overrideMimeType(w)), (c.contentType || !1 !== c.contentType && c.data && "GET" != c.type.toUpperCase()) && E("Content-Type", c.contentType || "application/x-www-form-urlencoded"),
                c.headers) for (v in c.headers) E(v, c.headers[v]);
                if (O.setRequestHeader = E, O.onreadystatechange = function() {
                    if (4 == O.readyState) {
                        O.onreadystatechange = u, clearTimeout(b);
                        var e, n = !1;
                        if (O.status >= 200 && O.status < 300 || 304 == O.status || 0 == O.status && "file:" == S) {
                            if (d = d || l(c.mimeType || O.getResponseHeader("content-type")), "arraybuffer" == O.responseType || "blob" == O.responseType) e = O.response; else {
                                e = O.responseText;
                                try {
                                    "script" == d ? (0, eval)(e) : "xml" == d ? e = O.responseXML : "json" == d && (e = j.test(e) ? null : t.parseJSON(e));
                                } catch (t) {
                                    n = t;
                                }
                                if (n) return s(n, "parsererror", O, c, p);
                            }
                            a(e, O, c, p);
                        } else s(O.statusText || null, O.status ? "error" : "abort", O, c, p);
                    }
                }, !1 === o(O, c)) return O.abort(), s(null, "abort", O, c, p), O;
                var P = !("async" in c) || c.async;
                if (O.open(c.type, c.url, P, c.username, c.password), c.xhrFields) for (v in c.xhrFields) O[v] = c.xhrFields[v];
                for (v in x) C.apply(O, x[v]);
                return c.timeout > 0 && (b = setTimeout(function() {
                    O.onreadystatechange = u, O.abort(), s(null, "timeout", O, c, p);
                }, c.timeout)), O.send(c.data ? c.data : null), O;
            }, t.get = function() {
                return t.ajax(p.apply(null, arguments));
            }, t.post = function() {
                var e = p.apply(null, arguments);
                return e.type = "POST", t.ajax(e);
            }, t.getJSON = function() {
                var e = p.apply(null, arguments);
                return e.dataType = "json", t.ajax(e);
            }, t.fn.load = function(e, n, r) {
                if (!this.length) return this;
                var i, o = this, a = e.split(/\s/), s = p(e, n, r), c = s.success;
                return a.length > 1 && (s.url = a[0], i = a[1]), s.success = function(e) {
                    o.html(i ? t("<div>").html(e.replace(b, "")).find(i) : e), c && c.apply(o, arguments);
                }, t.ajax(s), this;
            };
            var O = encodeURIComponent;
            t.param = function(e, n) {
                var r = [];
                return r.add = function(e, n) {
                    t.isFunction(n) && (n = n()), null == n && (n = ""), this.push(O(e) + "=" + O(n));
                }, d(r, e, n), r.join("&").replace(/%20/g, "+");
            };
        }(n), function(t) {
            t.fn.serializeArray = function() {
                var e, n, r = [], i = function(t) {
                    if (t.forEach) return t.forEach(i);
                    r.push({
                        name: e,
                        value: t
                    });
                };
                return this[0] && t.each(this[0].elements, function(r, o) {
                    n = o.type, e = o.name, e && "fieldset" != o.nodeName.toLowerCase() && !o.disabled && "submit" != n && "reset" != n && "button" != n && "file" != n && ("radio" != n && "checkbox" != n || o.checked) && i(t(o).val());
                }), r;
            }, t.fn.serialize = function() {
                var t = [];
                return this.serializeArray().forEach(function(e) {
                    t.push(encodeURIComponent(e.name) + "=" + encodeURIComponent(e.value));
                }), t.join("&");
            }, t.fn.submit = function(e) {
                if (0 in arguments) this.bind("submit", e); else if (this.length) {
                    var n = t.Event("submit");
                    this.eq(0).trigger(n), n.isDefaultPrevented() || this.get(0).submit();
                }
                return this;
            };
        }(n), function(t) {
            "__proto__" in {} || t.extend(t.zepto, {
                Z: function(e, n) {
                    return e = e || [], t.extend(e, t.fn), e.selector = n || "", e.__Z = !0, e;
                },
                isZ: function(e) {
                    return "array" === t.type(e) && "__Z" in e;
                }
            });
            try {
                getComputedStyle(void 0);
            } catch (t) {
                var e = getComputedStyle;
                window.getComputedStyle = function(t, n) {
                    try {
                        return e(t, n);
                    } catch (t) {
                        return null;
                    }
                };
            }
        }(n);
    },
    h2Jj: function(t, e) {
        !function(t) {
            function e(t, e) {
                var n = this.os = {}, r = this.browser = {}, i = t.match(/Web[kK]it[\/]{0,1}([\d.]+)/), o = t.match(/(Android);?[\s\/]+([\d.]+)?/), a = !!t.match(/\(Macintosh\; Intel /), s = t.match(/(iPad).*OS\s([\d_]+)/), c = t.match(/(iPod)(.*OS\s([\d_]+))?/), u = !s && t.match(/(iPhone\sOS)\s([\d_]+)/), l = t.match(/(webOS|hpwOS)[\s\/]([\d.]+)/), f = /Win\d{2}|Windows/.test(e), h = t.match(/Windows Phone ([\d.]+)/), p = l && t.match(/TouchPad/), d = t.match(/Kindle\/([\d.]+)/), m = t.match(/Silk\/([\d._]+)/), v = t.match(/(BlackBerry).*Version\/([\d.]+)/), g = t.match(/(BB10).*Version\/([\d.]+)/), y = t.match(/(RIM\sTablet\sOS)\s([\d.]+)/), b = t.match(/PlayBook/), w = t.match(/Chrome\/([\d.]+)/) || t.match(/CriOS\/([\d.]+)/), x = t.match(/Firefox\/([\d.]+)/), E = t.match(/MSIE\s([\d.]+)/) || t.match(/Trident\/[\d](?=[^\?]+).*rv:([0-9.].)/), S = !w && t.match(/(iPhone|iPod|iPad).*AppleWebKit(?!.*Safari)/), j = S || t.match(/Version\/([\d.]+)([^S](Safari)|[^M]*(Mobile)[^S]*(Safari))/);
                (r.webkit = !!i) && (r.version = i[1]), o && (n.android = !0, n.version = o[2]),
                u && !c && (n.ios = n.iphone = !0, n.version = u[2].replace(/_/g, ".")), s && (n.ios = n.ipad = !0,
                n.version = s[2].replace(/_/g, ".")), c && (n.ios = n.ipod = !0, n.version = c[3] ? c[3].replace(/_/g, ".") : null),
                h && (n.wp = !0, n.version = h[1]), l && (n.webos = !0, n.version = l[2]), p && (n.touchpad = !0),
                v && (n.blackberry = !0, n.version = v[2]), g && (n.bb10 = !0, n.version = g[2]),
                y && (n.rimtabletos = !0, n.version = y[2]), b && (r.playbook = !0), d && (n.kindle = !0,
                n.version = d[1]), m && (r.silk = !0, r.version = m[1]), !m && n.android && t.match(/Kindle Fire/) && (r.silk = !0),
                w && (r.chrome = !0, r.version = w[1]), x && (r.firefox = !0, r.version = x[1]),
                E && (r.ie = !0, r.version = E[1]), j && (a || n.ios || f) && (r.safari = !0, n.ios || (r.version = j[1])),
                S && (r.webview = !0), n.tablet = !!(s || b || o && !t.match(/Mobile/) || x && t.match(/Tablet/) || E && !t.match(/Phone/) && t.match(/Touch/)),
                n.phone = !(n.tablet || n.ipod || !(o || u || l || v || g || w && t.match(/Android/) || w && t.match(/CriOS\/([\d.]+)/) || x && t.match(/Mobile/) || E && t.match(/Touch/)));
            }
            e.call(t, navigator.userAgent, navigator.platform), t.__detect = e;
        }(Zepto);
    }
});