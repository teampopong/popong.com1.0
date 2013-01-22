(function () {
    var names = {
        "cornchz": "developer",
        "daybreaker": "developer",
        "echojuliett": "data miner",
        "weirdclaire": "UX designer"
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
