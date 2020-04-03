
$(document).ready(function() {
  var table = $('#asset_table').DataTable({
      'ajax': {
        url:"/asset/api/asset",
        dataSrc: ''
      },
      'dom': '<"dt_head"<"dt_button">lf>t<"dt_footer"pi>',
      'columns': [
        {
          data: null,
          render: function(data, type, full, meta){
            /*if ( data.child_asset.length > 0) {
              return '<i class="fas fa-plus-circle" style="color: green; font-size:1.2em;"></i>';
            } else { return ''; }*/
            return '';
          },
          width: 1,
          searchable: false,
          orderable: false,
          className: 'child-control'
        },
        {data:'name', title:'Name'},
        {data:'status', title:'Status'},
        {data:'organization.region', title:'Region'},
        {data:'organization.name', title:'Organization'},
        {data:'spatial_scale', title:'Spatial Scale'},
        {
          data: null,
          render: function(data, type, full, meta){
            return "<a href='/asset/detail/"+ data.id +"/'><i class='fas fa-info-circle' style='font-size: 1.2em;'></i></a>";
          },
          searchable: false,
          orderable: false
        },
        {data:'subject_tags', visible: false},
        {data:'place_tags', visible: false}
      ],
      order: [[1, 'asc']],
      stateSave: true
    });

    // add event listener for opening and closing details
    // ?? not sure why svg works but i doesn't in the delegate call?
    $('#asset_table tbody').delegate("tr td.child-control svg", "click", function(e){
      e.preventDefault();
      var tr =  $(this).closest('tr');
      var row = table.row(tr);

      if ( row.child.isShown() ) {
        // row is open, close it.

        $(this).toggleClass("fa fa-plus-circle");
        $(this).css("color", "green")

        // animate closing using slide effect
        $('div.slider', row.child()).slideUp( function() {
          row.child.hide();
          tr.removeClass('shown');
        });
      } else {
        // open row
        row.child( format_asset(row.data()), "no-padding" ).show();
        tr.addClass('shown');

        $('div.slider', row.child()).slideDown();

        $(this).toggleClass("fa fa-minus-circle");
        $(this).css("color", "red")
      }
    });

    $("div.dt_button").html("<a class='btn btn-primary' href='/asset/add/'>Add</a>");
});
