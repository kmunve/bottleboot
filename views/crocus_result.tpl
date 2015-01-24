
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
          <div class="container">
              <h1>Bootstrap Easy Tabs</h1>

              <div class="well">
                  <form id="season_plots">
                      <section data-tab-name="Lagdeling" class="tab-pane">
                          <img src="{{ url_snowgraintype }}" height="33%" class="img-responsive">
                      </section>
                      <section data-tab-name="Tetthett" class="tab-pane">
                          <img src="{{ url_density }}" height="33%" class="img-responsive">
                      </section>
                  </form>

              </div>
          </div>
	  </th>
	</tr>
      </tbody>
    </table>
  </div>
</div>
% end
