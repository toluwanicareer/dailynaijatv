$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-product").modal("show");
      },
      success: function (data) {
        $("#modal-product .modal-content").html(data.html_form);
      }
    });
  };

});