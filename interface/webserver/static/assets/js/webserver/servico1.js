function post_servico_saudavel() {
    $.ajax({
        type: 'GET',
        url: url_servico_saudavel,
        data: {},
        success: function (response) {
            resultado = response;
            $("#ultima_requisicao_saudavel").text(resultado.ultima_requisicao_saudavel);
            $("#tempo_medio_resposta_saudavel").text(resultado.tempo_medio_resposta_saudavel);
            $("#numero_requisicoes_realizadas_saudavel").text(resultado.numero_requisicoes_realizadas_saudavel);
            $("#numero_requisicoes_bem_sucedidas_saudavel").text(resultado.numero_requisicoes_bem_sucedidas_saudavel);
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
            $("#tempo_medio_resposta_chaos").text(resultado.tempo_medio_resposta_chaos);
            $("#numero_requisicoes_realizadas_chaos").text(resultado.numero_requisicoes_realizadas_chaos);
            $("#numero_requisicoes_bem_sucedidas_chaos").text(resultado.numero_requisicoes_bem_sucedidas_chaos);
        }
    });
}

$(document).ready(function() {

})