!
function(e, t) {
    function a(a) {
        function i() {
            r && clearInterval && clearInterval(r),
            r = setInterval && setInterval(function() {
                a && a(r)
            },
            500)
        }
        var n = t.body,
        r = null;
        e.onload = function(t) {
            i(t),
            e.addEventListener && (n.addEventListener("DOMSubtreeModified", i, !1), n.addEventListener("DOMNodeInserted", i, !1))
        }
    }
    function i() {
        this._imgMaps = {},
        this._mapDone = {},
        this._ubtImgs = [],
        this._init()
    }
    i.prototype = {
        _init: function() {
            var e = this,
            a = Object.create(HTMLImageElement.prototype);
            a.createdCallback = function() {
                var t = this.getAttribute("src"),
                a = this.getAttribute("pageCode"),
                i = e._absolutePath(t);
                e._mapDone[i] || e._imgMaps[i] || (e._imgMaps[i] = {
                    url: i,
                    pageCode: a
                },
                e._getAjaxHeader(t))
            },
            t.registerElement && t.registerElement("c-img", {
                prototype: a,
                "extends": "img"
            })
        },
        _getAjaxHeader: function(t) {
            function a() {
                return e.ActiveXObject ? new ActiveXObject("Microsoft.XMLHTTP") : e.XMLHttpRequest ? new XMLHttpRequest: void 0
            }
            function i() {
                try {
                    n = a(),
                    n.onreadystatechange = function() {
                        if (4 == n.readyState) try {
                            r._imgMaps[s].ajaxReady = !0,
                            r._imgMaps[s].status = n.status;
                            var e = n.getResponseHeader("img-proc-id"),
                            t = n.getResponseHeader("img-ver");
                            r._imgMaps[s] && (r._imgMaps[s].imgProcId = e, r._imgMaps[s].imgVer = t)
                        } catch(a) {}
                    },
                    n.open("GET", t, !0),
                    n.send(null)
                } catch(e) {}
            }
            var n, r = this,
            s = r._absolutePath(t);
            i(t)
        },
        _getImgEntries: function() {
            var t = this;
            if (e.performance && e.performance.getEntries) for (var a = e.performance.getEntries(), i = 0; i < a.length; i++) {
                var n = a[i];
                if (n && "img" == n.initiatorType) {
                    var r = n.name;
                    t._imgMaps[r] && (t._imgMaps[r].duration = n.duration, t._imgMaps[r].size = n.transferSize)
                }
            }
        },
        _absolutePath: function(e) {
            var a = t.createElement("a");
            a.setAttribute("href", e);
            var i = a.href;
            return a = null,
            i
        },
        sendUbt: function() {
            for (var t, a = 0; a < n._ubtImgs.length; a++) t = n._ubtImgs[a],
            e.__bfi = e.__bfi || [],
            e.__bfi.push(["_trackMatrix", "h5_pic_download", {
                imgProcId: t.imgProcId,
                imgVer: t.imgVer,
                pageCode: t.pageCode,
                url: t.url,
                status: t.status
            },
            {
                duration: t.duration,
                size: t.size
            }]);
            this._ubtImgs = []
        },
        show: function() {
            return this._getImgEntries(),
            this._imgMaps
        }
    };
    var n = new i;
    a(function(e) {
        var t = n.show(),
        a = !0;
        for (var i in t) n._imgMaps[i].ajaxReady ? n._mapDone[i] || (n._mapDone[i] = 1, n._ubtImgs.push(t[i])) : a = !1;
        a && clearInterval && clearInterval(e),
        n.sendUbt()
    })
} (window, document);
//# sourceMappingURL=ImgMonitor.js.ad9b7c82.map
