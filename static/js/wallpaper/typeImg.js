let scrollTime=0;

//要获取当前的类型和页数
typeImg=window.location.href.split("=")[1]
// 后续作一个延缓拉下的函数，减轻服务器负担
window.onscroll = function () {
    //可视化的最大高度
    var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
    //滚动条最大高度
    var scrollHeight = document.documentElement.scrollHeight||document.body.scrollHeight;
    //滚动条距离顶部的高度
    var scrollTop = document.documentElement.scrollTop||document.body.scrollTop;
//当可视化高度加上滚动条高度等于高度时就是相当于拉到了底部，此时进行数据获取
    if (windowHeight+parseInt(scrollTop)==scrollHeight){
        scrollTime +=1;
        if (scrollTime % 3==0){
            alert("请稍等一会再继续下拉！");
        }else {
        let mainDom=document.getElementsByClassName("main")[0];
        axios.get("/wallpaper/typeNextImg?type="+typeImg)
            .then(function (res){
            console.log(res.data);
            resData=res.data;
                for(i=0;i<resData.length;i++){
                    idata=resData[i]
                    mainDom.innerHTML+= createDom(idata[0],idata[1]);
                }
        })
            .catch(function (error){
                // console.log(error);
                alert("不要再往下拉了，此分类没有更多图片了");
            })
    }
}
}
