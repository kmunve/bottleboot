% # Template for the profile and seasonal plots for a single station

    <div class="row" id="crocus_results">

        <div class="panel panel-default">
          <div class="panel-heading">
              % # in future maybe link to position of station in Google maps
            <h3 class="panel-title">Modellert snødekke ved stasjon <a href="{{ url_gmap }}">{{ station_name }} (StNo: {{ station_id }}, {{station_elev}} moh)</a></h3>
          </div>
          <div class="panel-body">

            <div class="row">
              <div class="col-md-6">
                <img src="{{url_vertprofile}}" class="img-responsive">
              </div>

              <div class="col-md-6">
                <ul class="nav nav-tabs">
                  <li class="active"><a aria-expanded="true" href="#graintype{{ station_id }}" data-toggle="tab">Kornform</a></li>
                  <li class=""><a aria-expanded="false" href="#density{{ station_id }}" data-toggle="tab">Tetthet</a></li>

                  <li class=""><a aria-expanded="false" href="#lwc{{ station_id }}" data-toggle="tab">Vanninnhold</a></li>
                  <li class=""><a aria-expanded="false" href="#temperature{{ station_id }}" data-toggle="tab">Temperatur</a></li>
                </ul>

                <div id="seasonal_tab" class="tab-content">

                  <div class="tab-pane fade" id="density{{ station_id }}">
                    <p><img src="{{url_density}}"  class="img-responsive"></p>
                  </div>

                  <div class="tab-pane fade active in" id="graintype{{ station_id }}">
                    <p><img src="{{url_snowgraintype}}"  class="img-responsive"></p>
                  </div>

                  <div class="tab-pane fade" id="lwc{{ station_id }}">
                    <p><img src="{{url_lwc}}" class="img-responsive"></p>
                  </div>

                  <div class="tab-pane fade" id="temperature{{ station_id }}">
                    <p><img src="{{url_temperature}}"  class="img-responsive"></p>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
    </div>