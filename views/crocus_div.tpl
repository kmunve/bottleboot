<!DOCTYPE html>
<html lang="no-nb">

  <head>
    <LINK href="http://karsten.pythonanywhere.com/views/flatly.min.css" rel="stylesheet" type="text/css">

  </head>

  <body> 

    <div class="col-lg-11">




      <p>

	<div class="panel panel-default">
	  <div class="panel-heading">
	    <h3 class="panel-title"><a name="{{ region }}">Modellert snødekke i {{ region }}</a></h3>
	  </div>
	  <div class="panel-body">

	    <table class="table table-striped table-hover ">
	      <thead>
		<tr>
		  <th><img src={{ url_vertprofile }} height="400" class="img-responsive"></th>
		  <th>
		    <img src={{ url_snowgraintype }} width="400" class="img-responsive">
		    <br>
		    <img src={{ url_density }} width="400" class="img-responsive">
		  </th>
		</tr>
	      </thead>
	    </table>

	  </div>
	</div>

      </p>

    </div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="http://karsten.pythonanywhere.com/views/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

</body>
</html>
