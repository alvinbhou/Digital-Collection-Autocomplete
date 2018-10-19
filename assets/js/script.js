$(document).ready(function(){
    $('#submit-btn').click(function(){
        var ref_id = $('#ref-id').val();
        var ref_cname = $('#ref-cname').val();
        var content = $('#content-text').val();
        ref_id = ref_id.split(/\r?\n/);
        content = content.split(/\r?\n/);
        ref_cname = ref_cname.split(/\r?\n/);
        var content_dict = {};
        for(var i = 0; i < content.length; ++i){
            var pair = content[i].split(" ");
            if(pair.length >= 2){
                content_dict[pair[0]] = pair.join("").replace(pair[0], "");
            }
        }
        var result_arr = [];
        var result = "";
        var nhm_header = "國立歷史博物館藏"

        for(var i = 0; i < ref_id.length; ++i){
            if( ref_id[i].toString().length == 0)continue;
            if(ref_id[i] in content_dict){
                result +=  nhm_header + '《' + ref_cname[i] + '》（' + ref_id[i] + "），" +  content_dict[ref_id[i]] +'\n'
                // result_arr.push({ cname: ref_cname[i], content: content_dict[ref_id[i]]});
            }
            else {
                result +=  '找不到文物說明\n';
            }
        }
        console.log(ref_id);
        console.log(content_dict);
        // console.log(result_arr);
        // console.log(result);
        $('#result-text').val(result);
    });

    $('#copy-btn').click(function(){
        $('#result-text').select();
        document.execCommand("copy");
        $('#result-text').blur();
        toastr.success('Text copied!');
    });
    
});
