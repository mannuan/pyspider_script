function fun1(o, n, a) {
    for (var s, l, c, u = 0, p = []; u < o.length; u++) l = o[u], i[l] && p.push(i[l][0]),
    i[l] = 0;
    for (s in n) Object.prototype.hasOwnProperty.call(n, s) && (e[s] = n[s]);
    for (r && r(o, n, a); p.length; ) p.shift()();
    if (a) for (u = 0; u < a.length; u++) c = t(t.s = a[u]);
    return c;
}

var param1 = {
            LWyc: function(t, e, i) {
            "use strict";
            Object.defineProperty(e, "__esModule", {
                value: !0
            });
            var o = i("TToO"),
            s = i("309y"),
            n = i.n(s),
            r = i("+X65"),
            a = i.n(r),
            l = i("RyI1"),
            c = i.n(l),
            u = i("kvU2"),
            p = i.n(u),
            h = i("kbi+"),
            d = i.n(h),
            f = i("KgVm"),
            g = i.n(f),
            m = i("yKmV"),
            y = i("KoQ7"),
            v = i("yaBp"),
            b = i("6rBr"),
            w = i("oVmA"),
            S = i("rfSs"),
            _ = i("+b/N"),
            k = i("cPge"),
            x = i("LpuJ"),
            C = i("za/N"),
            P = i("X8N+"),
            I = i("WxdK"),
            T = i("bjbd"),
            L = i("bV2p"),
            j = i("+3UB"),
            A = i("y9O2"),
            O = i("V5ch"),
            D = i("YGS1"),
            M = i("IVDy"),
            E = i("19gJ"),
            q = i("gsCt"),
            F = i("q2rF"),
            H = i("VeCz"),
            N = i("30VQ"),
            R = (i.n(N), i("tk9w")),
            B = (i.n(R), i("A70E")),
            z = (i.n(B), i("j8K2")),
            K = (i.n(z), i("oEgB")),
            G = i("sM4E"),
            U = i("+6wk"),
            W = i("H80H"),
            V = i("8ZTd"),
            Q = i("wLUE"),
            Z = i("IOAa"),
            Y = i("E+zg"),
            J = i("meYf"),
            X = i("vrqZ"),
            tt = i("vvlq"),
            et = i("CK3L"),
            it = i("+JQy"),
            ot = i("CJ1A"),
            st = new _.b({
                key: "MESSAGE_FLAG",
                lifeTime: "24H",
                isUserData: !0,
                defaultData: {
                    oversea_price_tip: ""
                }
            }),
            nt = new _.b({
                key: "S_HOTEL_QUERY",
                lifeTime: "48H",
                isUserData: !0
            }),
            rt = {
                bedtype: [{
                    key: 1,
                    val: "\u5355\u4eba\u5e8a"
                },
                {
                    key: 2,
                    val: "\u5927\u5e8a"
                },
                {
                    key: 4,
                    val: "\u53cc\u5e8a"
                },
                {
                    key: 8,
                    val: "\u4e09\u4eba/\u5bb6\u5ead\u623f"
                }],
                breakfast: [{
                    key: 1,
                    val: "\u542b\u65e9\u9910"
                },
                {
                    key: 2,
                    val: "\u5355\u4efd\u65e9\u9910"
                },
                {
                    key: 4,
                    val: "\u53cc\u4efd\u65e9\u9910"
                }],
                facility: [{
                    key: 1,
                    val: "\u514d\u8d39WIFI\u4e0a\u7f51"
                },
                {
                    key: 2,
                    val: "\u514d\u8d39\u6709\u7ebf\u5bbd\u5e26"
                },
                {
                    key: 2048,
                    val: "\u589e\u503c\u7a0e\u4e13\u7528\u53d1\u7968"
                }],
                paytype: [{
                    key: 1,
                    val: "\u5728\u7ebf\u4ed8\u6b3e"
                },
                {
                    key: 2,
                    val: "\u5230\u5e97\u4ed8\u6b3e"
                }],
                service: [{
                    key: 1,
                    val: "\u643a\u7a0b\u81ea\u8425"
                },
                {
                    key: 2,
                    val: "\u514d\u8d39\u53d6\u6d88"
                },
                {
                    key: 4,
                    val: "\u7acb\u5373\u786e\u8ba4"
                },
                {
                    key: 8,
                    val: "\u53ef\u8ba2"
                }],
                promotion: [{
                    key: 1,
                    val: "\u53ef\u52a0\u5e8a"
                },
                {
                    key: 2,
                    val: "\u6ee1\u5341\u9001\u4e00"
                }],
                feature: [{
                    key: 202,
                    val: "\u949f\u70b9\u623f"
                }]
            },
            at = {
                room: 1,
                adult: 1,
                children: [ - 1, -1, -1]
            },
            lt = function(t) {
                function e() {
                    for (var e = [], i = 0; i < arguments.length; i++) e[i] = arguments[i];
                    var o = t.apply(this, e) || this;
                    return o.pageName = "searchlist",
                    o
                }
                return o.a(e, t),
                e.prototype.ready = function() {
                    var e = this;
                    this.hideHeader(),
                    this.searchStatusProvider = new O.a,
                    this.pageStatus = this.generatePageStatus(),
                    "#gotoDetail" === location.hash && "HotelListMap" !== this.pageStatus.currentPage && (document.getElementsByTagName("html")[0].style.opacity = "1"),
                    this.pageStatus.request.cityName || this.showPositionForUserLocationSearch(),
                    4 == (4 & this.pageStatus.request.controlBitMap) && this.morningStore.setStatus(!0),
                    st.getAttr("oversea_price_tip") && this.closeOverseaPriceTip(),
                    this.loginguideStatusProvider = new E.a("loginguidestatus_hotellist"),
                    this.initLoginGuide(),
                    this.pageStatus.response.hotelListMap && ($("#header").hide(), this.$el.hide(), this.showHTML(), this.onOpenMap(), this.pageStatus.response.hotelListMap = !1, document.getElementsByTagName("html")[0].style.opacity = "1"),
                    this.pageStatus.response.uiModifyInfo.priceStarText && (this.pageStatus.priceStarText = this.pageStatus.response.uiModifyInfo.priceStarText),
                    this.hotelListMenu = new H.a({
                        wrapper: $(".js_hotelistmenu_c"),
                        datamodel: {
                            isOversea: this.pageStatus.response.oversea,
                            selectedFilterCount: this.pageStatus.response.uiModifyInfo.filterItemList.length,
                            sortFilterText: this.pageStatus.response.uiModifyInfo.orderText,
                            areaFilterText: this.pageStatus.response.uiModifyInfo.areaText,
                            priceStarFilterText: this.pageStatus.response.uiModifyInfo.priceStarText
                        }
                    }),
                    this.hotelListMenu.on("filterPanelOpen", this.openFilterPanel.bind(this)),
                    this.hotelListMenu.on("filterPanelClose", this.closeFilterPanel.bind(this)),
                    this.hotelListMenu.on("areaFilterPanelOpen", this.openAreaFilterPanel.bind(this)),
                    this.hotelListMenu.on("areaFilterPanelClose", this.closeAreaFilterPanel.bind(this)),
                    this.hotelListMenu.on("sortFilterPanelOpen", this.openSortFilterPanel.bind(this)),
                    this.hotelListMenu.on("sortFilterPanelClose", this.closeSortFilterPanel.bind(this)),
                    this.hotelListMenu.on("priceStarFilterPanelOpen", this.openPriceStarFilterPanel.bind(this)),
                    this.hotelListMenu.on("priceStarFilterPanelClose", this.closePriceStarFilterPanel.bind(this)),
                    this.hotelListMenu.on("opening",
                    function() {
                        $(".js_list_container").css("overflow-y", "hidden")
                    }),
                    this.hotelListMenu.on("closing",
                    function() {
                        $(".js_list_container").css("overflow-y", "scroll")
                    }),
                    this.hotelListMenu.show(),
                    this.quickFilter = new G.a($(".js_quick_filter")),
                    this.quickFilter.on("onItemClick",
                    function(t, i, o) {
                        e.onQuickFilterClick(t, i, o)
                    }),
                    this.quickFilter.on("openPaytypePanel", this.openPaytypePanel.bind(this)),
                    this.quickFilter.on("ownAround", this.onQuickFilterOwnAround.bind(this)),
                    this.quickFilter.on("cancelOwnAround", this.cancelOwnAround.bind(this)),
                    this.quickFilter.show(),
                    this.hotelListMenu.$el.on("click",
                    function() {
                        e.paytypePanel && e.paytypePanel.hide()
                    }),
                    this.hotelListMenu.mask.$el.on("click",
                    function() {
                        e.quickFilter.$(".js_paytype i").removeClass("font-g-arrow-up").addClass("font-g-arrow-down"),
                        e.paytypePanel && e.paytypePanel.hide()
                    }),
                    this.keywordBar = new U.a({
                        wrapper: $(".js_kewordbar"),
                        request: this.pageStatus.request
                    }),
                    this.keywordBar.on("onOpenKeywordPanel",
                    function() {
                        e.openKeywordPanel().then(function() {
                            e.keywordPanel.isTriggerbyUI = !0,
                            e.pageStatus.displayKeywordText && (e.keywordPanel.searchbar.update({
                                cityID: e.pageStatus.request.cityID,
                                keyword: e.pageStatus.displayKeywords
                            }), e.keywordPanel.searchbar._setSearchBoxStatus({
                                txt: e.pageStatus.displayKeywords || "",
                                iconLoading: !1,
                                btnRight: 0
                            }), e.keywordPanel.searchbar.hideKWACList(), e.keywordPanel.$el.find(".js_kw_content").removeAttr("style"))
                        })
                    }),
                    this.keywordBar.on("onKeywordBarClear",
                    function(t) {
                        e.onKeywordBarClear(t)
                    }),
                    this.keywordBar.show(),
                    this.keywordBar.updateKeywordBarText(this.pageStatus.displayKeywords),
                    this.hotelListProvider = new D.a,
                    this.hotelListProvider.on("getHotelListDataFail",
                    function() {}),
                    this.hotelListProvider.on("getHotelNextPageSuccess",
                    function(t) {
                        e.hotellistpanel.updatePageDomStatus(t, e.pageStatus.hasViewTotalPrice ? e.updatePrice: null),
                        e.showHotSearchKeyword(),
                        e.updateExposedZoneList()
                    }),
                    this.hotelListProvider.on("getHotelNextPageLoading",
                    function() {
                        e.hotellistpanel.loading()
                    }),
                    this.hotelListProvider.on("getHotelHomePageSuccess",
                    function(t) { (e.onHotelListProviderGetHotelHomePageSuccess(t, e.pageStatus.hasViewTotalPrice ? e.updatePrice: null), e.showHotSearchKeyword(), e.addBrowseHistoryStyle(), st.getAttr("oversea_price_tip") && e.closeOverseaPriceTip(), "loginsuc" === e.getOneMessage("showToast")) && new P.a({
                            datamodel: {
                                content: "\u767b\u5f55\u6210\u529f"
                            }
                        }).show()
                    }),
                    this.hotelListProvider.on("getHotelHomePageFail",
                    function() {
                        e.onAbnromalNetwork()
                    }),
                    this.hotellistpanel = new Z.a($(".js_list_container"));
                    var i = this;
                    window.addEventListener("scroll",
                    function(t) {
                        i.hotellistpanel.onScroll.call(i.hotellistpanel, t)
                    }),
                    this.hotellistpanel.on("onFetchHotelData",
                    function() {
                        e.hotelListProvider.getHotelNextPage(e.pageStatus),
                        e.recordUserActionFlow("list_scorenextpage")
                    }),
                    this.inAndOutPanel = this.$el.find(".js_inoutday .star p"),
                    t.prototype.ready.call(this),
                    this.prepareHomeNextHotelData(),
                    this.restoreComponentsStatus(),
                    1 === this.pageStatus.response.isAroundhotellanding && this.ownAround(),
                    this.hideToast(),
                    this.addBrowseHistoryStyle(),
                    this.updateHeader(),
                    this.updateHotelQueryStore(),
                    this.hotellistpanel.onScroll(this),
                    this.showNewGuestCouponEntr(),
                    this.showHotSearchKeyword(),
                    this.overseaTraceLog(),
                    this.initRoomPeopleNumSelect()
                },
                e.prototype.initRoomPeopleNumSelect = function() {
                    if (this.pageStatus.request.oversea) {
                        var t = this.pageStatus.request,
                        e = t.adultCounts,
                        i = t.childAges,
                        o = t.roomQuantity;
                        if (!e) {
                            var s = nt.getAttr("queryParams") || {};
                            s.numselect && (o = s.numselect.room, e = s.numselect.adult, i = s.numselect.children)
                        }
                        if (e && i) {
                            var r = i.split("|"),
                            a = c()(r,
                            function(t) {
                                return parseInt(t, 10) >= 0
                            }).length,
                            l = [];
                            n()(r,
                            function(t) {
                                return l.push(parseInt(t))
                            }),
                            this.$(".js_numselect_adult").html("\u6210\u4eba&nbsp;" + e),
                            this.$(".js_numselect_child").html("\u513f\u7ae5&nbsp;" + a),
                            this.pageStatus.numselect = {
                                room: o,
                                adult: e,
                                children: l
                            },
                            this.updateHotelQueryStore()
                        }
                        this.$(".js_keywordbar_content").attr("placeholder", "\u4f4d\u7f6e/\u54c1\u724c/\u9152\u5e97"),
                        this.$(".js_numselect").show()
                    }
                },
                e.prototype.showHotSearchKeyword = function() {
                    var t = parseInt(this.pageStatus.request.pageIndex, 10),
                    e = $(".js_hotsearchkeyword"),
                    i = this.pageStatus.response.hotSearchKeywordGroupList;
                    this.hotSearchKeyword && 1 === t && (this.hotSearchKeyword.destroy(), delete this.hotSearchKeyword),
                    e && e[0] && i && i.length >= 1 && (this.hotSearchKeyword || (this.hotSearchKeyword = new et.a({
                        wrapper: e,
                        datamodel: {
                            hotSearchKeywordGroupList: i
                        }
                    }), this.hotSearchKeyword.on("selectHotSearchKeyword", this.onSelectHotSearchKeyword.bind(this)), this.hotSearchKeyword.on("cancelHotSearchKeyword", this.onCancelHotSearchKeyword.bind(this))), this.hotSearchKeyword.update(this.pageStatus.response.uiModifyInfo && this.pageStatus.response.uiModifyInfo.displayKeyword), this.hotSearchKeyword.show())
                },
                e.prototype.restoreHotSearchKeyword = function() {
                    var t = $(".js_hotsearchkeyword");
                    t && t[0] && t.html(""),
                    this.showHotSearchKeyword()
                },
                e.prototype.onSelectHotSearchKeyword = function(t) {
                    this.onKeywordDirectSearch(t, !0)
                },
                e.prototype.onCancelHotSearchKeyword = function() {
                    this.keywordBar.onClear()
                },
                e.prototype.overseaTraceLog = function() {
                    if (this.pageStatus.request.oversea) {
                        var t = "";
                        this.pageStatus.request.starItemList && this.pageStatus.request.starItemList.forEach(function(e) {
                            var i = e.split("-");
                            i.length >= 2 && (t = t ? t + "," + i[1] : "" + i[1])
                        });
                        var e = {
                            cityid: this.pageStatus.request.cityID,
                            starttime: b.a.parse(this.pageStatus.request.checkinDate).format("Y-m-d"),
                            endtime: b.a.parse(this.pageStatus.request.checkoutDate).format("Y-m-d"),
                            star: t,
                            keywords: this.pageStatus.request.keyword,
                            position: this.pageStatus.request.userLocationSearch ? this.pageStatus.request.cityName: ""
                        };
                        window.__bfi.push(["_tracklog", "hotel_oversea_listpage_H5", JSON.stringify(e)])
                    }
                },
                e.prototype.listContScrollHandler = function() {
                    if (this.channelData.isHideHeader || v.a.vendor.is("CTRIP")) return $("html,body").css("overflow", "hidden"),
                    void $("#content").css("height", "100%");
                    var t = this.$el.find(".js_list_container"),
                    e = t.scrollTop();
                    $("html,body").css("overflow", "hidden"),
                    $("#content").css({
                        height: "100%",
                        "padding-bottom": "2.2rem",
                        "box-sizing": "border-box"
                    });
                    var i = 2 * $("#header").height(),
                    o = function() {
                        var o = t.scrollTop(),
                        s = t.height(),
                        n = t[0].scrollHeight;
                        if (! (o + s + i > n || o < 0)) {
                            var r = window.navigator.userAgent.indexOf("iPhone OS 11_2") >= 0 ? "150%": "calc(100% + 4.4rem)";
                            o > e ? $("body").css({
                                height: r,
                                "-webkit-transform": "translateY(-4.4rem)",
                                transform: "translateY(-4.4rem)",
                                "-webkit-transition": "all 200ms linear",
                                transition: "all 200ms linear"
                            }).attr("direction", "up") : o < e && $("body").css({
                                height: "100%",
                                "-webkit-transform": "translateY(0)",
                                transform: "translateY(0)",
                                "-webkit-transition": "all 200ms linear",
                                transition: "all 200ms linear"
                            }).attr("direction", "down"),
                            e = o
                        }
                    };
                    t.on("scroll", a()(o, 200))
                },
                e.prototype.stopHeaderAnimate = function() {
                    $("body").removeAttr("style")
                },
                e.prototype.restoreHeaderAnimation = function() {
                    "up" === $("body").attr("direction") && $("body").css({
                        height: "calc(100% + 4.4rem)",
                        "-webkit-transform": "translateY(-4.4rem)",
                        transform: "translateY(-4.4rem)"
                    })
                },
                e.prototype.hideHeaderInListMap = function() {
                    if (this.hotelListMapPanel && this.hotelListMapPanel.inMapPage) return void this.$header.hide()
                },
                e.prototype.resetPanelTopInListMap = function(t) {
                    if (this.hotelListMapPanel && this.hotelListMapPanel.inMapPage) {
                        var e = $(".map-hd").height();
                        e && (t.panelTop = e)
                    }
                },
                e.prototype.hideHeader = function() {
                    1 === this.channelData.isHideHeader && $("#header").hide()
                },
                e.prototype.showPositionForUserLocationSearch = function() {
                    var t = this;
                    this.pageStatus.request.userLocationSearch && !this.pageStatus.response.positionInfo.cityName && I.a.requestAMapAddress(this.pageStatus.request.userLongitude, this.pageStatus.request.userLatitude,
                    function(e) {
                        t.pageStatus.request.cityName = e.address,
                        t.updateHeader()
                    },
                    function() {})
                },
                e.prototype.forbidScroll = function() {
                    this.$(".js_list_container").css({
                        overflowY: "hidden"
                    }),
                    this.disableScroll()
                },
                e.prototype.unForbidScroll = function() {
                    this.$(".js_list_container").css({
                        overflowY: "scroll"
                    }),
                    this.enableScroll()
                },
                e.prototype.showNewGuestCouponEntr = function() {
                    var t = this,
                    e = this;
                    if (this.canShowNewGuestCoupon()) {
                        this.loginGuide && this.loginGuide.hide(),
                        this.newGuestCouponEntr || (this.newGuestCouponEntr = new j.a({
                            wrapper: $(".js_newguestcoupon"),
                            isMemberLogin: this.appData.isMemberLogin,
                            datamodel: {
                                canReceive: this.pageStatus.newGuestCouponEntrance.canReceive,
                                isOversea: this.pageStatus.request.oversea,
                                fromList: !0
                            }
                        }), this.newGuestCouponEntr.on("refreshCallBack",
                        function() {
                            e.refreshHotelListBody()
                        }), this.newGuestCouponEntr.on("loginShow",
                        function() {
                            e.forbidScroll()
                        }), this.newGuestCouponEntr.on("loginHide",
                        function() {
                            e.unForbidScroll()
                        }), this.newGuestCouponEntr.on("showingLayer",
                        function() {
                            e.forbidScroll()
                        }), this.newGuestCouponEntr.on("closeLayer",
                        function() {
                            e.unForbidScroll()
                        }));
                        var i = this.pageStatus.request.oversea;
                        if (void 0 !== this.pageStatus.locatedOversea && (i = this.pageStatus.locatedOversea), this.newGuestCouponEntr.update({
                            canReceive: this.pageStatus.newGuestCouponEntrance.canReceive,
                            isOversea: i,
                            fromList: !0
                        }), this.newGuestCouponEntr.show(), this.newGuestCouponEntr.updateBackImage(i), e.pageData && e.pageData.showLandingPageNewGuestCouponPop) {
                            var o = new A.a;
                            o.on("click",
                            function() {
                                o.hide(),
                                t.newGuestCouponEntr.handleNewGuestCoupon()
                            }),
                            o.showIfExpired()
                        }
                    }
                },
                e.prototype.canShowNewGuestCoupon = function() {
                    return ! (v.a.vendor.is("CTRIP") || this.channelData && this.channelData.isHideRedEnvelope) && (this.pageStatus.newGuestCouponEntrance && this.pageStatus.newGuestCouponEntrance.showEntrance && this.pageStatus.newGuestCouponEntrance.canReceive)
                },
                e.prototype.initLoginGuide = function() {
                    var t = this,
                    e = this.loginguideStatusProvider.getCache();
                    if (! (e && e.length > 0)) {
                        if (!this.pageStatus.response.canShowLoginGuide || this.canShowNewGuestCoupon()) return void(this.loginGuide && this.loginGuide.hide());
                        this.loginGuide || (this.loginGuide = new M.a({
                            wrapper: t.$el.find(".js_login_guide_container"),
                            datamodel: {
                                islist: !0
                            }
                        }), this.loginGuide.on("onLoginSuccess",
                        function() {
                            new P.a({
                                datamodel: {
                                    content: "\u767b\u5f55\u6210\u529f"
                                }
                            }).show(),
                            t.refreshPage()
                        }), this.loginGuide.on("CloseByUser",
                        function() {
                            e && e.length > 0 || (t.loginguideStatusProvider.setCache("CloseByUser"), t.updateListContainer(), t.loginGuideHeight = 0)
                        })),
                        this.loginGuide.show();
                        var i = t.$el.find(".js_login_guide_container");
                        i && i.length > 0 && (this.loginGuideHeight = i.offset().height)
                    }
                },
                e.prototype.updateListContainer = function() {
                    var t = this.$el.find(".js_list_container");
                    if ("block" !== this.$el.find(".js_login_guide_container .view").css("display") && t && t.length > 0 && this.loginGuideHeight > 0) {
                        var e = t.offset().height + this.loginGuideHeight;
                        t.css("height", e + "px")
                    }
                },
                e.prototype.onAbnromalNetwork = function() {
                    var t = this;
                    $("#header").hide(),
                    this.$el.hide(),
                    C.a.hide(),
                    $(".container-drag44").hide(),
                    this.abnormalNetwork || (this.abnormalNetwork = new J.a({
                        wrapper: $("body"),
                        request: this.pageStatus.request
                    }), this.abnormalNetwork.show()),
                    this.abnormalNetwork.on("abnormalNetwordReload",
                    function() {
                        t.refreshHotelListBody()
                    }),
                    this.abnormalNetwork.on("abnormalNetwordBack",
                    function() {
                        t.onBack()
                    })
                },
                e.prototype.getBrowsedHistoryHotelIds = function() {
                    var t = Object(X.c)() || [],
                    e = b.a.getServerDate().getTime(),
                    i = [];
                    return n()(t,
                    function(t) {
                        if (e - t.timeStamp <= 2592e5) {
                            var o = t.oridata && t.oridata.hotelid || "";
                            i.push(o)
                        }
                    }),
                    i
                },
                e.prototype.addBrowseHistoryStyle = function() {
                    var t = this.getBrowsedHistoryHotelIds();
                    if (0 !== t.length) {
                        var e = this.$el.find(".js_single_hotel");
                        0 !== e.length && n()(e,
                        function(e) {
                            if ($(e).length > 0) {
                                var i = $(e).data("id") || "";
                                i && !isNaN(parseInt(i, 10)) && t.indexOf(parseInt(i, 10)) > -1 && $(e).addClass("browse")
                            }
                        })
                    }
                },
                e.prototype.prepareHomeNextHotelData = function() {
                    if (this.isBack()) {
                        if ("AssociateSearch" === this.pageStatus.currentPage) return;
                        if ("DestinationSearch" === this.pageStatus.currentPage) return void this.refreshHotelListBody();
                        if ("HotelListSearch" === this.pageStatus.currentPage) return void this.hotelListProvider.prepareHotelPreData(this.pageStatus)
                    }
                    this.hotelListProvider.prepareHotelPreData(this.pageStatus)
                },
                e.prototype.restoreComponentsStatus = function() {
                    if (this.isBack()) {
                        switch (this.pageStatus.currentPage) {
                        case "AssociateSearch":
                            this.restoreKeywordAssociateSearch().then(function() {
                                history.pushState({},
                                document.title, location.href)
                            });
                            break;
                        case "DestinationSearch":
                            this.restoreDestinationAssociateSearch();
                            break;
                        case "HotelListMap":
                            this.restoreHotelListMap();
                            break;
                        case "HotelListSearch":
                            this.restoreHotelListSearch()
                        }
                        this.restoreBackStatus()
                    }
                },
                e.prototype.restoreBackStatus = function() {
                    this.pageStatus.currentPage = "",
                    history.replaceState({},
                    document.title, location.origin + location.pathname),
                    this.pageStatus.destinationSearchKey = ""
                },
                e.prototype.restoreKeywordAssociateSearch = function() {
                    var t = this;
                    return this.restorePageStatusKeyword(),
                    this.getKeywordPanel().then(function() {
                        t.keywordPanel.restoreKeywordAssociate({
                            displayKeywordText: t.pageStatus.displayKeywordText
                        }),
                        t.showHTML(),
                        t.updateComponentsFromPageStatus(),
                        t.refreshHotelListBody()
                    })
                },
                e.prototype.restoreDestinationAssociateSearch = function() {
                    var t = this;
                    return this.getCityList().then(function() {
                        t.cityList.restoreDestinationAssociate(),
                        t.showHTML()
                    })
                },
                e.prototype.restoreHotelListMap = function() {
                    $("#header").hide(),
                    this.$el.hide(),
                    this.showHTML(),
                    this.updateComponentsFromPageStatus(),
                    this.openMap(),
                    document.getElementsByTagName("html")[0].style.opacity = "1",
                    this.hotelListMapPanel.restoreStatus(),
                    this.hotellistpanel.restoreHoteListLastStatus(this.pageStatus)
                },
                e.prototype.restoreHotelListSearch = function() {
                    if (this.showHTML(), this.updateNewGuestCoupon(!this.pageStatus.request.oversea, this.pageStatus.request.oversea), this.updateComponentsFromPageStatus(), this.pageStatus.nowInDate !== this.pageStatus.request.checkinDate || this.pageStatus.nowOutDate !== this.pageStatus.request.checkoutDate) return void this.refreshHotelListBody();
                    this.hotellistpanel.restoreHoteListLastStatus(this.pageStatus),
                    this.restoreHotSearchKeyword()
                },
                e.prototype.showHTML = function() {
                    $("#js_fake_loading2").remove()
                },
                e.prototype.isBack = function() {
                    return "#gotoDetail" === location.hash
                },
                e.prototype.openKeywordPanel = function() {
                    var t = this;
                    return this.getKeywordPanel().then(function() {
                        t.keywordPanel.open(),
                        t.recordUserActionFlow("list_openkeywords")
                    })
                },
                e.prototype.getKeywordPanel = function() {
                    var t = this;
                    return this.keywordPanel ? Promise.resolve(this.keywordPanel) : i.e(11).then(i.bind(null, "Qb6a")).then(function(e) {
                        var i = e.
                    default;
                        return t.keywordPanel = new i({
                            request: t.pageStatus.request,
                            selectedDestinationData: {
                                id: t.pageStatus.request.keywordFilterItem,
                                text: t.pageStatus.displayKeywords
                            }
                        }),
                        t.keywordPanel.on("onFilterSelect",
                        function(e) {
                            t.onKeywordFilterSelect(e)
                        }),
                        t.keywordPanel.on("onDirectSearch",
                        function(e) {
                            t.onKeywordDirectSearch(e)
                        }),
                        t.keywordPanel.on("onJumpToHotelDetail",
                        function(e) {
                            t.onKeywordJumpToHotelDetail(e)
                        }),
                        t.keywordPanel.on("onSearchBarClear",
                        function() {
                            t.onSearchBarClear()
                        }),
                        t.keywordPanel
                    })
                },
                e.prototype.destroyKeywordPanel = function() {
                    this.keywordPanel && (this.keywordPanel.destroy(), delete this.keywordPanel)
                },
                e.prototype.destroyFilterPanel = function() {
                    this.filterPanel && (this.filterPanel.destroy(), delete this.filterPanel)
                },
                e.prototype.destroyAreaPanel = function() {
                    this.areafilterPanel && (this.areafilterPanel.destroy(), delete this.areafilterPanel)
                },
                e.prototype.destroyPriceAndStarPanel = function() {
                    this.PriceStarFilterPanel && (this.PriceStarFilterPanel.destroy(), delete this.PriceStarFilterPanel)
                },
                e.prototype.getEvents = function() {
                    return {
                        "click .js_inoutday": this.onInOutDayEdit.bind(this),
                        "click .js_hotellistmap": this.onOpenMap.bind(this),
                        "click .js_single_hotel": this.onHotelJumpToDetail.bind(this),
                        "click .js_filter_tag": this.closeDobber.bind(this),
                        "click .js_full_tip .js_close": this.closeFullRoomTip.bind(this),
                        "click .js_oversea_pricetip .js_close": this.closeOverseaPriceTip.bind(this),
                        "click .js_zonefilter_item": this.listZoneFilterAction.bind(this),
                        "click .js_a_seo": this.eventStopSEOTagA.bind(this),
                        "click .js_goTop": this.goTop.bind(this),
                        "click .js_goHistory": this.goHistory.bind(this),
                        "click .js_bottomViewMoreHotelEntr": this.goToHotelList.bind(this),
                        "click .js_numselect": this.handleRoomPeopleNumSelect.bind(this),
                        "click .js_jumptocityguide": this.goToCityGuide.bind(this)
                    }
                },
                e.prototype.goToCityGuide = function() {
                    var t = this.pageStatus.response.cityGuideInfo.gongLueId,
                    e = this.pageStatus.response.cityGuideInfo.cityId,
                    i = this.pageStatus.response.cityGuideInfo.name,
                    o = this.pageStatus.response.cityGuideInfo.jumpURLPrefix,
                    s = this.pageStatus.request.roomQuantity,
                    n = this.pageStatus.request.adultCounts;
                    n = 0 === parseInt(n) ? 1 : parseInt(n);
                    var r = this.pageStatus.request.childAges || "";
                    r = "" === r ? "-1_-1_-1": r.replace(/\|/g, "_");
                    var a = this.pageStatus.request.checkinDate || "",
                    l = this.pageStatus.request.checkinDate,
                    c = this.pageStatus.request.checkoutDate,
                    u = this.pageStatus.request.starItemList;
                    u.length > 0 && (u = u.map(function(t) {
                        return t.substr(0, 4) + t.substr(t.length - 1)
                    }).join(""));
                    var p = this.pageStatus.request.lowestPrice;
                    p = "" === p ? "": "v" + p;
                    var h = this.pageStatus.request.highestPrice;
                    h = "" === h ? "": "v" + h;
                    var d = b.a.getIntervalDay(this.pageStatus.request.checkinDate, this.pageStatus.request.checkoutDate) || "";
                    d = this.morningStore.getStatus() ? d + 1 : d;
                    var f = this.pageStatus.request.oversea,
                    g = f ? "2": "1",
                    m = "";
                    if (this.pageStatus.request.locationItemList.length > 0) {
                        var y = this.pageStatus.request.locationItemList[0].toString(),
                        v = y.indexOf("|");
                        v > 0 && (m = y.substring(0, v).replace(/-/g, ""))
                    }
                    var w = encodeURIComponent(o + "/webapp/hotel/oversea/city" + e + "/" + p + h + m + u + "/?atime=" + a + "&days=" + d + "&rcount=" + s + "&adult=" + n + "&child=" + r),
                    S = o + "/webapp/nb/strategy/" + t + "?cityid=" + e + "&cityname=" + i + "&isHideNavBar=YES&biz=" + g + "&atime=" + a + "&days=" + d + "&checkin=" + l + "&checkout=" + c + "&rcount=" + s + "&adult=" + n + "&child=" + r + "&star=" + u + p + h + "&from=" + w;
                    this.goTo("", S)
                },
                e.prototype.handleRoomPeopleNumSelect = function(t) {
                    var e = this,
                    i = $(t.currentTarget),
                    o = this.pageStatus.request.oversea;
                    if (void 0 !== this.pageStatus.locatedOversea && (o = this.pageStatus.locatedOversea), o) {
                        var s = this.pageStatus.numselect ? {
                            room: this.pageStatus.numselect.room,
                            adult: this.pageStatus.numselect.adult,
                            children: this.pageStatus.numselect.children
                        }: at;
                        new it.a({
                            datamodel: s,
                            onChanged: function(t) {
                                var o = c()(t.children,
                                function(t) {
                                    return t >= 0
                                }).length;
                                i.find(".js_numselect_adult").html("\u6210\u4eba&nbsp;" + t.adult),
                                i.find(".js_numselect_child").html("\u513f\u7ae5&nbsp;" + o);
                                var s = e.pageStatus.request.roomQuantity <= 1 && t.room > 1 || e.pageStatus.request.roomQuantity > 1 && t.room <= 1;
                                e.pageStatus.numselect = t,
                                e.pageStatus.request.roomQuantity = t.room,
                                e.pageStatus.request.adultCounts = t.adult,
                                e.pageStatus.request.childAges = t.children.toString().replace(/\,/g, "|"),
                                e.refreshHotelListBody(),
                                e.updateHotelQueryStore();
                                var n = e.$el.find('.js_quick_filter [data-identify="4"]');
                                n && s && (t.room > 1 ? n.html("\u770b\u6bcf\u95f4\u603b\u4ef7") : n.html("\u770b\u603b\u4ef7"))
                            }
                        }).show()
                    }
                },
                e.prototype.goToHotelList = function(t) {
                    var e = $(t.currentTarget).data("cityename"),
                    i = this.pageData.isoversea ? "overseaHotelList": "domesticHotelList",
                    o = this.pageStatus && this.pageStatus.request || {},
                    s = o && o.cityID,
                    n = o && o.checkinDate || "",
                    r = o && o.checkoutDate || "",
                    a = b.a.getIntervalDay(n, r);
                    this.morningStore.isMorning() && (a += 1),
                    history.replaceState({},
                    document.title, "#gotoHotelList");
                    var l = "";
                    l = F.a.getenvHost() + "/webapp/hotel/" + e + s + "/?atime=" + n + "&days=" + a,
                    this.goTo(i, l)
                },
                e.prototype.goTop = function() {
                    $(".js_list_container")[0].scrollTop = 0,
                    $(".js_list_container").trigger("scroll")
                },
                e.prototype.goHistory = function() {
                    var t = this.pageStatus && this.pageStatus.request || {},
                    e = t && t.cityID,
                    i = t && t.checkinDate || "",
                    o = t && t.checkoutDate || "",
                    s = this.morningStore.getStatus() ? 1 : 0,
                    n = F.a.getenvHost() + "/webapp/hotel/browsedhotellist?cid=" + e + "&inday=" + i + "&outday=" + o + "&ismorning=" + s + "#fromList";
                    this.goTo("browsedhotellist", n)
                },
                e.prototype.eventStopSEOTagA = function(t) {
                    t.preventDefault(),
                    t.stopPropagation()
                },
                e.prototype.listZoneFilterAction = function(t) {
                    var e = this,
                    i = $(t.currentTarget),
                    o = i.attr("data-id") || "",
                    s = e.pageStatus;
                    i.hasClass("current") ? s.request.locationItemList = [] : (s.request.locationItemList = [o], s.request.searchByExposedZone = !0),
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.closeFullRoomTip = function() {
                    this.$el.find(".js_full_tip").hide()
                },
                e.prototype.closeOverseaPriceTip = function() {
                    this.$el.find(".js_oversea_pricetip").hide(),
                    st.setAttr("oversea_price_tip", 1)
                },
                e.prototype.closeDobber = function(t) {
                    var e = this,
                    i = $(t.currentTarget),
                    o = i.attr("data-cat"),
                    s = i.attr("data-id"),
                    n = e.pageStatus;
                    switch (o) {
                    case "Property":
                        var r = this.pageStatus.request.filterItemList.indexOf(s);
                        n.request.filterItemList.splice(r, 1);
                        break;
                    case "Location":
                        var a = this.pageStatus.request.locationItemList.indexOf(s);
                        if (n.request.locationItemList.splice(a, 1), "distance" === s.substring(0, s.indexOf("-"))) {
                            n.request.locationItemList.push("distance-50|||50\u516c\u91cc\u4ee5\u5185|@distance")
                        }
                        break;
                    case "KeyWord":
                        n.request.keywordFilterItem = "",
                        n.request.keyword = "",
                        n.displayKeywords = "",
                        n.request.filterItemList = [],
                        n.request.locationItemList = [],
                        n.request.orderItem = "",
                        n.request.hotelIdList = [];
                        break;
                    case "Star":
                        var l = this.pageStatus.request.starItemList.indexOf(s);
                        n.request.starItemList.splice(l, 1);
                        break;
                    case "Price":
                        n.request.lowestPrice = 0,
                        n.request.highestPrice = 0
                    }
                    this.pageStatus = n,
                    this.updateComponentsFromPageStatus(),
                    e.refreshHotelListBody()
                },
                e.prototype.onHotelJumpToDetail = function(t) {
                    this.pageStatus.currentPage = "HotelListSearch",
                    this.pageStatus.nowInDate = this.pageStatus.request.checkinDate,
                    this.pageStatus.nowOutDate = this.pageStatus.request.checkoutDate,
                    this.pageStatus.currentDom = $(".js_list_container").find(".js_hotellistinfo").html(),
                    this.pageStatus.scrollTop = $(".js_list_container").scrollTop();
                    var e = $(t.currentTarget),
                    i = e[0].dataset.id,
                    o = this.pageStatus.request.oversea;
                    this.jumpToHotelDetail(i, o, $(t.currentTarget).parent().index() + 1)
                },
                e.prototype.importHeader = function() {
                    this.headerview = i.e(15).then(i.bind(null, "KxhM"))
                },
                e.prototype.getHeaderSettings = function() {
                    var t = this;
                    return {
                        events: {
                            "click .js_open_citylist": function(e) {
                                t.openCityList()
                            },
                            "click .js_page_select_title": function(e) {
                                t.openCityList()
                            },
                            "click .js_own_around": function(e) {
                                t.ownAround()
                            },
                            "click .js_back": function() {
                                t.onBack()
                            },
                            "click .js_inoutday": function(e) {
                                t.onInOutDayEdit()
                            },
                            "click .js_hotellistmap": function(e) {
                                t.onOpenMap()
                            }
                        },
                        isBindEvtOnly: !0
                    }
                },
                e.prototype.openCityList = function() {
                    var t = this;
                    this.getCityList().then(function() {
                        t.cityList.open(),
                        t.recordUserActionFlow("list_opencity")
                    })
                },
                e.prototype.getCityList = function() {
                    var t = this;
                    return this.cityList ? Promise.resolve(this.cityList) : i.e(9).then(i.bind(null, "l6/h")).then(function(e) {
                        var i = e.
                    default;
                        return t.cityList = new i({
                            datamodel: {
                                hasHeader: !0
                            },
                            selectedCity: {
                                cityId: t.pageStatus.request.cityID,
                                did: t.pageStatus.request.districtID
                            },
                            destinationSearchKey: t.pageStatus.destinationSearchKey,
                            area: t.pageStatus.response.oversea ? "oversea": "domestic",
                            onDestItemClick: t.onDestItemClick.bind(t)
                        }),
                        t.cityList.on("onSelectedCity",
                        function(e) {
                            t.onCityListSelectedCity(e)
                        },
                        !1),
                        t.cityList
                    })
                },
                e.prototype.onQuickFilterOwnAround = function() {
                    var t = this,
                    e = function() {
                        t.quickFilter.$(".js_quickfilter_ownaround").addClass("current")
                    };
                    this.ownAround(e)
                },
                e.prototype.cancelOwnAround = function() {
                    this.pageStatus.request.orderItem = "",
                    this.pageStatus.request.locationItemList = c()(this.pageStatus.request.locationItemList,
                    function(t) {
                        return "distance-4|||4\u516c\u91cc\u4ee5\u5185|@distance" !== t
                    }),
                    this.pageStatus.request.userLatitude = "",
                    this.pageStatus.request.userLongitude = "",
                    this.pageStatus.request.userLocationSearch = !1,
                    this.pageStatus.request.pageIndex = 0,
                    this.pageStatus.request.cityName = "",
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.ownAround = function(t) {
                    var e = this;
                    w.a.GeoLocation.UnSubscribe("hotel/searchlist"),
                    w.a.GeoLocation.Subscribe("hotel/searchlist", {
                        onStart: function() {},
                        onComplete: function(t) {
                            this.address = t,
                            this.pageStatus.request.cityName = t.address,
                            this.pageStatus.locatedOversea = !("CHN" === t.countryShortName),
                            this.showNewGuestCouponEntr(),
                            this.updateRoomPeopleNumSelect()
                        },
                        onError: function() {},
                        onPosComplete: function(t, e) {
                            this.pageStatus.displayKeywords = "",
                            this.pageStatus.areaText = "",
                            this.pageStatus.priceStarText = "",
                            this.pageStatus.orderText = "",
                            this.pageStatus.request = {
                                checkinDate: this.pageStatus.request.checkinDate,
                                checkoutDate: this.pageStatus.request.checkoutDate,
                                controlBitMap: this.pageStatus.request.controlBitMap,
                                locationItemList: ["distance-4|||4\u516c\u91cc\u4ee5\u5185|@distance"],
                                orderItem: "sort-4|2",
                                userLatitude: e,
                                userLongitude: t,
                                userLocationSearch: !0
                            }
                        },
                        onCityComplete: function(e) {
                            e && e.CityEntities && e.CityEntities.length >= 1 && (this.pageStatus.request.cityID = e.CityEntities[0].CityID, this.pageStatus.request.districtID = 0, this.pageStatus.cnameforownaround = e.CityEntities[0].CityName, this.refreshHotelListBody()),
                            t && "function" == typeof t && t()
                        },
                        onCityError: function() {},
                        onPosError: function() {
                            e.locationFailCallBack()
                        }
                    },
                    this, !0, 35e3, !1, !0),
                    this.recordUserActionFlow("list_nearby")
                },
                e.prototype.updatePrice = function(t, e) {
                    t && n()(t,
                    function(t) {
                        var i = $(t).find(".js_refund") || {},
                        o = $(t).find(".js_price") || {};
                        if (e) {
                            var s = i.data("avgrefund");
                            i.html(s);
                            var n = o.data("avgprice");
                            n && o.html("<small>&yen;</small>" + n + '<em class="price-star">\u8d77</em>')
                        } else {
                            var r = i.data("totalrefund");
                            i.html(r);
                            var a = o.data("totalprice");
                            a && o.html("<small>&yen;</small>" + a + '<em class="price-star">\u8d77</em>')
                        }
                    })
                },
                e.prototype.locationFailCallBack = function() {
                    var t = this;
                    new T.
                default({
                        maskToHide:
                        !0,
                        needAnimat: !1,
                        datamodel: {
                            content: "\u5b9a\u4f4d\u5931\u8d25\uff0c\u8bf7\u91cd\u65b0\u5c1d\u8bd5\uff0c\u6216\u9009\u62e9\u57ce\u5e02\u67e5\u8be2",
                            btns: [{
                                name: "\u77e5\u9053\u4e86",
                                className: "cui-btns-cancel"
                            },
                            {
                                name: "\u9009\u62e9\u57ce\u5e02",
                                className: "cui-btns-ok"
                            }]
                        },
                        events: {
                            "click .cui-btns-ok": "okAction"
                        },
                        okAction: function() {
                            this.hide(),
                            w.a.GeoLocation.UnSubscribe("hotel/searchlist"),
                            t.openCityList()
                        },
                        cancelAction: function() {
                            this.hide(),
                            w.a.GeoLocation.UnSubscribe("hotel/searchlist")
                        },
                        onHide: function() {
                            this.destroy()
                        }
                    }).show()
                },
                e.prototype.onOpenMap = function(t) {
                    var e = this;
                    this.openMap(),
                    t && (this.hotelListMapPanel.isTriggerbyUI = !0),
                    this.hotelListMapPanel.open(function() {
                        $("#header").hide(),
                        e.$el.hide()
                    }),
                    this.recordUserActionFlow("list_openmap")
                },
                e.prototype.openMap = function() {
                    this.hotelListMapPanel || (this.hotelListMapPanel = new W.a({
                        datamodel: {
                            checkintext: this.$(".js_inoutday .star p").eq(0).text() || this.$header.find(".js_inoutday .star p").eq(0).text(),
                            checkouttext: this.$(".js_inoutday .star p").eq(1).text() || this.$header.find(".js_inoutday .star p").eq(1).text(),
                            keyword: this.pageStatus.displayKeywords
                        },
                        pageStatus: this.pageStatus
                    }), this.hotelListMapPanel.on("onSelectHotel", this.mapToHotelDetail.bind(this)), this.hotelListMapPanel.on("onSearch", this.onMapSearch.bind(this)), this.hotelListMapPanel.on("onOpenKeywordPanel", this.openKeywordPanel.bind(this)), this.hotelListMapPanel.on("onOpenCalendar", this.onInOutDayEdit.bind(this)), this.hotelListMapPanel.on("onClearKeyword", this.onKeywordBarClear.bind(this)), this.hotelListMapPanel.on("onback", this.show.bind(this)), this.hotelListMapMenu = this.hotelListMapPanel.getHotelListMapMenu(), this.hotelListMapMenu.on("filterPanelOpen", this.openFilterPanel.bind(this)), this.hotelListMapMenu.on("filterPanelClose", this.closeFilterPanel.bind(this)), this.hotelListMapMenu.on("areaFilterPanelOpen", this.openAreaFilterPanel.bind(this)), this.hotelListMapMenu.on("areaFilterPanelClose", this.closeAreaFilterPanel.bind(this)), this.hotelListMapMenu.on("sortFilterPanelOpen", this.openSortFilterPanel.bind(this)), this.hotelListMapMenu.on("sortFilterPanelClose", this.closeSortFilterPanel.bind(this)), this.hotelListMapMenu.on("priceStarFilterPanelOpen", this.openPriceStarFilterPanel.bind(this)), this.hotelListMapMenu.on("priceStarFilterPanelClose", this.closePriceStarFilterPanel.bind(this)))
                },
                e.prototype.onInOutDayEdit = function() {
                    var t = this;
                    L.a.start("onCalendarOpened"),
                    this.calendar && (this.calendar.destroy(), delete this.calendar),
                    this.calendar || i.e(12).then(i.bind(null, "MvGl")).then(function(e) {
                        var i = e.
                    default;
                        return t.calendar = new i,
                        t.calendar.on("onItemClick", t.onInOutDaySelected.bind(t)),
                        t.openCalendar(),
                        t.calendar
                    })
                },
                e.prototype.openCalendar = function() {
                    var t = this.pageStatus.request,
                    e = this.pageStatus.response;
                    this.calendar.open(e.utcOffSet, e.oversea, t.checkinDate, t.checkoutDate, this.morningStore.getStatus())
                },
                e.prototype.onInOutDaySelected = function(t) {
                    var e = new b.a(t.checkinDate).format("Ymd"),
                    i = new b.a(t.checkoutDate).format("Ymd"),
                    o = new b.a(t.checkinDate).format("m-d"),
                    s = new b.a(t.checkoutDate).format("m-d");
                    this.$(".js_inoutday .star p").eq(0).html("\u4f4f&nbsp;" + o),
                    this.$(".js_inoutday .star p").eq(1).html("\u79bb&nbsp;" + s),
                    this.header.$(".js_inoutday .star p").eq(0).html("\u4f4f&nbsp;" + o),
                    this.header.$(".js_inoutday .star p").eq(1).html("\u79bb&nbsp;" + s),
                    this.hotelListMapPanel && this.hotelListMapPanel.updateInOutDate(o, s),
                    this.morningStore.setStatus(t.isMorning),
                    t.isMorning && (this.pageStatus.request.controlBitMap |= 4),
                    this.pageStatus.request.checkinDate = e,
                    this.pageStatus.request.checkoutDate = i;
                    var n = nt.getAttr("queryParams") || {};
                    n.inDay = e.substring(0, 4) + "-" + e.substring(4, 6) + "-" + e.substring(6, 8),
                    n.outDay = i.substring(0, 4) + "-" + i.substring(4, 6) + "-" + i.substring(6, 8);
                    var r = b.a.getIntervalDay(n.inDay, n.outDay);
                    r = t.isMorning ? r + 1 : r,
                    n.days = r,
                    nt.setAttr("queryParams", n),
                    this.refreshHotelListBody()
                },
                e.prototype.onCityListSelectedCity = function(t) {
                    this.changeCity(t)
                },
                e.prototype.onBack = function() {
                    if (v.a.vendor.is("CTRIP")) return void new Promise(function(t) {
                        t()
                    }).then(i.bind(null, "IJ3o")).then(function(t) {
                        new t.
                    default.Fn("back_to_last_page").run()
                    });
                    if (location.search.indexOf("from=") >= 0) this.back(),
                    this.recordUserActionFlow("list_gotbackoutsite");
                    else {
                        var t = this.pageStatus.response.oversea ? "oversea/": "",
                        e = this.pageStatus.request.cityID > 0 ? "&city=" + this.pageStatus.request.cityID: "",
                        o = this.pageStatus.request.checkinDate || "",
                        s = b.a.getIntervalDay(this.pageStatus.request.checkinDate, this.pageStatus.request.checkoutDate) || "";
                        s = this.morningStore.getStatus() ? s + 1 : s;
                        var n = this.morningStore.getStatus() ? "&ismorning=1": "",
                        r = "";
                        if (this.pageStatus.request.userLocationSearch) {
                            var a = this.pageStatus.request.cityName || this.pageStatus.response.positionInfo && this.pageStatus.response.positionInfo.cityName;
                            r = "&latlng=" + this.pageStatus.request.userLatitude + "_" + this.pageStatus.request.userLongitude + "_" + a
                        }
                        this.goTo("index", F.a.getenvHost() + "/webapp/hotel/" + t + "?atime=" + o + "&days=" + s + e + n + r),
                        this.recordUserActionFlow("list_goback")
                    }
                },
                e.prototype.changeCity = function(t) {
                    this.hotelListMapPanel && (this.pageStatus.response.oversea && !t.isoversea || !this.pageStatus.response.oversea && t.isoversea) && (this.hotelListMapPanel.destroy(), delete this.hotelListMapPanel),
                    this.replaceUrlForCity(t);
                    var e = this.pageStatus.request.oversea;
                    this.changePageStatusCity(t),
                    t.topkeyword && this.changedPageStatusKeywordDirect(t.topkeyword),
                    this.updateComponentsFromPageStatus(),
                    this.updateRoomPeopleNumSelect(),
                    this.updateNewGuestCoupon(e, t.isoversea),
                    this.pageStatus.hasViewTotalPrice = !1,
                    this.refreshHotelListBody(),
                    this.showHeaderAndInout(),
                    t.isoversea ? ($(".js_own_around").data("ubt-key", "c_hotel_oversea_searchlist_aroundhotel"), $(".js_inoutday").data("ubt-key", "c_hotel_oversea_searchlist_calendar"), $(".js_hotellistmap").data("ubt-key", "c_hotel_oversea_searchlist_map"), this.header.$(".js_open_citylist").data("ubt-key", "c_hotel_oversea_searchlist_map")) : ($(".js_own_around").data("ubt-key", "c_hotel_inland_searchlist_aroundhotel"), $(".js_inoutday").data("ubt-key", "c_hotel_inland_searchlist_calendar"), $(".js_hotellistmap").data("ubt-key", "c_hotel_inland_searchlist_map"), this.header.$(".js_open_citylist").data("ubt-key", "c_hotel_inland_searchlist_map"))
                },
                e.prototype.showHeaderAndInout = function() {
                    this.$header.show(),
                    this.$el.find(".lt-inout").show()
                },
                e.prototype.replaceUrlForCity = function(t) {
                    var e = location.pathname.substr(14),
                    i = t.isoversea ? location.origin + "/webapp/hotel/oversea/": location.origin + "/webapp/hotel/";
                    0 === location.pathname.indexOf("/webapp/hotel/oversea/") && (e = location.pathname.substr(22));
                    var o = e.match(/\d+\.html/);
                    o && (e = e.substr(0, o.index - 1)),
                    i = -1 === e.indexOf("/") ? "" + i + t.seo + t.cityId: "" + i + t.seo + t.cityId + e.substr(e.indexOf("/")),
                    i = "" + i + location.hash,
                    history.replaceState({},
                    document.title, i),
                    x.a.addHistory("searchlist", i)
                },
                e.prototype.changePageStatusCity = function(t) {
                    this.pageStatus.displayKeywords = "",
                    this.pageStatus.areaText = "",
                    this.pageStatus.priceStarText = "",
                    this.pageStatus.orderText = "";
                    var e = this.pageStatus.request.controlBitMap;
                    if (4 == (4 & this.pageStatus.request.controlBitMap) && t.isoversea) {
                        this.morningStore.setStatus(!1),
                        this.morningStore.setIsOverSea(t.isoversea);
                        var i = new b.a(new Date(b.a.getServerDate().getTime() + 1e3 * t.tzone));
                        this.pageStatus.request.checkinDate = i.format("Ymd"),
                        this.pageStatus.request.checkoutDate = i.addDay(1).format("Ymd"),
                        e -= 4
                    }
                    this.pageStatus.request = {
                        cityID: t.cityId,
                        cityName: t.cname,
                        districtID: t.did,
                        oversea: t.isoversea,
                        checkinDate: this.pageStatus.request.checkinDate,
                        checkoutDate: this.pageStatus.request.checkoutDate,
                        controlBitMap: e
                    },
                    delete this.pageStatus.locatedOversea
                },
                e.prototype.changeDestination = function(t) {
                    this.replaceUrlForCity({
                        isoversea: t.region.countryid > 1,
                        cPY: t.region.city ? t.region.city.seo: t.region.cengname,
                        cityId: 8 === t.type ? t.region.distid + "_" + t.region.cid: t.region.cid
                    }),
                    this.changePageStatusDestination(t),
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.changePageStatusDestination = function(t) {
                    var e = 4 | this.pageStatus.request.controlBitMap;
                    if (t.region.countryid > 1 && (e = 4 == (4 & this.pageStatus.request.controlBitMap) ? this.pageStatus.request.controlBitMap - 4 : this.pageStatus.request.controlBitMap), 4 == (4 & this.pageStatus.request.controlBitMap) && t.region.countryid > 1) {
                        var i = new b.a(new Date(b.a.getServerDate().getTime() + 1e3 * t.region.tzone));
                        this.pageStatus.request.checkinDate = i.format("Ymd"),
                        this.pageStatus.request.checkoutDate = i.addDay(1).format("Ymd")
                    }
                    this.pageStatus.request = {
                        cityID: t.region.cid,
                        cityName: t.region.cname,
                        districtID: t.region.distid,
                        oversea: t.region.countryid > 1,
                        checkinDate: this.pageStatus.request.checkinDate,
                        checkoutDate: this.pageStatus.request.checkoutDate,
                        controlBitMap: e,
                        keywordFilterItem: t.id
                    },
                    this.pageStatus.areaText = "",
                    this.pageStatus.priceStarText = "",
                    this.pageStatus.orderText = "",
                    this.pageStatus.displayKeywords = t.attribute.keyword + (t.region.countryid > 1 && t.attribute.engkeyword ? "|" + t.attribute.engkeyword: ""),
                    t.id.indexOf("districtzone-") >= 0 && t.attribute && t.attribute.keyword && (this.pageStatus.request.cityName = t.attribute.keyword + "(" + t.region.cname + ")", this.pageStatus.displayKeywords = ""),
                    this.isPoiSearch(t.id) && (this.pageStatus.areaText = "4\u516c\u91cc\u4ee5\u5185", this.pageStatus.orderText = "\u8ddd\u79bb \u8fd1\u2192\u8fdc", this.pageStatus.request.locationItemList = ["distance-4|||4\u516c\u91cc\u4ee5\u5185|@distance"], this.pageStatus.request.orderItem = "sort-4|2")
                },
                e.prototype.onDestItemClick = function(t) {
                    return 64 === t.type ? void this.onDestinationJumpToHotelDetail(t) : 32 === t.type ? void this.changeCity({
                        cityId: t.region.cid,
                        cname: t.region.cname,
                        did: t.region.distid,
                        isoversea: t.region.countryid > 1,
                        topkeyword: t.currentTopKeyword,
                        seo: t.attribute.engkeyword.replace(/ /g, "").toLowerCase()
                    }) : void this.changeDestination(t)
                },
                e.prototype.onDestinationJumpToHotelDetail = function(t) {
                    if (t && t.id) {
                        this.pageStatus.request = {
                            cityID: t.region.cid,
                            cityName: t.region.cname,
                            districtID: t.region.distid,
                            oversea: t.region.countryid > 1,
                            checkinDate: this.pageStatus.request.checkinDate,
                            checkoutDate: this.pageStatus.request.checkoutDate,
                            controlBitMap: this.pageStatus.request.controlBitMap,
                            keywordFilterItem: t.id
                        },
                        this.pageStatus.areaText = "4\u516c\u91cc\u4ee5\u5185",
                        this.pageStatus.orderText = "\u8ddd\u79bb \u8fd1\u2192\u8fdc",
                        this.pageStatus.request.locationItemList = ["distance-4|||4\u516c\u91cc\u4ee5\u5185|@distance"],
                        this.pageStatus.request.orderItem = "sort-4|2";
                        var e = t.id.substring(t.id.indexOf("-") + 1).split("|");
                        this.pageStatus.displayKeywords = e[3],
                        this.pageStatus.destinationSearchKey = t.key,
                        this.pageStatus.cityName = t.region.cname,
                        this.pageStatus.currentPage = "DestinationSearch",
                        this.jumpToHotelDetail(e[0], parseInt(e[4], 10) > 1)
                    }
                },
                e.prototype.onFilterPanelClickOK = function(t) {
                    this.pageStatus.request.filterItemList = t,
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.reloadHotelListInfo = function(t) {
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.changePageStatusArea = function(t) {
                    var e = p()(this.pageStatus.request.locationItemList),
                    i = this.getDistanceInfo(e),
                    o = i && i.distanceItem,
                    s = i && i.onlyDistance,
                    n = this.isPoiSearch(this.pageStatus.request.keywordFilterItem),
                    r = this.isAreaPoiSearch(e),
                    a = this.isAreaPoiSearch(t.areafilter),
                    l = this.isAreaPoiClear(t),
                    c = this.areaFilterType(t.areafilter, "@distance");
                    this.pageStatus.areaText = t.text,
                    this.pageStatus.request.locationItemList = t.areafilter,
                    c || (this.pageStatus.request.userLocationSearch = !1, this.pageStatus.request.referencePoint = ""),
                    a && (this.pageStatus.request.orderItem && "sort-0|1" !== this.pageStatus.request.orderItem || (this.pageStatus.request.orderItem = "sort-4|2", this.pageStatus.orderText = "\u8ddd\u79bb \u8fd1\u2192\u8fdc")),
                    n && s && !t.arefilter && t.areafilter.length < 1 && (this.pageStatus.request.locationItemList = ["distance-50|||50\u516c\u91cc\u4ee5\u5185|@distance"]),
                    n && a && (this.pageStatus.request.orderItem && "sort-0|1" !== this.pageStatus.request.orderItem || (this.pageStatus.request.orderItem = "sort-4|2", this.pageStatus.orderText = "\u8ddd\u79bb \u8fd1\u2192\u8fdc")),
                    n && r && !t.areafilter && t.areafilter.length < 1 && (this.pageStatus.request.locationItemList = [o]);
                    var u = "sort-4|2" === this.pageStatus.request.orderItem; ! n && r && l && u && (this.pageStatus.request.orderItem = "sort-0|1", this.pageStatus.orderText = "\u6b22\u8fce\u5ea6\u6392\u5e8f"),
                    n && r && l && (this.pageStatus.request.locationItemList = [o]),
                    n && !a && !c && t.areafilter && t.areafilter.length >= 1 && this.pageStatus.request.locationItemList.push(o)
                },
                e.prototype.getDistanceInfo = function(t) {
                    if (t && t.length > 1) return {
                        distanceItem: t[1],
                        onlyDistance: !1
                    };
                    if (t && 1 === t.length) {
                        if (this.areaFilterType(t, "@distance")) return {
                            distanceItem: t[0],
                            onlyDistance: !0
                        }
                    }
                    return {
                        distanceItem: "",
                        onlyDistance: !1
                    }
                },
                e.prototype.isAreaPoiClear = function(t) {
                    var e = this.areaFilterType(t.areafilter, "@metro"),
                    i = this.areaFilterType(t.areafilter, "metrostation"),
                    o = t && t.areafilter.length > 0 && t.areafilter[0].indexOf("@distance") >= 0;
                    return 0 === t.areafilter.length || e && !i || o
                },
                e.prototype.isAreaPoiSearch = function(t) {
                    var e = this.areaFilterType(t, "@airportandtrainstation"),
                    i = this.areaFilterType(t, "@popularlandmark"),
                    o = this.areaFilterType(t, "@metro"),
                    s = this.areaFilterType(t, "metrostation");
                    return e || i || o && s
                },
                e.prototype.areafilterHotelList = function(t) {
                    if (this.areaFilterType(t.areafilter, "@childcity")) {
                        var e = t.areafilter,
                        i = 0; - 1 !== e[0].indexOf("_") ? i = e[0].substring(e[0].indexOf("_") + 1, e[0].indexOf("|")) : this.pageStatus.request.cityID = e[0].substring(e[0].indexOf("-") + 1, e[0].indexOf("|"));
                        var o = e[0].split("|"),
                        s = o[o.length - 1].split("@")[0];
                        this.changeCity({
                            cityId: this.pageStatus.request.cityID,
                            cname: t.text,
                            did: i,
                            cPY: s.replace(/ /g, ""),
                            isoversea: this.pageStatus.request.oversea,
                            seo: s.replace(/ /g, "").toLowerCase()
                        })
                    } else this.changePageStatusArea(t),
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.areaFilterType = function(t, e) {
                    return t.length > 0 && t[0].indexOf(e) >= 0
                },
                e.prototype.onSortItemClick = function(t, e) {
                    this.pageStatus.orderText = e,
                    this.pageStatus.request.orderItem = t,
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.changePageStatusQuickFilter = function(t, e, i) {
                    "add" === e && i && 2 === parseInt(i, 10) && (this.pageStatus.request.filterItemList = this.filterConflict("@comment"), this.pageStatus.request.highestPrice = "", this.pageStatus.request.lowestPrice = "");
                    var o = this.pageStatus.request.filterItemList.indexOf(t);
                    if ("del" === e && o >= 0 && (this.pageStatus.request.filterItemList.splice(o, 1), "kjbrand-all|||\u5168\u90e8\u5feb\u6377\u8fde\u9501|@kjbrand@brand" === t)) {
                        var s = this.pageStatus.request.filterItemList.indexOf("kjbrand-all|||\u5feb\u6377\u8fde\u9501|@hoteltype");
                        s >= 0 && this.pageStatus.request.filterItemList.splice(s, 1)
                    }
                    "add" === e && o < 0 && ("kjbrand-all|||\u5168\u90e8\u5feb\u6377\u8fde\u9501|@kjbrand@brand" === t && (this.pageStatus.request.filterItemList = this.filterConflict("@kjbrand@brand"), this.pageStatus.request.filterItemList.push("kjbrand-all|||\u5feb\u6377\u8fde\u9501|@hoteltype")), "breakfast-1|||\u542b\u65e9\u9910|@breakfast" === t && (this.pageStatus.request.filterItemList = this.filterConflict("@breakfast")), t.indexOf("@comment") >= 0 && (this.pageStatus.request.filterItemList = this.filterConflict("costperformance")), this.pageStatus.request.filterItemList.push(t))
                },
                e.prototype.onQuickFilterClick = function(t, e, i) {
                    if (this.changePageStatusQuickFilter(t, e, i), 4 === parseInt(i, 10)) return this.pageStatus.hasViewTotalPrice = "add" === e,
                    void this.updatePrice(this.$el.find(".js_hotellistinfo a"), !this.pageStatus.hasViewTotalPrice);
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.filterConflict = function(t) {
                    return c()(this.pageStatus.request.filterItemList,
                    function(e) {
                        return e.slice( - t.length) !== t
                    })
                },
                e.prototype.changePageStatusKeywordClear = function() {
                    this.pageStatus.request.keyword = "",
                    this.pageStatus.request.keywordFilterItem = "",
                    this.pageStatus.request.filterItemList = [],
                    this.pageStatus.request.locationItemList = [],
                    this.pageStatus.request.orderItem = "",
                    this.pageStatus.areaText = "",
                    this.pageStatus.orderText = "",
                    this.pageStatus.displayKeywords = "",
                    this.pageStatus.request.searchByExposedHotSearchKeyword = !1
                },
                e.prototype.onKeywordBarClear = function(t) {
                    t && (this.changePageStatusKeywordClear(), this.updateComponentsFromPageStatus(), this.refreshHotelListBody())
                },
                e.prototype.onSearchBarClear = function() {
                    this.changePageStatusKeywordClear(),
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.changePageStatusKeywordFilter = function(t) {
                    this.pageStatus.request.keyword = "",
                    this.pageStatus.request.cityID = t.cityId || this.pageStatus.request.cityID,
                    this.pageStatus.request.cityName = t.cityName || this.pageStatus.request.cityName,
                    this.pageStatus.request.districtID = t.districtId || this.pageStatus.request.districtID,
                    this.pageStatus.request.filterItemList = [],
                    this.pageStatus.request.keywordFilterItem = t.id,
                    this.pageStatus.request.locationItemList = [],
                    this.pageStatus.request.orderItem = null,
                    this.pageStatus.displayKeywords = t.text,
                    this.pageStatus.areaText = "",
                    this.pageStatus.orderText = "",
                    this.isPoiSearch(t.id) && (this.pageStatus.areaText = "4\u516c\u91cc\u4ee5\u5185", this.pageStatus.orderText = "\u8ddd\u79bb \u8fd1\u2192\u8fdc", this.pageStatus.request.locationItemList = ["distance-4|||4\u516c\u91cc\u4ee5\u5185|@distance"], this.pageStatus.request.orderItem = "sort-4|2"),
                    this.isAreaSearch(t.id) && (this.pageStatus.request.userLocationSearch = !1, this.pageStatus.request.referencePoint = "")
                },
                e.prototype.onKeywordFilterSelect = function(t) {
                    this.changePageStatusKeywordFilter(t),
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.changedPageStatusKeywordDirect = function(t, e) {
                    this.pageStatus.displayKeywords = t,
                    this.pageStatus.request.keyword = t,
                    this.pageStatus.request.orderItem = null,
                    this.pageStatus.request.keywordFilterItem = "",
                    this.pageStatus.request.filterItemList = [],
                    this.pageStatus.request.locationItemList = [],
                    this.pageStatus.request.searchByExposedHotSearchKeyword = e
                },
                e.prototype.onKeywordDirectSearch = function(t, e) {
                    this.changedPageStatusKeywordDirect(t, e),
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.onKeywordJumpToHotelDetail = function(t) {
                    if (t && t.id) {
                        var e = t.id.substring(t.id.indexOf("-") + 1).split("|")[3];
                        this.pageStatus.displayKeywords = e,
                        this.pageStatus.request.keywordFilterItem = t.id,
                        this.pageStatus.currentPage = "AssociateSearch",
                        this.pageStatus.displayKeywordText = this.keywordPanel.searchbar.elInput.val(),
                        this.restorePageStatusKeyword(t);
                        var i = t.id.substring(t.id.indexOf("-") + 1, t.id.length),
                        o = i.split("|");
                        if (o && o.length >= 5) {
                            var s = o[0];
                            this.jumpToHotelDetail(s, parseInt(o[4], 10) > 1)
                        }
                    }
                },
                e.prototype.restorePageStatusKeyword = function(t) {
                    t ? (this.pageStatus.cityID = t.cityId, this.pageStatus.cityName = t.cityName, this.pageStatus.districtID = t.districtId) : (this.pageStatus.request.cityID = this.pageStatus.cityID, this.pageStatus.request.cityName = this.pageStatus.cityName, this.pageStatus.request.districtID = this.pageStatus.districtID);
                    var e = location.href;
                    e = location.search ? e + "&city=" + this.pageStatus.request.cityID + "#gotoDetail": e + "?city=" + this.pageStatus.request.cityID + "#gotoDetail",
                    history.replaceState({},
                    document.title, e)
                },
                e.prototype.changePageStatusPriceStar = function(t) {
                    if (t.star && t.star.value ? this.pageStatus.request.starItemList = t.star.value: this.pageStatus.request.starItemList = [], t.price && t.price.value) {
                        var e = t.price.value.split(",");
                        this.pageStatus.request.lowestPrice = Number(e[0]),
                        this.pageStatus.request.highestPrice = Number(e[1])
                    } else this.pageStatus.request.lowestPrice = 0,
                    this.pageStatus.request.highestPrice = 0; (this.pageStatus.request.lowestPrice > 0 || this.pageStatus.request.highestPrice > 0) && (this.pageStatus.request.filterItemList = this.filterConflict("costperformance"));
                    var i = "";
                    t.star && n()(t.star.text,
                    function(t) {
                        i = i + ("" !== i ? "\u3001": "") + t.split("/")[0]
                    }),
                    t.price && (i = i + ("" !== i ? "\u3001": "") + t.price.text),
                    this.pageStatus.priceStarText = i
                },
                e.prototype.onPriceStarConfirm = function(t) {
                    this.changePageStatusPriceStar(t),
                    this.updateComponentsFromPageStatus(),
                    this.refreshHotelListBody()
                },
                e.prototype.isPoiSearch = function(t) {
                    return !! t && (t.indexOf("airportandtrainstation-") >= 0 || t.indexOf("popularlandmark-") >= 0 || t.indexOf("metrostation-") >= 0 || t.indexOf("spot-") >= 0 || t.indexOf("landmark-") >= 0 || t.indexOf("hotel-") >= 0)
                },
                e.prototype.isAreaSearch = function(t) {
                    return !! t && (this.isPoiSearch(t) || 0 === t.indexOf("zone-") || 0 === t.indexOf("xingzhengqv-") || 0 === t.indexOf("metroline-"))
                },
                e.prototype.jumpToHotelDetail = function(t, e, o) {
                    var s = this;
                    if (v.a.vendor.is("CTRIP")) return void new Promise(function(t) {
                        t()
                    }).then(i.bind(null, "IJ3o")).then(function(i) {
                        var o = new i.
                    default.Fn("open_url");
                        if (e) {
                            var n = s.pageStatus.request,
                            r = (n.adultCounts, n.roomQuantity, n.childAges, "ctrip://wireless/hotel_inland_detail?checkInDate=" + s.pageStatus.request.checkinDate + "&checkOutDate=" + s.pageStatus.request.checkoutDate + "&hotelId=" + t + "&cityId=" + s.pageStatus.request.cityID);
                            o.run(r, 1)
                        } else o.run("ctrip://wireless/hotel_inland_detail?checkInDate=" + s.pageStatus.request.checkinDate + "&checkOutDate=" + s.pageStatus.request.checkoutDate + "&hotelId=" + t + "&cityId=" + s.pageStatus.request.cityID, 1)
                    });
                    o = o || 0,
                    this.searchStatusProvider.setCache(this.pageStatus),
                    history.replaceState({},
                    document.title, "#gotoDetail");
                    var n = e ? "oversea/": "",
                    r = new b.a(new Date(b.a.getServerDate().getTime() + 1e3 * this.pageStatus.response.utcOffSet)),
                    a = this.pageStatus.request.checkinDate,
                    l = b.a.getIntervalDay(r.format("Y-m-d"), this.pageStatus.request.checkinDate),
                    u = b.a.getIntervalDay(this.pageStatus.request.checkinDate, this.pageStatus.request.checkoutDate);
                    u = this.morningStore.isMorning() && !e ? u + 1 > 0 ? u + 1 : 1 : u > 0 ? u: 1;
                    var p = this.pageData.hotelListResponse.utcOffSet || 0;
                    this.setOneMessage("entry-detail", "searchlist");
                    var h = "0",
                    f = c()(this.pageStatus.request.filterItemList,
                    function(t) {
                        return t.indexOf("paytype") >= 0
                    });
                    if (f && f.length > 0 && f[0]) {
                        var g = f[0].split("@")[0].split("|")[0].split("-");
                        h = g.length >= 2 ? g[1] : "0"
                    }
                    var m = this.pageStatus.request.lowestPrice,
                    w = this.pageStatus.request.highestPrice,
                    S = ""; (m > 0 || w > 0) && (S = "&pricerange=" + m, w > 0 && w < 2147483647 && (S = S + "," + w));
                    var _ = c()(this.pageStatus.request.filterItemList,
                    function(t) {
                        return t.indexOf("paytype") < 0
                    }),
                    k = this.getFilterQueryParams(_);
                    this.recordUserActionFlow("list_gotodetail");
                    var x = this.morningStore.getStatus() ? 4 : 0;
                    this.setOneMessage("entry", "searchlist");
                    var C = d()(this.pageStatus.response.hotelInfoList,
                    function(e) {
                        return e.hotelid === t
                    });
                    if (this.setOneMessage("list_hotel_price", C && C.listpagempinfo), y.a.remove("list_hotel_price"), C && C.listpagempinfo) {
                        var P = {
                            traceid: C.listpagempinfo.traceid,
                            pageid: C.listpagempinfo.pageid,
                            searchcandidate: C.listpagempinfo.searchcandidate,
                            timestamp: C.listpagempinfo.timestamp,
                            minpriceroom: C.listpagempinfo.minpriceroominfo
                        };
                        y.a.set("list_hotel_price", JSON.stringify(P), 60)
                    }
                    var I = this.pageData.hotelListRequest && void 0 !== this.pageData.hotelListRequest.adultCounts ? this.pageData.hotelListRequest.adultCounts: "",
                    T = this.pageData.hotelListRequest && void 0 !== this.pageData.hotelListRequest.childAges ? this.pageData.hotelListRequest.childAges.replace(/\|/g, "_") : "",
                    L = 1;
                    this.pageStatus.numselect && (I = this.pageStatus.numselect.adult, L = this.pageStatus.numselect.room, T = this.pageStatus.numselect.children && this.pageStatus.numselect.children.toString().replace(/\,/g, "_"));
                    var j = "";
                    if (e) {
                        var A = this.pageStatus.hasViewTotalPrice ? 1 : 0;
                        j = F.a.getenvHost() + "/webapp/hotel/" + n + "hoteldetail/" + t + ".html?atime=" + a + "&days=" + u + "&contrl=" + x + "&pay=" + h + "&tzone=" + p + S + k + "&rcount=" + L + "&adult=" + I + "&child=" + T + "&listindex=" + o + "&totalprice=" + A + "#fromList"
                    } else {
                        var O = this.generateLatLon();
                        j = F.a.getenvHost() + "/webapp/hotel/" + n + "hoteldetail/" + t + ".html?atime=" + a + "&daylater=" + l + "&days=" + u + "&contrl=" + x + "&pay=" + h + "&latlon=" + O + S + k + "&listindex=" + o + "#fromList"
                    }
                    if (this.sendPriceUBT(C, e), C) {
                        var D = new ot.a;
                        D.setOneMessage("not_yet_send_list_to_detail_ubt", 1),
                        D.setOneMessage("list_to_detail_bookable", 0 === C.fullbooking ? 1 : 0)
                    }
                    this.goTo("hoteldetails", j)
                },
                e.prototype.sendPriceUBT = function(t, e) {
                    if (this.pageStatus && this.pageStatus.response && t) try {
                        var i = {
                            hotelid: t.hotelid,
                            checkin: this.pageStatus.request.checkinDate,
                            checkout: this.pageStatus.request.checkoutDate,
                            roomid: t.priceInfo.startPriceRoomId,
                            amount: parseInt(t.priceInfo.originalStartPrice, 10),
                            price: parseInt(t.priceInfo.priceAfterAllReturn, 10),
                            arrange: this.pageStatus.request.orderItem ? this.pageStatus.request.orderItem: "sort-0|1",
                            bookable: 0 === t.fullbooking ? 1 : 0,
                            filter: this.pageStatus.request.filterItemList.map(function(t) {
                                var e = t.split("|");
                                return e[e.length - 2]
                            }),
                            isshadow: t.minPriceIsShadow ? 1 : 0,
                            ismemberlogin: this.pageStatus.response.memberLogin,
                            hasfilters: this.pageStatus.response.uiModifyInfo.hasFilters
                        },
                        o = e ? "o_h5_128_list_click": "o_h5_80_list_click"; (new ot.a).setOneMessage("list_to_detail_price_info", JSON.stringify(i)),
                        window.__bfi.push(["_tracklog", o, JSON.stringify(i)])
                    } catch(t) {}
                },
                e.prototype.getFilterQueryParams = function(t) {
                    var e = [];
                    t && t.length > 0 && t.forEach(function(t) {
                        var i = t.split("|")[0].split("-");
                        if (! (i.length < 2)) {
                            var o = i[0],
                            s = parseInt(i[1], 10);
                            if (rt[o]) {
                                if (! (g()(rt[o],
                                function(t) {
                                    return t.key === s
                                }) < 0)) {
                                    var n = g()(e,
                                    function(t) {
                                        return t.type === o
                                    });
                                    n < 0 ? e.push({
                                        type: o,
                                        val: s
                                    }) : e[n].val += s
                                }
                            }
                        }
                    });
                    var i = "";
                    return e.forEach(function(t) {
                        i += "&" + t.type + "=" + t.val
                    }),
                    i
                },
                e.prototype.generateLatLon = function() {
                    var t = this,
                    e = "";
                    if (this.pageStatus.request.userLocationSearch) return e = this.pageStatus.request.userLatitude + "," + this.pageStatus.request.userLongitude + ",,99,",
                    encodeURI(e);
                    if (this.pageStatus.request.locationItemList) {
                        var i = d()(this.pageStatus.request.locationItemList,
                        function(e) {
                            return ! t.areaFilterType(t.pageStatus.request.locationItemList, "@distance")
                        });
                        e = this.getlatlon(i)
                    }
                    return ! e && e.length <= 0 && this.pageStatus.request.keywordFilterItem && (e = this.getlatlon(this.pageStatus.request.keywordFilterItem)),
                    e
                },
                e.prototype.getlatlon = function(t) {
                    var e = "";
                    if (t && t.length > 0) {
                        var i = t.indexOf("@");
                        i > 0 && (t = t.substring(0, i));
                        var o = t.split("-"),
                        s = this.convertFilterType(o[0]);
                        if (s > 0) {
                            var n = o[1] && o[1].split("|");
                            e = n[1] + "," + n[2] + "," + n[3] + "," + s + "," + n[0]
                        }
                    }
                    return encodeURI(e)
                },
                e.prototype.convertFilterType = function(t) {
                    var e = 0;
                    switch (t) {
                    case "zone":
                        e = 3;
                        break;
                    case "landmark":
                        e = 5;
                        break;
                    case "metrostation":
                        e = 7;
                        break;
                    case "airportandtrainstation":
                        e = 8;
                        break;
                    default:
                        e = 0
                    }
                    return e
                },
                e.prototype.mapToHotelDetail = function(t) {
                    this.pageStatus.currentPage = "HotelListMap",
                    this.pageStatus.currentDom = $(".js_list_container").find(".js_hotellistinfo").html(),
                    this.pageStatus.scrollTop = $(".js_list_container").scrollTop(),
                    this.jumpToHotelDetail(t.hotelid, this.pageStatus.request.oversea)
                },
                e.prototype.onMapSearch = function(t, e, i) {
                    this.address = e;
                    var o = t.radius / 1e3,
                    s = o >= 1 ? Math.floor(o) + "\u516c\u91cc\u4ee5\u5185": Math.floor(1e3 * o) + "\u7c73\u4ee5\u5185";
                    this.pageStatus.request.locationItemList = ["distance-" + o + "|||" + s + "@distance"],
                    this.pageStatus.request.userLatitude = t.lat,
                    this.pageStatus.request.userLongitude = t.lon,
                    this.pageStatus.request.userLocationSearch = !0,
                    this.pageStatus.request.referencePoint = e.address,
                    this.pageStatus.request.cityName = e.address,
                    this.pageStatus.cnameforownaround = i && i.CityName,
                    i && this.pageStatus.request.cityID !== i.CityID && (this.pageStatus.request.highestPrice = 0, this.pageStatus.request.lowestPrice = 0, this.pageStatus.request.starItemList = [], this.pageStatus.request.filterItemList = [], this.pageStatus.request.keywordFilterItem = null, this.pageStatus.request.keyword = ""),
                    this.refreshHotelListBody(),
                    this.pageStatus.locatedOversea = !("CHN" === e.countryShortName),
                    this.showNewGuestCouponEntr(),
                    this.updateRoomPeopleNumSelect()
                },
                e.prototype.generatePageStatus = function() {
                    var t = this.searchStatusProvider.getCache();
                    return this.isBack() && t.response && t.response.uiModifyInfo ? t: ($("#js_fake_loading2").remove(), this.operatePageStatus(this.pageData))
                },
                e.prototype.operatePageStatus = function(t) {
                    var e = t.hotelListResponse.totalPageCount,
                    i = t.hotelListResponse,
                    o = p()(t.hotelListRequest),
                    s = i.uiModifyInfo,
                    n = t.newGuestCouponEntrance,
                    r = "";
                    return s && (o.keyword = s.keyword, o.keywordFilterItem = s.keywordFilterItem, o.filterItemList = s.filterItemList, o.locationItemList = s.locationItemList, o.starItemList = s.starItemList, o.orderItem = s.orderItem, o.highestPrice = s.filterPriceInfo && s.filterPriceInfo.maxPrice, o.lowestPrice = s.filterPriceInfo && s.filterPriceInfo.minPrice, r = s.displayKeyword),
                    {
                        request: o,
                        totalPageCount: e,
                        response: i,
                        displayKeywords: r,
                        newGuestCouponEntrance: n
                    }
                },
                e.prototype.hideToast = function() {
                    setTimeout(function() {
                        $(".js_hotel_count_toast").hide()
                    },
                    2500)
                },
                e.prototype.onHotelListProviderGetHotelHomePageSuccess = function(t, e) {
                    this.abnormalNetwork && this.abnormalNetwork.hide(),
                    this.updateHotelQueryStore(),
                    this.hotellistpanel.setHomePageDomStatus(t, e),
                    Object(k.a)(t),
                    this.hotelListMapPanel && this.hotelListMapPanel.refreshMap(this.pageStatus),
                    this.updateComponentsFromPageStatus(),
                    this.hideToast(),
                    C.a.hide()
                },
                e.prototype.refreshHotelListBody = function(t) {
                    this.overseaTraceLog(),
                    C.a.show(),
                    this.hotelListProvider.getHotelHomePage(this.pageStatus, t),
                    this.goTop(),
                    $("body").css({
                        "-webkit-transition": "",
                        transition: ""
                    })
                },
                e.prototype.handleRedbag = function(t) {
                    var e = new K.a;
                    if (e.setData(this.appData.isMemberLogin), this.appData.isMemberLogin) {
                        var i = e.showPOP({
                            rdpinfo: {
                                hasred: 5
                            }
                        });
                        m.a.get("/webapp/hotel/j/hotellist/hongbao", {},
                        function(t) {
                            i.hide(),
                            e.showPOP({
                                rdpinfo: t
                            })
                        },
                        function() {
                            var t = {
                                rdpinfo: {
                                    hasred: 1,
                                    redmessage: "\u5f88\u62b1\u6b49\uff0c\u6682\u65f6\u65e0\u6cd5\u9886\u53d6\u7ea2\u5305"
                                }
                            };
                            i.hide(),
                            e.showPOP(t)
                        },
                        3e4)
                    } else {
                        var o = {
                            rdpinfo: {
                                hasred: 4
                            }
                        },
                        s = e.showPOP(o);
                        CLogin.uipageview.loaddynamic("hongbao_logincontainer",
                        function(t) {
                            if (0 == +t.ReturnCode) {
                                s.loged = !0,
                                s.hide();
                                var i = e.showPOP({
                                    rdpinfo: {
                                        hasred: 5
                                    }
                                });
                                m.a.get("/webapp/hotel/j/hotellist/hongbao", {},
                                function(t) {
                                    i.hide(),
                                    e.showPOP({
                                        rdpinfo: t
                                    })
                                },
                                function() {
                                    i.hide(),
                                    e.showPOP({
                                        rdpinfo: {
                                            hasred: 1,
                                            redmessage: "\u5f88\u62b1\u6b49\uff0c\u6682\u65f6\u65e0\u6cd5\u9886\u53d6\u7ea2\u5305"
                                        }
                                    })
                                },
                                3e4)
                            }
                        })
                    }
                    var n = this;
                    e.onHongBaoPopHide(function() {
                        "undefined" != typeof loginpop && loginpop.loged && n.refreshPage()
                    })
                },
                e.prototype.refreshPage = function() {
                    this.appData.isLogin || location.reload()
                },
                e.prototype.updateHotelQueryStore = function() {
                    var t = b.a.parse(this.pageStatus.request.checkinDate).format("Y-m-d"),
                    e = b.a.parse(this.pageStatus.request.checkoutDate).format("Y-m-d"),
                    i = b.a.getIntervalDay(t, e);
                    this.morningStore.isMorning() && (i += 1);
                    var o = {
                        inDay: t,
                        outDay: e,
                        isSearchListWithCity: !this.pageStatus.request.userLocationSearch,
                        isGeoLocation: !1,
                        days: i,
                        hotelType: this.pageStatus.response.oversea ? 2 : 1,
                        needGetGeo: void 0 === this.address,
                        requestLocale: this.address,
                        address: this.address,
                        sort: this.pageStatus.request.userLocationSearch ? {
                            dir: 2,
                            idx: 1,
                            ordby: 4,
                            size: 10
                        }: {},
                        radius: this.pageStatus.request.userLocationSearch ? {
                            id: 4e3,
                            text: ""
                        }: {},
                        city: {
                            cityId: this.pageStatus.response.positionInfo.cityId,
                            cname: this.pageStatus.response.positionInfo.cityName,
                            cPY: this.pageStatus.response.positionInfo.cityNameEN,
                            ctryId: this.pageStatus.response.positionInfo.countryId,
                            did: this.pageStatus.response.positionInfo.districtId,
                            type: this.pageStatus.response.oversea ? 2 : 1,
                            seo: this.pageStatus.response.positionInfo.cityNameEN.toLowerCase().replace(/ /g, ""),
                            tzone: this.pageStatus.response.utcOffSet
                        },
                        rooms: 1,
                        numselect: this.pageStatus.numselect ? {
                            adult: this.pageStatus.numselect.adult,
                            room: this.pageStatus.numselect.room,
                            children: this.pageStatus.numselect.children.toString().replace(/\,/g, "|")
                        }: {
                            adult: 1,
                            room: 1,
                            children: "-1|-1|-1"
                        }
                    };
                    nt.setAttr("queryParams", o),
                    nt.setAttr("city", {}),
                    nt.setAttr("searchParams", {})
                },
                e.prototype.openFilterPanel = function(t) {
                    this.filterPanel || (this.filterPanel = new V.a({
                        request: this.pageStatus.request
                    }), this.filterPanel.on("onClickOK", this.onFilterPanelClickOK.bind(this))),
                    this.resetPanelTopInListMap(t),
                    this.filterPanel.setDefaultStyle(t),
                    this.filterPanel.show(),
                    this.stopHeaderAnimate(),
                    this.recordUserActionFlow("list_openfilter")
                },
                e.prototype.closeFilterPanel = function() {
                    this.filterPanel.hide(),
                    this.hideHeaderInListMap(),
                    this.restoreHeaderAnimation()
                },
                e.prototype.openAreaFilterPanel = function(t) {
                    this.areafilterPanel || (this.areafilterPanel = new Q.a({
                        request: this.pageStatus.request,
                        state: this.pageStatus.request.locationItemList
                    }), this.areafilterPanel.on("onConfirm", this.areafilterHotelList.bind(this))),
                    this.resetPanelTopInListMap(t),
                    this.areafilterPanel.setDefaultStyle(t),
                    this.areafilterPanel.show(),
                    this.stopHeaderAnimate(),
                    this.recordUserActionFlow("list_openzone")
                },
                e.prototype.closeAreaFilterPanel = function() {
                    this.areafilterPanel.hide(),
                    this.hideHeaderInListMap(),
                    this.restoreHeaderAnimation()
                },
                e.prototype.openPriceStarFilterPanel = function(t) {
                    this.PriceStarFilterPanel || (this.PriceStarFilterPanel = new S.
                default({
                        needMask:
                        !1,
                        biz: this.pageStatus.response.oversea ? 2 : 1,
                        data: {
                            star: {
                                selected: {
                                    value: this.pageStatus.response.uiModifyInfo.starItemList
                                }
                            },
                            price: {
                                selected: {
                                    value: this.pageStatus.response.uiModifyInfo.filterPriceInfo.minPrice + "," + this.pageStatus.response.uiModifyInfo.filterPriceInfo.maxPrice
                                },
                                config: {
                                    step: this.pageStatus.response.oversea ? 100 : 50,
                                    range: this.pageStatus.response.oversea ? "0|1900": "0|550"
                                }
                            }
                        },
                        animation: {
                            inAnimation: "animated fadeInDown",
                            outAnimation: ""
                        },
                        onConfirm: this.onPriceStarConfirm.bind(this)
                    })),
                    this.resetPanelTopInListMap(t),
                    this.PriceStarFilterPanel.setDefaultStyle(t),
                    this.PriceStarFilterPanel.show(),
                    this.stopHeaderAnimate(),
                    this.recordUserActionFlow("list_openstarprice")
                },
                e.prototype.closePriceStarFilterPanel = function() {
                    this.PriceStarFilterPanel.hide(),
                    this.hideHeaderInListMap(),
                    this.restoreHeaderAnimation()
                },
                e.prototype.openSortFilterPanel = function(t) {
                    this.sortFilterPanel || (this.sortFilterPanel = new Y.a({
                        orderItem: this.pageStatus.request.orderItem
                    }), this.sortFilterPanel.on("onSortItemClick", this.onSortItemClick.bind(this))),
                    this.resetPanelTopInListMap(t),
                    this.sortFilterPanel.setDefaultStyle(t),
                    this.sortFilterPanel.show(),
                    this.stopHeaderAnimate(),
                    this.recordUserActionFlow("list_opensort")
                },
                e.prototype.closeSortFilterPanel = function() {
                    this.sortFilterPanel.hide(),
                    this.hideHeaderInListMap(),
                    this.restoreHeaderAnimation()
                },
                e.prototype.openPaytypePanel = function() {
                    var t = this;
                    this.hotelListMenu.mask.show();
                    var e = this.$(".js_quick_filter").offset(),
                    i = e.height,
                    o = {
                        panelTop: i,
                        panelHeight: window.innerHeight - i - 50
                    };
                    this.paytypePanel || (this.paytypePanel = new tt.a, this.paytypePanel.on("onPaytypeItemClick",
                    function(e, i) {
                        var o = Math.max(t.pageStatus.request.filterItemList.indexOf("paytype-1|||\u5728\u7ebf\u4ed8\u6b3e|@paytype"), t.pageStatus.request.filterItemList.indexOf("paytype-2|||\u5230\u5e97\u4ed8\u6b3e|@paytype"));
                        "null" === e ? o > -1 && (t.pageStatus.request.filterItemList[o] = e, t.pageStatus.request.filterItemList.splice(o, 1)) : -1 === o ? t.pageStatus.request.filterItemList.push(e) : t.pageStatus.request.filterItemList[o] = e,
                        t.updateComponentsFromPageStatus(),
                        t.refreshHotelListBody(),
                        t.paytypePanel.hide()
                    })),
                    this.paytypePanel.filterItem = this.pageStatus.request.filterItemList,
                    this.paytypePanel.setDefaultStyle(o),
                    this.paytypePanel.show(),
                    this.$(".js_list_container").css({
                        overflowY: "hidden"
                    }),
                    this.paytypePanel.on("onHide",
                    function() {
                        t.$(".js_list_container").css({
                            overflowY: "scroll"
                        })
                    })
                },
                e.prototype.show = function() {
                    $("#header").show(),
                    this.$el.show()
                },
                e.prototype.updateComponentsFromPageStatus = function() {
                    this.updateKeywordsPanel(),
                    this.updateKeywordBar(),
                    this.updateQuickFilter(),
                    this.updateHeader(),
                    this.updateInAndOutPanel(),
                    this.updateHotelListMenu(),
                    this.updateFilterPanel(),
                    this.updateAreaFilterPanel(),
                    this.updatePriceStarFilterPanel(),
                    this.updateSortFilterPanel(),
                    this.updateHotelListMapMenu(),
                    this.updateHotelListMapPanel(),
                    this.updateCityListPanel(),
                    this.updateExposedZoneList(),
                    this.updateLoginGuide(),
                    this.updateListContainer()
                },
                e.prototype.updateRoomPeopleNumSelect = function() {
                    var t = this.pageStatus.request.oversea;
                    void 0 !== this.pageStatus.locatedOversea && (t = this.pageStatus.locatedOversea),
                    t ? (this.$(".js_numselect").show(), this.$(".js_keywordbar_content").attr("placeholder", "\u4f4d\u7f6e/\u54c1\u724c/\u9152\u5e97")) : (this.$(".js_numselect").hide(), this.$(".js_keywordbar_content").attr("placeholder", "\u5173\u952e\u5b57/\u4f4d\u7f6e/\u54c1\u724c/\u9152\u5e97\u540d")),
                    this.pageStatus.numselect && (delete this.pageStatus.numselect, this.updateHotelQueryStore(), this.$(".js_numselect_adult").html("\u6210\u4eba&nbsp;1"), this.$(".js_numselect_child").html("\u513f\u7ae5&nbsp;0"))
                },
                e.prototype.updateLoginGuide = function() {
                    this.pageStatus.request.oversea ? this.loginGuide && this.loginGuide.hide() : this.initLoginGuide()
                },
                e.prototype.updateExposedZoneList = function() {
                    if (! (this.pageStatus.request.pageIndex > 2)) {
                        var t = this.$el.find(".js_exposed_zonelist");
                        t.children().removeClass("current");
                        var e = this.pageStatus.request.locationItemList,
                        i = e && e.length > 0 && e[0].indexOf("zone-") >= 0 ? e[0] : null;
                        if (t && i) {
                            t.find("[data-id = '" + i + "']").addClass("current")
                        }
                    }
                },
                e.prototype.updateCityListPanel = function() {
                    this.cityList && this.pageStatus.request.userLocationSearch && this.cityList.updateCityListSelectedCity({
                        cityId: this.pageStatus.request.cityID,
                        oversea: this.pageStatus.request.oversea,
                        cname: this.pageStatus.cnameforownaround
                    })
                },
                e.prototype.updateInAndOutPanel = function() {
                    var t = b.a.parse(this.pageStatus.request.checkinDate).format("m-d"),
                    e = b.a.parse(this.pageStatus.request.checkoutDate).format("m-d");
                    this.inAndOutPanel.eq(0).html("\u4f4f&nbsp;" + t),
                    this.inAndOutPanel.eq(1).html("\u79bb&nbsp;" + e)
                },
                e.prototype.updateKeywordsPanel = function() {
                    var t = this;
                    this.keywordPanel && (this.pageStatus.request.cityID !== this.keywordPanel.request.cityID || this.pageStatus.request.districtID !== this.keywordPanel.request.districtID ? this.destroyKeywordPanel() : this.getKeywordPanel().then(function() {
                        t.keywordPanel.updateSearchBarText({
                            cityID: t.pageStatus.request.cityID,
                            keyword: t.pageStatus.displayKeywords
                        })
                    }))
                },
                e.prototype.updateKeywordBar = function() {
                    this.keywordBar.updateKeywordBarText(this.pageStatus.displayKeywords)
                },
                e.prototype.updateQuickFilter = function() {
                    this.quickFilter.updateChangedCity(this.pageStatus.request),
                    this.quickFilter.updateStyle(this.pageStatus.request)
                },
                e.prototype.updateNewGuestCoupon = function(t, e) {
                    var i = this;
                    if (t !== e) {
                        var o = e ? 1 : 0;
                        m.a.get("/webapp/hotel/api/getnewguestcouponentrance?oversea=" + o, {},
                        function(t) {
                            i.pageStatus.newGuestCouponEntrance = t,
                            t && t.showEntrance ? i.showNewGuestCouponEntr() : i.newGuestCouponEntr && i.newGuestCouponEntr.hide()
                        },
                        function() {},
                        3e4, {
                            dataType: "json"
                        })
                    }
                },
                e.prototype.updateHeader = function() {
                    var t = this.$header.find(".js_open_citylist"),
                    e = this.pageStatus.request.cityName;
                    e && t.html() !== e && this.$header.find(".js_open_citylist").html(e || "&nbsp;&nbsp;")
                },
                e.prototype.updateHotelListMenu = function() {
                    this.hotelListMenu.updateSelectedFilterCount(this.pageStatus.request.filterItemList),
                    this.hotelListMenu.updateAreaFilter(this.pageStatus.areaText),
                    this.hotelListMenu.updatePriceStarFilter(this.pageStatus.priceStarText, this.pageStatus.request.oversea),
                    this.hotelListMenu.updateSortFilter(this.pageStatus.orderText),
                    this.hotelListMenu.switchToggle()
                },
                e.prototype.updateFilterPanel = function() {
                    this.filterPanel && (this.pageStatus.request.cityID !== this.filterPanel.request.cityID || this.pageStatus.request.districtID !== this.filterPanel.request.districtID ? this.destroyFilterPanel() : this.filterPanel && this.filterPanel.resetSelectedItems(this.pageStatus.request.filterItemList))
                },
                e.prototype.updateAreaFilterPanel = function() {
                    this.areafilterPanel && (this.pageStatus.request.cityID !== this.areafilterPanel.request.cityID || this.pageStatus.request.districtID !== this.areafilterPanel.request.districtID ? this.destroyAreaPanel() : this.areafilterPanel && this.areafilterPanel.updateState(this.pageStatus.request.locationItemList))
                },
                e.prototype.updatePriceStarFilterPanel = function() {
                    this.PriceStarFilterPanel && ((this.pageStatus.request.oversea ? 2 : 1) !== this.PriceStarFilterPanel.biz ? this.destroyPriceAndStarPanel() : this.PriceStarFilterPanel && this.PriceStarFilterPanel.updateState(this.pageStatus.request.oversea, this.pageStatus.request.starItemList, {
                        minPrice: this.pageStatus.request.lowestPrice,
                        maxPrice: this.pageStatus.request.highestPrice
                    }))
                },
                e.prototype.updateSortFilterPanel = function() {
                    this.sortFilterPanel && this.sortFilterPanel.update(this.pageStatus.request.orderItem)
                },
                e.prototype.updateHotelListMapMenu = function() {
                    this.hotelListMapMenu && (this.hotelListMapMenu.updateSelectedFilterCount(this.pageStatus.request.filterItemList), this.hotelListMapMenu.updateAreaFilter(this.pageStatus.areaText), this.hotelListMapMenu.updatePriceStarFilter(this.pageStatus.priceStarText, this.pageStatus.request.oversea), this.hotelListMapMenu.updateSortFilter(this.pageStatus.orderText), this.hotelListMapMenu.switchToggle())
                },
                e.prototype.updateHotelListMapPanel = function() {
                    this.hotelListMapPanel && (this.hotelListMapPanel.updateKeywordText(this.pageStatus.displayKeywords), this.hotelListMapPanel.updateInOutDate(b.a.parse(this.pageStatus.request.checkinDate).format("m-d"), b.a.parse(this.pageStatus.request.checkoutDate).format("m-d")))
                },
                e
            } (F.a);
            q.a.init(new lt($("#content")))
        },
};

fun1([21, 4, 8, 18],param1,["LWyc"]);
