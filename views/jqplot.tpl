<!DOCTYPE html>
<html>

<head>
  <title>jqPlot test site</title>
  <!--[if lt IE 9]><script language="javascript" type="text/javascript"
                             src="/static/excanvas.js"></script><![endif]-->

  <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.11.3.min.js"></script>
  <script type="text/javascript" src="/resources/jqplot/jquery.jqplot.min.js"></script>
  <script type="text/javascript" src="/resources/jqplot/plugins/jqplot.barRenderer.js"></script>
  <script type="text/javascript" src="/resources/jqplot/plugins/jqplot.pieRenderer.js"></script>
  <script type="text/javascript" src="/resources/jqplot/plugins/jqplot.categoryAxisRenderer.js"></script>
  <script type="text/javascript" src="/resources/jqplot/plugins/jqplot.pointLabels.js"></script>
  <link rel="stylesheet" type="text/css" hrf="/resources/jqplot/jquery.jqplot.min.css" />

  <script class="code" type="text/javascript">
    $(document).ready(function() {
      var s1 = [2, 6, 7, 10];
      var s2 = [7, 5, 3, 2];
      var ticks = ['a', 'b', 'c', 'd'];

      plot2 = $.jqplot('chart2', [s1, s2], {
        seriesDefaults: {
          renderer: $.jqplot.BarRenderer,
          pointLabels: {
            show: true
          }
        },
        axes: {
          xaxis: {
            renderer: $.jqplot.CategoryAxisRenderer,
            ticks: ticks
          }
        }
      });

      $('#chart2').bind('jqplotDataHighlight',
        function(ev, seriesIndex, pointIndex, data) {
          $('#info2').html('series: ' + seriesIndex + ', point: ' + pointIndex + ', data: ' + data);
        }
      );

      $('#chart2').bind('jqplotDataUnhighlight',
        function(ev) {
          $('#info2').html('Nothing');
        }
      );
    });
  </script>


</head>

<body>

  <h1>jqPlot test site</h1>

  <div id="chart2" style="height:400px;width:600px; "></div>

</body>

</html>
