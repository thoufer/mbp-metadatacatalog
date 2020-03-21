/*
 Apply masks to phone numbers to enforce validation and formatting
*/
$("#id_primary_contact_phone").mask("(999) 999-9999");
$("#id_data_contact_phone").mask("(999) 999-9999");


function copyContactHandler(checkbox){
    /*Copy information from primary contact to data contact.*/
    $("#id_data_contact_name").val($("#id_primary_contact_name").val());
    $("#id_data_contact_address1").val($("#id_primary_contact_address1").val());
    $("#id_data_contact_address2").val($("#id_primary_contact_address2").val());
    $("#id_data_contact_city").val($("#id_primary_contact_city").val());
    $("#id_data_contact_state").val($("#id_primary_contact_state").val());
    $("#id_data_contact_zip").val($("#id_primary_contact_zip").val());
    $("#id_data_contact_phone").val($("#id_primary_contact_phone").val());
    $("#id_data_contact_phone_ext").val($("#id_primary_contact_phone_ext").val());
    $("#id_data_contact_email").val($("#id_primary_contact_email").val());
}

function format_asset(d) {
  // `d` is the orignal data object for the row
  /* since their could be more than one child, iterate through
  the asset */
  BEGIN = '<div class="slider"><table class="child">';
  END = '</table></div>';
  rows = ''
  for (i=0; i < d.child_asset.length; i++){
    rec = d.child_asset[i];
    rows += '<tr role="row"><td width="385px">'+ rec.name
        +'</td><td width="92px">'+ rec.status
        +'</td><td width="80px">'+ rec.organization.region
        +'</td><td width="209px">'+ rec.organization.name
        +'</td><td>'+ rec.spatial_scale
        +'</td><td><a href="/asset/detail/'+ rec.id +'/"><i class="fas fa-info-circle" style="font-size: 1.2em"></i></a></td></tr>';
  }
  return BEGIN + rows +END;
}

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
