<html>
<head>
	<title>{{get('title','Horoscope')}}</title>
    <link type="text/css" rel="stylesheet" href="static/style.css">
</head>

<body>
    <div class="main">
        <div class="goroLeft">
            <div class="goroImg">
                <div class="date">
                    <img src="static/all.png">
					% if type(get('day',''))!=int:
                    <span class="day icon">
					% else:
					<span class="day">
					% end
                        {{get('day','')}}
                        <span class="month">
                           {{get('month','')}}
                            </span>
                    </span>
                 </div>
             </div>
        </div>
        <div class="goroRight">
            <div class="content">
                <div class="header">
					<span class="spanHeader">
                        {{get('header','')}}
                </div>
                <div class="links">
                    <div class="inlineLinks">
					% if get('zodiac',''):
					% for ru,lt in zodiac:
                        <a class="link" href="{{lt}}">{{ru}}</a>
					% end
					% end
                    </div>
                </div>
                <div class="divText">
                    <p class="text">{{get('text','')}}</p>
                </div>
                % if type(get('day',''))!=int:
                <div class="divBack">
					<a class="link" href="/">Назад</a>
                </div>
				% end
            </div>
        </div>
    </div>
</body>

</html>