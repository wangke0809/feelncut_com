$("#amz-go-top").hide(); 
$(function() {
	$(window).scroll(function() { //只要窗口滚动,就触发下面代码 
		var scrollt = document.documentElement.scrollTop + document.body.scrollTop; //获取滚动后的高度 
		if (scrollt > 200) { //判断滚动后高度超过200px,就显示  
			//$("#amz-go-top").show(); 
			$("#amz-go-top").fadeIn(400)//淡出     
		} else {
			$("#amz-go-top").stop().fadeOut(400); //如果返回或者没有超过,就淡入.必须加上stop()停止之前动画,否则会出现闪动   
		}
	});
	$("#amz-go-top").click(function() { //当点击标签的时候,使用animate在200毫秒的时间内,滚到顶部
		$("html,body").animate({
			scrollTop: "0px"
		},
		200);
	});
});
function uaredirect(f) {
    try {
        if (document.getElementById("bdmark") != null) {
            return
        }
        var b = false;
        if (arguments[1]) {
            var e = window.location.host;
            var a = window.location.href;
            if (isSubdomain(arguments[1], e) == 1) {
                f = f + "/#m/" + a;
                b = true
            } else {
                if (isSubdomain(arguments[1], e) == 2) {
                    f = f + "/#m/" + a;
                    b = true
                } else {
                    f = a;
                    b = false
                }
            }
        } else {
            b = true
        }
        if (b) {
            var c = window.location.hash;
            if (!c.match("fromapp")) {
                if ((navigator.userAgent.match(/(iPhone|iPod|Android|ios)/i))) {
                    location.replace(f)
                }
            }
        }
    } catch(d) {}
}
function isSubdomain(c, d) {
    this.getdomain = function(f) {
        var e = f.indexOf("://");
        if (e > 0) {
            var h = f.substr(e + 3)
        } else {
            var h = f
        }
        var g = /^www\./;
        if (g.test(h)) {
            h = h.substr(4)
        }
        return h
    };
    if (c == d) {
        return 1
    } else {
        var c = this.getdomain(c);
        var b = this.getdomain(d);
        if (c == b) {
            return 1
        } else {
            c = c.replace(".", "\\.");
            var a = new RegExp("\\." + c + "$");
            if (b.match(a)) {
                return 2
            } else {
                return 0
            }
        }
    }
};
uaredirect(window.location.href.replace('Home','m/Home').replace('old_index','m/old_index'));