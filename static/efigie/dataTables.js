$(function(){
  if (typeof id_modal != "undefined"){

    $('#'+id_modal).on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget) // Button that triggered the modal
      var name = button.data('name') // Extract info from data-* attributes
      var model = button.data('model')

      // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
      // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
      var modal = $(this)
      modal.find('.modal-body span').text( name )
      modal.find('.modal-footer a').attr('href', model)
    });
  }
});


$(function(){
  if (typeof id_list != "undefined"){
    $('#'+id_list).DataTable({
      "paging": true,
      "lengthChange": true,
      "searching": true,
      "ordering": true,
      "info": true,
      "autoWidth": false,
      "language": {
        // "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese.json"
        "url": language
        }
    });
  }
});

