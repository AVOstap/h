<html>
<head>
	<title>{{ title }}</title>
    <link type="text/css" rel="stylesheet" href="static/style.css">
    <link type="image/x-icon" rel="shortcut icon" href="static/favicon.ico">
</head>

<body>
    <div class="main">
        <div class="goroLeft">
            <div class="goroImg">
                <div class="date">
                    <img src="static/zodiac-circle.png">
                    <span class="day">
                        {{ now_day }}
                        <span class="month">
                           {{ now_month }}
                        </span>
                    </span>
                 </div>
             </div>
        </div>
        <div class="goroRight">
            <div class="content">
                <div class="header">
					<span class="spanHeader">
                        {{ topic }}
                    </span>
                </div>
                <div class="links">
                    <div class="inlineLinks">
					% for ru,lt in zodiac_choices:
                        <a class="link" href="{{lt}}">{{ru}}</a>
					% end
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>

</html>