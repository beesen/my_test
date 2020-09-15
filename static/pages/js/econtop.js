$(document).ready(function () {
    $(".main-menu__link").on("click", function () {
        // remove "is-active"
        $(".main-menu__link").removeClass("is-active")

        // add "is-active" to this
        $(this).addClass("is-active")
    })
    $(".main-menu__link").hover(function (event) {
        const elem = $(this).find(".material-icons.md-econtop:first-child")
        if (elem.css("color")==="rgb(153, 153, 153)") {
            elem.css("color", "#000") }
        else {
            elem.css("color", "#999")
        }
    })
})
