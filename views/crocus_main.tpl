<!DOCTYPE html>
<html lang="no-nb">

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

        <LINK href="http://karsten.pythonanywhere.com/views/simplex.css" rel="stylesheet" type="text/css">
        <style>
            body {
                margin: 0;
                padding-top: 70px;
            }
        </style>
    </head>

    <body>

        <div class="container">


            <nav class="navbar navbar-default">
              %#<div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">

                </div>

                <ul class="nav navbar-nav">
                    <li class="active"><a href="/crocus/model">Snødekkemodell <span class="sr-only">(current)</span></a></li>
                    <li class="disabled"><a href="/crocus/map">Kart</a></li>
                    <li><a href="/crocus/help">Hjelp</a></li>
                    <li class="disabled"><a href="/corcus/feedback">Tilbakemeldinger</a></li>
                </ul>

              %#</div><!-- /.container-fluid -->
            </nav>

             <div class="row col-md-12">
                 {{ !crocus_page }}
             </div>

        </div>




        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="http://karsten.pythonanywhere.com/views/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    </body>
</html>