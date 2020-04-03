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
