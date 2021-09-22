function createDom(size,url) {
    innerBefore = "<div class='pictures'> <a href='detail/" + url + "'><img src='/static/img/fake/" + url + "' alt=''> <div class='size'>" + size + "</div></a></div>";
    return innerBefore;
}
//展示和隐藏左边栏
function showLeft() {
    let clickbuttom=document.getElementsByClassName("nav-box")[1];
    clickbuttom.innerHTML="<p onclick='hideInside()'>所有分类</p>";
    document.getElementById("hideDom").style.display="inherit";
    //这里作那个类型数据的获取，然后返回在侧边栏展示
}
function hideInside() {
    let clickbuttom=document.getElementsByClassName("nav-box")[1];
    document.getElementById("hideDom").style.display="none";
    clickbuttom.innerHTML="<a href='javascript:void(0)' onclick='showLeft()'>所有分类</a>";
}
const leftMain=document.getElementById("leftMain");
//左边栏ajax获取到信息
function getAllTypes() {
    axios({
      method: 'get',
      url: '/wallpaper/allType',
    })
    .then(function (response){
        console.log(response);
        resData=response.data.imgTypes;
        let inHtml="";
        for (i=0;i<resData.length;i++){
            inHtml+="<li><a href='/wallpaper/type="+resData[i]+"'>"+resData[i]+"</a><li>";
        }
        console.log(inHtml)
        leftMain.innerHTML=inHtml;
    })
    .catch(function (error){
        console.log(error);
    })
}

//主动修改alert样式
window.alert =function (text){
    var divInnerHtml ="<div id='allHide'><div id='alert'><p>"+text+"</p><div onclick='clearAlert()'><a href='javascript:void(0)'>退出</a></div></div></div>"
    document.body.innerHTML+=divInnerHtml;
    document.body.style.overflow="hidden";
}

function clearAlert() {
    var allHide=document.getElementById("allHide");
    allHide.remove();
    document.body.style.overflow="auto";
}
