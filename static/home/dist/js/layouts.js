(function ($) {
    'use strict';
    $(function () {
        $('.file-upload-browse').on('click', function () {
            var file = $(this).parent().parent().parent().find('.file-upload-default');
            file.trigger('click');
        });
        $('.file-upload-default').on('change', function () {
            $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
        });
    });
    $(document).ready(function () {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var listDelete = $('.remove-privilege-delete');

        /**
         Função que vai permitir remover a permissão, enviando os dados para o backend
        */
        listDelete.on('click', function () {

            swal({
                title: "Desejas remover ?",
                text: " Tens a ceteza que desejas remover esta permissão?",
                icon: "warning",
                buttons: ["Cancelar", "Delete Agora"],
                dangerMode: true,
            })
                .then((willDelete) => {
                    if (willDelete) {
                        var lista = []
                        var um = $(this).attr("href");
                        var valor = document.querySelectorAll("#remove-priv:checked");
                        for (var i = 0; i < valor.length; i++) {
                            lista.push(valor[i].value)
                        }
                        if (lista.length > 0) {
                            $.ajax({
                                url: '/ajax/remove_privilege_categoria/',
                                type: 'POST',
                                data: JSON.stringify({
                                    'groupo': $('.groupo-id').text(),
                                    'lista_perm': lista,
                                }),
                                dataType: 'json',
                                headers: {
                                    'X-CSRFToken': getCookie('csrftoken'),
                                    'Accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                                },
                                success: function (data) {
                                    swal({
                                        title: "Removido",
                                        text: "Privilegio removido com sucesso!",
                                        icon: "success",
                                        confirmButtonText: 'OK'
                                    }).then(function () {
                                        window.location.reload();
                                    });
                                }
                            });

                        }
                        else {
                            $.ajax({
                                url: '/ajax/remove_privilege_categoria/',
                                type: 'POST',
                                data: JSON.stringify({
                                    'groupo': $('.groupo-id').text(),
                                    'lista_perm': um,
                                }),
                                dataType: 'json',
                                headers: {
                                    'X-CSRFToken': getCookie('csrftoken'),
                                    'Accept': 'application/json',
                                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                                },
                                success: function (data) {
                                    swal({
                                        title: "Removido",
                                        text: "Privilegio removido com sucesso!!",
                                        icon: "success",
                                        confirmButtonText: 'OK'
                                    }).then(function () {
                                        window.location.reload();
                                    });

                                }

                            });

                        }

                    } else {
                        swal("Operação foi cancelada!");
                    }

                });
        });

        $('.html-editor').summernote({
            height: 300,
            tabsize: 2
        });
    })
})(jQuery);