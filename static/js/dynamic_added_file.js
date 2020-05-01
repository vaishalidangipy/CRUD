var lang = window.location.pathname.split('/')[1];

$(document).ready(function (){
    function updateElementIndex(el, prefix, ndx, action) {
        var id_regex, replacement;
        if (action == 'add') {
            id_regex = new RegExp('-__prefix__-');
            replacement =  '-' + ndx + '-';
        }else{
            id_regex = new RegExp('(' + prefix + '-\\d+-)');
            replacement = prefix + '-' + ndx + '-';
        }
        if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
        replacement));
        if (el.id) el.id = el.id.replace(id_regex, replacement);
        if (el.name) el.name = el.name.replace(id_regex, replacement);
    }

    function deleteForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        // Delete the item/form
        $(btn).parents('.item').remove();
        var forms = $('.item').not(':first'); // Get all the forms
        // Update the total number of forms (1 less than before)
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        var i = 0;

        // Go through the forms and set their indices, names and IDs
        for (formCount = forms.length; i < formCount; i++) {
            if(formid = $(forms.get(i)).find('input[type=hidden]')[0]!=undefined){
                formid = $(forms.get(i)).find('input[type=hidden]')[0];
                updateElementIndex(formid, prefix, i, 'del');
            }
            $(forms.get(i)).children().children().children().children().children().each(function () {
                updateElementIndex(this, prefix, i, 'del');
            });
        }
        return false;
    }

    function addForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        // You can only submit a maximum of 10 todo items
        if (formCount < 50) {
            // Clone a form (without event handlers) from the first form
            var row = $(".clone-class .item:first").clone(false).get(0);
            $(row).removeClass('hide');
            // Insert it after the last form
            $(row).removeAttr('id').hide().insertAfter(".file-field .form-group:last").slideDown(300);

            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().children().children().removeClass("has-error");

            // Relabel or rename all the relevant bits
            $(".file-field .custom-file").children().each(function () {
                updateElementIndex(this, prefix, formCount, 'add');
                $(this).val("");
            });

            // Add an event handler for the delete item/form link
            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);
        } // End if
        else {
            alert("Sorry, you can only enter a maximum of ten items.");
        }
        return false;
    }
    // Register the click event handlers
    $(document).on('click', '#add', function(){
        return addForm(this, "documents");
    });

    $(".delete").click(function () {
        var add_id = $($(this).data('addid')).val();
        if (add_id === undefined || add_id=="None") {
            return deleteForm(this, "address_set");
        }else{
            $('#id_address_set-INITIAL_FORMS').val($('#id_address_set-INITIAL_FORMS').val()-1);
            return deleteAddress(add_id, deleteForm(this, "address_set"));
        }
    });

    function deleteAddress(add_id, callback){
        csrfmiddlewaretoken = $("input[name]").val();
        $.ajax({
            type: 'POST',
            url: '/' + lang +'/contact/delete-addresses/' + add_id +'/',
            data: {'csrfmiddlewaretoken': csrfmiddlewaretoken },
            dataType: 'json',
            success: function(res) {
                        if (res.success == "success"){
                            console.log("Address deleted successfully");
                        }
                        else{
                            console.log(res.error);
                        }
                    },
            error:  function(xhr, status, error) {
                       console.log(error);
                       $('#id_address_set-INITIAL_FORMS').val($('#id_address_set-INITIAL_FORMS').val()+1);
                    },
        });
    }
    if($('#add').parent().parent().parent().prev().hasClass('hide')){
        $('#add').click();
    }
});

