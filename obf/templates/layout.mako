<html>
    <head>
        <!-- Bootstrap core CSS -->
        <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
        <!-- Custom styles for this scaffold -->
        <link href="{{request.static_url('obf:static/theme.css')}}" rel="stylesheet">
    </head>
    <body>
        <div class="home">
            <%block name="home"/>
        </div>
        ${self.body()}
    </body>
</html>