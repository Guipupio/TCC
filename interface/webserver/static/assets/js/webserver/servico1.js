function post_servico_saudavel() {
    $("#informe_saudavel").show()
    $.ajax({
        type: 'GET',
        url: url_servico_saudavel,
        data: {},
        success: function (response) {
            $("#informe_saudavel").hide();
            $("#informe_saudavel_ok").show();
            timeoutID = setTimeout('$("#informe_saudavel_ok").hide()', 1*1000);
            resultado = response;
            $("#ultima_requisicao_saudavel").text(resultado.ultima_requisicao_saudavel);
            $("#tempo_medio_resposta_saudavel").text(resultado.tempo_medio_resposta_saudavel);
            $("#numero_requisicoes_realizadas_saudavel").text(resultado.numero_requisicoes_realizadas_saudavel);
            $("#numero_requisicoes_bem_sucedidas_saudavel").text(resultado.numero_requisicoes_bem_sucedidas_saudavel);
        },
        error: function(request, satus, error){
            $("#informe_saudavel").hide()
        }
    });
}

function post_servico_teste() {
    $("#informe_chaos").show()
    $.ajax({
        type: 'GET',
        url: url_servico_teste,
        data: {},
        success: function (response) {
            $("#informe_chaos").hide();
            $("#informe_chaos_ok").show();
            timeoutID = setTimeout('$("#informe_chaos_ok").hide()', 1*1000);
            resultado = response;
            $("#ultima_requisicao_chaos").text(resultado.ultima_requisicao_chaos);
            $("#tempo_medio_resposta_chaos").text(resultado.tempo_medio_resposta_chaos);
            $("#numero_requisicoes_realizadas_chaos").text(resultado.numero_requisicoes_realizadas_chaos);
            $("#numero_requisicoes_bem_sucedidas_chaos").text(resultado.numero_requisicoes_bem_sucedidas_chaos);
        },
        error: function(request, satus, error){
            $("#informe_chaos").hide()
        }
    });
}

$(document).ready(function() {

})