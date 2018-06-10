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
                    <span class="day icon">
                        {{ icon }}
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
                <div class="divText">
                    <p class="text">{{ text }}</p>
                </div>
                <div class="divBack">
					<a class="link" href="/">Назад</a>
                </div>
            </div>
        </div>
    </div>
</body>

</html>