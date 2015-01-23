
% for station in station_list:
<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title"><a name="{{ station }}">Modellert snødekke i {{ station }}</a></h3>
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
  </div>
</div>
% end
