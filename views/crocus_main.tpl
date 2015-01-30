<!DOCTYPE html>
<html lang="no-nb">

    <head>
        <LINK href="http://karsten.pythonanywhere.com/views/journal.css" rel="stylesheet" type="text/css">
        <style>
            body {
                margin: 0;
                padding-top: 70px;
            }
        </style>
    </head>

    <body>

        <div class="col-lg-11">

            <div class="col-lg-11">

                <div class="btn-group">
                    <!-- Here goes the selection form  -->
                    {{!crocus_form}}
                </div>





                <!-- Here goes the result -->
                % for result in crocus_result:
                {{!result}}
                % end

            </div>

        </div>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="http://karsten.pythonanywhere.com/views/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    </body>
</html>