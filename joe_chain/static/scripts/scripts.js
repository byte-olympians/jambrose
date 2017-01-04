  $(document).ready(function() {
    $('select').material_select();

    // handles logic for form in joe_chain/templates/index.html
    $('#form-1').hide();
    $('#form-2').hide();
    $(document).on('change','.api-form',function(){
      var active = $('select[name=selector]').val();
      if (active === '1'){
        $('#form-1').show();
        $('#form-2').hide();
      } else if (active === '2') {
        $('#form-1').show();
        $('#form-2').show();
      } else {
        $('#form-1').hide();
        $('#form-2').hide();
      }

    });
  });
