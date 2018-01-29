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
