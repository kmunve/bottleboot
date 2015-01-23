<!DOCTYPE html>
<html lang="no-nb">

<head>
    <LINK href="http://karsten.pythonanywhere.com/views/flatly.min.css" rel="stylesheet" type="text/css">

</head>

<body>

<div class="col-lg-11">

<p>
<form action="/region_submit" method="post">
<div class="btn-group">
  <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
    Velg varslingsregion
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu">
    % for region in region_list:
    <li><input name="region" class="form-control" type="submit" value="{{region}}"></input></li>
    % end
    <li class="divider"></li>
  </ul>
</div>
</form>

</p>

<p>

% for region in region_list:
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title"><a name="{{ region }}">Modellert snødekke i {{ region }}</a></h3>
  </div>
  <div class="panel-body">

    <table class="table table-striped table-hover ">
      <tbody>
	<tr>
	  <th><img src="{{ url_vertprofile }}" height="100%" class="img-responsive"></th>
	  <th>
	    <img src="{{ url_snowgraintype }}" height="33%" class="img-responsive">
	    <br>
	    <img src="{{ url_density }}" height="33%" class="img-responsive">
	  </th>
	</tr>
      </tbody>
    </table>

    <br>
    <p align="left">Last ned som <a href="http://karsten.pythonanywhere.com/media/{{ region }}.pdf">PDF</a> eller <a href="http://karsten.pythonanywhere.com/media/{{ region }}.png">bildefil</a>.</p>

  </div>
</div>
% end

</p>

</div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="http://karsten.pythonanywhere.com/views/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

</body>
</html>
