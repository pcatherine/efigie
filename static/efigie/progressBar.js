/*
  Example:

    {% block content %}
      <div class="progress" >
        <div id="progress1" class="progress-bar progress-bar-green" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100">
        </div>
      </div>

      <div class="progress" >
        <div id="progress2" class="progress-bar progress-bar-green" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100">
        </div>
      </div>
    {% endblock %}

    {% block script %}
      <script src="{% static 'efigie/progressBar.js' %}"></script>
      <script >
        progressBar(3, 10, '#progress1', '#progress2' )
      </script>
    {% endblock %}


    sweeptime in SECONDS

    AJAX REQUEST
      $.get("/app/update-progress", function(data){

      })
*/

function progressBar(_callback, nsensor, sweeptime, id_partialbar, id_totalbar){
  partialProgess(id_partialbar, nsensor, sweeptime);
  totalProgress(id_totalbar, nsensor, sweeptime);
  setTimeout(function(){
    _callback();
  }, sweeptime*1000*nsensor + 1000);
}

function partialProgess(id, nsensor, sweeptime) {
  var completed_times = 0;
  var percentage = 0;

  var partialprogresspump = setInterval(function(){
    $(id).css('width',percentage+'%').attr("aria-valuenow", percentage+ '%').text( percentage + '%');

    /* test to see if the job has completed */
    if(percentage == 100){
      percentage = 0;
      completed_times += 1;
    }

    if(completed_times == nsensor ) {
      clearInterval(partialprogresspump); // Finishes here
    }

    percentage += 1;
  }, sweeptime*10);
}

function totalProgress(id, nsensor, sweeptime) {
  var percentage = 0;

  var totalprogresspump = setInterval(function(){
    $(id).css('width',percentage+'%').attr("aria-valuenow", percentage+ '%').text(percentage+ '%');

    /* test to see if the job has completed */
    if(percentage == 100 ) {
      clearInterval(totalprogresspump); // Finishes here
    }

    percentage += 1;
  }, sweeptime*10*nsensor);
}
