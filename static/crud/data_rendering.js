"use strict";

var KTDefaultDatatableDemo = function () {
	// Private functions
	var status = "";
	var company_code = "";
	var invoice_date = "";
	var date_created = "";
	var date_paid = "";

	// basic demo
	var demo = function () {
		var datatable = $('.kt_datatable').KTDatatable({
			data: {
				type: 'remote',
				source: {
					read: {
						url: '/crud/grupo-economico-list/',
						method: 'GET',
						map: function(raw) {
							var dataSet = raw;
							if (typeof raw.data !== 'undefined') {
							  dataSet = raw.data;
							}
							return dataSet;
						},
					}
				},
				pageSize: 20,
				serverPaging: true,
				serverFiltering: true,
                serverSorting: true,
                saveState : {
                    cookie : true,
                }
			},

			layout: {
				scroll: false,
				footer: false
			},
			sortable: true,

			filterable: false,

			pagination: true,

			search: {
				input: $('#generalSearch'),
				delay: 600,
			},

			rows: {
				autoHide: false,
			},
			columns: [
				{
					field: 'id_grupo_economico',
					title: 'id',
				}, {
					field: 'r1',
					title: 'r1',
				}, {
					field: 'r2',
					title: 'r2',
				}, {
					field: 'r3',
					title: 'r3',
				}, {
					field: 'cadastro_grupo',
					title: 'Cadastro grupo',
				}, {
					field: 'nome',
					title: 'Nome'
				},
				{
					field: 'data_atualizacao',
					title: 'Data atualizacao'
                },
                {
                    field: 'Actions',
                    width: 110,
                    title: 'Actions',
                    sortable: false,
                    overflow: 'visible',
                    autoHide: false,
                    template: function (e) {
						return '\
		                  <a href="/crud/update-grupo-economico/'+e.id_grupo_economico+'/" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Edit details">\
		                      <i class="la la-edit"></i>\
		                  </a>\
		                  <a href="/crud/delete-grupo-economico/'+e.id_grupo_economico+'/" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Delete">\
		                      <i class="la la-trash"></i>\
						  </a>\
						  <a href="/crud/detail-grupo-economico/'+e.id_grupo_economico+'/" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Delete">\
		                      <i class="la la-book"></i>\
						  </a>\
		              ';
                    },
                }
			],
		});

    $('.kt_form_status').on('change', function() {
        status = $(this).val();
	});
  };

	return {
		// public functions
		init: function () {
			demo();
		}

	};
}();



var arrows;
if (KTUtil.isRTL()) {
	arrows = {
		leftArrow: '<i class="la la-angle-right"></i>',
		rightArrow: '<i class="la la-angle-left"></i>'
	}
} else {
	arrows = {
		leftArrow: '<i class="la la-angle-left"></i>',
		rightArrow: '<i class="la la-angle-right"></i>'
	}
}

jQuery(document).ready(function () {
	KTDefaultDatatableDemo.init();
});
