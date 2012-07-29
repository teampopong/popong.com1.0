(function () {
    var names = {
        "cornchz": "핵심 개발자",
        "daybreaker": "개발자",
        "jooddang": "얼굴마담",
        "echojuliett": "데이터마이너",
        "allsolution": "서버 개발자",
        "minspiration": "UX 기획자",
        "uni208": "데이터마이너",
        "jihye": "기획자",
        "sanxiyn": "개발자",
        "dongx3": "모바일 개발자",
        "netj": "개발자",
        "unrealive": "기획자",
        "ingtellect": "개발자"
        };

    $.each(names, function(name, description) {
        document.write("<li id=\"" + name + "\">");
        document.write("<h3 class=\"member-name\"><a href=\"http://twitter.com/" + name + "\">" + name + "</a></h3>");
        document.write("<img src=\"images/member-" + name + ".jpg\">");
        document.write("<div class=\"member-description shadow\">" + description + "</div>");
        // document.write("<div class=\"member-photo-" + name + "\"></div>");
        document.write("</li>");
    });
}());
