/**
 * Created by Administrator on 2017/8/26.
 */
$('table').on('click','.edit_btn',function () {
    $('#myModal').modal('show');
    // $('.add_submit').hide();
    $('.form-horizontal').attr('action','/edit/');
    // console.log();
    var current_row=$(this).parent().parent();
    $('#id').val(current_row.children('.info_id').text());
    $('#container').val(current_row.children('.info_container').text());
    $('#image').val(current_row.children('.info_image').text());
    $('#ip').val(current_row.children('.info_ip').text());
    $('#hostname').val(current_row.children('.info_hostname').text());
    $('#status').val(current_row.children('.info_status').text());
    $('#tag').val(current_row.children('.info_tag').text());
    $('#user').val(current_row.children('.info_user').text());
});