(function () {
    var names = {
        "cornchz": "핵심 개발자",
        "daybreaker": "개발자",
        "echojuliett": "데이터마이너",
        "weirdclaire": "UX 디자이너"
        };

    $.each(names, function(name, description) {
        document.write("<li id=\"" + name + "\">");
        document.write("<h3 class=\"member-name\"><a href=\"http://twitter.com/" + name + "\">" + name + "</a></h3>");
        document.write("<img src=\"/static/images/member-" + name + ".jpg\">");
        document.write("<div class=\"member-description shadow\">" + description + "</div>");
        // document.write("<div class=\"member-photo-" + name + "\"></div>");
        document.write("</li>");
    });
}());
