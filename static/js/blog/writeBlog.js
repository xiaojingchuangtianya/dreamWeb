
//主动修改alert样式
window.alert =function (text){
    if (text){
        divInnerHtml=" <div id='allHide'><div id='alert'>" +
            "<p>"+text+"</p>" +
            "<button class='cancelButton' type='button' onclick='cleanAlert()'>关闭</button> " +
            "</div></div>";
    }
    else{
        var divInnerHtml ="<div id='allHide'>" +
            "<div id='alert'> " +
            "<p>类名：<label for='typeAdd'>" +
            "<input type='text' name='addType' id='addType' autocomplete='off' minlength='1'  maxlength='8'></label></p> <div> " +
            "<button class='addButton' type='button' onclick='addBlogType()'>新增</button> " +
            "<button class='cancelButton' type='button' onclick='cleanAlert()'>取消</button> " +
            "</div></div></div>";
    }

    document.body.innerHTML+=divInnerHtml;
    document.body.style.overflow="hidden";
};

//弹出弹窗，有个输入框，以便新增博客类型
function addBlogType() {
    var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var createType=document.getElementById("addType").value;
    if (createType.length >=2 && createType.length<8){
        const request = new Request(
            "/blog/createType",
            {headers: {
                'content-type': 'application/json',
                'X-CSRFToken': csrfToken
            }}
        );
        fetch(request, {
            method: 'POST',
            // body:"name=lin",
            body:JSON.stringify({"addType":createType}),
            mode: 'same-origin'  // Do not send CSRF token to another domain.
        }).then(function(response) {
            return response.json();
            })
                .then(function (data){
                    //如果返回码是1则进行新增，否则什么也不做
                    var typeSelect=document.getElementById("id_type")
                    if (data.ResCode == 1){
                        if (typeSelect.options[0].text == '---------'){
                            typeSelect.options[0].text =data.typeName;
                        }
                        else{
                            var addOption=document.createElement("option");
                            addOption.value=data.typeName;
                            addOption.text=data.typeName;
                            addOption.selected=true;
                            typeSelect.append(addOption);
                        }
                        cleanAlert()
                    }
                    else{
                        typeSelect.options[0].text =data.typeName;
                        console.log("此时不需要新增select");
                        cleanAlert();
                    }
                })
            .catch(function (error) {
                console.log(error);
        })
    }
    else{
        document.getElementById("allHide").remove();
        alert("你的类名长度不符合规范");
    }
//   此处进行ajax请求新增添加到，按照返回结果处理 0已存在 1新增成功
//    无论如何都将弹窗关闭，1时新增select选项 其他情况不做处理
}

//关闭，新增成功后或者直接退出收起弹窗
function cleanAlert() {
    document.getElementById("allHide").remove()
}


