function post_servico_saudavel() {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: url_servico_saudavel,
        data: {
            csrfmiddlewaretoken: csrftoken
        },
        success: function (response) {
            resultado = response;
            $("#ultima_requisicao_saudavel").text(resultado.ultima_requisicao_saudavel);
            $("#ultima_requisicao_chaos").text(resultado.ultima_requisicao_chaos);
            $("#tempo_request_saudavel").text(resultado.tempo_request_saudavel);
            $("#tempo_request_chaos").text(resultado.tempo_request_chaos);
        }
    });
}

$(document).ready(function() {

})