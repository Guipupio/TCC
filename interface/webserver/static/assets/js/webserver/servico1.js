function post_servico_saudavel() {
    $.ajax({
        type: 'GET',
        url: url_servico_saudavel,
        data: {},
        success: function (response) {
            resultado = response;
            $("#ultima_requisicao_saudavel").text(resultado.ultima_requisicao_saudavel);
            $("#tempo_medio_request_saudavel").text(resultado.tempo_request_saudavel);
        }
    });
}

function post_servico_teste() {
    $.ajax({
        type: 'GET',
        url: url_servico_teste,
        data: {},
        success: function (response) {
            resultado = response;
            $("#ultima_requisicao_chaos").text(resultado.ultima_requisicao_chaos);
            $("#tempo_medio_request_chaos").text(resultado.tempo_request_chaos);
        }
    });
}

$(document).ready(function() {

})