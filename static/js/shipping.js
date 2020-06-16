(function () {

  /* -------------------------------
              Time to move the gift
              --------------------------------*/
  var $, acceptCheckbox, body, boughtProduct, inputs, totalInputs, truck;

  jQuery.fn.toggleAttr = function (attr) {
    return this.each(function () {
      var $this;
      $this = $(this);
      if ($this.attr(attr)) {
        return $this.removeAttr(attr);
      } else {
        return $this.attr(attr, attr);
      }
    });
  };

  $ = jQuery;

  body = $('body');

  /* -------------------------------
                    Only validate when there's content
                    --------------------------------*/
  $(':required').on('blur keydown', function () {
    if (!$(this).val()) {
      return $(this).removeClass('touched');
    } else {
      return $(this).addClass('touched');
    }
  });

  boughtProduct = $('.icon-gift');

  truck = $('.icon-truck');

  inputs = $('input:not([type="checkbox"])');

  acceptCheckbox = $('input[type="checkbox"]');

  totalInputs = inputs.size();

  inputs.on("change paste", function () {
    var totalEmptyInputs;
    totalEmptyInputs = inputs.filter(function () {
      return !$(this).val();
    }).length;
    totalEmptyInputs = totalEmptyInputs;
    if (totalEmptyInputs >= 0) {
      if ($(this).val() === "") {

      } else {
        if (totalEmptyInputs > 1) {
          boughtProduct.animate({
            opacity: 1.0 });

        }
        if (totalEmptyInputs < totalInputs / 2) {
          boughtProduct.addClass('is-almost-there');
        }
        if (totalEmptyInputs === 0) {
          boughtProduct.toggleClass('is-almost-there is-there');
          return acceptCheckbox.change(function () {
            if (!acceptCheckbox.attr('checked')) {
              boughtProduct.toggleClass('is-going-into-the-truck');
              truck.toggleClass('is-delivering');
              return $('[disabled]').toggleAttr('disabled');
            }
          });
        }
      }
    }
  });

}).call(this);


//# sourceURL=coffeescript